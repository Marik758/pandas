import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales.loc[:4, ["product_code","product_group"]])


# print(sales.iloc[[5,6,7,8], [0,1]])
#
# print(sales.iloc[5:9, :2])
#
#
# import numpy as np
#
# df = pd.DataFrame(
#   np.random.randint(10, size=(4,4)),
#   index = ["a","b","c","d"],
#   columns = ["col_a","col_b","col_c","col_d"]
#   )
#
# print(df)
#
# print("\nSelect two rows and two columns using loc:")
# print(df.loc[["b","d"], ["col_a","col_c"]])