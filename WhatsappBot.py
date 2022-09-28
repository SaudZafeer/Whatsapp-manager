from argparse import Action
from ast import Try
import pywhatkit
import imp
from importlib.resources import path
from msilib.schema import File
from multiprocessing import Value
from re import I, search
import time
from tkinter.ttk import Style
from tokenize import Name
from urllib import response
from selenium import webdriver
import pyscreenshot
from PIL import ImageGrab
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import os
import openpyxl
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
from PIL import Image
from io import BytesIO
from os import listdir
from os.path import isfile, join
import pandas as pd
from pathlib import Path
import datetime
import pyautogui, sys
import psutil
import shutil
import  requests


def get_profile_path(profile):
    FF_PROFILE_PATH = os.path.join(os.environ['APPDATA'],'Mozilla', 'Firefox', 'Profiles')

    try:
        profiles = os.listdir(FF_PROFILE_PATH)
    except WindowsError:
        print("Could not find profiles directory.")
        sys.exit(1)
    try:
        for folder in profiles:
            print(folder)
            if folder.endswith(profile):
                loc = folder
    except StopIteration:
        print("Firefox profile not found.")
        sys.exit(1)
    return os.path.join(FF_PROFILE_PATH, loc)

mime_types = "text/csv"
profile = webdriver.FirefoxProfile(get_profile_path('9t4cu8gz.For Azn_data_u4'))

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
Gecko_path = r"C:\Users\junai\OneDrive\Reporting\U2\gecko\geckodriver.exe"
driver = webdriver.Firefox(firefox_profile=profile ,executable_path= Gecko_path, options=options)


#CreATING WHatsapp function
def whatsapp():
    url = 'https://web.whatsapp.com'
    driver.get(url)
    driver.maximize_window()
    WebDriverWait(driver, 10)
    #let the user scan the barcode
    time.sleep(30)
    
    data = pd.read_excel (r"C:\Users\junai\Downloads\RequiredText(2).xlsx") 

    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data, columns=['style','gender','price','image'])
    print("Given Dataframe :\n", df)
    print(type(df))
    print("\nIterating over rows using iloc function :\n")
    #Clicking on whatsapp searchBar
    driver.find_element(By.CSS_SELECTOR,"#side > div.uwk68 > div > div > div._16C8p > div > div._13NKt.copyable-text.selectable-text").click()
    time.sleep(5)
    #control A
    driver.find_element(By.CSS_SELECTOR,"#side > div.uwk68 > div > div > div._16C8p > div > div._13NKt.copyable-text.selectable-text").send_keys(Keys.CONTROL+'a')
    time.sleep(5)
    #inserting name of the person/group on the search bar
    driver.find_element(By.CSS_SELECTOR,"#side > div.uwk68 > div > div > div._16C8p > div > div._13NKt.copyable-text.selectable-text").send_keys(int and str("Styles") + Keys.ENTER)
    time.sleep(3)
    #clicking on the chat of the person/group
    driver.find_element(By.CSS_SELECTOR,"._2_TVt > div:nth-child(2)").click()
    time.sleep(3)
    #loop to iterate our df
    #Creating A Loop to iterate our xlsx files
    for styles,gender,price,img in df.itertuples(index=False):
        #clicking on message box
        folder = r"C:\Users\junai\Downloads\Saad Bhai Images"
        for filename in os.listdir(folder):
            if styles in filename:
                driver.find_element(By.CSS_SELECTOR, "._2jitM > div:nth-child(1) > div:nth-child(1)").click()

                image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys(r"C:\Users\junai\Downloads\Saad Bhai Images\%s"%(filename))
                message_text = "*%s*"%(styles)
                # print(message_text)
                
                time.sleep(2)
                #clicking on textbar
                message_box=driver.find_element(By.CSS_SELECTOR,".Z2O8p > div:nth-child(2)")
                time.sleep(2)
                
                
                #Clicking on msg box
                message_box.click()
                time.sleep(1)
                #sending msg (Only sending one character)
                message_box.send_keys(message_text)
                time.sleep(1)
                #Sending control keys to remove that one character
                message_box.send_keys(Keys.CONTROL+'a')
                time.sleep(1)
                #Sending msg again
                message_box.send_keys(message_text)
                time.sleep(1)
                #Msg sent 
                message_box.send_keys(Keys.ENTER)
                time.sleep(1)
                time.sleep(8)
            else:
                print('ok')
whts = whatsapp()
driver.quit()