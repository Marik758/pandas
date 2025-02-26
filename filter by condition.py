


import pandas as pd

# read the sales csv file
sales = pd.read_csv("sales.csv")

# filter the sales data frame
# sales_filtered = sales[(sales["price"] > 100) & (sales["stock_qty"] < 400)]
sales_filtered = sales.query("price > 100 and stock_qty < 400")

# sales_filtered = sales[(sales["product_group"] == "PG1") | (sales["product_group"] == "PG2")]
#
# Есть и более практичный вариант - метод isin. Он принимает список значений, используемых для фильтрации.
# Мы можем выбрать товары, принадлежащие к группам товаров PG1, PG2 и PG3, следующим образом:

# sales_filtered = sales[sales["product_group"].isin(["PG1", "PG2", "PG3"])]


print(sales_filtered[["price","stock_qty"]].head())