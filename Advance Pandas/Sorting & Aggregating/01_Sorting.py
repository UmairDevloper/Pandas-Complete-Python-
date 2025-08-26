import pandas as pd


# Raw Data 
data = {
    "Name": ["Ali", "Ahmed", "Khalid", "Waseem", "Muneeb", "Emma", "Jack", "Hadi"],
    "Age": [25, 26, 27, 28, 54, 76, 43, 56],
}

# Creating DataFrame 
df = pd.DataFrame(data)

print(df)


# Sorting using Single Column 
print("After Sorting single column\n")
df.sort_values(by="Age", ascending=True , inplace=True)

print(df)


# Sorting using Multiple Columns 
print("After Sorting multiple column\n")
df.sort_values(by=["Age", "Name"], ascending=[False, False] , inplace=True)

print(df)