try:
    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    # Selenium was not installed
    pass


class YahooSelenium(object):

    LOGIN_URL = "https://login.yahoo.com"

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--ignore-ssl-errors")
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options,
        )

    def yahoo_login(self):
        try:
            self.driver.execute_script("window.open('{}');".format(self.LOGIN_URL))
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
            return {'cookies': cookies}
        except TimeoutException:
            return (
                "A timeout exception has occured.  Most likely it's due "
                "to invalid login credentials.  Please try again."
            )
