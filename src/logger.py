# This code is raising some errors
'''
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y %H:%M:%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = " %(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

if __name__ == "__main__":
    logging.info("Logging has started")
    '''

import logging
import os
from datetime import datetime

# 1. Format the filename without illegal characters like colons (:)
LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"

# 2. Define the path to the 'logs' directory
logs_path = os.path.join(os.getcwd(), "logs")

# 3. Create the directory
os.makedirs(logs_path, exist_ok=True)

# 4. Create the full path for the log file inside the directory
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=" %(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

''' if __name__ == "__main__":
    logging.info("Logging has started")
    print(f"Log file created at: {LOG_FILE_PATH}") # Added for confirmation '''