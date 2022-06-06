import logging
import pytest


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

# add file_handler to logger
logger.addHandler(file_handler)

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_add_user(test_input,expected):
    logger.info(f"data from pytest {test_input}, {expected}")
    pass
