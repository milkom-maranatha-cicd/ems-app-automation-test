# common_steps.py
from behave import given, when, then
from web.driver import WebDriver
from web.pages import SignInPage
from settings import APP_URL
import time

# ... Definisi langkah-langkah umum di sini ...

wd = WebDriver()


@given('I am on the sign in page')
def step_given_i_am_on_sign_in_page(context):
    wd.driver.get(APP_URL)


@when('I login with valid credentials')
def step_when_i_login_with_valid_credentials(context):
    # Open the sign-in page
    sign_in_page = SignInPage(wd)

    # Assert properties of the sign-in page
    sign_in_page.assert_properties()

    # Login with valid credentials
    context.dashboard_page = sign_in_page.run_login(
        username='admin@mail.com',
        password='Test@12345'
    )


@then('I should be on the dashboard page')
def step_then_i_should_be_on_dashboard_page(context):
    # Assert properties of the dashboard page
    context.dashboard_page.assert_properties()


@when('I logout from the system')
def step_when_i_logout_from_the_system(context):
    dashboard_page = context.dashboard_page

    context.sign_in_page_after_logout = dashboard_page.run_logout()
    time.sleep(1)


@then('I should be back on the sign in page')
def step_then_i_should_be_back_on_sign_in_page(context):
    sign_in_page_after_logout = context.sign_in_page_after_logout

    try:
        sign_in_page_after_logout.assert_properties()
    except ValueError as err:
        assert False, f'Sign In Page Assertion Failed: {str(err)}'
