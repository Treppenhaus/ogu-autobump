from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc

# VARIABLES TO CHANGE
username = "" #ur username
password = "" #ur password
threadurl = "" #ur threadurl
message = "" # message to send
bump_delay = 60 * 31 # 31 minutes


driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)

def c(selector):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector))).click()

def e(selector, inp):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector))).send_keys(inp)

def login():
    driver.get("https://ogu.gg/login")
    time.sleep(6)
    e("#fullcontainment > div > form:nth-child(3) > table > tbody > tr.tr-rounded > td > label > input", username)
    e("#fullcontainment > div > form:nth-child(3) > table > tbody > tr:nth-child(2) > td > label > input", password)
    time.sleep(1)
    c("#fullcontainment > div > form:nth-child(3) > table > tbody > tr:nth-child(4) > td > span > input")

def bump():
    driver.get(threadurl)
    time.sleep(6)
    e("#message", message)
    c("#quick_reply_submit")
    print("bump!")

login()
time.sleep(10)
while(1):
    bump()
    time.sleep(bump_delay)

# Close the webdriver