import pandas as pd


# Raw Data 
data = {
    "Name": ["Ali", "Ahmed", "Khalid", "Waseem", "Muneeb", "Emma", "Jack", "Hadi"],
    "Age": [25, 26, 27, 28, 54, 76, 43, 56],
}

# Creating DataFrame 
df = pd.DataFrame(data)

print(df)

# Aggregation

print(df["Age"].max())
print(df["Age"].min())
print(df["Age"].mean())
print(df["Age"].sum())
print(df["Age"].count())