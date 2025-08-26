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

missing_data = df.isnull().sum()

print(missing_data)
