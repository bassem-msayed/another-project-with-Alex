import pandas as pd

df = pd.read_csv("data.csv")

df.head()

df.describe()

#let's see what the avearge value is

df["value"].mean()