# Automation Tests for Employee Management System (EMS)

The automation testing respostory for the [EMS App](https://github.com/milkom-maranatha-cicd/ems-app) using Selenium for Python.

The automation testing covers these scenarios:
- Login, Validates employee data, Logout
- Login, Validates initial state of the employee data, Add new employee, Validates latest state of the employee data, Logout
- Login, Validates initial state of the employee data, Update existing employee, Validates latest state of the employee data, Logout
- Login, Validates initial state of the employee data, Delete existing employee, Validates latest state of the employee data, Logout

## Technologies Used

- [Selenium](https://www.selenium.dev/)
- [Selenium Web Driver](https://www.selenium.dev/documentation/webdriver/)

## Prerequisite

- Chrome web browser is installed.
- Setting up [`chromedriver`](https://chromedriver.chromium.org/) properly. Check [this out](https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ) on how you do it properly.
- In case you want to run automation tests on different browser, you need to setup a different web driver and modify the `WEB_DRIVER_TYPE` value in the `/settings.py`.
- Run `pip3 install -r requirements.txt`.


## How Run The Automation Tests

- Run [EMS App](https://github.com/milkom-maranatha-cicd/ems-app) locally or host it on your desired hosting providers.
- Open `/settings.py` and modify `APP_URL` into your localhost or the EMS domain.
- Execute script `./run.sh`.
- Once the automation tests are completed, you can find the report on `/report.html` file.