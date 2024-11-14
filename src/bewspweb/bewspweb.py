# Necessary modules to import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


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

    global driver, _url_main, _pwd, _user

    # set url, login and password if needed
    _url_main = url_main
    _pwd = pwd
    _user = user

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


def bewspweb_weave(type_element=None, element=None, type_subelement=None,
                   subelement=None, selsubtag=None, subtag=None, tries=10):
    """
    Objective:
    This function is to collect data from a web page defining the type of the element,
    the element itself, the type of the subelement, the subelement itself. The function
    returns a list with the data collected.

    Args:
        type_element (str, optional): Type of the element first level. Defaults to None.
        element (str, optional): Element from type_element first level. Defaults to None.
        type_subelement (str, optional): Type of the subelement second level. Defaults to None.
        subelement (str, optional): Subelement from type_subelement second level. Defaults to None.
        selsubtag (str, optional): To get a CSS Selector in third level. Defaults to None.
        subtag (str, optional): To get a attribute in third level. Defaults to None.
        tries (int, optional): Number of tries to collect the data. Defaults to 10.
    """

    list_woven = []

    while True:
        if tries > 0:                
            try:
                # collect_element
                get_element = driver.find_element(type_element, element)
                
                # collect_sublement
                if subelement is None:
                    pass
                else:
                    get_subelement = get_element.find_elements(type_subelement, subelement)

                    for i in get_subelement:
                        # print("--------------------------------------")
                        # print("Name: ", i.text)

                        x = i.find_element(By.CSS_SELECTOR, selsubtag)
                        # print("Data: ", x.get_attribute(subtag))

                        list_woven.append([i.text, x.get_attribute(subtag)])
                        # print("List: ", list_woven)
                        # input("APERTE ENTER PARA CONTINUAR (bewspweb_weave).")

                break

            except Exception as e:
                sleep(2)
                tries -= 1
                print("ERRO: ", e)
                pass
        else:
            print(f"NAO ENCONTROU O ELEMENTO: \n{type} | {element}")
            break

    return list_woven


def bewspweb_print(list=None, col_a=0, col_b=1):
    """
    Objective:
    This function is to print the collected data from a web page.

    Args:
        list (list): List with the data collected. Defaults to None.
        col_a (int): Column A. Defaults to 0.
        col_b (int): Column B. Defaults to 1.
    """

    for i in list:
        print(f"{i[col_a]} | {i[col_b]}")
