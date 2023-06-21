from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    invalidlogin = (By.CSS_SELECTOR,"input[name='email']")
    invalidpass  = (By.CSS_SELECTOR,"input[name='password']")
    signin       = (By.CSS_SELECTOR,"button[id='mui-3']")

    def invalidemail(self):
        return self.driver.find_element(*LoginPage.invalidlogin)

    def invalidpassword(self):
        return self.driver.find_element(*LoginPage.invalidpass)

    def signinbtn(self):
        return self.driver.find_element(*LoginPage.signin)
        #self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")
