from basetest import SeleniumTestCase
from selenium import webdriver

class Title(SeleniumTestCase):
    def checkTitle(self):
       super().setUp()
       self.driver.get('https://laurenalie.pythonanywhere.com/')
       self.driver.implicitly_wait(3)
       title = self.driver.title
       assert "Django Girls blog" in title
       self.driver.implicitly_wait(3)
       super().tearDown()

    def __init__(self, name):
        self.name = name

title_check = Title("testing title")
title_check.checkTitle()
