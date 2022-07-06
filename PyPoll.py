# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candiate won
# 5. The winner of the election based on popular vote.
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources" , "election_results.csv")
#file_to_load = os.path('./Resource/election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis" , "election_analysis.txt")
#  Initialise the total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each Row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

# Print the candidate list.
print(candidate_options)

# Print the total votes.
print(total_votes)

