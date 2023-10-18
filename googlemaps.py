from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep 

driver = webdriver.Chrome() 
driver.get("https://www.google.com/maps") 
sleep(5) 

def accept():
	   sleep(2)
	   accept=driver.find_element(By.XPATH,"/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button")
	   accept.click()
accept()

def searchplace():
	   sleep(3)
	   Place=driver.find_element(By.CLASS_NAME,"searchboxinput xiQnY")
	   Place.send_keys("Timisoara")
	   Submit=driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button")
	   Submit.click()
searchplace()

def directions():
	   sleep(4)	
	   directions=driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/span")
	   directions.click()
directions()

def find():
         sleep(4)
         find=driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
         find.send_keys("Deva")
         sleep(2)
         search=driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
         search.click()
find()

def kilometers():
               sleep(5)
               Totalkilometers=driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div")
               print("Total Kilometers:",Totalkilometers.text)
               sleep(5)
            #    Bus=driver.find_element(By.XPATH,"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
            #    print("Bus Travel:",Bus.text)
            #    sleep(7)
            #    Train=driver.find_element(By.XPATH,"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[1]/div")
            #    print("Train Travel:",Train.text)
            #    sleep(7)

kilometers()

# def available():
#                print("*COVID-19 Special Trains*")
#                sleep(7)
#                trainone=driver.find_element(By.XPATH,"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[2]/span/span[2]/span[1]/span[1]/span")
#                print("Train No:1",trainone.text)
               
# def availableone():           
# 	   trainsec=driver.find_element(By.XPATH,"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[2]/span/span[8]/span[1]/span[1]/span") 
# 	   print("Train No:2",trainsec.text)
# available()
# availableone()