print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

while True:
    try:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Enter the number of the operation: ")

        if operation not in ['1', '2', '3', '4']:
            raise ValueError()

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '4':
            if num2 == 0:
                raise ZeroDivisionError()
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

        repeat = input("Do you want to try again? (yes/no): ").lower()
        if repeat == 'no':
            print("Goodbye!")
            break

    except ValueError:
        print("Please enter numeric values only.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
