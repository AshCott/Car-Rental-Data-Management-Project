from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


driver_path = './\drivers\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

# Get the home page of the site
driver.get('http://127.0.0.1:8000')

logIn = driver.find_element_by_id('login')
sleep(1)
logIn.click()
sleep(1)


usernameField = driver.find_element_by_id("id_username")
usernameField.send_keys("admin")
sleep(1)
usernameField = driver.find_element_by_id("id_password")
usernameField.send_keys("admin")
sleep(1)
login = driver.find_element_by_id('submit_btn')
login.click()
sleep(3)

# First test: Click search button

home = driver.find_element_by_name('Home')
home.click()
sleep(1)

#assert 'Car Rental Company' in driver.title
featuredCar1 = driver.find_element_by_name('featureCar1')
featuredCar1.click()
sleep(1)

historyOpen = driver.find_element_by_id('history')
historyOpen.click()
sleep(1)

# Clean up
#driver.quit()
