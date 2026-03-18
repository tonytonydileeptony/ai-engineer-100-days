def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    try:
     return a / b
    except ZeroDivisionError:
        print("can not divided by zero")
        


def multiply(a, b):
    return a * b


def operation(a, b):
    choice = input("Enter your option from 1-4: ")

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")


def main():
    print("=== Sample Calculator ===")

    while True:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("\nChoose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation(a, b)

        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != 'y':
            print("Goodbye 👋")
            break


if __name__ == "__main__":
    main()