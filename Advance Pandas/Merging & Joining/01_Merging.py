import pandas as pd

df_customers = pd.DataFrame({
    "CustomerID" : [1, 2, 3, 4, 5],
    "Name" : ["Ali", "Ahmed", "Khalid", "Waseem", "Muneeb"],
})

df_transaction = pd.DataFrame({
    "TransactionID" : [1, 2, 3, 4, 5],
    "CustomerID" : [1, 2, 3, 6, 5],
    "Amount" : [1000, 2000, 3000, 4000, 5000]
})

print("Inner Join\n")
print(pd.merge(df_customers, df_transaction, how="inner", on="CustomerID"))

print("Left Join\n")
print(pd.merge(df_customers, df_transaction, how="left", on="CustomerID"))

print("Right Join\n")
print(pd.merge(df_customers, df_transaction, how="right", on="CustomerID"))

print("Outer Join\n")
print(pd.merge(df_customers, df_transaction, how="outer", on="CustomerID"))

print("Cross Join\n")
print(pd.merge(df_customers, df_transaction, how="cross"))