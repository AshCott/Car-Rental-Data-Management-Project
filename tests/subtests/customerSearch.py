from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

def main(driver, url):
    # Get the home page of the site
    driver.get(url)
    sleep(2)

    # Finding login buton
    logIn = driver.find_element_by_id('login')
    sleep(1)
    # Clicking Login button
    logIn.click()
    sleep(1)

    # Finding the Username field on login screen    
    usernameField = driver.find_element_by_id("id_username")
    usernameField.send_keys("admin")
    sleep(1)
   # Finding the password field on login screen
    usernameField = driver.find_element_by_id("id_password")
    usernameField.send_keys("admin")
    sleep(1)
    # Locating the submit button to log in.
    login = driver.find_element_by_id('submit_btn')
    # Clicking button
    login.click()
    sleep(3)

    # Finding and clicking customer info button
    logIn = driver.find_element_by_id('Customer_Info_Button')
    sleep(1)
    logIn.click()
    sleep(1)

    # Second Test = Enter a car make into the search bar.
    searchBar = driver.find_element_by_id('customerName')
    searchBar.send_keys("Ian")
    sleep(1)

    # Third Test = Submit the search.
    enter = driver.find_element_by_id("searchbtn")
    sleep(1)
    enter.click()
    sleep(3)

    # Search By customer address
    otherSearch = driver.find_element_by_id("searchBy")
    otherSearch.click()
    sleep(1)
    modelenter = driver.find_element_by_name("address")
    modelenter.click()
    sleep(1)

    # Remove previous search query entry
    searchBar = driver.find_element_by_id("customerName")
    searchBar.send_keys(Keys.BACKSPACE)
    searchBar.send_keys(Keys.BACKSPACE)
    searchBar.send_keys(Keys.BACKSPACE)

    # Search for a user address
    searchBar.send_keys("800 Corrinne Court")
    enter = driver.find_element_by_id("searchbtn")
    sleep(1)
    enter.click()
    sleep(1)
    
    # clean up by logging out first
    logout = driver.find_element_by_id('logout_btn')
    logout.click()

if __name__ == '__main__':
    driver_path = '../\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://127.0.0.1:8000'
    main(driver, url)
    driver.quit()
