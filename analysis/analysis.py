import pandas as pd
import numpy as np

df = pd.read_csv(r"A:\sales Dataset\archive\Sales Dataset.csv")

print(df.isnull().sum())

print("\n \n")

print(df.head())

print("\n \n")

print(df.info())

print("\n \n")

print(df.describe())

print("\n \n")

for i , col in enumerate(df.columns , 1):
    print(f"{i}. {col}")

df["Date"] = pd.to_datetime(df["Date"])

top_products = df.groupby("Product Category")["Total Amount"].sum().sort_values(ascending=False)


print(top_products.head())

top_volume = df.groupby("Product Category")["Quantity"].sum().sort_values(ascending=False)

print(top_volume)

daily_sales = df.groupby(["Product Category","Date"])["Total Amount"].sum()

consistency = daily_sales.groupby("Product Category").agg(
    mean_sales = np.mean,
    std_sales = np.std,
    var_sales = np.var
)

consistency = consistency.sort_values(by="std_sales")

print(consistency.head())

df["Month"] = df["Date"].dt.month

df["Month_Name"] = df["Date"].dt.strftime("%b")

monthly_sales = df.groupby(["Month_Name", "Product Category"])["Total Amount"].sum().reset_index()

print(monthly_sales)

monthly_volume = df.groupby(["Month_Name", "Product Category"])["Quantity"].sum().reset_index()

print(monthly_volume)

top_monthly = monthly_sales.sort_values(['Month_Name','Total Amount'],ascending=[True,False]).groupby(["Month_Name"]).head(1)

print(top_monthly)

# Revenue based aggregation 
product_sales = df.groupby("Product Category")["Total Amount"].sum().reset_index()

# Units sold aggregation
product_volume = df.groupby("Product Category")["Quantity"].sum().reset_index()


underperformers_revenue = product_sales.sort_values("Total Amount", ascending=True)
print(underperformers_revenue)

underperformers_volume = product_volume.sort_values("Quantity", ascending=True)
print(underperformers_volume)


