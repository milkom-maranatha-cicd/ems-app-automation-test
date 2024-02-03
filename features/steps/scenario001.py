from behave import given, when, then
from web.driver import WebDriver
from web.pages import SignInPage
from settings import APP_URL
from tests.data.employees import PREDEFINED_DATA
from common_steps import *
import time


@then('I should see the table headers')
def step_then_i_should_see_the_table_headers(context):
    dashboard_page = context.dashboard_page
    try:
        dashboard_page.assert_table_headers()
    except ValueError as err:
        assert False, f'Dashboard Page Assertion Failed: {str(err)}'


@then('the table content should match the predefined data')
def step_then_the_table_content_should_match_the_predefined_data(context):
    dashboard_page = context.dashboard_page

    actual_data = dashboard_page.table_dataset
    expected_data = PREDEFINED_DATA
    assert actual_data == expected_data, "Table content tidak sesuai dengan yang diharapkan"
