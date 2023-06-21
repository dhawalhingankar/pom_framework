import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from Pages.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestLoginPage(BaseClass):

    def test_invalidinput(self):
        time.sleep(5)
        log=self.getLogger()
        loginPage = LoginPage(self.driver)
        loginPage.invalidemail().send_keys("sty1@sty.com")
        loginPage.invalidpassword().send_keys("eclass1")
        loginPage.signinbtn().click()
        log.info("The email and password entered is incorrect")

    def test_blankinput(self):
        time.sleep(5)
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        loginPage.invalidemail().send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE)
        time.sleep(2)
        loginPage.invalidemail().send_keys("")
        time.sleep(2)
        loginPage.invalidpassword().send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.BACK_SPACE)
        loginPage.invalidpassword().send_keys("")
        time.sleep(2)
        loginPage.signinbtn().click()
        log.info("The email and password is blank")

    def test_invalidpass(self):
        time.sleep(5)
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        loginPage.invalidemail().send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE)
        time.sleep(2)
        loginPage.invalidemail().send_keys("sty@sty.com")
        loginPage.invalidpassword().send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE)
        time.sleep(2)
        loginPage.invalidpassword().send_keys("eclass1")
        loginPage.signinbtn().click()
        log.info("The password entered is incorrect")

    def test_invalidemail(self):
        time.sleep(5)
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        loginPage.invalidemail().send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE)
        time.sleep(2)
        loginPage.invalidemail().send_keys("sty1@sty.com")
        loginPage.invalidpassword().send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE)
        time.sleep(2)
        loginPage.invalidpassword().send_keys("eclass")
        loginPage.signinbtn().click()
        log.info("The email entered is incorrect")

    def test_valideinput(self):
        time.sleep(5)
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        loginPage.invalidemail().send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE)
        time.sleep(2)
        loginPage.invalidemail().send_keys("sty@sty.com")
        loginPage.invalidpassword().send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE)
        time.sleep(2)
        loginPage.invalidpassword().send_keys("eclass")
        loginPage.signinbtn().click()
        log.info("User Login Successfully")








