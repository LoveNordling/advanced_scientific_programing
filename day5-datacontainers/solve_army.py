import pandas as pd


raw_data = {
    "regiment": ["Nighthawks", "Nighthawks", "Nighthawks", "Nighthawks", "Dragoons", "Dragoons", "Dragoons", "Dragoons", "Scouts", "Scouts", "Scouts", "Scouts"],
    "company": ["1st", "1st", "2nd", "2nd", "1st", "1st", "2nd", "2nd", "1st", "1st", "2nd", "2nd"],
    "deaths": [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
    "battles": [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
    "size": [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
    "veterans": [1, 5, 62, 26, 73, 37, 949, 48, 435, 63, 345, 34],
    "readiness": ["high", "high", "medium", "medium", "medium", "high", "high", "low", "low", "medium", "medium", "high"],
    "armor": ["light", "light", "light", "heavy", "heavy", "light", "light", "light", "light", "heavy", "heavy", "heavy"],
    "deserters": [4, 24, 31, 2, 3, 13, 2, 2, 3, 7, 23, 21],
    "origin": ["Arizona", "Texas", "California", "Maine", "Florida", "Georgia", "Alaska", "Washington", "Oregon", "Wyoming", "Louisana", "Nevada"],
}

army = pd.DataFrame(raw_data).set_index("origin")

print(army["veterans"])
print(army[["veterans", "deaths"]])
print(army.columns)
print(army.loc[["Maine", "Alaska"], ["deaths", "size", "deserters"]])
print(army.iloc[3:8, 3:7])
print(army.iloc[4:])
print(army.iloc[:4])
print(army.iloc[:, 2:7])
print(army[army["deaths"] > 50])
print(army[(army["deaths"] > 500) | (army["deaths"] < 50)])
print(army[army["regiment"] != "Dragoons"])
print(army.loc[["Texas", "Arizona"]])
print(army.loc["Arizona"].iloc[2])
print(army["deaths"].iloc[2])
