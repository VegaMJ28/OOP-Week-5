def add():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a + b
    print(c)


def sub():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a - b
    print(c)


def multiply():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a * b
    print(c)


def divide():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    if b == 0:
        print("Division by zero is not possible")

    else:
        c = a / b
        print(c)


while 1:
    print("Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice = input("Enter your choice: ")

    if choice == "5":
        break

    elif choice == "1":
        add()

    elif choice == "2":
        sub()

    elif choice == "3":
        multiply()

    elif choice == "4":
            divide()


    else:
        print("Invalid choice")