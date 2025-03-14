import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan],
    "B": [2.4, 6.2, 5.1, np.nan],
    "C": ["foo","zoo","bar", np.nan]
})

df["A"] = df["A"].astype(pd.Int64Dtype())


print(df)

print(df.isna())

print(df.isna().sum())
