from selenium import webdriver
from time import sleep

def testLink(driver, item):
    # Find and click link
    link = driver.find_element_by_name(item)
    link.click()
    sleep(1)
    # Navigate home
    home_link = driver.find_element_by_name('Home')
    home_link.click()
    sleep(1)
    assert 'Car Rental Company' in driver.title

# Main function which tests the home page
def main(driver, url):
    # Get the home page of the site
    driver.get(url)

    # First test: assert that the title is correct
    assert 'Car Rental Company' in driver.title
    sleep(1)

    # Second test: ensure buttons lead to desired pages
    toTest = ["Home", "Search", "Login"]
    for item in toTest:
        testLink(driver, item)

# Define vars and call main if directly running test
if __name__ == '__main__':
    driver_path = './\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://127.0.0.1:8000'
    main(driver, url)
    driver.quit()
