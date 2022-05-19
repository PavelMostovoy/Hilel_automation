from pytest_bdd import scenarios, given, when, then, parsers
from pathlib import Path

BASE_DIR = Path.cwd().parent
features_folder = "features"
file_name = "web_login.feature"

feature_name = BASE_DIR.joinpath(features_folder, file_name).__str__()

scenarios(feature_name)

@given(parsers.re("As (?P<user>.*)"))
def step_impl(user):
    print(f"User name is {user}")


@given(parsers.re("URL page (?P<url>.*)"))
def step_impl(url):
    print(f"URL is  {url}")