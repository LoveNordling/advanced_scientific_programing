import sys

import pandas as pd


food = pd.read_csv(sys.argv[1], sep="\t")

print(food.head())
print(food.shape[0])
print(food.shape[1])
print(food.columns)
print(food.columns[104])
print(food.dtypes.iloc[104])
print(food.index)
print(food.loc[18, "product_name"])
