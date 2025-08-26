import pandas as pd


# Raw Data 
data = {
    "Name": ["Ali", "Ahmed", None],
    "Age": [25, None, 27],
    "Gender": ["Male", "Male", "Male"]
}

# Creating DataFrame 
df = pd.DataFrame(data)

print(df)

# Removing the row if it contains any missing data
# df.dropna(axis=0, inplace=True)

# print(df)


# Filling the missing data with a specific value
df.fillna(0, inplace=True)

print(df)