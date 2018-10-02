from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#driver_path = 'C:\\Users\\35nig_000\\Downloads\\geckodriver-v0.22.0-win64\\geckodriver.exe' 
driver_path = './\drivers\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

# Get the home page of the site
driver.get('http://127.0.0.1:8000')

# First test: Click search button
search_link = driver.find_element_by_name('search')
sleep(1)
search_link.click()
sleep(1)
#assert 'Car Rental Company' in driver.title

# Second Test = Enter a car make into the search bar.
searchBar = driver.find_element_by_id("carNAME")
searchBar.send_keys("BMW")
sleep(1)

# Third Test = Submit the search.
enter = driver.find_element_by_id("searchbtn")
sleep(1)
enter.click()
sleep(1)

# Fourth Test = Search by model
modelSearch = driver.find_element_by_id("searchBy")
sleep(1)
modelSearch.click()
sleep(1)
modelenter = driver.find_element_by_name("model")
sleep(1)
modelenter.click()
searchBar = driver.find_element_by_id("carNAME")
sleep(1)
searchBar.send_keys(Keys.BACKSPACE)
searchBar.send_keys(Keys.BACKSPACE)
searchBar.send_keys(Keys.BACKSPACE)
searchBar.send_keys("X5")
sleep(1)

# Clean up
#driver.quit()
