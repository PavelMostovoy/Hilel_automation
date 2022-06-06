import logging

# create logger
logger = logging.getLogger('Name_of_Logger')
logger.setLevel(logging.DEBUG)

# create file handler and set level to debug
file_handler = logging.FileHandler("log_file.log")
file_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to file_handlerh
file_handler.setFormatter(formatter)

# add file_handlerh to logger
logger.addHandler(file_handler)


def test_add_user():
    logger.info("data from pytest")
    pass
