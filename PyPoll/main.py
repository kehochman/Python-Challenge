import os, csv

num_votes = 0
candidate_option = []
candidates_votes = {}
winner = ""
winner_count = 0

#set path
csvpath = r'C:\Users\kehoc\Documents\GWU-ARL-DATA-PT-12-2019-U-C\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv'

#open the file
with open(csvpath,newline="") as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    #go line by line and process each vote
    for line in csvreader:
        
        #add to total number of votes
        num_votes = num_votes + 1
        
        #candidate voted for
        candidate = line["Candidate"]
        if candidate not in candidate_option:
            candidate_option.append(candidate)
            candidates_votes[candidate]=0
        candidates_votes[candidate]+=1
        
        #if candidate has other votes then add to vote tally
        # if candidate in candidate_option:
            # candidate_index = candidate_option.index(candidate)
            # candidates_votes[candidate_index] = candidates_votes[candidate_index] + 1
        #else create new spot in list for candidate
        # else:
        #     candidate_option.append(candidate)
        #     candidates_votes.append(1)

#print results
output=(
    f"\nElection Results\n"
    f"--------------------------\n"
    f"Total Votes: {num_votes}\n"
    f"--------------------------\n"
)
percentages = []
max_votes = 0

# max_index = 0
#find percentage of vote for each candidate and the winner
# for count in range(len(candidate_option)):

for candidate in candidates_votes:
   
    # vote_percentage = candidates_votes[candidate]/num_votes*100
    # percentages.append(vote_percentage)
    
    if candidates_votes[candidate] > max_votes:
        max_votes = candidates_votes[candidate]
        
        # print(max_votes)
        # max_index = candidate
        winner = candidate
    output+=f"{candidate}: {candidates_votes[candidate]/num_votes*100:.3f}% ({candidates_votes[candidate]})\n"
output+=f"---------------------------\nWinner: {winner}\n---------------------------"
print(output)
write_file = "pypoll_results_summary.txt"

# #open write file
filewriter = open(write_file, mode = 'w')

# #print analysis to file
filewriter.write(output)

# filewriter.write("Election Results\n")
# filewriter.write("--------------------------\n")
# filewriter.write(f"Total Votes: {num_votes}\n")
# for count in range(len(candidate_option)):
#     filewriter.write(f"{candidate_option[count]}: {percentages[count]}% ({candidates_votes[count]})\n")
# filewriter.write("---------------------------\n")
# filewriter.write(f"Winner: {winner}\n")
# filewriter.write("---------------------------\n")
# #close file
# filewriter.close()