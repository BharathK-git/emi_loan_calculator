import numpy as np

def generate_amortization(loan):
    balance = loan.principal
    r = loan.rate / (12 * 100)
    emi = loan.emi

    data = []

    for m in range(1, loan.tenure + 1):
        interest = balance * r
        principal = emi - interest
        balance -= principal

        data.append([m, emi, principal, interest, max(balance, 0)])

    return np.array(data)
