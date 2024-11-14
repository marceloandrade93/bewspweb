from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name="bewspweb",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'selenium',
        'webdriver-manager'
    ],
    author="Marcelo Andrade",
    description="Functions to extract data from a web page using selenium webdriver with not too much code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marceloandrade/bewspweb",
)
