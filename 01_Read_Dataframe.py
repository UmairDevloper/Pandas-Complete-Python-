import pandas as pd


#  Reading the file 

#  CSV file
# df = pd.read_csv("sales_data_sample.csv", encoding="latin-1")

# Excel file
# df = pd.read_excel("sales_data_sample.xlsx")

# JSON file
df = pd.read_json("sample.json") 

print(df)