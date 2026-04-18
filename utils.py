class InvalidLoanError(Exception):
    pass


def validate(principal, rate, tenure):
    if principal <= 0:
        raise InvalidLoanError("Principal must be > 0")
    if rate < 0:
        raise InvalidLoanError("Rate cannot be negative")
    if tenure <= 0:
        raise InvalidLoanError("Tenure must be > 0")
