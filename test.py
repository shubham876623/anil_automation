from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import csv
from urllib.request import urlopen
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.alert import Alert
  

sheet_url = "https://docs.google.com/spreadsheets/d/1oFRyFMn1L2-yRnspTMocLBDgZMPLOQeK8Vt68SbEjLA/edit#gid=0"
url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=") 
df=pd.read_csv(url_1)

# print(type(df))


print("00"+str(int(float((df['Order'][260])))))