import selenium.webdriver
from selenium import webdriver

driver = webdriver.Chrome()

search_input = selenium.webdriver.Chrome.find_element_by_name('quit')

driver.quit()
