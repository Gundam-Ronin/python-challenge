# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os


# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = r"..\\Resources\\Pybank"

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
total_net_changes = []
greatest_profits_increase = {'month': '', 'value': 0}
greatest_profits_decrease = {'month': '', 'value': 0}

# Open and read the csv

with open("Resources/budget_data.csv", mode='r') as file:
    reader = csv.reader(file)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row=next(reader)
    previous_profit_losses=int(first_row[1])
    total_months += 1
    total_net += previous_profit_losses


    # Track the total and net change
for row in reader:
    month = row[0]
    profit_losses = int(row[1])

    # Process each row of data

    total_months +=1
    total_net += profit_losses

        # Track the total
    total_months += 1

        # Track the net change
    total_net_changes = profit_losses - previous_profit_losses
    total_net_changes.append(total_net_changes)

        # Calculate the greatest increase in profits (month and amount)

if total_net_changes > greatest_profits_increase['value']:
    greatest_profits_increase['month'] = month
    greatest_profits_increase['value'] = total_net_changes

        # Calculate the greatest decrease in losses (month and amount)

if total_net_changes < greatest_profits_decrease['value']:
    greatest_profits_decrease['month'] = month
    greatest_profits_decrease['value'] = total_net_changes
    previous_profit_losses = profit_losses

# Calculate the average net change across the months
average_net_change = sum(total_net_changes) / len(total_net_changes)

# Generate the output summary
output_summary = f"""
Financial Analysis
-------------------
total months: {total_months}
total: ${total_net_changes}
average change: ${average_net_change: .2f}
greatest increase in profits: {greatest_profits_increase} (${greatest_profits_increase['value']})
greatest decrease in profits: {greatest_profits_increase} (${greatest_profits_decrease['value']})
"""
# Print the output
print(output_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)
