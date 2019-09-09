# Import module for logging
import logging
# Import module for date time. Used to create log file with today's date
import time

def log_message(message):
    # timestamp = time.strftime("%Y%m%d-%H%M%S")
    # Create log file with today's date
    timestamp = time.strftime("%Y%m%d")
    filename = timestamp + ".log"

    # Configure logging 
    logging.basicConfig(
        level=logging.INFO
        # format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
        # filename=filename,
        # filemode='a'
    )
    # Create logger
    logger = logging.getLogger()
    # Log messsage with Info level
    logger.info(message)