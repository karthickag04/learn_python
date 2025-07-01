class OperatorsDemo:

    def add(self):
        a = 10
        b = 20
        print(a + b)

    def subtract(self):
        a = 10
        b = 20
        print(a - b)

    def multiply(self):
        a = 10
        b = 20
        print(a * b)

    def divide(self):
        a = 10
        b = 20
        print(a / b)


opDemo = OperatorsDemo()  # Create an instance of OperatorsDemo
opDemo.add()        # Call the add method
opDemo.subtract()   # Call the subtract method
opDemo.multiply()   # Call the multiply method
opDemo.divide()     # Call the divide method





class OperatorsDemo:

    @staticmethod
    def add():
        a = 10
        b = 20
        return a + b

    @staticmethod
    def subtract():
        a = 10
        b = 20
        print(a - b)


print(OperatorsDemo.add()  )      # Call the add method
OperatorsDemo.subtract()   # Call the subtract method



