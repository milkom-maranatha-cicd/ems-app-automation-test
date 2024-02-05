from behave import given, when, then
from web.driver import WebDriver
from web.pages import DashboardPage, SignInPage
from settings import APP_URL
from tests.data.employees import PREDEFINED_DATA
from common_steps import *
import time


@when('I edit the first employee')
def step_when_i_edit_the_first_employee(context):
    row_number = 1
    to_be_edited, edit_employee_page = context.dashboard_page.run_edit_data(
        row_number=row_number
    )
    context.to_be_edited = to_be_edited
    context.edit_employee_page = edit_employee_page


@then('I should be on the edit employee page')
def step_then_i_should_be_on_edit_employee_page(context):
    try:
        context.edit_employee_page.assert_properties()
    except ValueError as err:
        context.fail(f'Edit Employee Page Assertion Failed: {str(err)}')


@when('I save the edited employee with the details')
def step_when_i_save_edited_employee(context):
    # Check if the table is available in the context
    if hasattr(context, 'table') and context.table:
        edited_employee_details = context.table.rows[0].as_dict()
    else:
        edited_employee_details = {}

    # Save new employee
    context.dashboard_page = context.edit_employee_page.run_edit_employee(
        edited_employee_details)
    time.sleep(1)


@then('the table dataset should contain the edited employee')
def step_then_table_dataset_should_contain_edited_employee(context):
    dashboard_page = context.dashboard_page

    table_dataset_size = len(dashboard_page.table_dataset)
    if table_dataset_size >= 10:
        dashboard_page.scroll_down()
