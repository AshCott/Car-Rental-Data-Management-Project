from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

def main(driver, url):
    # Get the home page of the site
    driver.get(url)
    sleep(1)

    # First test: Click Featured Car 1
    featuredCar = driver.find_element_by_name('featureCar1')
    sleep(1)
    featuredCar.click()
    sleep(1)

    # Navigate back to the homepage
    sleep(1)
    driver.get('http://127.0.0.1:8000')
    sleep(1)

    # Second Test: Click search button
    search_link = driver.find_element_by_name('Search')
    sleep(1)
    search_link.click()
    sleep(1)

    # Second Test: Enter a car make into the search bar.
    searchBar = driver.find_element_by_id("carNAME")
    searchBar.send_keys("mazda")
    sleep(1)

    # Third Test: Submit the search.
    enter = driver.find_element_by_id("searchbtn")
    sleep(1)
    enter.click()
    sleep(3)

    # Fourth Test: Search by model
    modelSearch = driver.find_element_by_id("searchBy")
    modelSearch.click()
    sleep(1)
    modelenter = driver.find_element_by_name("series")
    modelenter.click()
    sleep(1)
    searchBar = driver.find_element_by_id("carNAME")
    searchBar.send_keys(Keys.BACKSPACE)
    searchBar.send_keys(Keys.BACKSPACE)
    searchBar.send_keys(Keys.BACKSPACE)
    searchBar.send_keys(Keys.BACKSPACE)
    searchBar.send_keys(Keys.BACKSPACE)
    searchBar.send_keys("SHADES")
    enter = driver.find_element_by_id("searchbtn")
    sleep(1)
    enter.click()
    sleep(1)

    # Select first name in the table
    table = driver.find_element_by_name("year")
    table.send_keys(Keys.TAB)
    sleep(1)
    currentElement = driver.switch_to_active_element()
    currentElement.click()

if __name__ == '__main__':
    driver_path = '../\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://127.0.0.1:8000'
    main(driver, url)
    driver.quit()
