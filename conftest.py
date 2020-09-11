import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    #global driver
    from selenium import webdriver

    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/Home/PycharmProjects/AutomationFramework1/drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/Home/PycharmProjects/AutomationFramework1/drivers/geckodriver.exe")

    # driver = webdriver.Chrome(executable_path="C:/Users/Home/PycharmProjects/AutomationFramework1/drivers/chromedriver.exe")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Logged Out Successfully")