from PY_OLA_1A_Gulmayo_Salary import salary
from PY_OLA_1B_Gulmayo_Deductions import deductions

def net_salary(gross_salary, total_deductions):
    netSalary = gross_salary - total_deductions
    return netSalary

if __name__ == "__main__":
    print("Gulmayo, Shayne Marie F.")
    print("3BSIT-1\n")

    name = input("Enter Name: ")

    input = (
    int(input("Enter Hours: ")),
    float(input("Enter Loan: ")),
    float(input("Enter Health Insurance: "))
    )

    print("\n")

    gross_salary = salary(input[0])
    total_deductions, tax = deductions(gross_salary, input[1], input[2])
    net_salary = net_salary(gross_salary, total_deductions)

    print(f"Name: {name}")
    print(f"Hours: {input[0]}")
    print(f"Gross Salary: Php {gross_salary:.2f}")
    print(f"Tax: Php {tax:.2f}")
    print(f"Loan: Php {input[1]:.2f}")
    print(f"Health Insurance: Php {input[2]:.2f}")
    print(f"Total Deductions: Php {total_deductions:.2f}")
    print(f"Net Salary: Php {net_salary:.2f}")
