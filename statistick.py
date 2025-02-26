import pandas as pd

myseries = pd.Series([1, 2, 5, 7, 11, 36])

print(myseries.median())

sales = pd.read_csv("sales.csv")

print("mean: ")
print(sales["price"].mean())

print("median: ")
print(sales["price"].median())

print("mode: ")
print(sales["price"].mode()[0])

print("minimum: ")
print(sales["price"].min())

print("maximum: ")
print(sales["price"].max())