from selenium import webdriver
import os
from importlib import import_module
from time import sleep

# All variables may be changed to suit test cases. For example, change driver to firefox, or url to ifb299.rentals
driver_path = './\drivers\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
url = 'http://127.0.0.1:8000'

# Iterate over all files in (current)/subtests directory
for file in os.listdir(os.getcwd() + "/subtests"):
    # if it's a test, import it and run main
    if file.endswith(".py"):
        # Import the module using a relative import
        run = import_module('.' + file[:-3], package = 'subtests')
        print("Running " + run.__name__)
        run.main(driver, url)
        print("Finished " + run.__name__)
        sleep(3)

driver.quit()
