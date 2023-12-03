def _convert_salaries(data):
    """
    Convert all salary from that `data` into USD.
    """
    converted = []

    for item in data:
        salary = float(item['salary'])
        if salary.is_integer():
            str_salary = '${:,.0f}'.format(salary)
        else:
            str_salary = '${:,.2f}'.format(salary)

        converted.append({
            'no': item['no'],
            'first_name': item['first_name'],
            'last_name': item['last_name'],
            'email': item['email'],
            'salary': str_salary,
            'date': item['date']
        })

    return converted


PREDEFINED_DATA = _convert_salaries([
    {
        'no': '1',
        'first_name': 'Susan',
        'last_name': 'Jordon',
        'email': 'susan@example.com',
        'salary': '95000',
        'date': '2019-04-11'
    },
    {
        'no': '2',
        'first_name': 'Adrienne',
        'last_name': 'Doak',
        'email': 'adrienne@example.com',
        'salary': '80000',
        'date': '2019-04-17'
    },
    {
        'no': '3',
        'first_name': 'Rolf',
        'last_name': 'Hegdal',
        'email': 'rolf@example.com',
        'salary': '79000',
        'date': '2019-05-01'
    },
    {
        'no': '4',
        'first_name': 'Kent',
        'last_name': 'Rosner',
        'email': 'kent@example.com',
        'salary': '56000',
        'date': '2019-05-03'
    },
    {
        'no': '5',
        'first_name': 'Arsenio',
        'last_name': 'Grant',
        'email': 'arsenio@example.com',
        'salary': '65000',
        'date': '2019-06-13'
    },
    {
        'no': '6',
        'first_name': 'Laurena',
        'last_name': 'Lurie',
        'email': 'laurena@example.com',
        'salary': '120000',
        'date': '2019-07-30'
    }
])
