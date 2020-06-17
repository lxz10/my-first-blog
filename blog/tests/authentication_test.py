from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chromedriver_path = 'C:/Users/laure/bin/chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())

#User hears about a blog website they want to visit. They head over to its homepage.
browser.get('http://127.0.0.1:8000')

#User wants to add a new blog post because they are logged in as the super user so they click on the "new post" page icon
#User navigates to page where they can enter title, text, image and featured (tick box) to create a new post

#User changes their mind and wants to go back to the homepage, so selects the home icon.

#User is logged in as superuser and wants to edit a post. They click on the first post from the all posts section of the website.
#User clicks pen (edit) icon to edit the post. The page updates to show the post_edit view where the user can change the title, text,
#image or whether the post is featured.

#User saves post and is redirected to the webpage showing the full post (post_detail view)

#User decided to delete post so clicks on bin icon. User is then redirected to the homepage (post_list view)
#The previously viewed post has been removed from the website

browser.quit()