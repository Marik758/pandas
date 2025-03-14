import pandas as pd

grocery = pd.read_csv("grocery.csv")

# Creating the week column
grocery["sales_date"] = grocery["sales_date"].astype("datetime64[ns]")
grocery["week"] = grocery["sales_date"].dt.isocalendar().week

# Creating the pivot table
print(
  pd.pivot_table(
    data = grocery,
    values = "sales_quantity",
    index = "product_group",
    columns = "week",
    aggfunc = "sum"
  )
)