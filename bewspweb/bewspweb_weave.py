# Necessary modules to import
from selenium.webdriver.common.by import By
from time import sleep


def bewspweb_weave(wbdriver=None, type_element=None, element=None, type_subelement=None,
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
                get_element = wbdriver.find_element(type_element, element)
                
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

