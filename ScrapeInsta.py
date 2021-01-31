
#imports here
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import random
import time
#specify the path to chromedriver.exe (download and save on your computer)
driver = wd.Chrome(executable_path='C:/Users/Anshu/Desktop/Web Scraping/chromedriver_win32/chromedriver.exe')
driver.get("http://www.instagram.com")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))



username.clear()
username.send_keys(input("Enter Insta Account Username: ")) #"test___911")
password.clear()
password.send_keys(input("Enter Insta Account Password: ")) #"test___9111")
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()



#target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

#search for the hashtag cat
keyword = input("Enter Insta Id :")
searchbox.send_keys(keyword)
 
# Wait for 5 seconds
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)



driver.execute_script("window.scrollTo(0, 4000);")

#target all images on the page
images = driver.find_elements_by_tag_name('img')
#checks if The account to be scraped is private or not
check= driver.find_elements_by_class_name('rkEop')
#content = driver.find_elements_by_class_name('cdsfahethjtj')
print(check)
#Condition to check if Insta Account is private
#if private then just save the diplay picture
# else all pics including display picture
if  check:        
    images = [image.get_attribute('src') for image in images]
    images = images[:1]
else:
    images = [image.get_attribute('src') for image in images]
    images = images[:-2]

print('Number of scraped images: ', len(images))



path = os.getcwd()
path = os.path.join(path, keyword[1:] + str(random.randint(1,10000)))
print(path)
#create the directory
os.mkdir(path)


counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
