# Basics of writing Selenium tests

### Read the docs:

https://selenium-python.readthedocs.io/installation.html

### Change the driver_path variable

The driver exe files are available in the drivers folder, and can be accessed using the string format './\\drivers\\(driver name).exe'. This can be changed as necessary if a different browser is being tested.

### Base test cases off of the example - homepageTest.py

The example is a basic test case but covers core features of the Selenium library. Further info is available in the docs above and should be used where necessary to ensure good tests.

# Running tests

### Location of Tests:

Individual tests are all located in the subtests directory and can be run individually.

The master test function is located in this directory, and runs all tests in the subdirectory.

### Running tests:

Run any individual test on the command line with the usual command (eg. py homepageTest.py). Run all tests by running "py masterTest.py" while in the tests directory.
