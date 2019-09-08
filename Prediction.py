from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import cv2

pause()

driver = webdriver.Chrome("C:/Users/HP/Documents/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("https://cloud.google.com/automl/ui/vision/datasets/predict?dataset=ICN181326302667377721&model=ICN9201703406336611204&project=pennapps-2019")

#Uses the Selenium Module of Python to open up the Predict WIndow
#ENTER USERNAME AND PASSWORD
