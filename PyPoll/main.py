
import csv

PyPollcvs = "Resources/election_data.csv"

#Initialize lists for reading the .csv
ballotID =[]
county = []
candidate = []
#________________________________________________________________
with open(PyPollcvs) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    pollHeader = next(csvreader)

    for row in csvreader:
        ballotID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
#________________________________________________________________
# list for condensed list of candidates (No duplicates)
candidatelistsimplified = []

# 1. Getting the total number of votes by the len function
totalNumVotes = len(ballotID)

# 2. Search through the candidate list and collect each name once
# Note this method works even if the candidate's name appears in seperate places because it checks the new list to see if it already has that name.
for index, item in enumerate(candidate):
    if candidate[index] != candidate[index - 1] and not item in candidatelistsimplified:
        candidatelistsimplified.append(item)

totalvotesforcandidate = [0] * len(candidatelistsimplified) # initialize list to count number of votes with length equal to number of candidates

# 3. Collects each instance of a candidates name checking against "candidatelistsimplified" adds 1 to the total votes of that candidate in the correct position of the index
for item in candidate:
    if item  == candidatelistsimplified[0]:
        totalvotesforcandidate[0] = totalvotesforcandidate[0] + 1
    elif item  == candidatelistsimplified[1]:
        totalvotesforcandidate[1] = totalvotesforcandidate[1] + 1
    elif item  == candidatelistsimplified[2]:
        totalvotesforcandidate[2] = totalvotesforcandidate[2] + 1

# 4.Finds the percentage of votes each candidate won and saves it to a new list
percentOfVotes =[]
for index, item in enumerate(totalvotesforcandidate):
    percentOfVotes.append(round((item / totalNumVotes)* 100,3))


# 5. Finds the winner from the total "totalvotesforcandidate" list and uses the index position to find the name associated with it
Winnerindex = totalvotesforcandidate.index(max(totalvotesforcandidate))
winner = candidatelistsimplified[Winnerindex]

#________________________________________________________________
# Print out the conclussion for the user.
print("\nElecation Results\n____________________________\n")
print("Total Votes: " + str(totalNumVotes) + "\n____________________________\n")

# Run through the list of candidats, percent vote and their total votes per each one.
for index, i in enumerate(candidatelistsimplified):
    print( i + ": " + str(percentOfVotes[index]) + "% (" + str(totalvotesforcandidate[index]) + ")\n")

print("____________________________ \n\n Winner: " + winner + "\n____________________________")
#________________________________________________________________
#Create a .csv file for later analysis.

# List items together
finalvotes= zip(candidatelistsimplified,percentOfVotes,totalvotesforcandidate,[totalNumVotes,""],[winner,""])

# Set variable for output file
output_file = "analysis/Stats_PyPoll.csv"

#  Open the output filex
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Candidate Names", "Percent Won of Total Votes", "Number of Votes Per Candidate","Total Number of Votes","Winner"])

    # Write in the stats row
    writer.writerows(finalvotes)






