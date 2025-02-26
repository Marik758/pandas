import pandas as pd

myseries = pd.Series([10, 20, 30])


myseries = pd.Series(
     [10,20,30],
     index = ["a","b","c"]
)

print(myseries)


myseries = pd.Series(
   ["Jane","John","Emily","Matt"]
)

# Print the first item
print(myseries[0])


myseries = pd.Series([1,2,3,2])
print(myseries.is_unique)


df = pd.DataFrame({
    "Name": ["Jane", "John", "Matt", "Ashley"],
    "Age": [24, 21, 26, 32]
}, index = ["a","b","c","a"])

print(df)
print(df.shape)
