import pandas as pd
import numpy as np


# sales = pd.read_csv("sales.csv")
#
# print(sales.head())


sales = pd.read_csv("sales.csv", usecols=["product_code","product_group","stock_qty"])

print(sales.head())

arr = np.random.randint(1, 10, size=(3,5))

df = pd.DataFrame(arr, columns=["A","B","C","D","E"])

print(df)

sales = pd.read_csv("sales.csv")

print(sales.dtypes)

print("As index:")
print(sales.columns)

print("As list:")
print(list(sales.columns))