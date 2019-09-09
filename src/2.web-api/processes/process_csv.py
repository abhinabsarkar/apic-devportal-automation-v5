# process_csv.py

# Import library to read & write csv
import csv
# Import os to check the file properties
import os
import base64

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
            headers = ["App Name", "Client ID", "Client Secret", "Plan Name", "SID", "Subscription Requested"]
            csv_writer.writerow(headers)              
        csv_writer.writerow(subscribed_app)             
    return True

# Converts a base64 encoded string to csv file
def convertb64_to_file(b64_encoded_data, filename):
    decoded_bytes = base64.b64decode(b64_encoded_data)
    with open(filename, "wb") as fh:
        fh.write(decoded_bytes)
    return True

# Convert list to csv string
def list_to_csv_string(list_object):
    # Creating the csv formatted string
    csv_line_length = len(max(list_object,key=len))
    csv_string = ''
    # Add header row
    header_row = ["App Name", "Client ID", "Client Secret", "Plan Name", "SID", "Subscription Requested"]
    csv_string += ','.join(header_row) + '\n'
    # Loop through the list_object
    for row in list_object:
        csv_string += ','.join(row) + '\n'
    return csv_string