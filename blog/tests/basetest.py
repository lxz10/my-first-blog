from selenium import webdriver
from django.test import LiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumTestCase(LiveServerTestCase):
    """
    A base test case for Selenium, providing hepler methods for generating
    clients and logging in profiles.
    """
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)

    def open(self, url):
        self.driver.get("%s%s" % (self.live_server_url, url))

    def tearDown(self):
        self.driver.quit()
