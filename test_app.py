import requests
import pytest


def save_data(data):
    with open("log.txt", "a") as f:
        f.write(data)


class TestSuite:

    def setup_class(self):
        self.variable = []
        print("tests started")

    def teardown_class(self):
        save_data(str(self.variable))

    def setup(self):
        save_data("started \n")

    def teardown(self):
        save_data("finidhed \n")

    def test_first_check(self):
        status = requests.get("https://google.com").status_code
        self.variable.append(status)
        assert status == 200

    def test_second_check(self):
        status = requests.get("https://google.com/_").status_code
        self.variable.append(status)
        assert status == 404

    def test_third_check(self):
        status = requests.get("https://wikipedia.com").status_code
        self.variable.append(status)
        assert status == 202

    def test_forth_check(self):
        status = requests.get("https://www.aqa.science").status_code
        self.variable.append(status)
        assert status == 200
