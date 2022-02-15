








import requests
import pandas as pd
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import seed
from random import random
from time import process_time, sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
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
import pytube
import youtube_dl

from selenium.webdriver.common.alert import Alert

from pytube import Playlist
from pytube import YouTube

driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://www.youtube.com/')
driver.get('https://www.youtube.com/c/CodeWithHarry/playlists')
driver.maximize_window()
time.sleep(3)
# click on each playlist button .abs(x) ..

thumbnails_buttons=driver.find_elements_by_id('playlist-thumbnails')
for b in thumbnails_buttons:
    driver.execute_script("arguments[0].click();", b)
    time.sleep(3)
    playlist_url=driver.current_url
    p = Playlist(playlist_url)
    print(p.video_urls)
    for url in p.video_urls:
        yt=YouTube(url)
        t=yt.streams.filter(only_audio=True).all()
        t[0].download()   
    
    
    time.sleep(3)

time.sleep(50)