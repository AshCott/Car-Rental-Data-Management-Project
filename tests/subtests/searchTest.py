from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

def main(driver, url):
    # Get the home page of the site
    driver.get(url)
    sleep(1)

    # First test: Click search button
    search_link = driver.find_element_by_name('Search')
    sleep(1)
    search_link.click()
    sleep(1)
    #assert 'Car Rental Company' in driver.title

    # Second Test = Enter a car make into the search bar.
    searchBar = driver.find_element_by_id("carNAME")
    searchBar.send_keys("BMW")
    sleep(1)

    # Third Test = Submit the search.
    enter = driver.find_element_by_id("searchbtn")
    sleep(1)
    enter.click()
    sleep(3)

    # Fourth Test = Search by model
    modelSearch = driver.find_element_by_id("searchBy")
    modelSearch.click()
    sleep(1)
    modelenter = driver.find_element_by_name("model")
    modelenter.click()
    sleep(1)
    searchBar = driver.find_element_by_id("carNAME")
    searchBar.send_keys(Keys.BACKSPACE)
    searchBar.send_keys(Keys.BACKSPACE)
    searchBar.send_keys(Keys.BACKSPACE)
    searchBar.send_keys("X5")
    enter = driver.find_element_by_id("searchbtn")
    sleep(1)
    enter.click()
    sleep(1)

if __name__ == '__main__':
    driver_path = '../\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://127.0.0.1:8000'
    main(driver, url)
    driver.quit()
