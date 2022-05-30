import pytest
import requests
from selenium import webdriver


@pytest.mark.slow
@pytest.mark.all
@pytest.mark.ui
@pytest.mark.smoke
def test_request(message):
    url = "https://google.com"
    response = requests.get(url).status_code
    with pytest.raises(ZeroDivisionError):
        var = 1 / 0
    assert response == 200, f"failed with {url}"



@pytest.mark.parametrize("url", ["https://google.com",
                                 "https://vikipedia.com",
                                 "https://wikipedia.com",
                                 "https://google.com/_"])
@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.multy
@pytest.mark.api
def test_request_200(url, request):
    response = requests.get(url).status_code
    assert response == 200, f"failed with {url}"


@pytest.mark.all
@pytest.mark.smoke
def test_standalone(message, generator_0):
    assert message + generator_0 > 250


def test_selen(docker):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          options=options)
    element = driver.get("https://google.com")
