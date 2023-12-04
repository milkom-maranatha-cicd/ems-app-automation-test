from dateutil.parser import parse


def to_date_first(str_date: str) -> str:
    """
    Converts the date representation of `YYYY-MM-DD`
    to the date representation of `DD/MM/YYYY`
    """
    return parse(str_date, yearfirst=True).strftime('%d/%m/%Y')


def usd_salary_to_number(usd_salary: str) -> str:
    """
    Converts the USD salary into a number value.
    """
    if not ('$' in usd_salary):
        raise ValueError('Invalid salary format.')

    str_salary = usd_salary.replace('$', '')\
        .replace(',', '').replace('.', ',')

    salary = float(str_salary)
    if salary.is_integer():
        return f'{int(salary)}'

    return f'{salary}'
