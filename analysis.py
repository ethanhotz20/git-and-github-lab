import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")    
print("NRows: ", len(df))
print("M_Price: ", df["Price"].mean())
print("Med_Price: ", df["Price"].median())

# Print the largest sale 
print("Max_Price: ", df["Price"].max())
# Print the smallest sale
print("Min_Price: ", df["Price"].min())
