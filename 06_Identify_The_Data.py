import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin-1")


print(df)

# How big is the dataset and names of columns 

# Shape[rows, columns] 
print(df.shape)

# Columns Name 
print(df.columns)
