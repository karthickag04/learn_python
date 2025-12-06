# PRACTICE PROJECT: Scientific Calculator
# Demonstrates: OOP, operator overloading, exception handling, math functions

import math
import re
from abc import ABC, abstractmethod
from functools import reduce

# ============================================================================
# EXCEPTIONS
# ============================================================================

class CalculatorError(Exception):
    """Base calculator exception"""
    pass

class DivisionByZeroError(CalculatorError):
    """Division by zero"""
    def __init__(self):
        super().__init__("Cannot divide by zero")

class InvalidExpressionError(CalculatorError):
    """Invalid mathematical expression"""
    def __init__(self, expression):
        super().__init__(f"Invalid expression: {expression}")

class InvalidOperationError(CalculatorError):
    """Invalid mathematical operation"""
    def __init__(self, operation, reason=""):
        message = f"Invalid operation: {operation}"
        if reason:
            message += f" ({reason})"
        super().__init__(message)

# ============================================================================
# NUMBER CLASS WITH OPERATOR OVERLOADING
# ============================================================================

class Number:
    """Custom number class demonstrating operator overloading"""
    
    def __init__(self, value):
        if isinstance(value, Number):
            self._value = value._value
        else:
            self._value = float(value)
    
    @property
    def value(self):
        return self._value
    
    # Arithmetic operators
    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self._value + other._value)
        return Number(self._value + other)
    
    def __radd__(self, other):
        return Number(other + self._value)
    
    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self._value - other._value)
        return Number(self._value - other)
    
    def __rsub__(self, other):
        return Number(other - self._value)
    
    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self._value * other._value)
        return Number(self._value * other)
    
    def __rmul__(self, other):
        return Number(other * self._value)
    
    def __truediv__(self, other):
        other_val = other._value if isinstance(other, Number) else other
        if other_val == 0:
            raise DivisionByZeroError()
        return Number(self._value / other_val)
    
    def __rtruediv__(self, other):
        if self._value == 0:
            raise DivisionByZeroError()
        return Number(other / self._value)
    
    def __floordiv__(self, other):
        other_val = other._value if isinstance(other, Number) else other
        if other_val == 0:
            raise DivisionByZeroError()
        return Number(self._value // other_val)
    
    def __mod__(self, other):
        other_val = other._value if isinstance(other, Number) else other
        if other_val == 0:
            raise DivisionByZeroError()
        return Number(self._value % other_val)
    
    def __pow__(self, other):
        other_val = other._value if isinstance(other, Number) else other
        return Number(self._value ** other_val)
    
    def __neg__(self):
        return Number(-self._value)
    
    def __abs__(self):
        return Number(abs(self._value))
    
    # Comparison operators
    def __eq__(self, other):
        other_val = other._value if isinstance(other, Number) else other
        return self._value == other_val
    
    def __lt__(self, other):
        other_val = other._value if isinstance(other, Number) else other
        return self._value < other_val
    
    def __le__(self, other):
        other_val = other._value if isinstance(other, Number) else other
        return self._value <= other_val
    
    def __gt__(self, other):
        other_val = other._value if isinstance(other, Number) else other
        return self._value > other_val
    
    def __ge__(self, other):
        other_val = other._value if isinstance(other, Number) else other
        return self._value >= other_val
    
    # String representations
    def __str__(self):
        if self._value == int(self._value):
            return str(int(self._value))
        return str(round(self._value, 10))
    
    def __repr__(self):
        return f"Number({self._value})"

# ============================================================================
# OPERATIONS
# ============================================================================

class Operation(ABC):
    """Abstract base class for operations"""
    
    @property
    @abstractmethod
    def name(self):
        pass
    
    @property
    @abstractmethod
    def symbol(self):
        pass
    
    @abstractmethod
    def execute(self, *args):
        pass
    
    @property
    def arity(self):
        """Number of arguments required"""
        return 2

class BinaryOperation(Operation):
    """Binary operation (takes 2 arguments)"""
    
    @property
    def arity(self):
        return 2

class UnaryOperation(Operation):
    """Unary operation (takes 1 argument)"""
    
    @property
    def arity(self):
        return 1

# Binary Operations
class Add(BinaryOperation):
    name = "Add"
    symbol = "+"
    
    def execute(self, a, b):
        return Number(a) + Number(b)

class Subtract(BinaryOperation):
    name = "Subtract"
    symbol = "-"
    
    def execute(self, a, b):
        return Number(a) - Number(b)

class Multiply(BinaryOperation):
    name = "Multiply"
    symbol = "×"
    
    def execute(self, a, b):
        return Number(a) * Number(b)

class Divide(BinaryOperation):
    name = "Divide"
    symbol = "÷"
    
    def execute(self, a, b):
        return Number(a) / Number(b)

class Power(BinaryOperation):
    name = "Power"
    symbol = "^"
    
    def execute(self, a, b):
        return Number(a) ** Number(b)

class Modulo(BinaryOperation):
    name = "Modulo"
    symbol = "%"
    
    def execute(self, a, b):
        return Number(a) % Number(b)

# Unary Operations
class SquareRoot(UnaryOperation):
    name = "Square Root"
    symbol = "√"
    
    def execute(self, a):
        val = float(a._value if isinstance(a, Number) else a)
        if val < 0:
            raise InvalidOperationError("Square root", "Cannot compute for negative numbers")
        return Number(math.sqrt(val))

class Factorial(UnaryOperation):
    name = "Factorial"
    symbol = "!"
    
    def execute(self, a):
        val = int(a._value if isinstance(a, Number) else a)
        if val < 0:
            raise InvalidOperationError("Factorial", "Cannot compute for negative numbers")
        if val > 170:
            raise InvalidOperationError("Factorial", "Number too large")
        return Number(math.factorial(val))

class Sine(UnaryOperation):
    name = "Sine"
    symbol = "sin"
    
    def execute(self, a):
        val = float(a._value if isinstance(a, Number) else a)
        return Number(math.sin(math.radians(val)))

class Cosine(UnaryOperation):
    name = "Cosine"
    symbol = "cos"
    
    def execute(self, a):
        val = float(a._value if isinstance(a, Number) else a)
        return Number(math.cos(math.radians(val)))

class Tangent(UnaryOperation):
    name = "Tangent"
    symbol = "tan"
    
    def execute(self, a):
        val = float(a._value if isinstance(a, Number) else a)
        return Number(math.tan(math.radians(val)))

class Log(UnaryOperation):
    name = "Log (base 10)"
    symbol = "log"
    
    def execute(self, a):
        val = float(a._value if isinstance(a, Number) else a)
        if val <= 0:
            raise InvalidOperationError("Logarithm", "Cannot compute for non-positive numbers")
        return Number(math.log10(val))

class NaturalLog(UnaryOperation):
    name = "Natural Log"
    symbol = "ln"
    
    def execute(self, a):
        val = float(a._value if isinstance(a, Number) else a)
        if val <= 0:
            raise InvalidOperationError("Natural Log", "Cannot compute for non-positive numbers")
        return Number(math.log(val))

# ============================================================================
# MEMORY
# ============================================================================

class Memory:
    """Calculator memory storage"""
    
    def __init__(self):
        self._value = Number(0)
        self._history = []
    
    def store(self, value):
        """Store value in memory"""
        self._value = Number(value)
        return self._value
    
    def recall(self):
        """Recall value from memory"""
        return self._value
    
    def add(self, value):
        """Add to memory"""
        self._value = self._value + Number(value)
        return self._value
    
    def subtract(self, value):
        """Subtract from memory"""
        self._value = self._value - Number(value)
        return self._value
    
    def clear(self):
        """Clear memory"""
        self._value = Number(0)
    
    def add_to_history(self, expression, result):
        """Add calculation to history"""
        self._history.append({
            'expression': expression,
            'result': result
        })
    
    def get_history(self):
        """Get calculation history"""
        return self._history.copy()
    
    def clear_history(self):
        """Clear history"""
        self._history.clear()

# ============================================================================
# CALCULATOR
# ============================================================================

class Calculator:
    """Scientific calculator with memory and history"""
    
    # Operation registry
    BINARY_OPS = {
        '+': Add(),
        '-': Subtract(),
        '*': Multiply(),
        '×': Multiply(),
        '/': Divide(),
        '÷': Divide(),
        '^': Power(),
        '**': Power(),
        '%': Modulo(),
    }
    
    UNARY_OPS = {
        'sqrt': SquareRoot(),
        '√': SquareRoot(),
        'sin': Sine(),
        'cos': Cosine(),
        'tan': Tangent(),
        'log': Log(),
        'ln': NaturalLog(),
        '!': Factorial(),
    }
    
    CONSTANTS = {
        'pi': math.pi,
        'π': math.pi,
        'e': math.e,
        'phi': (1 + math.sqrt(5)) / 2,  # Golden ratio
    }
    
    def __init__(self):
        self.memory = Memory()
        self._last_result = Number(0)
    
    @property
    def last_result(self):
        return self._last_result
    
    def calculate(self, a, operator, b=None):
        """Perform a calculation"""
        operator = str(operator).lower()
        
        # Unary operation
        if operator in self.UNARY_OPS:
            op = self.UNARY_OPS[operator]
            result = op.execute(a)
        # Binary operation
        elif operator in self.BINARY_OPS:
            if b is None:
                raise InvalidOperationError(operator, "Second operand required")
            op = self.BINARY_OPS[operator]
            result = op.execute(a, b)
        else:
            raise InvalidOperationError(operator, "Unknown operator")
        
        # Store result
        self._last_result = result
        expr = f"{a} {operator} {b}" if b is not None else f"{operator}({a})"
        self.memory.add_to_history(expr, result)
        
        return result
    
    def evaluate_expression(self, expression):
        """Evaluate a mathematical expression string"""
        # Replace constants
        expr = expression.lower()
        for name, value in self.CONSTANTS.items():
            expr = expr.replace(name, str(value))
        
        # Replace 'ans' with last result
        expr = expr.replace('ans', str(self._last_result))
        
        # Handle unary functions: sin(x), cos(x), etc.
        for func_name in ['sqrt', 'sin', 'cos', 'tan', 'log', 'ln']:
            pattern = rf'{func_name}\(([^)]+)\)'
            while re.search(pattern, expr):
                match = re.search(pattern, expr)
                if match:
                    inner = match.group(1)
                    try:
                        inner_val = self._safe_eval(inner)
                        result = self.UNARY_OPS[func_name].execute(inner_val)
                        expr = expr[:match.start()] + str(result) + expr[match.end():]
                    except Exception as e:
                        raise InvalidExpressionError(expression)
        
        # Handle factorial: 5!
        while '!' in expr:
            pattern = r'(\d+)!'
            match = re.search(pattern, expr)
            if match:
                num = int(match.group(1))
                result = self.UNARY_OPS['!'].execute(num)
                expr = expr[:match.start()] + str(result) + expr[match.end():]
            else:
                break
        
        # Handle power with ^
        expr = expr.replace('^', '**')
        
        # Evaluate remaining expression
        try:
            result = Number(self._safe_eval(expr))
            self._last_result = result
            self.memory.add_to_history(expression, result)
            return result
        except ZeroDivisionError:
            raise DivisionByZeroError()
        except Exception:
            raise InvalidExpressionError(expression)
    
    def _safe_eval(self, expr):
        """Safely evaluate a mathematical expression"""
        # Only allow numbers, operators, and parentheses
        allowed = set('0123456789.+-*/()** ')
        expr_check = expr.replace(' ', '')
        
        # Check for any remaining letters (functions not replaced)
        if re.search(r'[a-zA-Z]', expr_check):
            raise InvalidExpressionError(expr)
        
        # Evaluate
        return eval(expr, {"__builtins__": {}}, {})
    
    # Statistical functions
    def mean(self, numbers):
        """Calculate mean of numbers"""
        if not numbers:
            raise InvalidOperationError("Mean", "Empty list")
        return Number(sum(numbers) / len(numbers))
    
    def median(self, numbers):
        """Calculate median of numbers"""
        if not numbers:
            raise InvalidOperationError("Median", "Empty list")
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        mid = n // 2
        if n % 2 == 0:
            return Number((sorted_nums[mid - 1] + sorted_nums[mid]) / 2)
        return Number(sorted_nums[mid])
    
    def std_dev(self, numbers):
        """Calculate standard deviation"""
        if len(numbers) < 2:
            raise InvalidOperationError("Standard Deviation", "Need at least 2 numbers")
        mean = sum(numbers) / len(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
        return Number(math.sqrt(variance))
    
    # Conversion functions
    def degrees_to_radians(self, degrees):
        """Convert degrees to radians"""
        return Number(math.radians(float(degrees)))
    
    def radians_to_degrees(self, radians):
        """Convert radians to degrees"""
        return Number(math.degrees(float(radians)))

# ============================================================================
# CLI INTERFACE
# ============================================================================

class CalculatorCLI:
    """Interactive calculator interface"""
    
    def __init__(self):
        self.calc = Calculator()
    
    def run(self):
        """Run the calculator"""
        self.show_banner()
        
        while True:
            try:
                expr = input("\n🔢 Enter expression (or 'help'): ").strip()
                
                if not expr:
                    continue
                
                command = expr.lower()
                
                if command in ('exit', 'quit', 'q'):
                    print("\n👋 Goodbye!")
                    break
                elif command == 'help':
                    self.show_help()
                elif command == 'history':
                    self.show_history()
                elif command == 'clear':
                    self.calc.memory.clear_history()
                    print("📋 History cleared")
                elif command.startswith('m'):
                    self.handle_memory(command)
                elif command == 'stats':
                    self.statistics_mode()
                else:
                    result = self.calc.evaluate_expression(expr)
                    print(f"   = {result}")
            
            except CalculatorError as e:
                print(f"❌ Error: {e}")
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
    
    def show_banner(self):
        """Show calculator banner"""
        print("\n" + "=" * 50)
        print("🔬 SCIENTIFIC CALCULATOR")
        print("=" * 50)
        print("Type expressions like: 2 + 3 * 4")
        print("Use 'help' for more commands")
        print("=" * 50)
    
    def show_help(self):
        """Show help information"""
        print("\n📖 HELP")
        print("=" * 50)
        print("\nBASIC OPERATIONS:")
        print("  +  Addition        -  Subtraction")
        print("  *  Multiplication  /  Division")
        print("  ^  Power           %  Modulo")
        
        print("\nSCIENTIFIC FUNCTIONS:")
        print("  sqrt(x)  Square root   sin(x)  Sine")
        print("  cos(x)   Cosine        tan(x)  Tangent")
        print("  log(x)   Log base 10   ln(x)   Natural log")
        print("  n!       Factorial")
        
        print("\nCONSTANTS:")
        print("  pi (π)   3.14159...    e       2.71828...")
        
        print("\nMEMORY:")
        print("  ms       Memory store  mr      Memory recall")
        print("  m+       Memory add    m-      Memory subtract")
        print("  mc       Memory clear")
        
        print("\nSPECIAL:")
        print("  ans      Previous result")
        print("  history  Show history")
        print("  clear    Clear history")
        print("  stats    Statistics mode")
        print("  exit     Exit calculator")
    
    def show_history(self):
        """Show calculation history"""
        history = self.calc.memory.get_history()
        if not history:
            print("\n📋 No history")
            return
        
        print("\n📋 CALCULATION HISTORY")
        print("-" * 40)
        for i, item in enumerate(history[-10:], 1):  # Last 10
            print(f"  {i}. {item['expression']} = {item['result']}")
    
    def handle_memory(self, command):
        """Handle memory commands"""
        mem = self.calc.memory
        
        if command == 'mr':
            print(f"   Memory: {mem.recall()}")
        elif command == 'mc':
            mem.clear()
            print("   Memory cleared")
        elif command.startswith('ms '):
            try:
                value = float(command[3:])
                mem.store(value)
                print(f"   Stored: {value}")
            except ValueError:
                print("❌ Invalid value")
        elif command.startswith('m+ '):
            try:
                value = float(command[3:])
                result = mem.add(value)
                print(f"   Memory: {result}")
            except ValueError:
                print("❌ Invalid value")
        elif command.startswith('m- '):
            try:
                value = float(command[3:])
                result = mem.subtract(value)
                print(f"   Memory: {result}")
            except ValueError:
                print("❌ Invalid value")
        else:
            print("❌ Unknown memory command")
    
    def statistics_mode(self):
        """Enter statistics mode"""
        print("\n📊 STATISTICS MODE")
        print("Enter numbers separated by commas, or 'exit' to return")
        
        while True:
            data = input("\nNumbers: ").strip()
            if data.lower() == 'exit':
                break
            
            try:
                numbers = [float(x.strip()) for x in data.split(',')]
                
                print(f"\n  Count: {len(numbers)}")
                print(f"  Sum: {sum(numbers)}")
                print(f"  Mean: {self.calc.mean(numbers)}")
                print(f"  Median: {self.calc.median(numbers)}")
                print(f"  Min: {min(numbers)}")
                print(f"  Max: {max(numbers)}")
                if len(numbers) >= 2:
                    print(f"  Std Dev: {self.calc.std_dev(numbers)}")
            except ValueError:
                print("❌ Invalid input. Use comma-separated numbers")
            except CalculatorError as e:
                print(f"❌ Error: {e}")

# ============================================================================
# DEMO
# ============================================================================

def demo():
    """Demonstrate calculator capabilities"""
    print("🔬 SCIENTIFIC CALCULATOR - DEMO")
    print("=" * 60)
    
    calc = Calculator()
    
    # Basic arithmetic
    print("\n📐 BASIC ARITHMETIC:")
    examples = [
        ("5 + 3", calc.calculate(5, '+', 3)),
        ("10 - 4", calc.calculate(10, '-', 4)),
        ("6 × 7", calc.calculate(6, '*', 7)),
        ("20 ÷ 4", calc.calculate(20, '/', 4)),
        ("2 ^ 8", calc.calculate(2, '^', 8)),
        ("17 % 5", calc.calculate(17, '%', 5)),
    ]
    for expr, result in examples:
        print(f"  {expr} = {result}")
    
    # Scientific functions
    print("\n🔬 SCIENTIFIC FUNCTIONS:")
    examples = [
        ("√(144)", calc.calculate(144, 'sqrt')),
        ("sin(30°)", calc.calculate(30, 'sin')),
        ("cos(60°)", calc.calculate(60, 'cos')),
        ("tan(45°)", calc.calculate(45, 'tan')),
        ("log(100)", calc.calculate(100, 'log')),
        ("ln(e)", calc.calculate(math.e, 'ln')),
        ("5!", calc.calculate(5, '!')),
    ]
    for expr, result in examples:
        print(f"  {expr} = {result}")
    
    # Expression evaluation
    print("\n📝 EXPRESSION EVALUATION:")
    expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "sqrt(16) + 2^3",
        "sin(30) + cos(60)",
        "log(1000) / 3",
        "pi * 2",
        "5!",
    ]
    for expr in expressions:
        result = calc.evaluate_expression(expr)
        print(f"  {expr} = {result}")
    
    # Using 'ans'
    print("\n🔄 USING PREVIOUS RESULT (ans):")
    result1 = calc.evaluate_expression("10 + 5")
    print(f"  10 + 5 = {result1}")
    result2 = calc.evaluate_expression("ans * 2")
    print(f"  ans * 2 = {result2}")
    result3 = calc.evaluate_expression("ans + 10")
    print(f"  ans + 10 = {result3}")
    
    # Statistics
    print("\n📊 STATISTICS:")
    numbers = [85, 90, 78, 92, 88, 76, 95]
    print(f"  Numbers: {numbers}")
    print(f"  Mean: {calc.mean(numbers)}")
    print(f"  Median: {calc.median(numbers)}")
    print(f"  Std Dev: {calc.std_dev(numbers)}")
    
    # Memory operations
    print("\n💾 MEMORY OPERATIONS:")
    calc.memory.store(100)
    print(f"  Store 100: Memory = {calc.memory.recall()}")
    calc.memory.add(50)
    print(f"  Add 50: Memory = {calc.memory.recall()}")
    calc.memory.subtract(25)
    print(f"  Subtract 25: Memory = {calc.memory.recall()}")
    
    # History
    print("\n📋 CALCULATION HISTORY (last 5):")
    for item in calc.memory.get_history()[-5:]:
        print(f"  {item['expression']} = {item['result']}")
    
    print("\n" + "=" * 60)
    print("✅ Demo complete!")
    print("=" * 60)

# Run
if __name__ == "__main__":
    print("\n1. Run Demo")
    print("2. Run Interactive Calculator")
    choice = input("\nChoice (1/2): ").strip()
    
    if choice == "2":
        cli = CalculatorCLI()
        cli.run()
    else:
        demo()
