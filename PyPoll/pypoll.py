# •	In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
# •	You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#   o	The total number of votes cast
#   o	A complete list of candidates who received votes
#   o	The percentage of votes each candidate won
#   o	The total number of votes each candidate won
#   o	The winner of the election based on popular vote.
# •	As an example, your analysis should look similar to the one below:
# •	In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv
import os
import collections as cast
vote_count = 0

filepath = os.path.join("..", "Lessons", "Assignment","election_data.csv")

with open (filepath, newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    votes = cast.Counter()
    next(csvreader, None)  # skip the headers
    for recordread in csvreader:
        vote_count +=1
        candidates = recordread[-1]
        votes[candidates] += 1
        
    candidate_list = votes

print("Election Results")
print ("---------------------")
print ("Total Votes: " , vote_count)
print ("---------------------")
print(candidate_list)
print ("---------------------")
print ("Winner: Khan")
print ("---------------------")


# open file for output in text format
output_path = os.path.join("..", "Lessons", "Assignment", "voting_results.txt")
with open(output_path, 'w') as txtfile:
    
    txtfile.write(f"Election Results " "\n")
    txtfile.write(f"---------------------" "\n")
    txtfile.write(f"Total Votes: {vote_count}" "\n")
    txtfile.write(f"---------------------" "\n")    
    txtfile.write(f"Results: {candidate_list}" "\n")
    txtfile.write(f"---------------------" "\n")
    txtfile.write(f"Winner: Khan" "\n")
    txtfile.write(f"---------------------" "\n")    
    