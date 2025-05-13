# stdlib
from typing import Dict, List

# third party
from requests.cookies import RequestsCookieJar

try:
    # third party
    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
except ImportError:
    # Selenium was not installed
    has_selenium = False
else:
    has_selenium = True


class YahooFinanceHeadless:
    LOGIN_URL = "https://login.yahoo.com"

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.cookies = RequestsCookieJar()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--ignore-ssl-errors")
        chrome_options.set_capability("pageLoadStrategy", "eager")
        service = Service()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def login(self):
        try:
            self.driver.execute_script(f"window.open('{self.LOGIN_URL}');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.find_element(By.ID, "login-username").send_keys(self.username)
            self.driver.find_element(By.XPATH, "//input[@id='login-signin']").click()
            password_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "login-passwd"))
            )
            password_element.send_keys(self.password)
            self.driver.find_element(By.XPATH, "//button[@id='login-signin']").click()

            cookies = self.driver.get_cookies()
            self.driver.quit()
            self._add_cookies_to_jar(cookies)

        except TimeoutException:
            return (
                "A timeout exception has occured.  Most likely it's due "
                "to invalid login credentials.  Please try again."
            )

    def _add_cookies_to_jar(self, cookies: List[Dict]):
        for cookie in cookies:
            cookie_dict = {
                "name": cookie["name"],
                "value": cookie["value"],
                "domain": cookie["domain"],
                "path": cookie["path"],
                "expires": None,  # You can set the expiration if available
            }
            self.cookies.set(**cookie_dict)
