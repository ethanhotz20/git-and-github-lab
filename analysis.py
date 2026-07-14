import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")    
print("Number of transactions: ", len(df))
print("Mean Transaction Price: ", df["Price"].mean())
print("Median Transaction Price: ", df["Price"].median())

# Print the largest sale 
print("Largest Transaction: ", df["Price"].max())
# Print the smallest sale
print("Smallest Transaction: ", df["Price"].min())
