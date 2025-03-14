import pandas as pd

staff = pd.read_csv("staff.csv")

print(f"\nStaff data frame has the following columns: \n{list(staff.columns)}\n")

print(staff)

staff = pd.read_csv("staff.csv")

print(staff["name"].str[0])

staff = pd.read_csv("staff.csv")

print(staff["name"].str.split(" "))

# Параметр expand функции split можно использовать для создания отдельных столбцов после разделения. Затем мы можем выбрать нужный нам столбец.

staff["last_name"] = staff["name"].str.split(" ", expand=True)[1]

print(staff[["name","last_name"]])

staff["name_lower"] = staff["name"].str.lower()
print(staff[["name","last_name"]])

print(staff.query("name > 'John Doe'").start_date.str[:4].astype("int"))
