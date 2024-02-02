from selenium import webdriver

from settings import (
    DriverType,
    USE_HEADLESS_BROWSER,
    WEB_DRIVER_TYPE,
)


class WebDriver:

    def __init__(self) -> None:
        """
        Initialize web driver based on the `WEB_DRIVER_TYPE`
        value defined in the project settings.
        """
        if WEB_DRIVER_TYPE == DriverType.CHROME:
            opts = webdriver.ChromeOptions()
            opts.add_experimental_option('detach', True)

            if USE_HEADLESS_BROWSER is True:
                opts.add_argument('--headless')

            self.driver = webdriver.Chrome(
                options=opts
            )

        elif WEB_DRIVER_TYPE == DriverType.FIREFOX:
            self.driver = webdriver.Firefox()

        elif WEB_DRIVER_TYPE == DriverType.SAFARI:
            self.driver = webdriver.Safari()

        else:
            raise ValueError('Unknown web driver!')
