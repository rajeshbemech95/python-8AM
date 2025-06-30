# import numpy as np
import pandas as pd

# a = [1,2,3,4,5]
# print(a)
# a = np.array([1,2,3,4,5])

# print(a)
# int 4 8 2 float str 

s =pd.Series(["name1","name2","name3"])
print(s)

data = {
    "name": ["name1","name2","name3"],
    "age" : [25,30,35],
    "location" : ["chennai", "bangalore", "delhi"]
}

df = pd.DataFrame(data)
print(df)
df = df[df["age"] < 30]
print(df)
pd.read_excel