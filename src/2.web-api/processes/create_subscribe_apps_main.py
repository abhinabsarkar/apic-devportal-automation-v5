# Importing my libraries
import processes.devportal_app_mgmt
import processes.process_csv
import processes.logger
import processes.encode
import processes.notify
# Import library for secure password prompt
import getpass
# Importing configuration parser
import configparser
# Import json module
import json
# Import the OS module for file handling operations
import os 
import time
import logging
import sys, traceback

# Parser to read configuration values
config = configparser.ConfigParser()
config.read("config.ini")

output_file = config["Default"]["output_file"]

def create_subscriptions(username, password, b64encoded_csv):
    try:    
        processes.logger.log_message("*****Start processing main*****")
        print("Processing...")

        # Convert the base64 encoded string to csv file
        timestamp = timestamp = time.strftime('%Y%m%d-%H%M%S')
        filename = 'temp_input_' + timestamp + '.csv'
        processes.process_csv.convertb64_to_file(b64encoded_csv, filename)

        # Get the details from the csv file & load into a List object
        processes.logger.log_message("Read csv file")
        consumer_list = processes.process_csv.read_csv(filename)

        # Parse through the consumer list
        processes.logger.log_message("Loop through the csv file")
        for counter in range(len(consumer_list)):    
            # Get the dev org name from the csv file
            processes.logger.log_message("Get the dev org name from csv file")
            dev_org_name = consumer_list[counter][0].strip()

            # Check if the dev org is already present
            processes.logger.log_message("Check if dev org name already exists")
            dev_org_check = processes.devportal_app_mgmt.dev_org_exists(username, password, dev_org_name)

            if dev_org_check[0] == False:
                # Create the dev org only if the dev org doesn't exist
                processes.logger.log_message("Create the dev org & get the id")
                dev_org_id = processes.devportal_app_mgmt.create_dev_org(username, password, dev_org_name)
            else:
                # Get the id of the existing dev org
                processes.logger.log_message("Get the id of the pre-existing dev org")
                dev_org_id = dev_org_check[1]
            
            # Get the dev org name from the csv file
            processes.logger.log_message("Get the app name from csv file")
            app_name = consumer_list[counter][1].strip() 
            # Create app & get the Client ID & Client Secret
            processes.logger.log_message("Create the app and get the client credentials")
            client_app = processes.devportal_app_mgmt.create_app(username, password, dev_org_id, app_name)
            client_id = client_app[1]
            client_secret = client_app[2]

            # Subscribe to the app
            processes.logger.log_message("Subscribe app to the product plan")
            plan_name = consumer_list[counter][2].strip() 
            subscription_requested = processes.devportal_app_mgmt.subscribe_app(username, password, dev_org_id, app_name, plan_name)

            # Write the subscribed app details to csv file
            processes.logger.log_message("Writing the details of subscribed app " + app_name + " to csv")
            # Base64 encode the dev org id
            sid = processes.encode.to_base64_string(dev_org_id)
            # Create the list object using the subscribed app details
            subscribed_app = [app_name, client_id, client_secret, plan_name, sid, subscription_requested]
            # Write to CSV
            processes.process_csv.write_csv(output_file, subscribed_app)

        # Get the csv file into a list object
        app_list = processes.process_csv.read_csv(output_file)

        # Get the csv string from list object
        csv_string = processes.process_csv.list_to_csv_string(app_list)     

        if len(consumer_list) == 0:
            subject = "Input file is empty. No subscription apps created"
            # processes.logger.log_message(subject)
            # Mail CSV. Need access to smtp server
            # processes.notify.send_mail(username, output_file, subject)
            return "Input file is empty. No subscription apps created"
        else:
            subject = "Subscription apps created succesfully. See details in App-Subsciption.csv"
            # processes.logger.log_message(subject)
            # Mail CSV. Need access to smtp server
            # processes.notify.send_mail(username, output_file, subject)
            # return "Subscription apps created succesfully"
            return csv_string
    except Exception as error:
        processes.logger.log_message(logging.exception("Exception occured"))
        raise 
    finally:
        # Delete the input csv file after it has been read
        if os.path.exists(filename):
            os.remove(filename)
        # Delete the output csv file after it has been created & mailed
        if os.path.exists(output_file):
            os.remove(output_file)