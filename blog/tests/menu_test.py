from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from basetest import SeleniumTestCase
from webdriver_manager.chrome import ChromeDriverManager


chromedriver_path = 'C:/Users/laure/bin/chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())


#User hears about a blog website they want to visit. They head over to its homepage.
browser.get('http://127.0.0.1:8000')



#User notices the page title has the name of the person's blog.
assert 'Lauren Alie\'s blog' in browser.title



#User wants to navigate through the website so clicks on menu icon (then closes it)
browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']").click()


def checkMenuCloses():
    close = browser.find_element_by_id("close")
    close.click()
    
    try:
        close  
        return "menu failed to close" 
    except:
        return "successful close of menu"

#User navigates to Featured page then closes the menu
def checkFeatured():
    browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']").click()
    
    browser.find_element_by_link_text("Featured").click()
    
    current = browser.current_url
    assert current == "http://127.0.0.1:8000/#featured"
    checkMenuCloses()

#User navigates to About Me page then closes the menu
def checkAbout():
    browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']").click()
    
    featured = browser.find_element_by_xpath("About Me").click()
    
    current = browser.current_url
    assert current == "http://127.0.0.1:8000/#about"
    checkMenuCloses()

# User navigates to All Posts page then closes the menu
def checkPosts():
    browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']").click()
    
    featured = browser.find_element_by_link_text("All Posts").click()
    
    current = browser.current_url
    assert current == "http://127.0.0.1:8000/#posts"
    checkMenuCloses()

# User navigates to About Me page then closes the menu
def checkAbout():
    browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']").click()
    
    featured = browser.find_element_by_link_text("About Me").click()
    
    current = browser.current_url
    assert current == "http://127.0.0.1:8000/#about"
    checkMenuCloses()

#User navigates back to Home page then closes the menu
def checkHome():
    browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']").click()
    
    featured = browser.find_element_by_link_text("Home").click()
    
    current = browser.current_url
    assert current == "http://127.0.0.1:8000/#home"
    checkMenuCloses()

#User wants to connect with blog creator on socia media.
#User clicks on the GitHub icon and is navigated to the creator's Github profile. They click the back button to navigate back to the blog homepage.
def checkGitHub():
    browser.find_element_by_xpath("//i[@class='fab fa-github']").click()
    
    current = browser.current_url
    assert current == "https://github.com/lxz10"

#User clicks on the LinkedIn icon and is navigated to the creator's LinkedIn profile. They click the back button to navigate back to the blog homepage.

def checkLinkedIn():
    browser.find_element_by_xpath("//i[@class='fab fa-linkedin-in']").click()
    
    current = browser.current_url
    assert current == "https://www.linkedin.com/in/lauren-alie-36b915149/"

#User clicks on the email icon and is navigated to create an email addressed to the blog creator. 


def checkEmail():
    browser.find_element_by_xpath("//i[@class='far fa-envelope']").click()
    
    current = browser.current_url
    assert current == "mailto:laurenalie0@gmail.com"

checkMenuCloses()
checkFeatured()
checkAbout()
checkPosts()
checkGitHub()
checkLinkedIn()
checkEmail()
#browser.quit()