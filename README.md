# Python-Challenge
Module 3 Challenge as part of Monash University Data Analytics Bootcamp

# PyBank
The Python script named "FinancialAnalysis.py" uses a dataset called "budget_data.csv" to analyze the financial records of a company. The dataset contains two columns, namely "Date" and "Profit/Losses". The script calculates the following financial metrics:

1. The total number of months covered in the dataset.
2. The net total amount of "Profit/Losses" for the entire period.
3. The changes in "Profit/Losses" for the entire period and their average value.
4. The date and amount of the greatest increase in profits for the entire period.
5. The date and amount of the greatest decrease in profits for the entire period.
6. Lastly, the script presents the analysis based on the above five points in the terminal and also exports the results in a text file called "Financial_Analysis_Results.txt" located in the "Analysis" folder.

## How to Use
1. To use this script, you can either clone this repository to your local machine or download the zip file and extract its contents.
2. Open the script in VS Code and run it.
3. The script generates the analysis, which is printed on the terminal, and also creates a text file named "Financial_Analysis_Results.txt" within a folder named "Analysis".

## Notes
* Place the "budget_data.csv" file in a folder called "Resources".
* The output text file will be generated in a directory named "Analysis".
* The script assumes that the CSV file contains a header row.
* The script expects the data to be in a specific format, with the Date in the first column and Profit/Losses in the second column. If the data is in a different format, the script needs to be adapted accordingly.

# PyPoll
This Python script analyzes election results using the "election_data.csv" dataset. The dataset has three columns: "Voter ID", "County", and "Candidate". The Python script named "ElectionAnalysis.py" performs the following calculations:

1. The total number of votes cast.
2. A comprehensive list of candidates who received votes.
3. The percentage of votes won by each candidate.
4. The total number of votes won by each candidate.
5. The winner of the election based on the popular vote.
6. Lastly, the script presents the analysis based on the above five points in the terminal and also exports the results in a text file called "Election_Results.txt" located in the "Analysis" folder.


## How to Use
1. To use this script, you can either clone this repository to your local machine or download the zip file and extract its contents.
2. Open the script in VS Code and run it.
3. The script generates the analysis, which is printed on the terminal, and also exports the results in a text file named "Election_Results.txt" to the "Analysis" folder.

## Notes
* Place the "election_data.csv" file in a folder called "Resources".
* The output text file will be generated in a directory named "Analysis".
* The script assumes that the CSV file contains a header row.
* The script expects the data to be in a specific format, with the Voter ID in the first column, County in the second column, and Candidate in the third column. If the data is in a different format, the script needs to be adapted accordingly.
