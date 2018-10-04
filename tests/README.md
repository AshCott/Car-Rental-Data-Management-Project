# Basics of writing Selenium tests

### Read the docs:

https://selenium-python.readthedocs.io/installation.html

### Download various drivers (starting with Chrome, add any more as required)

Very important to note that using a different driver requires you to change both the driver_path and the driver init - needs to be webdriver.Chrome, webdriver.Firefox depending on specified browsers

### Change the driver_path variable

The driver exe files are available in the drivers folder, and can be accessed using the string format './\\drivers\\(driver name).exe'. This can be changed as necessary if a different browser is being tested.

### Base test cases off of the example - homepageTest.py

The example is a basic test case but covers core features of the Selenium library. Further info is available in the docs above and should be used where necessary to ensure good tests.
