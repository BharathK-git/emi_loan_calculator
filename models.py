class Record:
    def __init__(self, name="LoanRecord"):
        self.name = name

    def display(self):
        print(f"Record: {self.name}")


class Loan(Record):
    def __init__(self, principal, rate, tenure):
        super().__init__("Loan")
        self.principal = principal
        self.rate = rate
        self.tenure = tenure
        self.emi = 0

    def compute_emi(self):
        r = self.rate / (12 * 100)
        n = self.tenure
        if r == 0:
            self.emi = self.principal
        else:
            self.emi = self.principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
        return self.emi

    def display(self):
        print(f"Loan: ₹{self.principal}, Rate: {self.rate}%, Tenure: {self.tenure} months, EMI: {round(self.emi, 2)}")


class Prepayment:
    def __init__(self, amount, month):
        self.amount = amount
        self.month = month
