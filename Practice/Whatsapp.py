from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Users/erayo/OneDrive/Masaüstü/Python/chromedriver.exe")

driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("User : \n")
msg = input("Message : \n")
# count = input("Count : \n")

user = driver.find_element(By.XPATH,f'//span[@title="{name}"]')
user.click()

msg_box = driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
msg_box.click()

while True:
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.RETURN)
    #return enter tusuna tekrar tekrar basmaya yarar


