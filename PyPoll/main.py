import os
import csv 

PyPoll = os.path.join("Resources", "election_data.csv")

with open(PyPoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    vote_count = 0
    Khan_vote = []
    Correy_vote = []
    Li_vote = []
    Tooley_vote = []

    winner = []

    for row in csvreader:
        # Total Number of votes 
        vote_count +=1

        # Complete list of each candidate who received votes
        if (row[2]== 'Khan' ):
            Khan_vote.append(row[2])
        elif (row[2] == 'Correy' ):
            Correy_vote.append(row[2])
        elif (row[2] == 'Li'):
            Li_vote.append(row[2])
        elif (row[2] == "O""'""Tooley"):
            Tooley_vote.append(row[2])

            #Finding the total number of votes for each candidate
        total_vote_khan = len(Khan_vote)
        total_vote_correy = len(Correy_vote)
        total_vote_li = len(Li_vote)
        total_vote_tooley = len(Tooley_vote)

        # Percentage
        Khan_percentage = (total_vote_khan/vote_count)*100
        Correy_percentage = (total_vote_correy/vote_count)*100
        Li_percentage = (total_vote_li/vote_count)*100
        tooley_percentage = (total_vote_tooley/vote_count)*100


        #Lets find the winner

        winner  = [total_vote_khan, total_vote_tooley,total_vote_li, total_vote_correy]
        final_winner = max(winner)
        if final_winner == total_vote_khan:
            winner_name = "Khan"
        elif final_winner == total_vote_correy:
            winner_name = "Correy"
        elif final_winner == total_vote_li:
            winner_name = "Li"
        elif final_winner == total_vote_tooley:
            winner_name = "O""'""Tooley"
            

print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {(vote_count)}")
print(f"-------------------------")
print(f"Khan: {round(Khan_percentage, 2)}% (${total_vote_khan})")
print(f"Correy: {round(Correy_percentage, 2)}% (${total_vote_correy})")
print(f"Li: {round(Li_percentage, 2)}% (${total_vote_li})")
print(f"O'Tooley: {round(tooley_percentage, 2)}% (${total_vote_tooley})")
print(f"Winner: {winner_name}")

Results_output = os.path.join("PyPollResults.txt")

with open(Results_output, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"------------------------")
    txtfile.write(f"Total Votes: {(vote_count)}\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Khan: {Khan_percentage} (${total_vote_khan})\n")
    txtfile.write(f"Correy: {Correy_percentage} (${total_vote_correy})\n")
    txtfile.write(f"Li: {Li_percentage} (${total_vote_li})\n")
    txtfile.write(f"O'Tooley: {tooley_percentage} (${total_vote_tooley})\n")
    txtfile.write(f"Winner: {winner_name}")
    

    


