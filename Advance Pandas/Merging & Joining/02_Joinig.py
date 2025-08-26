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

print("Concatenation in rows\n")
print(pd.concat([df_customers, df_transaction], axis=0, ignore_index=True))

print("Concatenation in columns\n")
print(pd.concat([df_customers, df_transaction], axis=1, ignore_index=False))