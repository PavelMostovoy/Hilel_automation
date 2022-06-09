import requests
import selenium
from  selenium import webdriver
from pytest_bdd import scenarios, given, when, then, parsers


@given(parsers.re("User '(?P<name_0>.*)'"))
def first_user(request, name_0):
    request.login = name_0
    print(f"user {name_0}")



@when(parsers.re("Add additional user '(?P<name>.*)'"))
def second_user(name, name_0, request):
    request.second_name = name
    request.primary_name = name_0
    print(f"added name {name} {name_0}")
    return name


@then("Compare Users names")
def comparation_l(request):
    assert request.primary_name == request.second_name
    # assert request.login == request.second_name

#
# @given(parsers.re("User_1 '(?P<name_1>.*)'"))
# def step_impl(name_1, request):
#     request.login = name_1
#     print(f"user {name_1}")
#
#
# @when(parsers.re("(?P<name>.*) open (?P<url>.*) using browser (?P<browser>.*)"))
# def step_impl(name, url, browser, request):
#     if browser in request.browsers:
#         client = getattr(request.browsers, browser)
#     else:
#         client = webdriver.Remote = ("http:browserstack")
#
#     client.get(url)
#     client.send_keys(name)
#
#     request.user_session = client
#
#
# @given("User fill <data> in form")
# def step_impl(request):
#     driver = request.user_session
#     driver.send_keys()
#
@when("User send Get request to <url>")
def step_impl(request):
    result = requests.get("url")
    request.data.get_request = result


@then(parsers.re("Check response (?P<code>.*)"))
def step_impl(code, request):
    assert request.data.get_request == code