from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def main(driver, url):
    # Get the home page of the site
    driver.get(url)

    # First test: Click the 'Recommended Cars' button
    recommendation = driver.find_element_by_id('Recommendation')
    sleep(1)
    recommendation.click()
    sleep(1)

    # Second Test: Recommendations by Store
    select_city = Select(driver.find_element_by_id('select_city'))
    sleep(1)
    select_city.select_by_visible_text('Alexandria') # select by visible text
    sleep(1)
    search = driver.find_element_by_id('Search')
    sleep(1)
    search.click()
    sleep(1)
    more_Info = driver.find_element_by_id('More_Info')
    sleep(1)

    sleep(1)

    # select by visible text
    #select.select_by_visible_text('Alexandria')
    # select by value
    #select.select_by_value('1')

if __name__ == '__main__':
    driver_path = './\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://127.0.0.1:8000'
    main(driver, url)
    driver.quit()
