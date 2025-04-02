print("Gulmayo, Shayne Marie F.")
print("2BSIT-2")

record = {}

def add_data():
    key = input("Enter key: ")
    value = input("Enter value: ")
    record[key] = value
    print("Data added successfully!")
    print("Current Record:", record)

def delete_data():
    key = input("Enter key: ")
    value = input("Enter value: ")
    if key in record and record[key] == value:
        del record[key]
        print("Data deleted successfully!")
        print("Current Record:", record)
    else:
        print("Data not found in the record.")

def main():
    while True:
        print("\nRecord Keeping App")
        print("1. Add Data")
        print("2. Delete Data")
        print("3. End")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_data()
        elif choice == "2":
            delete_data()
        elif choice == "3":
            print("Thank You")
            break
        else:
            print("Invalid choice. Please choose again.")

main()