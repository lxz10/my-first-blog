from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from basetest import SeleniumTestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


chromedriver_path = 'C:/Users/laure/bin/chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://laurenalie.pythonanywhere.com/resume/1/')

#User checks page header says 'CV'
def checkHeader():
    try:
        header = browser.find_element_by_class_name('page-header').text
        assert header == "CV"
    except NoSuchElementException:
        print("failed to locate header text")
        pass

#User reads through CV, checking the name at the top of the CV is the same as the domain name
def checkName():
    try:
        name = browser.find_element_by_xpath('//div[@class="resume-main"]/h1').text
        assert name == "Lauren Alie"
    except NoSuchElementException:
        print("failed to locate name on CV")
        pass

#User clicks LinkedIn link to navigate to blogger's profile
def checkLink():
    try:
        link = browser.find_element_by_link_text("LinkedIn")
        browser.execute_script("arguments[0].click();", link) 
        current = browser.current_url
        assert "linkedin" in current
        browser.get('https://laurenalie.pythonanywhere.com/resume/1/')
        
    except NoSuchElementException:
        print("failed to located LinkedIn link")
        pass

#User checks CV has education, technology, other experience, volunteering,
# extra curricular, activities and references sections
def checkCVSections():
    experiences = ['Education', 'Technology Experience', 'Other Experience', 'Volunteering Work',
                    'Extracurricular Activities', 'Achievements', 'References']
    try:
        sections = browser.find_elements_by_xpath('//h2[resume-body]')
        for section in sections:
            assert section.text in experiences
    except NoSuchElementException:
        print ("failed to locate titles of CV experiences")
        pass

#User clicks home page to navigate back to home
def checkHome():
    try:
        home = browser.find_element_by_xpath("//i[@class='fa fa-home']")
        browser.execute_script("arguments[0].click();", home) 
        current = browser.current_url
        assert current == "https://laurenalie.pythonanywhere.com/"
    except NoSuchElementException:
        print("failed to navigate back to homepage") 
        pass


checkHeader()
checkName()
checkLink()
checkCVSections()
checkHome()
print("successfully navigated through CV page")
browser.quit()