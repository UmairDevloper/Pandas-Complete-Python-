import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin-1")


# Displaying the first 10 records of the data and last 10 records 
# df.head(10) 
# df,tail(10) 

print(f"\n\nHead of the data\n{df.head(10)}\n\nTail of the data\n{df.tail(10)}")