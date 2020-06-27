import csv
import os

PyBank = os.path.join("Resources", "budget_data.csv")
 
 # Create list to store data
monthchange = []
profit = []
date = []

# Track output variables 
TotalMonths_count = 0
net_total_pl = 0
total_change_profit =  0
Initial_profit = []
greatest_increase_profits = 0
greatest_decrease_losses = 0

    # print(f"CSV Header: {csv_header}")  

with open(PyBank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    
    for row in csvreader:
       # date.append(row[0]) #not doing anything
        TotalMonths_count +=1
        
        #profit.append(row[1])  #not needed
        net_total_pl += int(row[1])

        final_profit = int(row[1])
        if TotalMonths_count ==1:
            monthchange = row[1]
            Initial_profit.append(row[1])
            index = 0
        else:
            monthchange = final_profit -int(Initial_profit[index])
            Initial_profit.append(row[1])
            index = index + 1

            total_change_profit = total_change_profit + monthchange

        #Find low and high profits amount and date

        if int(monthchange) > greatest_increase_profits:
            greatest_increase_profits = int(monthchange)
            greatest_month = row[0]

        if int(monthchange) < greatest_decrease_losses:
            greatest_decrease_losses = int(monthchange)
            lowest_month = row[0] # this line of code will reference the day once it finds the lowest profit

average_profits = total_change_profit/(TotalMonths_count - 1)

print(f"Financial Analysis")
print(f"------------------------")
print(f"Total Months: {(TotalMonths_count)}")
print(f"Total:  $ {net_total_pl}")
print(f"Average Change: $ {average_profits}")
print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase_profits})")
print(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease_losses})")

Results_output = os.path.join("PyBankResults.txt")

with open(Results_output, 'w') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Total Months: {(TotalMonths_count)}\n")
    txtfile.write(f"Total:  $ {net_total_pl}\n")
    txtfile.write(f"Average Change: $ {average_profits}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase_profits})\n")
    txtfile.write(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease_losses})\n")


        



       