from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

chromedriver_path = 'C:/Users/laure/bin/chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())

# User navigates to a blog post
browser.get("https://laurenalie.pythonanywhere.com/post/1")

# User scrolls to bottom of page to read post
def scrollPost():
    target = browser.find_element_by_link_text("Add comment")
    browser.execute_script('arguments[0].scrollIntoView(true);', target)

#User tries to submit empty comment but fails
def noComment():
    try:
        send = browser.find_element_by_css_selector("body > div.content.container > div > div > form > button")
        browser.execute_script("arguments[0].click();", send)  
        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/post/1/comment/"
    except NoSuchElementException:
        print("failed to find send button")

# User decides to add a comment to the post
# User fills out form to add a comment, then sees their comment appear on the webpage
def addComment():
    try:
        comment = browser.find_element_by_link_text("Add comment")
        browser.execute_script("arguments[0].click();", comment)  
        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/post/1/comment/"
        noComment()
        author = browser.find_element_by_id("id_author")
        author.send_keys("Stranger")
        text = browser.find_element_by_id("id_text")
        text.send_keys("Great article!")
        send = browser.find_element_by_css_selector("body > div.content.container > div > div > form > button")
        browser.execute_script("arguments[0].click();", send)  
        commented = browser.current_url
        assert commented == "https://laurenalie.pythonanywhere.com/post/1/"
    except NoSuchElementException:
        print("failed to find comment button")


#User navigates back to home page by clicking on the home icon
def goHome():
    try:
        home = browser.find_element_by_xpath("//i[@class='fa fa-home']")
        browser.execute_script("arguments[0].click();", home) 
        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/"
    except NoSuchElementException:
        print("failed to navigate back to homepage") 
        pass

scrollPost()
addComment()
goHome()

browser.quit()
print("Successfully viewed post and added comment")