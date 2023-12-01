from enum import IntEnum


class DriverType(IntEnum):
    CHROME = 1
    FIREFOX = 2
    SAFARI = 3


WEB_DRIVER_TYPE = DriverType.CHROME
