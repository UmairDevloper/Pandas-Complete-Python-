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

df.drop("Age", axis=1, inplace=True)

print(df)