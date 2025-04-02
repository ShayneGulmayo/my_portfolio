import os

print("Gulmayo, Shayne Marie F.")
print("2BSIT-2")

class Reservation:
    def __init__(self, date, time, name, adults, children):
        self.date = date
        self.time = time
        self.name = name
        self.adults = adults
        self.children = children

    def subtotal(self):
        return self.adults * 500 + self.children * 300

    def __str__(self):
        return f"{self.date} {self.time} {self.name:15} {self.adults:7} {self.children:12} {self.subtotal():.2f}"


class ReservationSystem:
    def __init__(self):
        self.reservations = []
        self.load()

    def load(self):
        if os.path.exists("reservations.txt"):
            with open("reservations.txt", "r") as file:
                for line in file:
                    reservation_data = line.strip().split(",")
                    reservation = Reservation(
                        reservation_data[0],
                        reservation_data[1],
                        reservation_data[2],
                        int(reservation_data[3]),
                        int(reservation_data[4])
                    )
                    self.reservations.append(reservation)

    def save(self):
        with open("reservations.txt", "w") as file:
            for reservation in self.reservations:
                file.write(f"{reservation.date},{reservation.time},{reservation.name},"
                           f"{reservation.adults},{reservation.children}\n")

    def view(self):
        if not self.reservations:
            print("No reservations found.")
            return
        print("# Date       Time     Name            Adults  Children  Subtotal")
        for i, reservation in enumerate(self.reservations, start=1):
            print(f"{i} {reservation}")

    def create(self):
        try:
            name = input("Enter name: ")
            date = input("Enter date: ")
            time = input("Enter time: ")
            adults = int(input("Enter number of adults: "))
            children = int(input("Enter number of children: "))
            if adults < 0 or children < 0:
                raise ValueError("Number of adults and children cannot be negative.")
        except ValueError as e:
            print(f"Error: {e}")
            return
        reservation = Reservation(date, time, name, adults, children)
        self.reservations.append(reservation)
        self.save()
        print("Reservation made successfully!")

    def delete(self):
        try:
            rNumber = int(input("Enter reservation number to delete: "))
            if rNumber < 1 or rNumber > len(self.reservations):
                raise ValueError("Invalid reservation number.")
        except ValueError as e:
            print(f"Error: {e}")
            return
        del self.reservations[rNumber - 1]
        self.save()
        print("Reservation deleted successfully!")

    def generate_report(self):
        if not self.reservations:
            print("No reservations found.")
            return
        total_adults = sum(reservation.adults for reservation in self.reservations)
        total_children = sum(reservation.children for reservation in self.reservations)
        grand_total = sum(reservation.subtotal() for reservation in self.reservations)

        print("# Date       Time     Name            Adults  Children  Subtotal")
        for i, reservation in enumerate(self.reservations, start=1):
            print(f"{i} {reservation}")

        print(f"Total number of Adults: {total_adults}")
        print(f"Total number of Kids: {total_children}")
        print(f"Grand Total: PHP {grand_total:.2f}")

    def main(self):
        while True:
            print("\n1. View Reservations")
            print("2. Make Reservation")
            print("3. Delete Reservation")
            print("4. Generate Report")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.view()
            elif choice == "2":
                self.create()
            elif choice == "3":
                self.delete()
            elif choice == "4":
                self.generate_report()
            elif choice == "5":
                print("Thank you!")
                break
            else:
                print("Invalid choice. Please choose again.")

system = ReservationSystem()
system.main()
