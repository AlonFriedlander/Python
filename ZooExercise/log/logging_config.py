import logging

# Create a formatter
formatter = logging.Formatter('%(levelname)s - date and time: %(asctime)s - file name: %(filename)s - line %(lineno)d -'
                              'msg: %(message)s')

# Create a file handler and set the formatter
log_file = 'zoo.log'
file_handler = logging.FileHandler(log_file, mode='w')

file_handler.setFormatter(formatter)

# Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Set the root logger level

# Add the file handler to the root logger
logger.addHandler(file_handler)



