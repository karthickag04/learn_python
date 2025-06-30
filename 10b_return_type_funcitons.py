def welcome():
    print("Welcome to the Python course!")


def operatorManipulation():
    print("Let's manipulate some operators!")
    a = 10
    b = 5
    return a + b, a - b, a * b, a / b

# welcome()
# print(operatorManipulation())

list01 = operatorManipulation()
print(list01)


for i in list01:
    print(i)

