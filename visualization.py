import matplotlib.pyplot as plt

def plot_balance(df):
    plt.plot(df["Month"], df["Balance"])
    plt.title("Outstanding Balance")
    plt.xlabel("Month")
    plt.ylabel("Balance")
    plt.show()


def plot_interest_principal(df):
    plt.bar(df["Month"], df["Principal"], label="Principal")
    plt.bar(df["Month"], df["Interest"], bottom=df["Principal"], label="Interest")
    plt.legend()
    plt.show()