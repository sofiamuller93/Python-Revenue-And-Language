# Modules
import os
import csv

# Set path for csv file
filepath = "C:\\Users\\Sofia\\OneDrive - Texas Tech University\\Personal\\Education\\Data Analysis Bootcamp\\Week 3 - Python I\\Homework 3\\python-challenge\\PyBank\\raw_data\\budget_data_1.csv"

Months = 0
Total_Revenue = 0
change = 0
prev_revenue = 0
greatest_increase = 0
greatest_decrease = 9999999999999999999999
idate = ""
ddate = ""
revenue_changes = []
with open(filepath) as csvfile:
    reader = csv.reader(csvfile)
    # for row in reader:
    #     print(row)
    next(reader,None)
    data = list(reader)
    Months = len(data)
    for row in data:
        cur_month = int(row[1])
        Total_Revenue += int(row[1])
        #The average change in revenue between months over the entire period
        #change = change
        #prev_revenue = prev_revenue
        change = int(row[1]) - prev_revenue
        # print(change)
        #date = int(row[0])
        # Reset the value of prev_revenue to the row I completed my analysis
        prev_revenue = int(row[1])
        # print(prev_revenue)
        # #Determine the greatest increase
        if (change > greatest_increase):
            greatest_increase = change
            # print(type(row))
            # print(row)
            idate = row[0]
# Greatest decrease
        if (change < greatest_decrease):
            greatest_decrease = change
            ddate = row[0]
        # Add to the changes list
        revenue_changes.append(int(row[1]))
    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)
    print("Total Months: " , Months)
    print("Total Revenue: " + "$" , Total_Revenue)
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + idate + " $"+str(greatest_increase) +"\n")
    print("Greatest Decrease: " + ddate + " $"+str(greatest_decrease) +"\n")
            # Total_Revenue = Total_Revenue + int(row[1])

#Export to a text file
    file_to_output = "Results.txt"
    with open(file_to_output, "w") as txt_file:
        txt_file.write("Total Months: ")
        txt_file.write(str(Months))
        txt_file.write("\n")
        txt_file.write("Total Revenue: ")
        txt_file.write(str(Total_Revenue))
        txt_file.write("\n")
        txt_file.write("Average Change: ")
        txt_file.write(str(round(sum(revenue_changes) / len(revenue_changes),2)))
        txt_file.write("\n")
        txt_file.write("Greatest Increase: ")
        txt_file.write(idate + " $"+str(greatest_increase))
        txt_file.write("\n")
        txt_file.write("Greatest Decrease: ")
        txt_file.write(ddate + " $"+str(greatest_decrease))