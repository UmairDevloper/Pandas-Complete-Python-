import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin-1")


# It displays the information (descriptive form) about the DataFrame 
print(df.describe())