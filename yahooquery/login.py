import random
import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from yahooquery.utils import USER_AGENT_LIST


class Login(object):

    LOGIN_URL = 'https://login.yahoo.com'

    def __init__(self, email, password, **kwargs):
        self.email = email
        self.password = password
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--user-agent=' + kwargs.get(
            'user_agent', random.choice(USER_AGENT_LIST)
        ))
        self.chrome_options.add_argument('headless')
        self.chrome_options.add_argument('--log-level=3')
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(
            chrome_options=self.chrome_options,
            desired_capabilities=self.chrome_options.to_capabilities()
        )

    def get_cookies(self):
        try:
            self.driver.execute_script("window.open('{}');".format(
                self.LOGIN_URL))
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.find_element_by_id('login-username').send_keys(
                self.email)
            self.driver.find_element_by_xpath(
                "//input[@id='login-signin']").click()
            password_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "login-passwd"))
            )
            password_element.send_keys(self.password)
            self.driver.find_element_by_xpath(
                "//button[@id='login-signin']").click()
            try:
                self.driver.find_element_by_link_text('Finance').click()
            except NoSuchElementException:
                self.driver.find_element_by_xpath('//a[@href="https://finance.yahoo.com/"]').click()
            cookies = self.driver.get_cookies()
            crumb = re.findall(
                '"CrumbStore":{"crumb":"(.+?)"', self.driver.page_source)
            if crumb:
                crumb = crumb[0].replace('\\u002F', '/')
            self.driver.quit()
            return {'cookies': cookies, 'crumb': crumb}
        except TimeoutException:
            return "A timeout exception has occured.  Most likely it's due to \
                    invalid login credentials.  Please try again."
