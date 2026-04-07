import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Bestsellers.csv")
print(data.head())

print(data.info())

print(data.isnull().sum())

mean_temperature=np.mean(data["Temperature(C)"])
print(mean_temperature)

for i in range(1,13):
    month=data.loc[data["month"]==i]["Temperature(C)"]
    print("For month: "+str(i))
    print("Average Temperature is: "+str(np.mean(month)))
    print("The temperature std is: "+str(np.std(month)))