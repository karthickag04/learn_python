# PRACTICE PROJECT: Quiz Game
# Demonstrates: OOP, File I/O, Random, Exception handling, User interaction

import json
import random
import os
from datetime import datetime
from abc import ABC, abstractmethod

# ============================================================================
# EXCEPTIONS
# ============================================================================

class QuizError(Exception):
    """Base exception for quiz operations"""
    pass

class QuizLoadError(QuizError):
    """Error loading quiz"""
    pass

class NoQuestionsError(QuizError):
    """No questions available"""
    pass

# ============================================================================
# QUESTION TYPES
# ============================================================================

class Question(ABC):
    """Abstract base class for questions"""
    
    def __init__(self, text, correct_answer, points=1, hint=None, explanation=None):
        self.text = text
        self.correct_answer = correct_answer
        self.points = points
        self.hint = hint
        self.explanation = explanation
        self.attempts = 0
        self.answered_correctly = False
    
    @abstractmethod
    def display(self):
        """Display the question"""
        pass
    
    @abstractmethod
    def check_answer(self, user_answer):
        """Check if answer is correct"""
        pass
    
    def get_hint(self):
        """Get hint for the question"""
        return self.hint or "No hint available"
    
    def get_explanation(self):
        """Get explanation for the answer"""
        return self.explanation or f"The correct answer is: {self.correct_answer}"
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'type': self.__class__.__name__,
            'text': self.text,
            'correct_answer': self.correct_answer,
            'points': self.points,
            'hint': self.hint,
            'explanation': self.explanation
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create question from dictionary - implemented by subclasses"""
        raise NotImplementedError

class MultipleChoiceQuestion(Question):
    """Multiple choice question"""
    
    def __init__(self, text, correct_answer, options, **kwargs):
        super().__init__(text, correct_answer, **kwargs)
        self.options = options
    
    def display(self):
        """Display the question with options"""
        print(f"\n📝 {self.text}")
        print("-" * 40)
        for i, option in enumerate(self.options, 1):
            print(f"  {i}. {option}")
        print()
    
    def check_answer(self, user_answer):
        """Check answer by number or text"""
        self.attempts += 1
        user_answer = user_answer.strip()
        
        # Check if answer is a number (option index)
        try:
            index = int(user_answer) - 1
            if 0 <= index < len(self.options):
                user_answer = self.options[index]
        except ValueError:
            pass
        
        self.answered_correctly = user_answer.lower() == self.correct_answer.lower()
        return self.answered_correctly
    
    def to_dict(self):
        data = super().to_dict()
        data['options'] = self.options
        return data
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            text=data['text'],
            correct_answer=data['correct_answer'],
            options=data['options'],
            points=data.get('points', 1),
            hint=data.get('hint'),
            explanation=data.get('explanation')
        )

class TrueFalseQuestion(Question):
    """True/False question"""
    
    def display(self):
        """Display the question"""
        print(f"\n📝 True or False: {self.text}")
        print("-" * 40)
        print("  Enter 'T' for True or 'F' for False")
        print()
    
    def check_answer(self, user_answer):
        """Check True/False answer"""
        self.attempts += 1
        user_answer = user_answer.strip().lower()
        
        # Accept various forms
        if user_answer in ['t', 'true', '1', 'yes']:
            user_answer = 'true'
        elif user_answer in ['f', 'false', '0', 'no']:
            user_answer = 'false'
        
        correct = str(self.correct_answer).lower()
        self.answered_correctly = user_answer == correct
        return self.answered_correctly
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            text=data['text'],
            correct_answer=data['correct_answer'],
            points=data.get('points', 1),
            hint=data.get('hint'),
            explanation=data.get('explanation')
        )

class FillBlankQuestion(Question):
    """Fill in the blank question"""
    
    def __init__(self, text, correct_answer, case_sensitive=False, **kwargs):
        super().__init__(text, correct_answer, **kwargs)
        self.case_sensitive = case_sensitive
    
    def display(self):
        """Display the question"""
        print(f"\n📝 Fill in the blank:")
        print("-" * 40)
        print(f"  {self.text}")
        print()
    
    def check_answer(self, user_answer):
        """Check fill-in answer"""
        self.attempts += 1
        user_answer = user_answer.strip()
        correct = self.correct_answer
        
        if not self.case_sensitive:
            user_answer = user_answer.lower()
            correct = correct.lower()
        
        self.answered_correctly = user_answer == correct
        return self.answered_correctly
    
    def to_dict(self):
        data = super().to_dict()
        data['case_sensitive'] = self.case_sensitive
        return data
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            text=data['text'],
            correct_answer=data['correct_answer'],
            case_sensitive=data.get('case_sensitive', False),
            points=data.get('points', 1),
            hint=data.get('hint'),
            explanation=data.get('explanation')
        )

# ============================================================================
# QUIZ
# ============================================================================

class Quiz:
    """Quiz container and manager"""
    
    QUESTION_TYPES = {
        'MultipleChoiceQuestion': MultipleChoiceQuestion,
        'TrueFalseQuestion': TrueFalseQuestion,
        'FillBlankQuestion': FillBlankQuestion
    }
    
    def __init__(self, title, description="", time_limit=None):
        self.title = title
        self.description = description
        self.time_limit = time_limit  # in seconds
        self.questions = []
        self.created_at = datetime.now()
    
    def add_question(self, question):
        """Add a question to the quiz"""
        self.questions.append(question)
    
    def get_questions(self, shuffle=False):
        """Get questions optionally shuffled"""
        questions = self.questions.copy()
        if shuffle:
            random.shuffle(questions)
        return questions
    
    @property
    def total_points(self):
        """Get total possible points"""
        return sum(q.points for q in self.questions)
    
    @property
    def question_count(self):
        """Get number of questions"""
        return len(self.questions)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'title': self.title,
            'description': self.description,
            'time_limit': self.time_limit,
            'questions': [q.to_dict() for q in self.questions]
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create quiz from dictionary"""
        quiz = cls(
            title=data['title'],
            description=data.get('description', ''),
            time_limit=data.get('time_limit')
        )
        
        for q_data in data.get('questions', []):
            q_type = q_data.get('type', 'MultipleChoiceQuestion')
            if q_type in cls.QUESTION_TYPES:
                question_class = cls.QUESTION_TYPES[q_type]
                question = question_class.from_dict(q_data)
                quiz.add_question(question)
        
        return quiz
    
    def save(self, filename):
        """Save quiz to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load(cls, filename):
        """Load quiz from file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return cls.from_dict(data)
        except (IOError, json.JSONDecodeError) as e:
            raise QuizLoadError(f"Could not load quiz: {e}")

# ============================================================================
# QUIZ SESSION
# ============================================================================

class QuizResult:
    """Result of a quiz session"""
    
    def __init__(self, quiz_title, questions_answered, correct_answers, 
                 total_points, earned_points, time_taken=None):
        self.quiz_title = quiz_title
        self.questions_answered = questions_answered
        self.correct_answers = correct_answers
        self.total_points = total_points
        self.earned_points = earned_points
        self.time_taken = time_taken
        self.timestamp = datetime.now()
    
    @property
    def percentage(self):
        if self.total_points == 0:
            return 0
        return round((self.earned_points / self.total_points) * 100, 1)
    
    @property
    def grade(self):
        pct = self.percentage
        if pct >= 90:
            return 'A'
        elif pct >= 80:
            return 'B'
        elif pct >= 70:
            return 'C'
        elif pct >= 60:
            return 'D'
        return 'F'
    
    def display(self):
        """Display the result"""
        print("\n" + "=" * 50)
        print("📊 QUIZ RESULTS")
        print("=" * 50)
        print(f"\nQuiz: {self.quiz_title}")
        print(f"Date: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        
        if self.time_taken:
            minutes = int(self.time_taken // 60)
            seconds = int(self.time_taken % 60)
            print(f"Time: {minutes}m {seconds}s")
        
        print(f"\nQuestions: {self.correct_answers}/{self.questions_answered}")
        print(f"Points: {self.earned_points}/{self.total_points}")
        print(f"Percentage: {self.percentage}%")
        print(f"Grade: {self.grade}")
        
        # Visual feedback
        if self.percentage >= 90:
            print("\n🏆 Excellent! Outstanding performance!")
        elif self.percentage >= 80:
            print("\n🎉 Great job! Well done!")
        elif self.percentage >= 70:
            print("\n👍 Good work! Keep it up!")
        elif self.percentage >= 60:
            print("\n📚 Not bad, but there's room for improvement.")
        else:
            print("\n💪 Keep practicing! You'll get better!")
    
    def to_dict(self):
        return {
            'quiz_title': self.quiz_title,
            'questions_answered': self.questions_answered,
            'correct_answers': self.correct_answers,
            'total_points': self.total_points,
            'earned_points': self.earned_points,
            'time_taken': self.time_taken,
            'percentage': self.percentage,
            'grade': self.grade,
            'timestamp': self.timestamp.isoformat()
        }

class QuizSession:
    """Manages a quiz-taking session"""
    
    def __init__(self, quiz, shuffle=True, allow_hints=True):
        self.quiz = quiz
        self.shuffle = shuffle
        self.allow_hints = allow_hints
        self.current_question_index = 0
        self.questions = []
        self.start_time = None
        self.end_time = None
    
    def start(self):
        """Start the quiz session"""
        if not self.quiz.questions:
            raise NoQuestionsError("Quiz has no questions")
        
        self.questions = self.quiz.get_questions(shuffle=self.shuffle)
        self.current_question_index = 0
        self.start_time = datetime.now()
        
        print("\n" + "=" * 50)
        print(f"🎯 {self.quiz.title}")
        print("=" * 50)
        
        if self.quiz.description:
            print(f"\n{self.quiz.description}")
        
        print(f"\nQuestions: {len(self.questions)}")
        print(f"Total Points: {self.quiz.total_points}")
        
        if self.allow_hints:
            print("\n💡 Type 'hint' for a hint (no penalty)")
        print("Type 'skip' to skip a question")
        print("Type 'quit' to end the quiz early")
        print("\n" + "-" * 50)
        
        input("Press Enter to start...")
    
    def run(self):
        """Run the quiz session"""
        self.start()
        
        while self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            question_num = self.current_question_index + 1
            
            print(f"\n[Question {question_num}/{len(self.questions)}]", end="")
            print(f" ({question.points} point{'s' if question.points > 1 else ''})")
            
            question.display()
            
            while True:
                answer = input("Your answer: ").strip()
                
                if answer.lower() == 'quit':
                    print("\n⏸️ Quiz ended early.")
                    self.end_time = datetime.now()
                    return self.get_result()
                
                if answer.lower() == 'skip':
                    print("⏭️ Skipped")
                    break
                
                if answer.lower() == 'hint' and self.allow_hints:
                    print(f"\n💡 Hint: {question.get_hint()}")
                    continue
                
                if not answer:
                    print("Please enter an answer.")
                    continue
                
                # Check the answer
                is_correct = question.check_answer(answer)
                
                if is_correct:
                    print("✅ Correct!")
                else:
                    print(f"❌ Wrong! {question.get_explanation()}")
                
                break
            
            self.current_question_index += 1
        
        self.end_time = datetime.now()
        return self.get_result()
    
    def get_result(self):
        """Get the quiz result"""
        time_taken = None
        if self.start_time and self.end_time:
            time_taken = (self.end_time - self.start_time).total_seconds()
        
        correct = sum(1 for q in self.questions if q.answered_correctly)
        earned = sum(q.points for q in self.questions if q.answered_correctly)
        
        return QuizResult(
            quiz_title=self.quiz.title,
            questions_answered=self.current_question_index,
            correct_answers=correct,
            total_points=self.quiz.total_points,
            earned_points=earned,
            time_taken=time_taken
        )

# ============================================================================
# SAMPLE QUIZZES
# ============================================================================

def create_python_quiz():
    """Create a sample Python basics quiz"""
    quiz = Quiz(
        title="Python Basics Quiz",
        description="Test your knowledge of Python fundamentals!"
    )
    
    # Multiple choice questions
    quiz.add_question(MultipleChoiceQuestion(
        text="What is the correct way to create a variable in Python?",
        options=["var x = 5", "x = 5", "int x = 5", "x := 5"],
        correct_answer="x = 5",
        points=1,
        hint="Python uses dynamic typing",
        explanation="In Python, you simply assign a value with '='."
    ))
    
    quiz.add_question(MultipleChoiceQuestion(
        text="Which data type is used to store a sequence of characters?",
        options=["int", "float", "str", "bool"],
        correct_answer="str",
        points=1,
        hint="Think about text..."
    ))
    
    quiz.add_question(MultipleChoiceQuestion(
        text="What is the output of: print(type([1, 2, 3]))?",
        options=["<class 'tuple'>", "<class 'list'>", "<class 'set'>", "<class 'dict'>"],
        correct_answer="<class 'list'>",
        points=2,
        hint="Square brackets create this data structure"
    ))
    
    quiz.add_question(MultipleChoiceQuestion(
        text="Which keyword is used to define a function in Python?",
        options=["function", "func", "def", "define"],
        correct_answer="def",
        points=1
    ))
    
    # True/False questions
    quiz.add_question(TrueFalseQuestion(
        text="Python is a case-sensitive language.",
        correct_answer=True,
        points=1,
        explanation="Python distinguishes between 'Name' and 'name'."
    ))
    
    quiz.add_question(TrueFalseQuestion(
        text="Lists in Python are immutable.",
        correct_answer=False,
        points=1,
        hint="Think about whether you can change list elements...",
        explanation="Lists are mutable. Tuples are immutable."
    ))
    
    quiz.add_question(TrueFalseQuestion(
        text="The 'elif' keyword is used for else-if conditions.",
        correct_answer=True,
        points=1
    ))
    
    # Fill in the blank questions
    quiz.add_question(FillBlankQuestion(
        text="The _____ function is used to get user input in Python.",
        correct_answer="input",
        points=1
    ))
    
    quiz.add_question(FillBlankQuestion(
        text="To create an empty dictionary, you use _____ or dict().",
        correct_answer="{}",
        points=2,
        hint="Think about curly braces..."
    ))
    
    quiz.add_question(FillBlankQuestion(
        text="The _____ statement is used to exit a loop early.",
        correct_answer="break",
        points=1
    ))
    
    return quiz

def create_math_quiz():
    """Create a math quiz"""
    quiz = Quiz(
        title="Basic Mathematics Quiz",
        description="Test your math skills!"
    )
    
    quiz.add_question(MultipleChoiceQuestion(
        text="What is 15 × 8?",
        options=["100", "120", "115", "125"],
        correct_answer="120",
        points=1
    ))
    
    quiz.add_question(MultipleChoiceQuestion(
        text="What is the square root of 144?",
        options=["10", "11", "12", "14"],
        correct_answer="12",
        points=2
    ))
    
    quiz.add_question(TrueFalseQuestion(
        text="The sum of angles in a triangle is 180 degrees.",
        correct_answer=True,
        points=1
    ))
    
    quiz.add_question(FillBlankQuestion(
        text="2³ equals _____",
        correct_answer="8",
        points=1
    ))
    
    quiz.add_question(FillBlankQuestion(
        text="The area of a rectangle is length × _____",
        correct_answer="width",
        points=1,
        case_sensitive=False
    ))
    
    return quiz

# ============================================================================
# CLI INTERFACE
# ============================================================================

class QuizGameCLI:
    """Command-line interface for quiz game"""
    
    def __init__(self):
        self.results_history = []
        self.quizzes = {
            'python': create_python_quiz(),
            'math': create_math_quiz()
        }
    
    def run(self):
        """Run the quiz game"""
        print("\n" + "=" * 50)
        print("🎮 QUIZ GAME")
        print("=" * 50)
        
        while True:
            print("\n📋 MENU:")
            print("  1. Take Python Quiz")
            print("  2. Take Math Quiz")
            print("  3. Load Quiz from File")
            print("  4. Create Custom Quiz")
            print("  5. View Results History")
            print("  6. Save Quiz to File")
            print("  0. Exit")
            
            choice = input("\nChoice: ").strip()
            
            try:
                if choice == '0':
                    print("\n👋 Thanks for playing!")
                    break
                elif choice == '1':
                    self.take_quiz('python')
                elif choice == '2':
                    self.take_quiz('math')
                elif choice == '3':
                    self.load_quiz()
                elif choice == '4':
                    self.create_quiz()
                elif choice == '5':
                    self.view_history()
                elif choice == '6':
                    self.save_quiz()
                else:
                    print("❌ Invalid choice")
            except QuizError as e:
                print(f"❌ Error: {e}")
    
    def take_quiz(self, quiz_name):
        """Take a quiz"""
        if quiz_name not in self.quizzes:
            print(f"❌ Quiz '{quiz_name}' not found")
            return
        
        quiz = self.quizzes[quiz_name]
        
        print(f"\n📝 Settings for: {quiz.title}")
        shuffle = input("Shuffle questions? (y/n) [y]: ").strip().lower() != 'n'
        hints = input("Allow hints? (y/n) [y]: ").strip().lower() != 'n'
        
        session = QuizSession(quiz, shuffle=shuffle, allow_hints=hints)
        result = session.run()
        
        result.display()
        self.results_history.append(result)
    
    def load_quiz(self):
        """Load a quiz from file"""
        filename = input("\nQuiz file path: ").strip()
        if not filename:
            return
        
        try:
            quiz = Quiz.load(filename)
            name = os.path.splitext(os.path.basename(filename))[0]
            self.quizzes[name] = quiz
            print(f"\n✅ Loaded quiz: {quiz.title}")
            
            take_now = input("Take this quiz now? (y/n): ").strip().lower()
            if take_now == 'y':
                self.take_quiz(name)
        except QuizLoadError as e:
            print(f"❌ {e}")
    
    def create_quiz(self):
        """Create a custom quiz"""
        print("\n✏️ CREATE CUSTOM QUIZ")
        print("-" * 40)
        
        title = input("Quiz title: ").strip()
        if not title:
            print("❌ Title is required")
            return
        
        description = input("Description (optional): ").strip()
        
        quiz = Quiz(title, description)
        
        print("\nAdd questions (type 'done' when finished)")
        print("Question types: 1=Multiple Choice, 2=True/False, 3=Fill Blank")
        
        question_num = 1
        while True:
            print(f"\n--- Question {question_num} ---")
            q_type = input("Type (1/2/3) or 'done': ").strip()
            
            if q_type.lower() == 'done':
                break
            
            try:
                if q_type == '1':
                    question = self.create_multiple_choice()
                elif q_type == '2':
                    question = self.create_true_false()
                elif q_type == '3':
                    question = self.create_fill_blank()
                else:
                    print("Invalid type")
                    continue
                
                if question:
                    quiz.add_question(question)
                    question_num += 1
                    print(f"✅ Question added ({quiz.question_count} total)")
            except Exception as e:
                print(f"❌ Error: {e}")
        
        if quiz.questions:
            name = title.lower().replace(' ', '_')
            self.quizzes[name] = quiz
            print(f"\n✅ Quiz '{title}' created with {quiz.question_count} questions")
            
            take_now = input("Take this quiz now? (y/n): ").strip().lower()
            if take_now == 'y':
                self.take_quiz(name)
        else:
            print("\n❌ No questions added. Quiz not saved.")
    
    def create_multiple_choice(self):
        """Create a multiple choice question"""
        text = input("Question text: ").strip()
        if not text:
            return None
        
        print("Enter options (empty line to finish):")
        options = []
        while True:
            opt = input(f"  Option {len(options)+1}: ").strip()
            if not opt:
                break
            options.append(opt)
        
        if len(options) < 2:
            print("Need at least 2 options")
            return None
        
        correct_num = input("Correct answer number: ").strip()
        try:
            correct_idx = int(correct_num) - 1
            if 0 <= correct_idx < len(options):
                correct = options[correct_idx]
            else:
                print("Invalid option number")
                return None
        except ValueError:
            print("Invalid number")
            return None
        
        points = int(input("Points [1]: ").strip() or "1")
        hint = input("Hint (optional): ").strip() or None
        
        return MultipleChoiceQuestion(
            text=text,
            options=options,
            correct_answer=correct,
            points=points,
            hint=hint
        )
    
    def create_true_false(self):
        """Create a true/false question"""
        text = input("Statement: ").strip()
        if not text:
            return None
        
        correct = input("True or False? (T/F): ").strip().lower()
        correct_bool = correct in ['t', 'true']
        
        points = int(input("Points [1]: ").strip() or "1")
        hint = input("Hint (optional): ").strip() or None
        
        return TrueFalseQuestion(
            text=text,
            correct_answer=correct_bool,
            points=points,
            hint=hint
        )
    
    def create_fill_blank(self):
        """Create a fill in the blank question"""
        text = input("Question (use ___ for blank): ").strip()
        if not text:
            return None
        
        correct = input("Correct answer: ").strip()
        if not correct:
            return None
        
        case_sensitive = input("Case sensitive? (y/n) [n]: ").strip().lower() == 'y'
        points = int(input("Points [1]: ").strip() or "1")
        hint = input("Hint (optional): ").strip() or None
        
        return FillBlankQuestion(
            text=text,
            correct_answer=correct,
            case_sensitive=case_sensitive,
            points=points,
            hint=hint
        )
    
    def view_history(self):
        """View results history"""
        if not self.results_history:
            print("\n📭 No quiz history yet")
            return
        
        print("\n📊 RESULTS HISTORY")
        print("=" * 60)
        
        for i, result in enumerate(self.results_history, 1):
            print(f"\n{i}. {result.quiz_title}")
            print(f"   Date: {result.timestamp.strftime('%Y-%m-%d %H:%M')}")
            print(f"   Score: {result.earned_points}/{result.total_points} ({result.percentage}%)")
            print(f"   Grade: {result.grade}")
    
    def save_quiz(self):
        """Save a quiz to file"""
        print("\nAvailable quizzes:")
        for name in self.quizzes:
            print(f"  - {name}")
        
        quiz_name = input("\nQuiz to save: ").strip()
        if quiz_name not in self.quizzes:
            print("❌ Quiz not found")
            return
        
        filename = input("Save as (e.g., my_quiz.json): ").strip()
        if not filename:
            filename = f"{quiz_name}.json"
        
        self.quizzes[quiz_name].save(filename)
        print(f"\n✅ Quiz saved to {filename}")

# ============================================================================
# DEMO
# ============================================================================

def demo():
    """Demonstrate quiz game features"""
    print("🎮 QUIZ GAME - DEMO")
    print("=" * 60)
    
    # Create and display quiz structure
    quiz = create_python_quiz()
    
    print(f"\n📋 Quiz: {quiz.title}")
    print(f"Description: {quiz.description}")
    print(f"Questions: {quiz.question_count}")
    print(f"Total Points: {quiz.total_points}")
    
    print("\n📝 Question Preview:")
    print("-" * 40)
    for i, q in enumerate(quiz.questions[:3], 1):
        print(f"\n{i}. [{q.__class__.__name__}] ({q.points} pts)")
        print(f"   {q.text[:60]}...")
    print("\n   ...")
    
    # Simulate a session
    print("\n🎯 Simulating Quiz Session...")
    print("-" * 40)
    
    session = QuizSession(quiz, shuffle=False, allow_hints=True)
    
    # Manually simulate some answers
    questions = session.quiz.get_questions(shuffle=False)
    
    # Simulate answering some questions correctly
    questions[0].check_answer("2")  # x = 5 (correct)
    questions[0].answered_correctly = True
    
    questions[1].check_answer("3")  # str (correct)
    questions[1].answered_correctly = True
    
    questions[2].check_answer("1")  # Wrong answer
    questions[2].answered_correctly = False
    
    questions[3].check_answer("3")  # def (correct)
    questions[3].answered_correctly = True
    
    questions[4].check_answer("True")  # Correct
    questions[4].answered_correctly = True
    
    # Calculate result
    correct = sum(1 for q in questions if q.answered_correctly)
    earned = sum(q.points for q in questions if q.answered_correctly)
    
    result = QuizResult(
        quiz_title=quiz.title,
        questions_answered=5,
        correct_answers=correct,
        total_points=quiz.total_points,
        earned_points=earned,
        time_taken=125  # 2 minutes 5 seconds
    )
    
    result.display()
    
    print("\n" + "=" * 60)
    print("✅ Demo complete!")
    print("=" * 60)

# Run
if __name__ == "__main__":
    print("\n1. Run Demo")
    print("2. Play Interactive Quiz")
    choice = input("\nChoice (1/2): ").strip()
    
    if choice == "2":
        game = QuizGameCLI()
        game.run()
    else:
        demo()
