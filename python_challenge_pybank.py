import csv
import pandas as pd
import numpy as np

df_csv = pd.read_csv("/Users/zacharypitts/Desktop/Repos/class_repo/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv")
df = pd.DataFrame(df_csv)
totalMonths = len(df["Date"])
netProfitLoss = np.sum(df["Profit/Losses"])
sum_changes = 0
change = 0
value = 0
n = 0
tempProfit = 0
tempLosses = 0
tempDateProfit = 0 
tempDateLoss = 0

for value in df.iterrows():
    if (n < (totalMonths-1)):
        change = (df.iloc[n+1, 1])-(df.iloc[n, 1])

if (change > tempProfit): 
            tempProfit = change
            tempDateProfit = n+1

elif (change < tempLosses):
            tempLosses = change
            tempDateLoss = n+1
sum_changes = sum_changes + change
avgChangePL = sum_changes / (totalMonths-1)
n = n + 1
grtIncreaseProfits = df["Date"].iloc[tempDateProfit]
grtDecreaseLosses = df["Date"].iloc[tempDateLoss]
print(df)
print("\n")
print("Financial Analysis")
print("---------------------------------------")
print("Total Months: " + str(totalMonths))
print("Net Profit/Loss: " + "$" + str(netProfitLoss))
print("Average Change: " + "$" + str(round(avgChangePL, 2)))
print("Greatest Increase in Profits: " + str(grtIncreaseProfits) + "\t" + "($" + str(tempProfit) + ")")
print("Greatest Decrease in Losses: " + str(grtDecreaseLosses)  + "\t" + "($" + str(tempLosses) + ")")