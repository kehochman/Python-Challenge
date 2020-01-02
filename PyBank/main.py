import os
import csv

budget = r'C:\Users\kehoc\Documents\GWU-ARL-DATA-PT-12-2019-U-C\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv'

# open and read csv
with open(budget, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # find net amount of profit and loss
    P = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    rev_change = []

    for x in range(1, len(P)):
        rev_change.append((int(P[x]) - int(P[x-1])))
    
    # calculate average revenue change
    rev_average = sum(rev_change) / len(rev_change)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    great_increase = max(rev_change)
    # greatest decrease in revenue
    great_decrease = min(revenue_change)


    # print the Results
    print("Financial Analysis")

    print("....................................................................................")

    print("Total Months: " + str(total_months))

    print("Total: " + "$" + str(sum(P)))

    print("Average change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))


    # output to a text file

    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("Total Months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(P)) + "\n")

    file.write("Average Change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()


