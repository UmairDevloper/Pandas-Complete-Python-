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

# Selecting a single column 

print(df["Age"])

# Selecting multiple columns 

print(df[["Name", "Age"]])