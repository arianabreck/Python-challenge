import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
output_file = "election_results.txt"
total_votes_cast = 0
candidate_votes = {}
total_votes_candidates = {}

with open(csvpath) as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')
    
    next(csv_read)
    
    for row in csv_read:
        total_votes_cast += 1

        candidate_name = row[2]
        
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1

winner_candidate = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes_cast}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage_votes = (votes / total_votes_cast) * 100
    total_votes_candidates[candidate] = votes
    print(f"{candidate}: {percentage_votes:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner_candidate}")
print("-------------------------")
print("Total Votes Each Candidate Won:")
for candidate, total_votes in total_votes_candidates.items():
    print(f"{candidate}: {total_votes}")

    
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total votes: {total_votes_cast}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage_votes = (votes / total_votes_cast) * 100
        total_votes_candidates[candidate] = votes 
        file.write(f"{candidate}: {percentage_votes:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner_candidate}\n")
    file.write("-------------------------\n")
    file.write("Totoal votes Each candidate won:\n")
    for candidate, total_votes in total_votes_candidates.items():
        file.write(f"{candidate}: {total_votes}\n")























# Print the final list of candidates who received votes
 #print("List of Candidates who received votes:")
#for candidate in candidate_list:
    #print(candidate)

















