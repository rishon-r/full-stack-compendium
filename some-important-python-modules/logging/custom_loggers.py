# When working with larger projects, oftentimes you also want separate log files: each pertaining to a particular feature or component
import logging

logging.basicConfig(level=logging.INFO, filename="custom_logs.log", filemode="w",
                     format="%(asctime)s - %(levelname)s - %(message)s")

# Creating a custom logger
logger = logging.getLogger(__name__) # You pass the name of the logger you want as the argument: if it exists, it will give it to you, otherwise it will create it
# Convention is to use __name__ as your logger name and to have one logger for every module

# Handle allows us to set custom configurations for a logger (i.e file it writes to, format, etc.)
handler = logging.FileHandler('test.log') # This will now log in test.log instead of the customs_logs.log file
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


logger.info("Testing the custom logger")
