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

# Square Brackets (Straightforward) 

# df["Salary"] = [1000, 2000, 3000]
# print(df)

# Inserting a new column using insert() 

df.insert(3, "Salary", [1000, 2000, 3000])

print(df)