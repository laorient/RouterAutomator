from routers.BaseRouter import BaseRouter
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Logger import Logger
import time

import sys

sys.path.append("../../selenium-3.4.3")


class Deco(BaseRouter):
    def logIn(self, username: str, password: str):
        # usernameInput = self.webdriver.find_element_by_id("userName")
        # usernameInput.clear()
        # usernameInput.send_keys(username)

        passwordInput = self.webdriver.find_element_by_class_name(
            "password-hidden")
        passwordInput.clear()
        passwordInput.send_keys(password)

        loginButton = self.webdriver.find_element_by_css_selector(
            "a.button-button")
        loginButton.click()
        time.sleep(5)

    def reboot(self, password):
        advancedButton = self.driverWait.until(
            EC.presence_of_element_located((By.XPATH, "//ul/li[@navi-value='advanced']/a")))
        advancedButton.click()
        time.sleep(2)

        systemButton = self.driverWait.until(
            EC.presence_of_element_located((By.XPATH, "//ul/li[@navi-value='system']/a")))
        systemButton.click()
        time.sleep(2)

        rebootButton = self.driverWait.until(
            EC.presence_of_element_located((By.XPATH, "//ul/li[@navi-value='reboot']/a")))
        rebootButton.click()
        time.sleep(5)

        rebootAllButton = self.driverWait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@title='REBOOT ALL']")))
        rebootAllButton.click()
        time.sleep(2)

        confirmButton = self.driverWait.until(
            EC.presence_of_element_located((By.XPATH, "//div/a[@title='Reboot']")))
        confirmButton.click()
        time.sleep(2)

        Logger.logInfo("Router rebooting")

        time.sleep(4)

    def logOut(self):
        self.driverWait.until(
            EC.presence_of_element_located((By.ID, "logout-button")))

        time.sleep(2)
        logoutButton = self.webdriver.find_element_by_xpath(
            "//div[@id='logout-button']/a")

        logoutButton.click()
