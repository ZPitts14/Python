import csv
import pandas as pd
import numpy as np

df_csv = pd.read_csv("/Users/zacharypitts/Desktop/Repos/class_repo/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv")
df = pd.DataFrame(df_csv)
totalVotes = len(df)
totalCandidates = 0
totalCandidates = len(df.drop_duplicates("Candidate"))
name = ""
votes = 0
percentage = 0
winner = ""
def voting():
    n = 0
    for item in df.iterrows():
        if (n < totalCandidates):
            name = df.drop_duplicates("Candidate").iloc[n, 2]
            votes = df["Candidate"].value_counts().to_dict()
            votes = votes[name]
            percentage = votes / totalVotes
            n = n+1             
            print(name + ": " + '{:.3%}'.format(percentage) + "\t (" + str(votes) + ")")
            if(n == totalCandidates):
                return
winner = df["Candidate"].value_counts().idxmax()
def printResults(totalVotes, winner):
    print("Election Results")
    print("-------------------------------")
    print("Total Votes: " + str(totalVotes))
    print("-------------------------------")
    voting()
    print("-------------------------------")
    print("Winner: " + winner)
    print("-------------------------------")
printResults(totalVotes, winner)
