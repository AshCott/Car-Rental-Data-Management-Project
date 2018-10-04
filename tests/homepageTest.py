from selenium import webdriver
from time import sleep

driver_path = './\\drivers\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

def testLink(item):
    # Find and click link
    link = driver.find_element_by_name(item)
    link.click()
    sleep(1)
    # Navigate home
    home_link = driver.find_element_by_name('Home')
    home_link.click()
    sleep(1)
    assert 'Car Rental Company' in driver.title

# Get the home page of the site
driver.get('http://127.0.0.1:5000')

# First test: assert that the title is correct
assert 'Car Rental Company' in driver.title
sleep(1)

# Second test: ensure buttons lead to desired pages
toTest = ["Home", "Search", "Login"]
for item in toTest:
    testLink(item)

# Clean up
driver.quit()
