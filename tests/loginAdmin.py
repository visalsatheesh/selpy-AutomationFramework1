from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/Home/PycharmProjects/AutomationFramework1/drivers/chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://www.phptravels.net/admin")
driver.find_element_by_name("email").send_keys("admin@phptravels.com")
driver.find_element_by_name("password").send_keys("demoadmin")
driver.find_element_by_xpath("/html/body/div[2]/form[1]/button/span[1]").click()
driver.find_element_by_link_text("Logout").click()

driver.close()
driver.quit()
print("Logged Out Successfully")