import pytest
from selenium import webdriver 
from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser: chrome, firefox or edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    return driver


def pytest_configure(config):
    config.stash[metadata_key] ["Project"] = "NopCommerce Automation"
    config.stash[metadata_key] ["Test Module"] = "Admin Login"
    config.stash[metadata_key] ["Tester"] = "Kacper Stec"
    

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Python", None)
    metadata.pop("Platform", None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
    metadata.pop("JAVA_HOME", None)
