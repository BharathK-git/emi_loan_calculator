from models import Loan, Prepayment
from calculations import generate_amortization
from prepayment import apply_prepayment
from analysis import create_dataframe, yearly_summary, total_interest
from visualization import plot_balance, plot_interest_principal
from storage import save_to_csv
from utils import validate


def main():
    print("\n========== EMI MASTER ==========")

    try:
        p = float(input("Enter Principal: "))
        r = float(input("Enter Rate (%): "))
        t = int(input("Enter Tenure (months): "))

        validate(p, r, t)

        loan = Loan(p, r, t)
        emi = loan.compute_emi()

        print("\n------ LOAN SUMMARY ------")
        loan.display()

        schedule = generate_amortization(loan)

        choice = input("\nDo prepayment? (y/n): ").strip().lower()

        if choice == 'y':
            amt = float(input("Enter prepayment amount: "))
            month = int(input("Enter month: "))

            pre = Prepayment(amt, month)

            schedule = apply_prepayment(loan, schedule, pre)

            print("\nPrepayment applied successfully.")

        df = create_dataframe(schedule)

        print("\n------ YEARLY SUMMARY ------")
        print(yearly_summary(df))

        print("\n------ TOTAL INTEREST ------")
        print(f"Total Interest Paid: {round(total_interest(df), 2)}")

        print("\n------ FILE STATUS ------")
        save_to_csv(df)

        print("\n------ VISUALIZATION ------")
        print("Displaying Balance Graph...")
        plot_balance(df)

        print("Displaying Interest vs Principal Chart...")
        plot_interest_principal(df)

        print("\n========== PROCESS COMPLETED ==========")

    except Exception as e:
        print("\n Error:", e)


if __name__ == "__main__":
    main()






