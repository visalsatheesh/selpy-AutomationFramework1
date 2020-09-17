from selenium import webdriver
import pytest
from pages.loginAdminPage import LoginAdminPage
from pages.dashboardPage import dashBoardPage
from utils import utils as utils
import allure
import moment

@pytest.mark.usefixtures("test_setup")
class TestLoginAdmin():
    # @pytest.fixture(scope="class")
    # def test_setup(self):
    #     global driver
    #     driver = webdriver.Chrome(executable_path="C:/Users/Home/PycharmProjects/AutomationFramework1/drivers/chromedriver.exe")
    #     driver.implicitly_wait(10)
    #     yield
    #     driver.close()
    #     driver.quit()
    #     print("Logged Out Successfully")

    def test_login(self):
        driver = self.driver
        driver.get(utils.ADMINURL)

        login = LoginAdminPage(driver)
        login.enter_email(utils.EMAIL)
        login.enter_password(utils.PASSWORD)
        login.click_login()

        # driver.find_element_by_name("email").send_keys("admin@phptravels.com")
        # driver.find_element_by_name("password").send_keys("demoadmin")
        # driver.find_element_by_xpath("/html/body/div[2]/form[1]/button/span[1]").click()

    def test_logout(self):
        try:
            driver = self.driver
            dashboard = dashBoardPage(driver)
            dashboard.click_logout()
            x = driver.title
            assert x == "Administator Login"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            x = moment.now().strftime('%m-%d-%Y_%H-%M-%S')
            testName = utils.whoami()
            screenshotName = testName + "_" + x
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Home/PycharmProjects/AutomationFramework1/screenshots/"+screenshotName+".png")
            raise
        except:
            print("There was an exception")
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("Finally block")

        # driver.find_element_by_link_text("Logout").click()