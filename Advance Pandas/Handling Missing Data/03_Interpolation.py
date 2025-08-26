import pandas as pd


# Raw Data 
data = {
    "Name": ["Ali", "Ahmed", "Khalid"],
    "Age": [25, None, 27],
    "Gender": ["Male", "Male", "Male"]
}

# Creating DataFrame 
df = pd.DataFrame(data)

print(df)

# Interpolation is to fill the gap between the data points in a series. 

df.interpolate(method= "linear" , axis=0, inplace=True)

print(df)