from selenium import webdriver

from settings import (
    DriverType,
    ENABLE_HEADLESS_BROWSER,
    WEB_DRIVER_TYPE,
)

from typing import Union


class WebDriver:

    def __init__(self) -> None:
        """
        Initialize web driver based on the `WEB_DRIVER_TYPE`
        value defined in the project settings.
        """
        if WEB_DRIVER_TYPE == DriverType.CHROME:
            opts = webdriver.ChromeOptions()
            opts.add_experimental_option('detach', True)

            self.enable_headless_browser(opts)
            self.driver = webdriver.Chrome(options=opts)

        elif WEB_DRIVER_TYPE == DriverType.FIREFOX:
            opts = webdriver.FirefoxOptions()

            self.enable_headless_browser(opts)
            self.driver = webdriver.Firefox(options=opts)

        elif WEB_DRIVER_TYPE == DriverType.SAFARI:
            self.driver = webdriver.Safari()

        else:
            raise ValueError('Unknown web driver!')

    def enable_headless_browser(
        self,
        opts: Union[
            webdriver.ChromeOptions,
            webdriver.FirefoxOptions,
            webdriver.Safari
        ]
    ) -> Union[
        webdriver.ChromeOptions,
        webdriver.FirefoxOptions,
        webdriver.Safari
    ]:
        """
        Return `webdriver` options for CI with Github Actions.
        """
        if ENABLE_HEADLESS_BROWSER is True:
            opts.add_argument('--headless')
