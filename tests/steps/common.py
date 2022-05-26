from pytest_bdd import scenarios, given, when, then, parsers


@given(parsers.re("User '(?P<name_0>.*)'"))
def first_user(request, name_0):
    request.login = name_0
    print(f"user {name_0}")



@when(parsers.re("Add additional user '(?P<name>.*)'"))
def second_user(name, name_0, request):
    request.second_name = name
    print(f"added name {name} {name_0}")
    return name


@then("Compare Users names")
def comparation_l(request):
    print("final result")
    # assert request.login == request.second_name
