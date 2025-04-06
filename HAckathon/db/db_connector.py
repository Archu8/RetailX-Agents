import pandas as pd

def load_inventory_from_csv():
    df = pd.read_csv("data/inventory_monitoring.csv")
    return df.to_dict(orient="records")