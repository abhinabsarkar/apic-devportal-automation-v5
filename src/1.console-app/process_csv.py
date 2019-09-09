# process_csv.py

# Import library to read & write csv
import csv
# Import os to check the file properties
import os

# Read entire csv file and return a list object
def read_csv(csv_file):
    with open(csv_file, mode='r') as csv_file:        
        csv_reader = csv.reader(csv_file)
        # Skip the first row of the CSV file.        
        next(csv_reader)
        consumer_list = []
        for row in csv_reader:
            consumer_list.append(row)               
    return consumer_list

# Write to csv file 
def write_csv(csv_file, subscribed_app):
    # Get the file path
    file_path = os.path.join(os.getcwd(), csv_file)   
    # Create a file and append rows to it
    with open(csv_file, mode='a', newline='') as csv_file:        
        csv_writer = csv.writer(csv_file)
        # Check whether file is empty or not
        file_empty = os.stat(file_path).st_size == 0
        # Write header row to the CSV file if empty
        if file_empty:
            headers = ["SID", "Client ID", "Client Secret", "Plan Name", "Subscription Requested"]
            csv_writer.writerow(headers)              
        csv_writer.writerow(subscribed_app)             
    return True