def deductions(gross_salary, loan, hInsurance):
    tax = gross_salary * .12
    total_deductions = tax + loan + hInsurance
    return total_deductions, tax
