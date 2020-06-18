from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from basetest import SeleniumTestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

chromedriver_path = 'C:/Users/laure/bin/chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())

#User hears about a blog website they want to visit. They head over to its homepage.
browser.get('https://laurenalie.pythonanywhere.com/')

#User navigates to Featured page
def goToFeatured():
    menu = browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']")
    browser.implicitly_wait(2)
    browser.execute_script("arguments[0].click();", menu)    
    try:
        featured = browser.find_element_by_link_text("Featured")
        browser.execute_script("arguments[0].click();", featured)
        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/#featured"
    except NoSuchElementException:
        print("failed to go to Featured page")
        pass

#User wants to see all featured posts so flicks through carousel (both left and right)

def checkCarouselMovement():
    #Check right movement
    for i in range(3):
        next = browser.find_element_by_xpath('//a[@class="right carousel-control"]')
        browser.execute_script("arguments[0].click();", next)
        browser.implicitly_wait(3)
    #Check left movement
    for i in range(3):
        prev = browser.find_element_by_xpath('//a[@class="left carousel-control"]')
        browser.execute_script("arguments[0].click();", prev)
        browser.implicitly_wait(3)
 

#User wants to check out one of the featured posts so clicks on it to read more.

def readFeatured():
    #click on post
    try:
        image = browser.find_element_by_tag_name("img")
        browser.execute_script("arguments[0].click();", image)  
        current = browser.current_url
        assert "https://laurenalie.pythonanywhere.com/post" in current
    except NoSuchElementException:
        print("failed to go to post by clicking on image")

    #User returns to Home by clicking on home icon
    try:
        home = browser.find_element_by_xpath("//i[@class='fa fa-home']")
        browser.execute_script("arguments[0].click();", home) 
        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/"
    except NoSuchElementException:
        print("failed to return to homepage")

   


goToFeatured()
checkCarouselMovement()
readFeatured()
browser.quit()
print("Successfully navigated Featured Posts")