print("Gulmayo, Shayne Marie F.")
print("2BSIT-2")

def add_record():
    name = input("Enter Name: ")
    email = input("Enter Email Address: ")
    address = input("Enter Home Address: ")

    with open("records.txt", "a") as file:
        file.write(f"{name},{email},{address}\n")
    print("Record added successfully!")


def view_records():
    try:
        with open("records.txt", "r") as file:
            records = file.readlines()
            if records:
                print("All Records:")
                for record in records:
                    print(record.strip())
            else:
                print("No records found!")
    except FileNotFoundError:
        print("No records found!")


def clear_records():
    with open("records.txt", "w") as file:
        file.write("")
    print("All records cleared!")


def main():
    while True:
        print("\nRecord Keeping App")
        print("A. Add a Record")
        print("B. View All Records")
        print("C. Clear All Records")
        print("D. Exit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'A':
            add_record()
        elif choice == 'B':
            view_records()
        elif choice == 'C':
            clear_records()
        elif choice == 'D':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
