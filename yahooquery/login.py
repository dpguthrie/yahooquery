import random
import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Login(object):

    USER_AGENT_LIST = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    ]

    LOGIN_URL = 'https://login.yahoo.com'

    def __init__(self, email, password, **kwargs):
        self.email = email
        self.password = password
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--user-agent=' + kwargs.get(
            'user_agent', random.choice(self.USER_AGENT_LIST)
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
            self.driver.find_element_by_link_text('Finance').click()
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
