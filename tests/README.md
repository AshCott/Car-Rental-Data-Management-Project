# Basics of writing Selenium tests

### Read the docs:

https://selenium-python.readthedocs.io/installation.html

### Download various drivers (starting with Chrome)

Very important to note that using a different driver requires you to change both the driver_path and the driver init - needs to be webdriver.Chrome, webdriver.Firefox depending on specified browsers

### Change the driver_path variable

Must be the path to the downloaded browser driver installed on your computer for this to work. Where this is actually downloaded depends on the person, so it can't be the same for everyone.

### Base stuff off of the example - homepageTest.py

The example is very basic but it does cover some core functionality needed to test other portions of the site. The docs also cover a similar example and goes more in depth with regards to functionality.
