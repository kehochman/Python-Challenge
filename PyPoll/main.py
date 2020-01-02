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
        candidate = line[2]

        #if candidate has other votes then add to vote tally
        if candidate in candidate_option:
            candidate_index = candidate_option.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidate_option.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(candidate_option)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidate_option[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidate_option)):
    print(f"{candidate_option[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"pypoll_results_summary.txt"

#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {num_votes}\n")
for count in range(len(candidate_option)):
    filewriter.write(f"{candidate_option[count]}: {percentages[count]}% ({vote_counts[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()