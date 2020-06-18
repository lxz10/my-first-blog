from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

chromedriver_path = 'C:/Users/laure/bin/chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())

# User navigates to blog
browser.get("https://laurenalie.pythonanywhere.com")

# User scrolls to All Posts

def scrollPosts():
    target = browser.find_element_by_id("posts")
    browser.execute_script('arguments[0].scrollIntoView(true);', target)
    

# User clicks on post title to look at post, then returns to all posts page via the menu to see the post_detail view
def viewPost():
    try:
        browser.get("https://laurenalie.pythonanywhere.com/#posts")
        post = browser.find_element_by_tag_name("a")
        browser.execute_script("arguments[0].click();", post)  
       # current = browser.current_url
       # print("current post url: " + current)
       # assert "https://laurenalie.pythonanywhere.com/post" in current
    except NoSuchElementException:
        print("failed to click on post to view")
    browser.get("https://laurenalie.pythonanywhere.com/#posts")


# User clicks on read more link on a post to see the post_detail view, then goes back to the all posts page
def readMore():
    try:
        more = browser.find_element_by_id("more")
        browser.execute_script("arguments[0].click();", more)
        current = browser.current_url
        assert "https://laurenalie.pythonanywhere.com/post" in current
    except NoSuchElementException:
        print("failed to find Read More button")
    browser.get("https://laurenalie.pythonanywhere.com/#posts")

# User clicks on comments link on a post to see the post_detail view with comments, then goes back to the all posts page
def seeComments():
    comments = browser.find_element_by_partial_link_text("Comments:")
    browser.execute_script("arguments[0].click();", comments)
    current = browser.current_url
    assert "https://laurenalie.pythonanywhere.com/post" in current
    browser.get("https://laurenalie.pythonanywhere.com/#posts")


scrollPosts()
viewPost()
readMore()
seeComments()
browser.quit()
print("Successfully navigated through All Posts page")
