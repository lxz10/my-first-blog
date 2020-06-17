from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chromedriver_path = 'C:/Users/laure/bin/chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())