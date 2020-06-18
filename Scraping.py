# -*- coding: utf-8 -*-
'''
# =============================================================================
  @author: IvanC-IT
   
  This code was run on Windows!
# =============================================================================
'''
try:
    import selenium
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'selenium'])
    import selenium
try:
    import requests
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'requests'])
    import requests

try:
    import time
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'time'])
    import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

download_dir = '' # name folder
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('window-size=800,600')# window size
preferences = {"download.default_directory": download_dir,"directory_upgrade": True,"safebrowsing.enabled": True }
chrome_options.add_experimental_option("prefs", preferences)
url = input('Entered your url (exsample:  google.com)-> ')
path_eseguibile_chrome = r'C:\Users\USERNAME\.wdm\drivers\chromedriver\83.0.4103.39\win32\chromedriver' # insert your uesr
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=path_eseguibile_chrome) 
driver.get('https://'+url);

'''
# =============================================================================
  To implement the commands for scraping see the official Selenium page at    
 'https://selenium-python.readthedocs.io/installation.html'                   
# =============================================================================
'''
