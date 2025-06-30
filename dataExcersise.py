import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# url = "https://raw.github.com/jbrownlee/Datasets/blob/master/monthly-writing-paper-sales.csv"
# df = pd.read_csv(url, parse_dates=["Months"])

df= pd.read_csv("monthly-paper-sales.csv")
# print(df)
print(df.head())
df.set_index("Month")

df["Sales MA"] = df["Sales"].rolling(window=3).mean()
df["pct_change"] = df["Sales"].pct_change() * 100
# jan + feb + mar  = 100 + 150 + 100 =350 = 115%

print(df["Sales MA"])
processed_frame = "processed.csv"
# df.to(processed_frame)


plt.figure(figsize=(10,5))
plt.plot(df.index, df["Sales"], label = "Monthly Sales", marker = "o")
plt.plot(df.index, df["Sales MA"], label = "Average of 3 months", linestyle = "--")

plt.title("Paper sales report")
plt.xlabel("month")
plt.ylabel("Average")
plt.grid(True)
plt.show()