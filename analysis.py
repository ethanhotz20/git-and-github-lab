import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")    
print("Number of rows: ", len(df))
print("Mean Price: ", df["Price"].mean())
print("Median Price: ", df["Price"].median())

# Print the largest sale 
print("Largest Sale: ", df["Price"].max())
# Print the smallest sale
print("Smallest Sale: ", df["Price"].min())
