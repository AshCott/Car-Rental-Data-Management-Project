from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#driver_path = 'C:\\Users\\35nig_000\\Downloads\\geckodriver-v0.22.0-win64\\geckodriver.exe' 
driver_path = './\drivers\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

# Get the home page of the site
driver.get('http://127.0.0.1:8000')

# First test: Testing Login
login_button = driver.find_element_by_id('login')
sleep(1)
login_button.click()
sleep(1)
username_box = driver.find_element_by_id("id_username")
username_box.send_keys("admin")
password_box = driver.find_element_by_id("id_password")
password_box.send_keys("admin")
sleep(1)

login_btn = driver.find_element_by_id("submit_btn")
sleep(1)
login_btn.click()

login_btn = driver.find_element_by_id("login_welcome")
assert 'Welcome admin!' in login_btn.text

# Second test: Testing Logout
logout_btn = driver.find_element_by_id("logout_btn")
sleep(1)
logout_btn.click()

logged_out_message = driver.find_element_by_id("logged_out_message")

assert 'You are logged out' in logged_out_message.text

driver.quit()