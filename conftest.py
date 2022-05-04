import subprocess

import pytest
import requests
from random import randint


@pytest.fixture
def docker():
    subprocess.run("docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug",shell=True, check=True)
    yield
    subprocess.run("docker rm -f selenium_chrome",shell=True, check=True)



@pytest.fixture
def generator_0():
    return randint(100, 200)