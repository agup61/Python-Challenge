# Python-Challenge
Module 3 Challenge as part of Monash University Data Analytics Bootcamp

# PyBank
This Python script analyses the financial records of a company using a dataset called "budget_data.csv". This dataset consists of two columns, "Date" and "Profit/Losses". The python code saved as "PyBank-main.py" calculates the following values:

1) The total number of months included in the dataset.
2) The net total amount of "Profit/Losses" over the entire period.
3) The changes in "Profit/Losses" over the entire period, and the average of those changes.
4) The greatest increase in profits (date and amount) over the entire period.
5) The greatest decrease in profits (date and amount) over the entire period.
6) Finally the script prints the analysis based on points 1 to 5 to the relevant terminal as well as exporting the results into text file titled "PyBank_Analysis_Results.txt" within the "Analysis" folder.

## How to Use
1) Clone this repository to your local machine or download the zip file and extract the contents.
2) Run the script using VS code.
3) The analysis will be printed to the terminal and a text file named "Financial_Analysis.txt" will be created in a folder named "Analysis".

## Notes
* The budget_data.csv file should be placed in a folder named "Resources".
* The results text file will be created in a folder named "Analysis".
* The script assumes that the header row in the CSV file is present.
* The script assumes that the data is in a specific format, with the Date in the first column and Profit/Losses in the second column. If the data is in a different format, the script will need to be modified accordingly.

# PyPoll
This Python script analyses election results based on the "election_data.csv" dataset. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". The Python script titled "PyPoll-main.py" analyses the votes and calculates the following:
1) The total number of votes cast
2) A complete list of candidates who received votes
3) The percentage of votes each candidate won
4) The total number of votes each candidate won
5) The winner of the election based on popular vote
6) Finally the script prints the analysis based on points 1 to 5 to the relevant terminal as well as exporting the results into text file titled "Election_Results.txt" within the "Analysis" folder.


## How to Use
1) Clone this repository to your local machine or download the zip file and extract the contents.
2) Run the script using VS code.
3) The script will output the analysis to the terminal and export a text file named "Election_Results.txt" to the "Analysis" folder.

## Notes
* The election_data.csv file should be placed in a folder named "Resources".
* The results text file will be created in a folder named "Analysis".
* The script assumes that the header row in the CSV file is present.
* The script assumes that the data is in a specific format, with the Voter ID in the first column, County in the second column, and Candidate in the third column. If the data is in a different format, the script will need to be modified accordingly.
