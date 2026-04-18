def apply_prepayment(loan, schedule, prepayment):

    r = loan.rate / (12 * 100)
    emi = loan.emi

    new_schedule = []
    balance = loan.principal

    for month in range(1, loan.tenure + 1):


        if month == prepayment.month:
            balance -= prepayment.amount
            if balance < 0:
                balance = 0

        interest = round(balance * r, 2)
        principal = round(emi - interest, 2)

        if principal > balance:
            principal = balance
            emi = principal + interest  # adjust EMI for last month

        balance = round(balance - principal, 2)

        new_schedule.append([month, round(emi, 2), principal, interest, balance])

        if balance <= 0:
            break

    return new_schedule
