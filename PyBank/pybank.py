#!/usr/bin/env python
# coding: utf-8

# In[23]:


import csv
import os
#file to load
file_to_load = os.path.join(".","Resources", "Budget_data.csv")

file_to_output = os.path.join(".", "budget_analysis.txt")

total_months = 0
total_net = 0

net_change_list = []
month_of_changes = []

total_months =+ 1
greatest = ["", 0]
least = ["", 9999999999999999999999]

with open(file_to_load) as financial_data:
    
    reader = csv.reader(financial_data)
    
    #read the header row
    header = next(reader)
    
    # print(f"Header: {header}")
    first_row = next(reader)

    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    
    for row in reader:
        
        # Track the total
        # total_months = total_months + 1
        total_months += 1
        total_net += int(row[1])
        
        
        
        
        
        
        
        # track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        

        
        
        # Calculate the greatest increase
        if(net_change > greatest[1]):
            greatest[0] = row[0]
            greatest[1] = net_change
        
        # Calculate the greatest decrease
        if(net_change < least[1]):
            least[0] = row[0]
            least[1] = net_change
        
        


net_monthly_average = sum(net_change_list)/ len(net_change_list)
        
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})\n"
    f"Greatest Decrease in Profits: {least[0]} (${least[1]})\n"
)

print(output)




#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


# In[ ]:




