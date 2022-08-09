# Introduction

This folder contains UI tests for https://petfriends.skillfactory.ru/login

Test suite was created within the educational project and uses Selenium Web driver.

# How To Run Tests

1.  Try to download a web driver for your browser from official page: 

    https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

3. Move the driver to "tests" folder in project

5. You can run all test from tests folder uses the next commands:

  - for Mozila Firefox: py.test -v --driver Firefox --driver-path geckodriver.exe  -m 'all_test'
  - for Google Chrome: py.test -v --driver Chrome --driver-path chromedriver.exe  -m 'all_test'

Note: You must use your path to webdriver if don't move driver to tests folder. You can use different marks to run some tests suits:

      -  auth: tests for the autentification page: https://petfriends.skillfactory.ru/login
      -  main: tests for the main page: https://petfriends.skillfactory.ru/all_pets
      -  user: tests for the page "My Pets": https://petfriends.skillfactory.ru/my_pets
      -  neg: all negative tests
      -  pos: all positive tests
      -  all_tests: run all tests from the "test" folder
      
     For example: 
      py.test -v --driver Firefox --driver-path geckodriver.exe  -m 'auth'
      
      py.test -v --driver Chrome --driver-path chromedriver.exe  -m 'user'
      
      
  # Note
  
  The project can be improved and supplemented. Currently version use individual autentification for tests. Coming soon, I'm planning to make general authorization for classes
    
   
    
    

   
