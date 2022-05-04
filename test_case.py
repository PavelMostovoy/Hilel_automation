"""
prerequisites  = https://www.wikipedia.org/
0. open URL
1 fill "Napoleon" in search field
2 click the search button
3 verify that element == Napoleon

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          options=options)


driver_2 = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          options=options)


uri_variable = "Napoleon"

url = ["https://www.wikipedia.org/"]

driver.get(url[0])

search_field = '//*[@id="searchInput"]'
element = driver.find_element(By.XPATH, search_field)

element.send_keys(uri_variable)

button = '//*[@id="search-form"]/fieldset/button'

element_button = driver.find_element(By.XPATH, button)

element_button.click()

expected_element_path = '//*[@id="firstHeading"]'

expected_element = driver.find_element(By.XPATH, expected_element_path)

if expected_element.text == "Napoleon":
    print("successful")
else:
    print("Failed")

# new_element = driver.find_elements(By.CLASS_NAME, 'noprint')
#
# print(new_element)

