from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint

def main(driver, url):
    # Get the home page of the site
    driver.get(url)
    # Get the store to test
    testStore = randint(1,40)
    sleep(1)

    # First test: Click the 'See All Stores' button
    store = driver.find_element_by_name('Stores')
    sleep(1)
    store.click()
    sleep(1)

    # Second test: Testing Link to the Individual Stores Page
    firstLink = driver.find_elements_by_name("link")
    firstLinkText = firstLink[testStore-1].text # Storing Store Location variable for use in the 3rd test
    firstLinkText = firstLinkText.split(',')[0] # convert to proper format
    firstLink[testStore-1].click()

    # Third test: Making sure correct individual store has been opened
    storeLocation = driver.find_element_by_id("StoreName").text # Finding Store Location from table

    # Comparing the Store Location found in the Stores Page to the location found
    # in the hyperlink that was clicked on to direct to the stores page
    if firstLinkText == storeLocation: # If variables match
        print("The Stores Page has been Verified: Correct Stores page has been opened.") # Test has been passed
    else: # If variables don't match
        print("The third test has failed: Incorrect Stores page has been opened") # Test has failed

    # Fourth test: Testing Avaliable Car Links
    firstCarLink = driver.find_element_by_name("CarInStore")
    firstCarLinkText = driver.find_element_by_name("CarInStore").text
    firstCarLink.click()

    # Fifth test: Making sure correct Car Details page is displayed
    CarInfo = driver.find_element_by_name("CarTitle").text # Finding Store Location from table

    # Comparing the Car Info found in the Car Details Page to the Car Info
    # in the hyperlink that was clicked on to direct to the Car Details Page
    if firstCarLinkText == CarInfo: # If variables match
        print("The Car Details Page has been Verified: Correct details page has been opened.") # Test has been passed
    else: # If variables don't match
        print("The Fifth test has failed: Incorrect Details page has been opened") # Test has failed

    sleep(1)

if __name__ == '__main__':
    driver_path = '../\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://127.0.0.1:8000'
    main(driver, url)
    driver.quit()
