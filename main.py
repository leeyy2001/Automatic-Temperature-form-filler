import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui

name = input("What is your name?")

#Assigns rank and name positions in the dropdown menu for the respective questions.
if name == "yy":
    rank_pos = 12
    name_pos = 17

elif name == "alvin":
    rank_pos = 8
    name_pos = 10

elif name =="yan":
    rank_pos = 12
    name_pos = 16

elif name == "julian":
    rank_pos = 12
    name_pos = 15

elif name == "kareem":
    rank_pos = 12
    name_pos = 18

day = datetime.datetime.now()

#instantiates the webdriver object and sets up the window to be in incognito mode.
option = webdriver.ChromeOptions()
option.add_argument("-incognito")

#defines the browser and option
browser = webdriver.Chrome(executable_path=r"D:\yylee\chromedriver.exe", options=option)

#Accesses the website using the link we provided it.
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdu2cOJxJtZjN-of4ycISSwyxw3o6DwO84CwKklpJJXu3QMUQ/viewform")

time.sleep(2)

#Finding all the classes that we will be using in this code for it to work.
date = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
rank_name = browser.find_elements_by_class_name("quantumWizMenuPaperselectContent")
temperature = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
submit_btn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")

#This sets up the day in dd/mm/yyyy format, and keys it into the form.
date[0].send_keys(day.strftime("%m" + "/" + "%d" + "/" + "%Y"))

#The function to select the appropriate Rank and Name selection from the respective dropdown menus.
def dropdown_clicker(x):
    for i in range(x):
        pyautogui.press("down")
    pyautogui.press("enter")

#Keying in the Rank and Name as well as temperature into the respective entries.
rank_name[0].click()
time.sleep(1)
dropdown_clicker(rank_pos)
time.sleep(1)
rank_name[14].click()
time.sleep(1)
dropdown_clicker(name_pos)
time.sleep(1)

temperature[1].send_keys("36.5")
temperature[2].send_keys("36.5")

#Click on the submit button.
submit_btn[0].click()

time.sleep(5)
