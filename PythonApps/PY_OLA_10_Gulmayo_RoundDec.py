import numpy as np

def displayMenu():
    print("\nRounding Decimals")
    print("[1] Truncation")
    print("[2] Rounding")
    print("[3] Floor")
    print("[4] Ceiling")
    print("[5] Summation")
    print("[6] Cumulative Summation")
    print("[0] Exit")
    choice = int(input("Please enter your choice: "))
    return choice
def main():
    print("Gulmayo, Shayne Marie F.")
    print("3BSIT-1")
    while True:
        choice = displayMenu()

        if choice == 0:
            print("Exiting program...")
            break
        elif choice == 1:
            print("\nTruncation")
            size = int(input("Enter size of the array: "))
            arr = [float(input(f"Enter element for array {i + 1}: ")) for i in range(size)]
            result = np.trunc(arr)
        elif choice == 2:
            print("\nRounding")
            size = int(input("Enter size of the array: "))
            arr = [float(input(f"Enter element for array {i + 1}: ")) for i in range(size)]
            result = np.round(arr)
        elif choice == 3:
            print("\nFloor")
            size = int(input("Enter size of the array: "))
            arr = [float(input(f"Enter element for array {i + 1}: ")) for i in range(size)]
            result = np.floor(arr)
        elif choice == 4:
            print("\nCeiling")
            size = int(input("Enter size of the array: "))
            arr = [float(input(f"Enter element for array {i + 1}: ")) for i in range(size)]
            result = np.ceil(arr)
        elif choice == 5:
            print("\nSummation")
            size = int(input("Enter size of the array: "))
            arr = [float(input(f"Enter element for array {i + 1}: ")) for i in range(size)]
            result = np.sum(arr)
        elif choice == 6:
            print("\nCumulative Summation")
            size = int(input("Enter size of the array: "))
            arr = [float(input(f"Enter element for array {i + 1}: ")) for i in range(size)]
            result = np.cumsum(arr)
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        print(f"\nOutput is {result}")


if __name__ == "__main__":
        main()