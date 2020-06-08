import os
import csv

#my dictionary
candidates = {}

csvpath = os.path.join ('..', 'PyPoll','Resources', 'election_data.csv')
with open (csvpath) as election_csv:
    csvreader = csv.reader(election_csv)
    next(csvreader)
    for row in csvreader:
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1

all_votes_total = sum(candidates.values())

li_votes_percent = candidates['Li'] / all_votes_total * (100)
khan_votes_percent = candidates['Khan'] / all_votes_total * (100)
otooley_votes_percent = candidates["O'Tooley"] / all_votes_total * (100)
correy_votes_percent = candidates['Correy'] / all_votes_total* (100)

li_votes_total = candidates['Li']
khan_votes_total = candidates['Khan']
otooley_votes_total = candidates["O'Tooley"]
correy_votes_total = candidates['Correy']

# winner calcs
winner = ""

if li_votes_total > khan_votes_total and li_votes_total > otooley_votes_total and li_votes_total > correy_votes_total:
    winner = "Li"
elif khan_votes_total > li_votes_total and khan_votes_total > otooley_votes_total and khan_votes_total > correy_votes_total:
    winner = "Khan"
elif otooley_votes_total > li_votes_total and otooley_votes_total > khan_votes_total and otooley_votes_total > correy_votes_total:
    winner = "O'Tooley"
else:
    winner = "Correy"

#results
print("Election Results")
print("_________________________")
print(f'Total Votes: {all_votes_total}')
print("_________________________")
print (f'Li:{li_votes_percent}%({li_votes_total})')
print (f'Khan: {khan_votes_percent}%({khan_votes_total})')
print (f"O'Tooley: {otooley_votes_percent}%({otooley_votes_total})")
print (f'Correy: {correy_votes_percent}%({correy_votes_total})')
print("_________________________")
print(f'Winner: {winner}')
print("_________________________")