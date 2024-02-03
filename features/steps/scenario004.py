import time
from behave import given, when, then
from web.pages import DashboardPage, SignInPage
from tests.data.employees import PREDEFINED_DATA
from web.converters import to_date_first, usd_salary_to_number
from common_steps import *


@when('I delete the first employee')
def step_when_i_delete_the_first_employee(context):
    row_number = 1
    context.deleted_data = context.dashboard_page.run_delete_data(
        row_number=row_number)
    context.deleted_data['date'] = to_date_first(context.deleted_data['date'])
    context.deleted_data['salary'] = usd_salary_to_number(
        context.deleted_data['salary'])
    time.sleep(1)


@then('the table dataset must not contain the deleted employee')
def step_then_table_dataset_must_not_contain_the_deleted_employee(context):
    dashboard_page = context.dashboard_page
    try:
        dashboard_page.assert_table_data_contains(context.deleted_data)
        assert False, "Table dataset still contains the deleted employee"
    except LookupError:
        pass  # The expected behavior is that the deleted data should not be found
