def taxcalc (income):
    # income = float(income)

    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 0.1
    else:
        tax = 0 + ((income - 10000) * 0.1) + ((income - 20000) * 0.2)

    return tax

tax = taxcalc(150000)
print(tax)