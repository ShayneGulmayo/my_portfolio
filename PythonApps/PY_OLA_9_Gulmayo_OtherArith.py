import numpy as np

def displayMenu():
    print("\nSimple Arithmetic Operations")
    print("[1] Power")
    print("[2] Remainder")
    print("[3] Quotient")
    print("[4] Absolute")
    print("[5] Exit")
    choice = int(input("\nPlease enter your choice: "))
    return choice

def power(arr, arr2):
    result = np.power(arr, arr2)
    return result

def remainder(arr, arr2):
    result = np.remainder(arr, arr2)
    return result

def quotient(arr, arr2):
    result = np.divmod(arr, arr2)
    return result

def absolute(arr):
    result = np.absolute(arr)
    return result

def main():
    print("Gulmayo, Shayne Marie F.")
    print("3BSIT-1")
    while True:
        choice = displayMenu()

        if choice == 5:
            break
        elif choice == 1:
            print("Power")
            size = int(input("Enter size of the array: "))
            arr = [float(input(f"Enter element for array 1 {i+1}: ")) for i in range(size)]
            arr2 = [float(input(f"Enter element for array 2 {i+1}: ")) for i in range(size)]
            print(f"\nPower value is {power(arr, arr2)}.")

        elif choice == 2:
            print("Remainder")
            size = int(input("Enter size of the array: "))
            arr = [float(input(f"Enter element for array 1 {i+1}: ")) for i in range(size)]
            arr2 = [float(input(f"Enter element for array 2 {i+1}: ")) for i in range(size)]
            print(f"Remainder value is {remainder(arr, arr2)}.")

        elif choice == 3:
            print("Quotient")
            size = int(input("Enter size of the array: "))
            arr = [float(input(f"Enter element for array 1 {i+1}: ")) for i in range(size)]
            arr2 = [float(input(f"Enter element for array 2 {i+1}: ")) for i in range(size)]
            quotient_result, remainder_result = quotient(arr, arr2)
            print(f"Quotient is {quotient_result}, Remainder is {remainder_result}.")

        elif choice == 4:
            print("Absolute")
            size = int(input("\nEnter size of the array: "))
            arr = [float(input(f"Enter element for array 1 {i+1}: ")) for i in range(size)]
            print(f"Absolute values are {absolute(arr)}.")

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()