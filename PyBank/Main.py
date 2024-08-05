import os
import csv
csvpath = os.path.join('..', 'Pybank', 'Resources', 'budget_data.csv')
total_months = 0
net_profit_loss = 0
profit_loss_change = []
previous_profit_loss = None
greatest_pro_increase_date = ""
greatest_pro_increase = 0
gretest_pro_decrease = 0
gretest_pro_decrease_date = ""
average_change = 0
with open(csvpath) as csvfile:
    csv_read = csv.reader(csvfile, delimiter=",")
    next(csv_read)
    for row in csv_read:
        total_months += 1
        profit_loss = int(row[1])
        net_profit_loss += profit_loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            profit_loss_change.append(change)
            if change > greatest_pro_increase:
                greatest_pro_increase = change
                greatest_pro_increase_date = row[0]
            if change < gretest_pro_decrease:
                gretest_pro_decrease = change
                gretest_pro_decrease_date = row[0]
        previous_profit_loss = profit_loss
if profit_loss_change:
    average_change = sum(profit_loss_change) / len(profit_loss_change)


# write into text file 

output_file = os.path.join('..', 'Pybank', 'Analysis', 'financial_analysis.txt')
with open(output_file, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: $ {net_profit_loss}\n")
    textfile.write(f"Average Change: $ {average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_pro_increase_date, greatest_pro_increase}\n")
    textfile.write(f"Greatest Decrease in Profits: {gretest_pro_decrease_date, gretest_pro_decrease}\n")


print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_profit_loss}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_pro_increase_date, greatest_pro_increase}")
print(f"Greatest Decrease in Profits: {gretest_pro_decrease_date, gretest_pro_decrease}")




