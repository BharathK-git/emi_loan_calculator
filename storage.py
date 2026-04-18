import pandas as pd

def save_to_csv(df, filename="loan_data.csv"):
    try:
        df.to_csv(filename, index=False)
        print("Saved successfully.")
    except Exception as e:
        print("File Error:", e)


def load_csv(filename="loan_data.csv"):
    try:
        return pd.read_csv(filename)
    except Exception as e:
        print("Load Error:", e)
        return None
