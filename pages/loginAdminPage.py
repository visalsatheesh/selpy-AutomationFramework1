class LoginAdminPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_txtbox_name = "email"
        self.password_txtbox_name = "password"
        self.login_button_xpath = "/html/body/div[2]/form[1]/button/span[1]"

    def enter_email(self, emailid):
        self.driver.find_element_by_name(self.email_txtbox_name).clear()
        self.driver.find_element_by_name(self.email_txtbox_name).send_keys(emailid)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_txtbox_name).clear()
        self.driver.find_element_by_name(self.password_txtbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
