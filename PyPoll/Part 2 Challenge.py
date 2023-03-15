#import all the python modules
import os
import csv
import sys
import statistics


#Create filepath to the "election_data.csv" file for analysis
csvpath = os.path.join("Resources","election_data.csv")
#Checking results with Print
#print(csvpath)

#Open CSV file path
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    
    #Skipping the header
    csv_header = next(csv_reader)

    #Creating a new list to house results from the analysis
    ballot_id = []
    county_id = []
    candidate_id = []

    #Setting the unique count to zero
    unique_count = 0

    #Setting up each column as list based on the lists created in line 18 to 20
    for rows in csv_reader:
        ballot_id.append(rows [0])
        county_id.append(rows [1])
        candidate_id.append (rows [2])

    #Counting the number of votes each unique candidate has received, first setting up dictionary and list
    vote_count = {}
    vote_count_value = []

    #Looping through each row to determine the number of votes casted
    for name in candidate_id:
        if name in vote_count:
            vote_count[name] += 1
        else:
            vote_count[name] = 1

    #Counting the total number of rows to determine the number of votes caseted (Ballot ID's)
    total_votes_casted = len(ballot_id)
    #Checking results with Print
    # print(total_votes_casted)
    # print("-------------------------------------------------------")

    #Looping through each unique candicate name and then calcualting the relevant votes each candidate received
    election_result = ''
    for name in vote_count:
        election_result += (name + ": " + str(round(vote_count[name]/total_votes_casted*100,3)) + "% " + "(" + str(vote_count[name]) + ")\n")   
    election_result = election_result[:-1]
    #Checking results with Print
    # print(election_result)
    # print("-------------------------------------------------------")
    
    #winning candidate list
    Winning_Candidate = max(vote_count, key=vote_count.get)
    #Checking results with Print
    #print(f"Winner: {Winning_Candidate}")
    #print("-------------------------------------------------------")

    #Print out results to the terminal per the instructions
    print(f"Election Results")
    print(f"-------------------------------------------------------")
    print(f"Total Votes: {total_votes_casted}")
    print(f"-------------------------------------------------------")
    print(f"{election_result}")
    print(f"-------------------------------------------------------")
    print(f"Winner: {Winning_Candidate}")
    print(f"-------------------------------------------------------")

    #Function to export a text file with the analysis results
    #Creating a text file in Analysis folder which houses the results from the analysis of 'Election'
    text_file = os.path.join("Analysis","Election_Results.txt")
    with open(text_file, "w") as f:
        f.write(f"Election Results\n"
        f"-------------------------------------------------------\n"
        f"Total Votes: {total_votes_casted}\n"
        f"-------------------------------------------------------\n"
        f"{election_result}\n"
        f"-------------------------------------------------------\n"
        f"Winner: {Winning_Candidate}\n"
        f"-------------------------------------------------------\n"
        )

    #Print that analysis is completed to notify the user
    print(f"The analysis of the election data is now completed.")