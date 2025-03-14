import pandas as pd

first_date = pd.to_datetime("2021-10-10")
second_date = pd.to_datetime("2021-10-02")

diff = first_date - second_date

print(type(diff))
print("\n")
print(diff.days)