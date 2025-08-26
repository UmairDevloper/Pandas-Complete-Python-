import pandas as pd


# Raw Data 
data = {
    "Name": ["Ali", "Ahmed", "Khalid", "Waseem", "Muneeb", "Emma", "Jack", "Hadi"],
    "Age": [25, 27, 27, 28, 54, 76, 43, 56],
    "Salary": [1000, 2000, 2000, 4000, 6000, 6000, 7000, 7000]
}

# Creating DataFrame 
df = pd.DataFrame(data)

print(df)

# Grouping 

# Grouping by single column 

grouped_df = df.groupby("Age")["Salary"].sum()

print(grouped_df)


# Grouping by multiple columns 

grouped_df = df.groupby(["Age", "Name"])["Salary"].sum()

print(grouped_df)