import pandas as pd

df = pd.read_csv("data.csv")

df.head()

df.describe()

#let's see what the minimum value is

df["value"].min()
