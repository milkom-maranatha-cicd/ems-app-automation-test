from enum import IntEnum


# Choices of the Automation Web Driver
class DriverType(IntEnum):
    CHROME = 1
    FIREFOX = 2
    SAFARI = 3


# Selected Web Driver
WEB_DRIVER_TYPE = DriverType.CHROME

# URL of the Single Page Application
APP_URL = 'http://localhost:3000/'
