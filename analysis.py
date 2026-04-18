import pandas as pd

def create_dataframe(schedule):
    df = pd.DataFrame(schedule, columns=["Month", "EMI", "Principal", "Interest", "Balance"])

    df["Year"] = ((df["Month"] - 1) // 12 + 1).astype(int)

    df = df.round(2)

    return df

def yearly_summary(dAf):
    return
    df.groupby("Year")[["Principal", "Interest"]].sum()


def total_interest(df):
    return df["Interest"].sum()



