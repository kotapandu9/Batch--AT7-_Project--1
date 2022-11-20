#Name - k.pandu ranga rao
#Batch - AT-7
#Project - 1



# Test case ID: TC_Login_01
#Successful Employee login to OrangeHRM portal

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")       # link of website
driver.maximize_window()                                                               #maximize chrome
time.sleep(10)
driver.find_element(By.XPATH,"//*[contains(@name,'username')]").send_keys("Admin")     # user name
driver.find_element(By.XPATH,"//*[contains(@name,'password')]").send_keys("admin123")  #pass word
time.sleep(2)
driver.find_element(By.XPATH,"//*[contains(@class,'oxd-button')]").click()              #login click
time.sleep(5)
driver.close()





# Test case ID: TC_Login_02

#invalied credentials

#Test case -2

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,"//*[contains(@name,'username')]").send_keys("Admin")      # user name(
driver.find_element(By.XPATH,"//*[contains(@name,'password')]").send_keys("admin1223")  #pass word
time.sleep(2)
driver.find_element(By.XPATH,"//*[contains(@class,'oxd-button')]").click()              #login click
time.sleep(5)
msg = driver.find_element(By.XPATH,"//*[(text()='Invalid credentials')]").text          # message displayed
print(msg)
print(msg == "Invalid credentials")                                                     # message printed
driver.close()




# ID: TC_PIM_01

# pim module filling employee detailes

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,"//*[contains(@name,'username')]").send_keys("Admin")     # user name
driver.find_element(By.XPATH,"//*[contains(@name,'password')]").send_keys("admin123")  #pass word
time.sleep(2)
driver.find_element(By.XPATH,"//*[contains(@class,'oxd-button')]").click()             #login click
time.sleep(5)
driver.find_element(By.XPATH,"(//*[contains(@class,'oxd-text oxd-text--span oxd-main-menu-item--name')])[2]").click()
time.sleep(3)

driver.find_element(By.XPATH,"(//*[text()='Add Employee'])[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[contains(@name,'firstName')]").send_keys("hareesh")
driver.find_element(By.XPATH,"//*[contains(@name,'middleName')]").send_keys("kumar")
driver.find_element(By.XPATH,"//*[contains(@name,'lastName')]").send_keys("kota")

driver.find_element(By.XPATH,"//*[contains(@class,'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").click()
time.sleep(3)
driver.close()






#Test case ID: TC_PIM_02

# edited employee detailes
# after editeding will save data


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//*[contains(@name,'username')]").send_keys("Admin")     # user name
driver.find_element(By.XPATH,"//*[contains(@name,'password')]").send_keys("admin123")  #pass word
time.sleep(2)
driver.find_element(By.XPATH,"//*[contains(@class,'oxd-button')]").click()         #login click
time.sleep(5)
driver.find_element(By.XPATH,"(//*[contains(@class,'oxd-text oxd-text--span oxd-main-menu-item--name')])[2]").click() #click pim module
time.sleep(3)
driver.find_element(By.XPATH,"(//*[contains(@class,'oxd-icon bi-pencil-fill')])[5]").click() # edited 0204employee
time.sleep(3)
driver.find_element(By.XPATH,"//*[contains(@class,'oxd-input oxd-input--active orangehrm-firstname')]").clear()
time.sleep(3)
driver.find_element(By.XPATH,"//*[contains(@class,'oxd-input oxd-input--active orangehrm-firstname')]").send_keys("pandu")# new data in that field
driver.find_element(By.XPATH,"//*[contains(@class,'oxd-input oxd-input--active orangehrm-middlename')]").clear()
driver.find_element(By.XPATH,"//*[contains(@class,'oxd-input oxd-input--active orangehrm-middlename')]").send_keys("kota")
driver.find_element(By.XPATH,"(//*[contains(@class,'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')])[2]").click()
driver.close()





#Test case ID: TC_PIM_03

#Delete existed employee detailes

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//*[contains(@name,'username')]").send_keys("Admin")     # user name
driver.find_element(By.XPATH,"//*[contains(@name,'password')]").send_keys("admin123")  #pass word
time.sleep(2)
driver.find_element(By.XPATH,"//*[contains(@class,'oxd-button')]").click()         #login click
time.sleep(5)
driver.find_element(By.XPATH,"(//*[contains(@class,'oxd-text oxd-text--span oxd-main-menu-item--name')])[2]").click() #click pim module
time.sleep(3)

driver.find_element(By.XPATH, "//*[contains(@class,'oxd-icon-button oxd-table-cell-action-space')]").click()
driver.find_element(By.XPATH, "//*[contains(@class,'oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin')]").click()
driver.close()





