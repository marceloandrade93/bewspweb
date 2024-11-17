# Necessary modules to import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def bewspweb_start(url_main=None, pwd=None, user=None, headless=False, mute_audio=False, window_mode=None):
    """
    Objective:
    This function is to start the driver and open the web page using the defined parameters.

    Args:
        url_main (str): URL of the web page to open. Defaults to None.
        pwd (str, optional): Password to access the web page. Defaults to None.
        user (str, optional): User to access the web page. Defaults to None.
        headless (bool, optional): To activate headless mode. Defaults to False.
        mute_audio (bool, optional): To mute audio. Defaults to False.
        window_mode (str, optional): To specify the window mode. Defaults to "None".
    """

    global _url_main, _pwd, _user

    # set url, login and password if needed
    _url_main = url_main
    _pwd = pwd
    _user = user

    try:
        # Driver options to start
        chrome_options = webdriver.ChromeOptions()

        # To activate headless mode
        if headless:
            chrome_options.add_argument("--headless")

        # To mute audio
        if mute_audio:
            chrome_options.add_argument("--mute-audio")

        # To start the driver
        driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
        driver.get(_url_main)

        # To specify the window mode to be used after the driver is started
        if window_mode == "maximize":
            driver.maximize_window()
        elif window_mode == "minimize":
            driver.minimize_window()
        elif window_mode == "fullscreen":
            driver.fullscreen_window()

        return driver

    except Exception as e:
        print(e)
