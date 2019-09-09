# Main python script which creates and subscribes app to a product in the Dev Org

# Importing my libraries
import devportal_app_mgmt
import process_csv
import logger
import encode
# Import library for secure password prompt
import getpass
# Importing configuration parser
import configparser
# Import json module
import json

# Parser to read configuration values
config = configparser.ConfigParser()
config.read("config.ini")

# Get the user input
username = input("Enter your username for the dev portal: ")
password = getpass.getpass("Enter your password: ")

logger.log_message("*****Start processing main*****")
print("Processing...")

# Get the details from the csv file & load into a List object
logger.log_message("Read csv file")
consumer_list = process_csv.read_csv("input.csv")

# Parse through the consumer list
logger.log_message("Loop through the csv file")
for counter in range(len(consumer_list)):    
    # Get the dev org name from the csv file
    logger.log_message("Get the dev org name from csv file")
    dev_org_name = consumer_list[counter][0].strip()

    # Check if the dev org is already present
    logger.log_message("Check if dev org name already exists")
    dev_org_check = devportal_app_mgmt.dev_org_exists(username, password, dev_org_name)

    if dev_org_check[0] == False:
        # Create the dev org only if the dev org doesn't exist
        logger.log_message("Create the dev org & get the id")
        dev_org_id = devportal_app_mgmt.create_dev_org(username, password, dev_org_name)
    else:
        # Get the id of the existing dev org
        logger.log_message("Get the id of the pre-existing dev org")
        dev_org_id = dev_org_check[1]
    
    # Get the dev org name from the csv file
    logger.log_message("Get the app name from csv file")
    app_name = consumer_list[counter][1].strip() 
    # Create app & get the Client ID & Client Secret
    logger.log_message("Create the app and get the client credentials")
    client_app = devportal_app_mgmt.create_app(username, password, dev_org_id, app_name)
    client_id = client_app[1]
    client_secret = client_app[2]

    # Subscribe to the ESTS app
    logger.log_message("Subscribe app to the product plan")
    plan_name = consumer_list[counter][2].strip() 
    subscription_requested = devportal_app_mgmt.subscribe_app(username, password, dev_org_id, app_name, plan_name)

    # Write the subscribed app details to csv file
    logger.log_message("Writing the details of subscribed app " + app_name + " to csv")
    # Base64 encode the dev org id
    sid = encode.to_base64_string(dev_org_id)
    # Create the list object using the subscribed app details
    subscribed_app = [sid, client_id, client_secret, plan_name, subscription_requested]
    # Write to CSV
    process_csv.write_csv("output.csv", subscribed_app) 

logger.log_message("Subscription apps created succesfully. See details in App-Subsciption.csv")
print("Subscription apps created succesfully. See details in App-Subsciption.csv")