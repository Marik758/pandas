import pandas as pd

grocery = pd.read_csv("grocery.csv")

print("The size of the DataFrame:")
print(grocery.shape)

print("\nThe column names are:")
print(list(grocery.columns))

print("\nThe first five rows:")
print(grocery.head())



print(grocery.groupby("product_group").mean(numeric_only=True))

# print(grocery[["product_group","price"]].groupby("product_group").mean())


# print(grocery.groupby("product_group").agg(avg_price = ("price","mean")))


print(grocery.groupby("product_group").agg(avg_price = ("price","mean"),total_sales = ("sales_quantity", "sum")))


print(
  grocery.groupby("product_description").agg(
    avg_price = ("price","mean"),
    total_sales = ("sales_quantity", "sum")
  ).sort_values(
    by="total_sales",
    ascending=False
  )
)