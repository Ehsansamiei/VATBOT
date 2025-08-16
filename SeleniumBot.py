from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random 
import pandas as pd 
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#####################################################################

# مسیر chromedriver

service = Service(r"C:\Users\Taraz Mohaseb server\Desktop\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://ttms.tax.gov.ir/t3/UserPanel.aspx")


username_input = driver.find_element(By.NAME, "ctl00$txtUserName")
password_input = driver.find_element(By.NAME, "ctl00$txtPassword")
captcha_element = driver.find_element(By.ID, "ctl00_imgCaptcha")
captcha_input = driver.find_element(By.NAME, "ctl00$txtCaptcha")
driver.save_screenshot("full.png")

# گرفتن موقعیت و اندازه المنت
location = captcha_element.location
size = captcha_element.size

x = location['x']
y = location['y']
w = size['width']
h = size['height']

# برش تصویر برای فقط کپچا
image = Image.open("full.png")
captcha_image = image.crop((x, y, x + w, y + h))
captcha_image.save("captcha.png")


img = Image.open("captcha.png")
img = img.convert("L") 

threshold = 140
img = img.point(lambda x: 0 if x < threshold else 255)

text = pytesseract.image_to_string(img, lang='eng')
print("CAPTCHA:", text.strip())

username_input.send_keys("0946535167583")
password_input.send_keys("G2wRdUzW")
captcha_input.send_keys(text)

time.sleep(20)

BuyService = driver.find_element(By.ID, "ctl00_cphMain_Image1")
BuyService.click()

time.sleep(random.randint(10, 15))

selected_season = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//td[@class='GridTDOver' and text()='بهار']"))
)

actions = ActionChains(driver)
actions.double_click(selected_season).perform()

time.sleep(random.randint(5, 15))

show_detail = driver.find_element(By.NAME, "ctl00$cphMain$ctl00$btnShow_Detail")
show_detail.click()
time.sleep(500000000000000)
#####################################################################


# خوندن فایل اکسل
df = pd.read_excel("Info.xlsx")  # مسیر فایل رو اینجا بزار

# # پیمایش هر ردیف
for index, row in df.iterrows():
    username = row['userName']
    password = row['Password']
    ExemptSale = int(row['ExemptSale'])
    VAT169 = int(row['VAT169'])
    NetSales169 = int(row['NetSales169'])

# اینجا با هر ردیف کاری که میخوای انجام بده
    # print(f"UserName: {username} / Password: {password} / ExemptSale: {ExemptSale} / VAT169: {VAT169} / NetSales169:{NetSales169}")


#####################################################################