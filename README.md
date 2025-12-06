# 🐍 Python Learning Path - Complete Beginner's Guide

Welcome to your comprehensive Python learning journey! This repository is structured to take you from absolute beginner to confident Python programmer with **40 lessons** organized into **11 modules** plus **4 practice projects**.

## 📚 Course Overview

| Module | Topic | Lessons | Files |
|--------|-------|---------|-------|
| 01 | Python Basics | 1-4 | 4 notebooks |
| 02 | Operators | 5-9 | 5 notebooks |
| 03 | Control Flow | 10-12 | 3 files |
| 04 | Data Structures | 13-17 | 5 notebooks |
| 05 | Loops | 18-21 | 4 notebooks |
| 06 | Functions | 22-26 | 5 notebooks |
| 07 | Math & Utilities | 27 | 1 notebook |
| 08 | OOP Basics | 28-32 | 5 files |
| 09 | OOP Advanced | 33-36 | 4 files |
| 10 | Exception Handling | 37-38 | 2 notebooks |
| 11 | Regular Expressions | 39-40 | 2 notebooks |
| - | Practice Projects | - | 4 projects |

---

## 🚀 Getting Started - Installation & Setup

### 1. Python Installation Options

#### Option A: Standard Python Installation
- **Download Python**: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Windows Users**: [Python Installation on Windows.pdf](./Python%20Installation%20on%20Windows.pdf) (Available in this repository)
- **Installation Guide**: Choose "Add Python to PATH" during installation
- **Verify Installation**: Open Command Prompt/Terminal and type `python --version`

#### Option B: Anaconda Python Distribution (Recommended for Data Science)
- **Download Anaconda**: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
- **Installation Guide**: [Anaconda_Python_installation_guide.pdf](./Anaconda_Python_installation_guide.pdf) (Available in this repository)
- **Benefits**: Pre-installed packages, Jupyter Notebooks, Package management with conda
- **Verify Installation**: Open Anaconda Prompt and type `python --version`

### 2. Development Environment Setup

#### Option A: Visual Studio Code (VS Code) - Recommended for Beginners
- **Download VS Code**: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
- **Required Extensions**:
  - Python Extension: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - Jupyter Extension: [https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- **Configuration Steps**:
  1. Install VS Code
  2. Install Python extension from Extensions marketplace
  3. Open Command Palette (Ctrl+Shift+P) → "Python: Select Interpreter"
  4. Choose your Python installation

#### Option B: PyCharm IDE
- **Community Edition (Free)**: [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)
- **Professional Edition**: [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/) (30-day free trial)
- **Configuration Steps**:
  1. Install PyCharm
  2. Create New Project
  3. Select Python Interpreter (the Python you installed)
  4. Configure project settings

### 3. Running Your First Python Program

#### In VS Code:
1. Open VS Code
2. Open a folder with a name of your choice (e.g., `python_projects`)
3. Inside the folder, create a new file with a `.py` extension (e.g., `hello.py`)
4. Type: `print("Hello, World!")`
5. Save the file (Ctrl+S)
6. Run the program:
  - **Method 1**: Click the "▶️" button in the top-right corner
  - **Method 2**: Right-click → "Run Python File in Terminal"
  - **Method 3**: Open Terminal (Ctrl+`) → type `python hello.py`

#### In PyCharm:
1. Open PyCharm
2. Create a New Project or open existing one
3. Right-click on project folder → New → Python File
4. Name your file (e.g., `hello.py`)
5. Type: `print("Hello, World!")`
6. Run the program:
   - **Method 1**: Right-click in editor → "Run 'hello'"
   - **Method 2**: Click the green ▶️ button next to the code
   - **Method 3**: Use keyboard shortcut Ctrl+Shift+F10

#### Expected Output:
```
Hello, World!
```

### 4. Working with Jupyter Notebooks
- **In VS Code**: Install Jupyter extension, then open `.ipynb` files
- **In Anaconda**: Launch Jupyter Notebook from Anaconda Navigator
- **In Browser**: Navigate to [https://jupyter.org/try](https://jupyter.org/try) for online Jupyter

### 5. Additional Resources
- **Python Official Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **Python Tutorial**: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- **VS Code Python Tutorial**: [https://code.visualstudio.com/docs/python/python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- **PyCharm Quick Start**: [https://www.jetbrains.com/help/pycharm/quick-start-guide.html](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)

---

## 📚 Learning Path - Course Contents

### 📖 Core Python Concepts

#### Fundamentals (Start Here!)
- **01_helloworld.py** 🎯  
  Your first Python program! This script demonstrates the classic "Hello, World!" program, which is often the first step in learning any programming language. It shows how to use the `print()` function to display output and includes a simple arithmetic example. The file is heavily commented to explain the syntax, the use of string literals, and the purpose of the print function in Python.

- **02_comments.py**  
  This file explains how to write comments in Python, covering both single-line comments (using `#`) and multi-line comments (using triple quotes). It discusses why comments are important for code documentation and how they can be used to annotate or temporarily disable code during development.

- **03_variables.py**  
  This script introduces variables in Python, showing how to assign values, use variables in expressions, and print results. It covers naming conventions, best practices for choosing variable names, and highlights Python's reserved keywords (with a list included in the comments). The file also provides tips for writing clear, maintainable code using variables.

- **04_datatypes.py**  
  This file explores Python's fundamental data types, including integers, floats, strings (both single-line and multi-line), booleans, lists, tuples, dictionaries, sets, and the special `None` type. It demonstrates how to create, access, and modify these types, and explains the concepts of mutability and immutability. The script also shows how to check the type of a variable using the `type()` function.

#### Operators & Decision Making
- **05_py_operators.ipynb**  
  This Jupyter notebook provides a hands-on introduction to Python operators. It covers arithmetic, assignment, comparison, logical, and bitwise operators, with code cells and markdown explanations. Each operator is demonstrated with practical examples, and the notebook includes explanations of how and when to use each type of operator in Python code.

- **05a_py_operators.ipynb**  
  This notebook organizes all major Python operators into categories: arithmetic, comparison, logical, assignment, bitwise, identity, membership, and ternary. Each operator is listed in a Python list with comments describing its function. This file serves as a quick reference or summary of Python's operator syntax and usage.

- **06_Conditional.ipynb**  
  This notebook introduces conditional statements in Python, including `if`, `elif`, and `else` constructs. It demonstrates how to use logical operators within conditions and introduces the `match` statement for pattern matching (available in recent Python versions). The notebook provides practical code examples for decision making and branching logic in Python programs.

#### Data Structures
- **07_data_structure_list.ipynb**  
  Comprehensive introduction to Python lists - creation, indexing, slicing, methods, and list comprehensions.

- **07b_Data_Structures_Dict.ipynb**  
  Deep dive into Python dictionaries - key-value pairs, methods, nested dictionaries, and practical applications.

- **07c_Data_Structures_Tuple.ipynb**  
  Understanding tuples - immutable sequences, tuple packing/unpacking, and when to use tuples vs lists.

- **07d_Data_Structures_Set.ipynb**  
  Sets in Python - unique elements, set operations, and mathematical set theory applications.

- **07e_DataStructure_Practice.ipynb**  
  Hands-on practice combining all data structures with real-world examples.

- **07f_String_Manipulation_practice.ipynb**  
  String methods, formatting, regular expressions, and text processing techniques.

#### Control Flow & Loops
- **08_loops.ipynb**  
  Introduction to loops in Python - `for` loops, `while` loops, nested loops, and loop control statements.

- **08a_loops.py** & **08b_loops_practical_02.py**  
  Practical loop examples and exercises to reinforce loop concepts.

- **08a_practice_loops_demo.ipynb**  
  Interactive practice with loops through various scenarios and challenges.

#### Functions & Advanced Concepts
- **09_math_functions.ipynb** & **09_math.py**  
  Mathematical functions, the math module, and numerical computations in Python.

- **10_functions_demo.ipynb**  
  Introduction to functions - defining functions, parameters, arguments, and scope.

- **10a_function_with_return.ipynb**  
  Functions that return values, multiple return values, and return statement best practices.

- **10b_functions_inside_functions.ipynb**  
  Nested functions, closures, and advanced function concepts.

- **10c_lambda_function.ipynb**  
  Lambda functions (anonymous functions), functional programming concepts, and practical applications.

#### Object-Oriented Programming (OOP)
- **11_classes_and_objects.ipynb**  
  Introduction to OOP concepts - classes, objects, attributes, and methods.

- **11a_class_with_constructor.py** through **11h_encapsulation_classmethod.ipynb**  
  Progressive OOP topics including constructors, instance/class variables, static methods, encapsulation, and advanced OOP concepts.

#### Inheritance & Advanced OOP
- **12_Inheritance.ipynb** through **12f_abstractdemo.py**  
  Complete inheritance tutorial covering single, multiple, multilevel, hierarchical, and hybrid inheritance patterns, plus abstract classes.

#### Error Handling & Advanced Topics
- **13_exception_handling.ipynb** & **13a_exception_handling.py**  
  Exception handling, try-except blocks, custom exceptions, and defensive programming.

- **14_pattern_findings.ipynb** & **14a_regular_expressions.ipynb**  
  Pattern matching, regular expressions, and text processing with regex.

### 📁 Practice Projects
- **classpractice/**: Additional class and object practice files
- **filehandling/**: File I/O operations and file manipulation examples

---

## 🎯 Recommended Learning Path

### Week 1: Python Foundations
1. Complete Python/Anaconda installation
2. Set up VS Code or PyCharm
3. Run your first program (01_helloworld.py)
4. Study: comments, variables, data types (02-04)

### Week 2: Operations & Logic
1. Master operators (05, 05a)
2. Learn conditional statements (06)
3. Practice with provided exercises

### Week 3: Data Management
1. Study all data structures (07 series)
2. Practice string manipulation
3. Work through data structure exercises

### Week 4: Control Flow
1. Master loops (08 series)
2. Combine loops with data structures
3. Complete loop practice challenges

### Week 5-6: Functions
1. Function basics (10 series)
2. Advanced function concepts
3. Math functions and modules (09)

### Week 7-8: Object-Oriented Programming
1. Classes and objects (11 series)
2. Inheritance concepts (12 series)
3. Build practice projects

### Week 9: Error Handling & Advanced Topics
1. Exception handling (13)
2. Regular expressions (14)
3. File handling operations

---

## 💡 Tips for Success

1. **Practice Daily**: Spend at least 30 minutes coding each day
2. **Run Every Example**: Don't just read - execute the code!
3. **Experiment**: Modify examples to see what happens
4. **Use Both Environments**: Try examples in both VS Code and PyCharm
5. **Start with .py files**: Master basics before moving to Jupyter notebooks
6. **Ask Questions**: Use comments in your code to explain your understanding

---

## 🔧 Troubleshooting Common Issues

### Python Not Found
- **Windows**: Reinstall Python with "Add to PATH" checked
- **Check Installation**: Run `python --version` in terminal

### VS Code Not Running Python
- Install Python extension
- Select correct Python interpreter (Ctrl+Shift+P → "Python: Select Interpreter")

### PyCharm Issues
- Check Python interpreter in Settings → Project → Python Interpreter
- Ensure project is configured correctly

---

## 📚 Additional Resources & References

### Official Documentation
- **Python.org**: [https://www.python.org/](https://www.python.org/)
- **Python Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **Python Tutorial**: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)

### Development Tools
- **VS Code**: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- **PyCharm**: [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)
- **Jupyter**: [https://jupyter.org/](https://jupyter.org/)
- **Anaconda**: [https://www.anaconda.com/](https://www.anaconda.com/)

### Package Management
- **PyPI (Python Package Index)**: [https://pypi.org/](https://pypi.org/)
- **Conda**: [https://docs.conda.io/](https://docs.conda.io/)

### Online Learning Platforms
- **Python.org Beginner's Guide**: [https://wiki.python.org/moin/BeginnersGuide](https://wiki.python.org/moin/BeginnersGuide)
- **Real Python**: [https://realpython.com/](https://realpython.com/)
- **Python Institute**: [https://pythoninstitute.org/](https://pythoninstitute.org/)

### Practice Platforms
- **LeetCode**: [https://leetcode.com/](https://leetcode.com/)
- **HackerRank**: [https://www.hackerrank.com/domains/python](https://www.hackerrank.com/domains/python)
- **Codewars**: [https://www.codewars.com/](https://www.codewars.com/)

---

## 🤝 Getting Help

1. **Read Error Messages**: Python provides helpful error messages
2. **Use Print Statements**: Debug by printing variable values
3. **Check Documentation**: Use `help()` function in Python
4. **Online Communities**: 
   - Stack Overflow: [https://stackoverflow.com/questions/tagged/python](https://stackoverflow.com/questions/tagged/python)
   - Reddit r/Python: [https://www.reddit.com/r/Python/](https://www.reddit.com/r/Python/)
   - Python Discord: [https://discord.gg/python](https://discord.gg/python)

---

## 🗺️ Complete Learning Roadmap

### **Phase 1: Foundations (Lessons 1-12)**

#### 📁 01_basics/
| Lesson | File | Topic |
|--------|------|-------|
| 1 | `01_hello_world.ipynb` | Hello World, print() |
| 2 | `02_comments_and_docs.ipynb` | Comments, docstrings |
| 3 | `03_variables_and_naming.ipynb` | Variables, naming |
| 4 | `04_data_types.ipynb` | int, float, str, bool |

#### 📁 02_operators/
| Lesson | File | Topic |
|--------|------|-------|
| 5 | `01_arithmetic_operators.ipynb` | +, -, *, /, //, %, ** |
| 6 | `02_assignment_operators.ipynb` | =, +=, -=, etc. |
| 7 | `03_comparison_operators.ipynb` | ==, !=, <, >, etc. |
| 8 | `04_logical_operators.ipynb` | and, or, not |
| 9 | `05_bitwise_operators.ipynb` | &, \|, ^, ~, <<, >> |

#### 📁 03_control_flow/
| Lesson | File | Topic |
|--------|------|-------|
| 10 | `01_if_else.ipynb` | if, elif, else |
| 11 | `02_match_case.ipynb` | Pattern matching |
| 12 | `03_control_flow_practice.py` | Practice exercises |

### **Phase 2: Data Structures & Loops (Lessons 13-21)**

#### 📁 04_data_structures/
| Lesson | File | Topic |
|--------|------|-------|
| 13 | `01_lists.ipynb` | Lists, methods |
| 14 | `02_tuples.ipynb` | Tuples, unpacking |
| 15 | `03_dictionaries.ipynb` | Key-value pairs |
| 16 | `04_sets.ipynb` | Sets, operations |
| 17 | `05_strings.ipynb` | String methods |

#### 📁 05_loops/
| Lesson | File | Topic |
|--------|------|-------|
| 18 | `01_for_loops.ipynb` | For loops, range() |
| 19 | `02_while_loops.ipynb` | While loops |
| 20 | `03_loop_control.ipynb` | break, continue |
| 21 | `04_pattern_printing.ipynb` | Nested loops, patterns |

### **Phase 3: Functions & Math (Lessons 22-27)**

#### 📁 06_functions/
| Lesson | File | Topic |
|--------|------|-------|
| 22 | `01_function_basics.ipynb` | def, parameters |
| 23 | `02_return_values.ipynb` | Return statements |
| 24 | `03_lambda_functions.ipynb` | Lambda, map, filter |
| 25 | `04_scope.ipynb` | Local, global scope |
| 26 | `05_recursion.ipynb` | Recursive functions |

#### 📁 07_math_and_utilities/
| Lesson | File | Topic |
|--------|------|-------|
| 27 | `01_math_module.ipynb` | Math functions |

### **Phase 4: Object-Oriented Programming (Lessons 28-36)**

#### 📁 08_oop_basics/
| Lesson | File | Topic |
|--------|------|-------|
| 28 | `01_classes_and_objects.ipynb` | Classes, __init__ |
| 29 | `02_constructors_and_methods.ipynb` | Methods |
| 30 | `03_encapsulation.ipynb` | Private, properties |
| 31 | `04_instance_vs_class.ipynb` | Instance vs class |
| 32 | `05_oop_practice.py` | OOP exercises |

#### 📁 09_oop_advanced/
| Lesson | File | Topic |
|--------|------|-------|
| 33 | `01_inheritance.ipynb` | Inheritance, super() |
| 34 | `02_polymorphism.ipynb` | Polymorphism |
| 35 | `03_abstract_classes.ipynb` | ABC, abstract |
| 36 | `04_advanced_oop_practice.py` | Advanced OOP |

### **Phase 5: Error Handling & Regex (Lessons 37-40)**

#### 📁 10_exception_handling/
| Lesson | File | Topic |
|--------|------|-------|
| 37 | `01_exception_basics.ipynb` | try, except, finally |
| 38 | `02_custom_exceptions.ipynb` | Custom exceptions |

#### 📁 11_regular_expressions/
| Lesson | File | Topic |
|--------|------|-------|
| 39 | `01_regex_basics.ipynb` | Patterns, matching |
| 40 | `02_regex_advanced.ipynb` | Groups, lookahead |

### **🏗️ Practice Projects**

| Project | File | Description |
|---------|------|-------------|
| 1 | `practice_projects/01_student_management.py` | Student Management System |
| 2 | `practice_projects/02_calculator.py` | Scientific Calculator |
| 3 | `practice_projects/03_contact_book.py` | Contact Book with file storage |
| 4 | `practice_projects/04_quiz_game.py` | Interactive Quiz Game |

---

## 🎉 Ready to Start Your Python Journey?

1. **Install Python** (choose Standard Python or Anaconda)
2. **Set up your IDE** (VS Code or PyCharm)  
3. **Start with 01_basics/** folder
4. **Follow the lessons in order** (1 through 40)
5. **Complete the practice projects** to solidify your skills

**Happy Coding! 🐍✨**

---

*This repository takes you from complete beginner to intermediate Python programmer with 40 structured lessons. Take your time, practice regularly, and experiment with the code examples!*