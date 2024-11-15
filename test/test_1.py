import unittest
from bewspweb import *


class TestBewspweb(unittest.TestCase):
    def test_bewspweb(self):
        # Initialize driver
        bewspweb_start(url_main="https://webscraper.io/test-sites/e-commerce/scroll")

        # Start webscrapping
        list_name = bewspweb_weave(type_element=By.XPATH,
            element="/html/body/div[1]/div[3]/div/div[2]/div[2]",
            type_subelement=By.XPATH,
            subelement="/html/body/div[1]/div[3]/div/div[2]/div[2]/div",
            selsubtag="a",
            subtag="title",
            tries=10)

        # Print woven list
        bewspweb_print(list=list_name, col_a=0, col_b=1)

        self.assertEqual(len(list_name), 3)


if __name__ == "__main__":
    unittest.main()