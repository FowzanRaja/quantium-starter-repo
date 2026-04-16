import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

tables = []

for file in files:
    data = pd.read_csv(file)

    data = data[data["product"] == "pink morsel"].copy()

    data["price"] = data["price"].replace("[$,]", "", regex=True).astype(float)

    data["Sales"] = data["quantity"] * data["price"]

    data = data[["Sales", "date", "region"]]

    data.columns = ["Sales", "Date", "Region"]

    tables.append(data)

finalData = pd.concat(tables, ignore_index=True)

finalData.to_csv("data/ProcessedQuantiumData.csv", index=False)