import time

from behave import when, then
from tests.data.employees import PREDEFINED_DATA
from common_steps import *  # noqa: F401, F403


@then('the table dataset should be initially empty or match the predefined data')
def step_then_table_dataset_should_be_initially_empty_or_match_predefined_data(context):
    dashboard_page = context.dashboard_page

    # Assert initial state of the table dataset
    # Validates if table content is empty or matches predefined data
    if len(dashboard_page.table_dataset) == 0:
        dashboard_page.assert_table_data_is_empty()
    else:
        actual_data = dashboard_page.table_dataset
        expected_data = PREDEFINED_DATA
        assert actual_data == expected_data, "Dataset validation failed"


@when('I open the add employee page')
def step_when_i_open_add_employee_page(context):
    # Open add employee page
    context.add_employee_page = context.dashboard_page.run_add_data()


@then('I should be on the add employee page')
def step_then_i_should_be_on_add_employee_page(context):
    # Assert properties of the add employee page
    context.add_employee_page.assert_properties()


@then('the add employee page should have the required properties')
def step_then_add_employee_page_should_have_required_properties(context):
    # Implement assertions for the properties of the add employee page
    context.add_employee_page.assert_properties()


@when('I save a new employee with the details')
def step_when_i_save_new_employee(context):
    # Check if the table is available in the context
    if hasattr(context, 'table') and context.table:
        new_employee_details = context.table.rows[0].as_dict()
    else:
        new_employee_details = {}

    # Save new employee
    context.dashboard_page = context.add_employee_page.run_add_employee(
        new_employee_details)
    time.sleep(1)


@then('the table dataset should contain the new employee')
def step_then_table_dataset_should_contain_new_employee(context):
    dashboard_page = context.dashboard_page

    # Scrolls down/up to see dataset of the table employee (if needed)
    table_dataset_size = len(dashboard_page.table_dataset)
    if table_dataset_size >= 10:
        dashboard_page.scroll_down()
