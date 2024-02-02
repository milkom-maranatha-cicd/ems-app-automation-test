import os

from enum import IntEnum
from dotenv import load_dotenv


load_dotenv()


# Choices of the Automation Web Driver
class DriverType(IntEnum):
    CHROME = 1
    FIREFOX = 2
    SAFARI = 3


# Selected Web Driver
WEB_DRIVER_TYPE = DriverType.CHROME

# URL of the Single Page Application
APP_URL = 'http://localhost:3000/'

# Headless browser configuration
USE_HEADLESS_BROWSER = os.environ.get('USE_HEADLESS_BROWSER', 'false').lower() in ['true', 'yes', '1']
