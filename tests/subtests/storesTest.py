from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

def main(driver, url):
    # Get the home page of the site
    driver.get(url)

    # First test: Click the 'See All Stores' button
    store = driver.find_element_by_name('Stores')
    sleep(1)
    store.click()
    sleep(1)

    # Second test: Testing Link to the Individual Stores Page
    firstLink = driver.find_element_by_name("link")
    firstLinkText = driver.find_element_by_name("link").text # Storing Store Location variable for use in the 3rd test
    firstLink.click()

    # Third test: Making sure correct individual store has been opened
    storeLocation = driver.find_element_by_id("StoreName").text # Finding Store Location from table
    firstLinkText = "Location: " + firstLinkText # Converting link text to same format as storeLocation variable

    # Comparing the Store Location found in the Stores Page to the location found
    # in the hyperlink that was clicked on to direct to the stores page
    if firstLinkText == storeLocation: # If variables match
        print("The Stores Page has been Verified: Correct Stores page has been opened.") # Test has been passed

    if firstLinkText != storeLocation: # If variables don't match
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

    if firstCarLinkText != CarInfo: # If variables don't match
        print("The Fifth test has failed: Incorrect Details page has been opened") # Test has failed

if __name__ == '__main__':
    driver_path = './\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://127.0.0.1:8000'
    main(driver, url)
    driver.quit()
