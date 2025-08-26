import pandas as pd


# Raw Data 
data = {
    "Name": ["Ali", "Ahmed", "Khalid"],
    "Age": [25, 26, 27],
    "Gender": ["Male", "Male", "Male"]
}

# Creating DataFrame 
df = pd.DataFrame(data)

# Creating the folder for that file 
df.to_csv("Updated_File.csv", index=False)