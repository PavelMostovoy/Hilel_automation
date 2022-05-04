"""
docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""


from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')


driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)

driver.get("http://google.com")

button = driver.find_elements(By.XPATH, '//button')