from selenium import webdriver
from time import sleep

#driver_path = 'C:\\Users\\35nig_000\\Downloads\\geckodriver-v0.22.0-win64\\geckodriver.exe' 
driver_path = './\drivers\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

# Get the home page of the site
driver.get('http://127.0.0.1:8000')

# First test: assert that the title is correct
assert 'Car Rental Company' in driver.title
sleep(1)

# Second test: ensure button with "Home" text leads back to home page
home_link = driver.find_element_by_partial_link_text('Home')
sleep(1)
home_link.click()
sleep(1)
assert 'Car Rental Company' in driver.title

# Clean up
driver.quit()
