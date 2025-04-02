print("Gulmayo, Shayne Marie F.")
print("2BSIT-2\n")

name = input("Employee Name: ")
hours = int(input("Enter number of hours: "))
sss = int(input("SSS contribution: "))
ph = int(input("Phil health: "))
loan = int(input("Housing loan: "))
print("===========PAYSLIP===========")
print("===========EMPLOYEE INFORMATION===========")
gs = hours*500
info = ("Employee Name: %s\n"
        "Rendered Hours: %d\n"
        "Rate per Hour: 500\n"
        "Gross Salary: %d") % (name, hours, gs)
print(info)
print("===========DEDUCTIONS===========")
td = (sss+ph+loan+500)
net = gs - td
deductions = ("SSS: %d\n"
              "PhilHealth: %d\n"
              "Other Loan: %d\n"
              "Tax: 500\n"
              "Total Deductions: %d\n\n"
              "Net Salary: PHP %d") % (sss, ph, loan, td, net)
print(deductions)





