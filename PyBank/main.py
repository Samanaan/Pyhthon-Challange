
import csv

PyBankcvs = "Resources/Budget_Data.csv"

# Lists to store 2 columns of data
listofmonths = []
ProfitLosses = []
#___________________________________________________________
#Open .csv file and store the data inside
with open(PyBankcvs) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #read the header in and move to the next row
    for row in csvreader:
        listofmonths.append(row[0]) # Hold column 1/A
        ProfitLosses.append(row[1]) # Hold column 2/B
#___________________________________________________________
#Collecting stats from the columns pulled from the .csv file

changesOverPeriods = [] # list to collect the difference in profit/loss between two dates

numOfMonths = len(listofmonths) # Save num of months

# Problem with data type was throwing the error: unsupported operand type(s) for +: 'int' and 'str' 
# Note: to change the data type of a list use the following
sumOfProfitLoss = sum(map(int,ProfitLosses)) #Sum all profits and losses for the total period

# Run through the "ProfitLosses" list record the difference in profit/loss for each period (month to month)
oldnum = 0
newnum = 0
for num in ProfitLosses:
    newnum = int(num)
    if newnum > oldnum and oldnum != 0:
        changesOverPeriods.append(abs(oldnum - newnum))
    elif oldnum != 0:
        changesOverPeriods.append(abs(oldnum - newnum)* -1)
    oldnum = newnum


# Greatest increase in a period by searching through the above list
greatestIncrease = max(changesOverPeriods)

# Greatest decrease in a period by searching through the above list
greatestDecrease = min(changesOverPeriods)

# the average of the changes per period
averageChange = sum(changesOverPeriods) / len(changesOverPeriods)

# This can be paired down later
greatestIncreaseIndex = changesOverPeriods.index(greatestIncrease)
greatestDecreaseIndex = changesOverPeriods.index(greatestDecrease)

greatestIncreaseDate = listofmonths[greatestIncreaseIndex + 1]
greatestDecreaseDate = listofmonths [greatestDecreaseIndex + 1]


#________________________________________________________
# Print out stats for the user
print("Financial Analysis")
print("____________________________")
print("Total Months: " + str(numOfMonths)) #Print num of months
print("Total: $" + str(sumOfProfitLoss)) # Print
print("Average Change: $" + str(averageChange))
print("Greatest Increase in Profits: " + greatestIncreaseDate + " (" + str(greatestIncrease)+ ")")
print("Greatest Decrease in Profits: " + greatestDecreaseDate + " (" + str(greatestDecrease)+ ")")
#________________________________________________________
#Create the .csv file for later analysis

# List items together
finalStats= [numOfMonths,sumOfProfitLoss,averageChange,greatestIncrease,greatestDecrease]

# Set variable for output file
output_file = "analysis/Stats_PyBank.csv"

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Total Months", "Total Profits", "Average Change", "Greatest Increase in Profits ("+ greatestIncreaseDate + ")", "Greatest Decrease in Profits ("+ greatestDecreaseDate +")"])

    # Write in the stats row
    writer.writerow(finalStats)
