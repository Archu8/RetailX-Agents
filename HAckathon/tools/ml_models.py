import pandas as pd

def forecast_demand():
    print("[ML] Forecasting demand from CSV...")
    df = pd.read_csv("data/demand_forecasting.csv")
    demand_by_product = df.groupby("Product ID")["Sales Quantity"].mean().to_dict()
    return demand_by_product