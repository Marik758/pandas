import pandas as pd

grocery = pd.read_csv("grocery.csv")

grocery["price_updated"] = grocery["price"].where(
  grocery["price"] >= 3,
  other = grocery["price"] * 1.1
)

print("Checking prices less than $3:")
print(grocery[grocery["price"] < 3][["price","price_updated"]].head())

print("\nChecking prices of $3 or more:")
print(grocery[grocery["price"] >= 3][["price","price_updated"]].head())