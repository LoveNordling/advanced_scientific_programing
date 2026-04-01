import pandas as pd


drinks = pd.read_csv("data/drinks.csv")

print(drinks.groupby("continent")["beer_servings"].mean().sort_values(ascending=False))
print(drinks.groupby("continent")["wine_servings"].describe())
print(drinks.groupby("continent").mean(numeric_only=True))
print(drinks.groupby("continent").median(numeric_only=True))
print(drinks.groupby("continent")["spirit_servings"].agg(["mean", "min", "max"]))
