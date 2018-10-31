from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# Define main function to run the test


def main(driver, url):
    # Get the home page of the site
    driver.get(url)
    sleep(1)

    # ---------------First test: Testing Logged out---------------
    print('Testing Customer Info is Restricted: ', end='')

    # Navigate to webpage
    driver.get('http://127.0.0.1:8000/customer_details/11055')

    # test if the not logged in alert is shown
    try:
        login_alert = driver.find_element_by_id("not_logged_in_alert")
    except Exception:
        print("FAILED")
        print("\n Testing Halted")
        exit()
    print("PASSED")

    print('Testing Car History Info is Restricted: ', end='')

    # Navigate to webpage
    driver.get('http://localhost:8000/car_details/14883')

    # test if history element is not on page
    try:
        car_history_logged_out = driver.find_element_by_id("history")
    except Exception:
        print("PASSED")

    # ---------------Second test: Testing Logged In---------------
    print('Testing Customer Info Logged In: ', end='')

    driver.get(url)

    # Navigate to login
    login_button = driver.find_element_by_id('login')
    sleep(1)
    login_button.click()
    sleep(1)

    # Login to website
    username_box = driver.find_element_by_id("id_username")
    username_box.send_keys("admin")
    password_box = driver.find_element_by_id("id_password")
    password_box.send_keys("admin")
    sleep(1)

    login_btn = driver.find_element_by_id("submit_btn")
    sleep(1)
    login_btn.click()

    # Navigate to webpage
    driver.get('http://127.0.0.1:8000/customer_details/11055')

    # Test if customer history is visible
    try:
        customer_info = driver.find_element_by_id("history")
    except Exception:
        print("FAILED")
        print("\n Testing Halted")
        exit()
    print("PASSED")

    print('Testing Car History Logged In: ', end='')

    # Navigate to webpage
    driver.get('http://localhost:8000/car_details/14872')

    # Test if car history is visible
    try:
        car_history = driver.find_element_by_id("history")
    except Exception:
        print("FAILED")
    print("PASSED")
    sleep(1)


# If this individual test is run, define vars and pass. Otherwise, main can be run directly
if __name__ == '__main__':
    driver_path = '../\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://127.0.0.1:8000'
    main(driver, url)
    driver.quit()
