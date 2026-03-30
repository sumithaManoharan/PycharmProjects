import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260122.csv")
# print(data.head(10))

counts = data["Primary Fur Color"].value_counts()

counts.to_csv("counts.csv")