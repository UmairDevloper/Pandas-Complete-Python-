import pandas as pd


# Raw Data 
data = {
    "Name": ["Ali", "Ahmed", "Khalid"],
    "Age": [25, 26, 27],
    "Gender": ["Male", "Male", "Male"]
}

# Creating DataFrame 
df = pd.DataFrame(data)

print(df)


# Specific column updating

# df.loc[1, "Age"] = 30

# print(df)

# Entire Column Updating 

df["Age"] = df["Age"] * 10

print(df)