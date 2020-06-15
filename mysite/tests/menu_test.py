from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chromedriver_path = 'C:/Users/laure/bin/chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())

#User hears about a blog website they want to visit. They head over to its homepage.
browser.get('http://127.0.0.1:8000')

#User notices the page title has the name of the person's blog.
assert 'Lauren Alie\'s blog' in browser.title

#User wants to navigate through the website so clicks on menu icon

#User navigates to Featured page

#User navigates to About Me page then closes the menu

#User navigates to All Posts page then closes the menu

#User navigates back to Home page then closes the menu

#User wants to connect with blog creator on socia media.
#User clicks on the GitHub icon and is navigated to the creator's Github profile. They click the back button to navigate back to the blog homepage.

#User clicks on the LinkedIn icon and is navigated to the creator's LinkedIn profile. They click the back button to navigate back to the blog homepage.

#User clicks on the email icon and is navigated to create an email addressed to the blog creator. 

browser.quit()