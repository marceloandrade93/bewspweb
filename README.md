# bewspweb
In this repository you can find a module that allows you to extract data from a homepage with some functions, passing a few parameters and storing them in a list.

## Getting Started

### Prerequisites
To use it assertively, it is necessary to install some modules.

* Selenium
* Webdriver-manager

```bash
pip install selenium
pip install webdriver-manager
```

### Installation
To install de package, just run the command:

```bash
pip install bewspweb
```

## Functions
This module has some functions:

### `bewspweb_start()`
This function is to start the driver and open the web page using the defined parameters.

### `bewspweb_weave()`
This function is to collect data from a web page defining the type of the element, the element itself, the type of the subelement, the subelement itself. The function returns a list with the data collected.

### `bewspweb_print()`
This function is to print the collected data from a web page.

## How to Use

* **Start driver with bewspweb()**

```python
from bewspweb import bewspweb_start

bewspweb_start(url_main="https://webscraper.io/test-sites/e-commerce/scroll")
```

```python
from bewspweb import bewspweb_start

bewspweb_start(url_main="https://webscraper.io/test-sites/e-commerce/scroll", headless=True, windows_mode="maximize", mute_audio=True)
```

* **Collecting with bewspweb_weave()**

```python
from bewspweb import bewspweb_start, bewspweb_weave
from selenium.webdriver.common.by import By

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
```

* **Printing with bewspweb_print()**

```python
from bewspweb import bewspweb_start, bewspweb_weave, bewspweb_print
from selenium.webdriver.common.by import By

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
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

- **Email:** [andradeswork@gmail.com](mailto:andradewswork@gmail.com)