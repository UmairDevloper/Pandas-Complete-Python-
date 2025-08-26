import pandas as pd


# Raw Data 
data = {
    "Name": ["Ali", "Ahmed", "Khalid"],
    "Age": [25, 26, 27],
    "Gender": ["Male", "Male", "Female"]
}

# Creating DataFrame 
df = pd.DataFrame(data)

print(df)

# Filtering the data by single condition 

filtered_data = df[df["Age"] > 25]

print(filtered_data)

# Filtering the data by multiple conditions 

filtered_data = df[(df["Age"] > 25) & (df["Gender"] == "Male")]

print(filtered_data)