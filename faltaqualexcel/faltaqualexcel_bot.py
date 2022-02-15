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

from selenium.webdriver.common.alert import Alert
  

sheet_url = "https://docs.google.com/spreadsheets/d/1RA_j5wL6gTi7zd5DvyNJ_yQXcfNDCyNPuTjCTBpg_Ek/edit#gid=0"
url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=") 
df=pd.read_csv(url_1)

# print((df))

driver=webdriver.Chrome(ChromeDriverManager().install())


driver.get('http://faltaqualexcel.stockexcel.com/OnlineInspect.aspx')
time.sleep(3)
driver.find_element_by_xpath('/html/body/form/div[3]/div/table/tbody/tr[1]/td[3]/input').send_keys('subham')
driver.find_element_by_xpath('/html/body/form/div[3]/div/table/tbody/tr[2]/td[3]/input').send_keys('subham@098')
driver.find_element_by_xpath('/html/body/form/div[3]/div/table/tbody/tr[2]/td[3]/input').send_keys(Keys.ENTER)
time.sleep(3)
for i in range (123,139):
# for i in range(135,len(df['Buyer Code'].values.tolist())+1):
    # driver.get('http://faltaqualexcel.stockexcel.com/OnlineInspectCheck.aspx?OIC_ID=173068&ItemID=100775')
    # driver.get('http://faltaqualexcel.stockexcel.com/OnlineInspectDisplay.aspx')
    driver.get('http://faltaqualexcel.stockexcel.com/OnlineInspect.aspx')
    driver.maximize_window()
    time.sleep(2)
    print(df['Buyer Code'][i],"index",i)
    
    # filing date .
    driver.find_element_by_xpath('/html/body/form/div[3]/div[7]/div/div/table/tbody/tr[4]/td[3]/input').clear()
    
    driver.find_element_by_xpath('/html/body/form/div[3]/div[7]/div/div/table/tbody/tr[4]/td[3]/input').send_keys(str(df['Check Date'][i]))
    
    # filing buyer code .
   
    el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlBuyerCode')
    el.send_keys(df['Buyer Code'][i])
    time.sleep(6)
    
    
    

    # order number ...
    if int(float(df['Order No'][i]))<10:
        el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlOrderNo')
        
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(("00")+str(int(float(df['Order No'][i])))):
                option.click() # select() in earlier versions of webdriver
                break
    elif 10<int(float(df['Order No'][i]))<100:
        el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlOrderNo')
        
        # el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlOrderNo')
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(("0")+str(int(float(df['Order No'][i])))):
                option.click() # select() in earlier versions of webdriver
                break        
    else:
        el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlOrderNo')
        
        # el = driver.find_element_by_id('ContentPlaceHolder1_ddlOrderNo')
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(str(int(float(df['Order No'][i])))):
                option.click() # select() in earlier versions of webdriver
                break 
            
    ##  Iteam code 
    time.sleep(3)      
    el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlItemCode')
    el.send_keys(str(int(float(df['Item Code'][i]))))
    
    # Color .. 
    el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlColor')
    el.send_keys(str(df['Color'][i]))
    
    
    # Line Name ..await
    
    
    # line name ...
    el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlLineNo')
    el.send_keys(str(df['Line Name'][i]))  
    
      
     ## line superviser ..
    el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlLineSuperVisor')
    el.send_keys(str(df['Line Supervisor'][i]))  
    
    # quality inspecter ..
    el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlQCInspector')
    el.send_keys(str(df['Q.C. Inspector'][i]))  
    
    # /html/body/form/div[3]/div[7]/div/div/table/tbmjmjhmjhmjhmjhmhmghmghmnghmghmghnhnymghmtymtmttttttttttttttody/tr[6]/td[11]/input
    # Q.F No
    el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_txtQFNo')
    el.clear()
    el.send_keys(str(df['Q.F No'][i])) 
    # time.sleep(20)reser7y6r
    
    
    # click on add button ..
    
    time.sleep(2)
    add_buton=driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnAdd')
    add_buton.click()
    
    # click on first link of the list ..
    time.sleep(4)
    
    driver.find_element_by_xpath('/html/body/form/div[3]/div[7]/div/table/tbody/tr[4]/td/div/table/tbody/tr[2]/td[1]/table/tbody/tr/td[3]/a').click()
    
    # clik on add new button ..
    
    time.sleep(2)
    driver.find_element_by_id('ctl00_ContentPlaceHolder1_lbtnAdd').click()
    # Entering operaor number ..
    time.sleep(3)
    driver.find_element_by_id('ctl00_ContentPlaceHolder1_txtOperatorNo').send_keys(str(df['Operator No'][i]))
    
    # operations number ..
    time.sleep(6)
    el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlOperationNo')
    if (int(float(df['Operation No'][i])))<10:
         for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format("0"+str(df['Operation No'][i])):
                option.click() # select() in earlier versions of webdriver
                break  
        
        # driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlOperationNo').send_keys("0"+str(df['Operation No'][i]))
    else:
        # el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlOperationNo')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(str(df['Operation No'][i])):
                option.click() # select() in earlier versions of webdriver
                break  
     
        # driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlOperationNo').send_keys(str(df['Operation No'][i]))
        
    # checked ..
    time.sleep(3)
    
    driver.find_element_by_id('ctl00_ContentPlaceHolder1_txtChkQty').send_keys(str(int(float(df['Checked Qty'][i]))))
    
    # Defect Found........
    
    el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlDefectStat')
    for option in el.find_elements_by_tag_name('option'):
        if option.text == '{}'.format(df['Defect Found'][i]):
            option.click() # select() in earlier versions of webdriver
            break  
    time.sleep(3) 
    # click on add check ....
    driver.find_element_by_id('ctl00_ContentPlaceHolder1_lbtnAddCheck').click()    
    time.sleep(3)
    # driver.find_element_by_xpath("//*[contains(text(), 'Details')]").click()
    
    
    ############### THIRD PAGE .... #################################.........
    soup=BeautifulSoup(driver.page_source,'html.parser')
    all_a=soup.find('tbody').find_all('a')[-1]

    # time.sleep(3)
    
    driver.get("http://faltaqualexcel.stockexcel.com/"+all_a.get('href'))
    # all_a=driver.find_element_by_xpath('/html/body/form/div[3]/div[7]/div[1]/div/table/tbody/tr[3]/td/div/table').find_elements_by_tag_name('a')
    # # all_a[-1].click()
    time.sleep(2)
    # # click on add deaails ..
    driver.find_element_by_id('ctl00_ContentPlaceHolder1_lbtnAdd').click()
    time.sleep(1)
    # defect name ..
    driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlDefect').send_keys(df['Defect Name'][i])
    time.sleep(3) 
    # defect method name ..  
    
    driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlMethod').send_keys(df['Method Name'][i])   
    # defect quantity ..
    time.sleep(2)
    try:
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_txtDefectQty').send_keys(str(int(float(df['Defect Qty'][i])) )) 
    except:
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_txtDefectQty').send_keys(str(df['Defect Qty'][i])) 
        
             
    # Rectify quantity ...
    driver.find_element_by_id('ctl00_ContentPlaceHolder1_txtRectify').send_keys(str(int(float(df['Rectify Qty'][i]))  )) 
    # print(all_a)
    # CLICK ON ctl00_ContentPlaceHolder1_lbtnAdd
    
    adddefect=driver.find_element_by_id('ctl00_ContentPlaceHolder1_lbtnDefectAdd')
    driver.execute_script("arguments[0].click();", adddefect)
    # driver.execute_script("arguments[0].click();", adddefect)
    # time.sleep(1000)