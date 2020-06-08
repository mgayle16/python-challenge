import os
import csv

months = []
p_and_l = []
csvpath = os.path.join ('..', 'PyBank','Resources', 'Budget_Data.csv')
with open (csvpath) as Budget_CSV:
    csvreader = csv.reader(Budget_CSV)
    next(csvreader)
    for row in csvreader:
        months.append(str(row[0]))
        p_and_l.append(int(row[1]))
        
#This is to get the total months for the data given
total_months = len(months)

#calc for net loss or profit
net_losses = 0

for x in p_and_l:
    net_losses = net_losses + x

#Calc for avg. proft or loss
prior_mnth_amount = 0
avg_mnth_change_list = []

for x in range(len(p_and_l)):
    if x == 0:
        prior_mnth_amount = p_and_l[x]
    else:
        monthly_change = p_and_l[x] - prior_mnth_amount
        avg_mnth_change_list.append(monthly_change)
        prior_mnth_amount = p_and_l[x]

#Monthly average change
length = len(avg_mnth_change_list)
total = sum(avg_mnth_change_list)
avg_loss_profit = total / length
print(avg_loss_profit)

#min/max for the resptive month of data
month_max_reduction = ''
dollar_max_reduction = 0
month_max_jump = ''
dollar_max_jump = 0

for x in range(len(avg_mnth_change_list)):
    if avg_mnth_change_list[x] > dollar_max_jump:
        dollar_max_jump = avg_mnth_change_list[x]
        month_max_jump = months[x+1]
    elif avg_mnth_change_list[x] < dollar_max_reduction:
        dollar_max_reduction = avg_mnth_change_list[x]
        month_max_reduction = months[x+1]

print(f'Total Months: {total_months}')

print(f'Total: ${net_losses}')

print(f'Average Change: {avg_loss_profit}')

print(f'Greatest Increase in Profits: {month_max_jump} (${dollar_max_jump})')

print(f' Greatest Increase in Profits: {month_max_reduction}  (${dollar_max_reduction})')

    

