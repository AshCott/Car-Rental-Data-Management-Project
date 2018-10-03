from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# Initialise Selenium
driver_path = './\drivers\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# Get the home page of the site
driver.get('http://127.0.0.1:8000')

# ---------------First test: Testing Login---------------
print('Testing Login: ', end='')

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

# Verify that user is logged in
login_btn = driver.find_element_by_id("login_welcome")
try:
    assert 'Welcome admin!' in login_btn.text
except AssertionError:
    print("FAILED")
    print("\n Testing Halted")
    exit()
print("PASSED")

# ---------------Second test: Testing Logout---------------
print('Testing Logout: ', end='')

# Click Loggout
logout_btn = driver.find_element_by_id("logout_btn")
sleep(1)
logout_btn.click()

# Verify that user is logged out
logged_out_message = driver.find_element_by_id("logged_out_message")
try:
    assert 'You are logged out' in logged_out_message.text
except AssertionError:
    print("FAILED")
    print("\n Testing Halted")
    exit()
print("PASSED")
sleep(1)

print("Tests Passed:", str(2)+ "/" + str(2))

# Clean Up
driver.quit()