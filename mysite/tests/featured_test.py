from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chromedriver_path = 'C:/Users/laure/bin/chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())

#User hears about a blog website they want to visit. They head over to its homepage.
browser.get('http://127.0.0.1:8000')

#User navigates to Featured page

#User wants to see all featured posts so flicks through carousel (both left and right)

#User wants to check out one of the featured posts so clicks on it to read more.
#When the user clicks on the post title, the page updates to show the full blog post on the left and the blog image on the right
#The user has successfully navigated to post_detail view



browser.quit()