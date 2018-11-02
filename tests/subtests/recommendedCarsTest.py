from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def main(driver, url):
    # Get the home page of the site
    driver.get(url)
    sleep(1)

    # First test: Click the 'Recommended Cars' button
    recommendation = driver.find_element_by_name('Recommendation')
    sleep(1)
    recommendation.click()
    sleep(1)

    # Second Test: Recommendations by Store
    select_city = Select(driver.find_element_by_id('select_city')) # Selecting City Dropbox
    sleep(1)
    select_city.select_by_visible_text('Alexandria') # Selecting Option Alexandria in Dropbox
    sleep(1)
    search = driver.find_element_by_id('Search') 
    sleep(1)
    search.click() # Clicking on the Search Button
    sleep(1)

    # Third Test: Clicking on the 'More Info' Button of the recommended Car
    more_Info = driver.find_element_by_id('More_Info')
    sleep(1)
    more_Info.click()
    sleep(1)

    # Redirecting Test back to the Recommendation Page
    driver.get(url) # Go back to the Homepage
    recommendation = driver.find_element_by_name('Recommendation') # Clicking on the recommendation button
    recommendation.click()
    sleep(1)

    # Fourth Test: Recommendations by Store and Car Brand - seeing if multiple requirement work.
    # Expectation is that there will be no Car recommended.
    select_city = Select(driver.find_element_by_id('select_city')) # Selecting City Dropbox
    sleep(1)
    select_city.select_by_visible_text('Brisbane') # Selecting Option Brisbane in Dropbox
    sleep(1)
    select_brand = Select(driver.find_element_by_id('select_car_brand'))  # Selecting Brand Dropbox
    sleep(1)
    select_brand.select_by_visible_text('MITSUBISHI') # Selecting Option MITSUBISHI in Dropbox
    sleep(1)
    search = driver.find_element_by_id('Search') 
    sleep(1)
    search.click() # Clicking on the Search Button
    sleep(1)

    #Fifth Test: Returning to the Recommendations page when no car has been recommended
    goBack = driver.find_element_by_id("goBack")
    sleep(1)
    goBack.click()
    sleep(1)


# Initialising the Test
if __name__ == '__main__':
    driver_path = '../\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://127.0.0.1:8000'
    main(driver, url)
    driver.quit()
