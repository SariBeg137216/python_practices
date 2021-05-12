def tax_of_in(income):
    if income <= 10000:
        payableTax = 0
    elif income <= 20000:
        payableTax = 10000 * 10 / 100
    else:
        payableTax = 10000 * 10 / 100
        payableTax += (income - 20000) * 20 / 100

    return payableTax


print(tax_of_in(55000))
