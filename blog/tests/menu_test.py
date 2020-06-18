from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from basetest import SeleniumTestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


chromedriver_path = 'C:/Users/laure/bin/chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())


#User hears about a blog website they want to visit. They head over to its homepage.
browser.get('https://laurenalie.pythonanywhere.com/')



#User notices the page title has the name of the person's blog.
assert 'Lauren Alie\'s blog' in browser.title



#User wants to navigate through the website so clicks on menu icon (then closes it)
browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']").click()


def checkMenuCloses():
    close = browser.find_element_by_class_name('closebtn')  
    try:
        browser.execute_script("arguments[0].click();", close)    
        #print("successful close of menu")
    except NoSuchElementException:
        print("menu failed to close") 
        

#User navigates to Featured page then closes the menu
def checkFeatured():
    menu = browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']")
    browser.execute_script("arguments[0].click();", menu)    
    try:
        featured = browser.find_element_by_link_text("Featured")
        browser.execute_script("arguments[0].click();", featured) 
        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/#featured"
        checkMenuCloses()
    except NoSuchElementException:
        print("failed to load featured")
        pass


#User navigates to About Me page then closes the menu
def checkAbout():
    menu = browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']")
    browser.execute_script("arguments[0].click();", menu)    
    
    try:
        about = browser.find_element_by_link_text("About Me")
        browser.execute_script("arguments[0].click();", about)
        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/#about"
        checkMenuCloses()
    except NoSuchElementException:
        print("failed to load about me")
        pass

   
# User navigates to All Posts page then closes the menu
def checkPosts():
    menu = browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']")
    browser.execute_script("arguments[0].click();", menu)   
     
    
    try:
        posts = browser.find_element_by_link_text("All Posts")
        browser.execute_script("arguments[0].click();", posts)

        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/#posts"
        checkMenuCloses()
    except NoSuchElementException:
        print("failed to load posts")
        pass
    
    browser.execute_script("arguments[0].click();", posts)

    current = browser.current_url
    assert current == "https://laurenalie.pythonanywhere.com/#posts"
    checkMenuCloses()

# User navigates to About Me page then closes the menu
def checkCV():
    menu = browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']")
    browser.execute_script("arguments[0].click();", menu)    
    
    try:
        cv = browser.find_element_by_link_text("CV")
        browser.execute_script("arguments[0].click();", cv)

        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/resume/1/"
        checkMenuCloses()
    except NoSuchElementException:
        print("failed to load cv")
        pass
    
   

#User navigates back to Home page then closes the menu
def checkHome():
    menu = browser.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']")
    browser.execute_script("arguments[0].click();", menu)    
    
    try:
        home = browser.find_element_by_link_text("Home")
        browser.execute_script("arguments[0].click();", home)
    
        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/#home"
        checkMenuCloses()
    except NoSuchElementException:
        print("failed to load home")
        pass

    

#User wants to connect with blog creator on socia media.
#User clicks on the GitHub icon and is navigated to the creator's Github profile. They click the back button to navigate back to the blog homepage.
def checkGitHub():
    browser.find_element_by_xpath("//i[@class='fab fa-github']").click()
    current = browser.current_url
    assert current == "https://github.com/lxz10"
    browser.get("https://laurenalie.pythonanywhere.com/")

#User clicks on the LinkedIn icon and is navigated to the creator's LinkedIn profile. They click the back button to navigate back to the blog homepage.

def checkLinkedIn():
    linkedin = browser.find_element_by_xpath("//i[@class='fab fa-linkedin-in']")
    browser.execute_script("arguments[0].click();", linkedin)
    current = browser.current_url
    assert "linkedin.com" in current
    browser.get("https://laurenalie.pythonanywhere.com/")

#User clicks on the email icon and is navigated to create an email addressed to the blog creator. 


def checkEmail():
    browser.find_element_by_xpath("//i[@class='far fa-envelope']").click()
    current = browser.current_url
    assert current == "https://laurenalie.pythonanywhere.com/"

checkMenuCloses()
checkFeatured()
checkAbout()
checkPosts()
checkCV()
checkGitHub()
checkLinkedIn()
checkEmail()
print("Menu testing successful")
browser.quit()