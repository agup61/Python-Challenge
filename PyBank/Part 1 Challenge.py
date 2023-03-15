#  Import Required Modules
import os
import csv
import statistics as st
import sys

#Create references to the CSV File - "budget_data.csv" 
csv_path = os.path.join("Resources","budget_data.csv")
with open (csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #identifying the headers of the csv
    csv_header = next(csvreader)
    
    #creating lists for the two data columns in the csv, along with the difference between each row
    date_column = []
    profit_loss_column = []
    diff_profit_loss_column = []
    
    # Loop through each row of data after the header, and append the relevant coloumns to the list setup in line 15
    for rows in csvreader:
        date_column.append(rows [0])
        profit_loss_column.append(int(rows [1]))

    # Calculate the total number of months included in the dataset, using the len function
    Number_of_months = len(date_column)
    #Print Check 
    #print(f"The total number of months is {Number_of_months}.")

    # Calculate the total profit/loss of the dataset, using the sum function
    Total_profit_loss = sum(profit_loss_column)
    #Print Check
    #print(Total_profit_loss)

    #Calculate the changes in "Profit/Losses" over the entire period on a month-by-month basis. 
    #Append difference to list setup in line 18
    for i in range(1,len(profit_loss_column)):
        #Extract the values in the specified column and convert them to floats
        current_value = float(profit_loss_column[i])
        pre_value = float(profit_loss_column[i-1])
        change = current_value - pre_value
        diff_profit_loss_column.append(change)
        #Print Check 
        #print(f"Change for row {i}: {change}")

    #Calcaulte avg change between periods in the dataset
    avg_change = round(st.mean(diff_profit_loss_column),2)
    #Print Check 
    #print(avg_change)
       
    #Calculate the greatest increase in profits (date and amount) over the entire period
    max_value = round(max(diff_profit_loss_column))
    #print("$" + str(max_value))
    index_max = diff_profit_loss_column.index(max_value) + 1
    max_month = date_column[index_max]
    #Print Check 
    #print(max_month)

    #Calculate the greatest decrease in profits (date and amount) over the entire period
    min_value = round(min(diff_profit_loss_column))
    #print("$" + str(min_value))
    index_min = diff_profit_loss_column.index(min_value) + 1
    min_month = date_column[index_min]
    #Print Check 
    #print(min_month)

#Print out results to the terminal per the instructions
print("_______________________________________________________")
print("Financial Analysis")
print("-------------------------------------------------------")
print(f"Total Months: {Number_of_months}")
print(f"Total: ${Total_profit_loss}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_value})")
print(f"Greatest Decrease in Profits: {min_month} (${min_value})")
print("_______________________________________________________")

#Function to export a text file with the results
#Creating a text file in Analysis folder which houses the results from the analysis of the financial summary of the company
text_output_file = os.path.join("Analysis","PyBank_Analsys_Results.txt") 
with open (text_output_file, "w") as f:
    f.write(f"_______________________________________________________\n"
    f"Financial Analysis\n"
    f"-------------------------------------------------------\n"
    f"Total Months: {Number_of_months}\n"
    f"Total: ${Total_profit_loss}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {max_month} (${max_value})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_value})\n"
    f"_______________________________________________________\n"
    )

    #Print that analysis is completed to notify the user
    print(f"The analysis of the company's financial data is now completed.")
