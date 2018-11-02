from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

def main(driver, url):
    # Get the home page of the site
    driver.get(url)

    # Finding login buton
    logIn = driver.find_element_by_id('login')
    sleep(1)
    # Clicking Login button
    logIn.click()
    sleep(1)

    # Finding the Username field on login screen
    usernameField = driver.find_element_by_id("id_username")
    # Entering the username "admin"
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

    # Going back to homepage after logging in 
    # Finding home button and clicking
    home = driver.find_element_by_name('Home')
    home.click()
    sleep(1)

    # Using one of the featured cars on the home page
    # to go to individual results page
    featuredCar1 = driver.find_element_by_name('featureCar1')
    featuredCar1.click()
    sleep(1)

    # Attempt to open car rental history panel
      try:
        historyOpen = driver.find_element_by_id('history')
        historyOpen.click()
        sleep(1)
    except Exception:
        print("FAILED")
        print("\n Testing Halted")
        exit()
    print("PASSED")
    
   

    # clean up by logging out first
    logout = driver.find_element_by_id('logout_btn')
    logout.click()

if __name__ == '__main__':
    driver_path = '../\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://127.0.0.1:8000'
    main(driver, url)
    driver.quit()
