from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc

# VARIABLES TO CHANGE
username = "" #ur username
password = "" #ur password


# make sure there is SAME amount of messages and threads! 4 threads = 4 messages in array!
threads = ["", "", "", ""]
messages = ["", "", "", ""]


bump_delay = (60 * 30 / len(threads)) + 60
print(f"bump delay: {bump_delay}")

driver = None
wait = None

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

def bump(threadurl, message):
    login()
    time.sleep(10)
    driver.get(threadurl)
    time.sleep(6)
    e("#message", message)
    time.sleep(1)
    c("#quick_reply_submit")
    time.sleep(1)
    print("bump!")
    driver.quit()

while(1):
    
    a = 0
    while(a < len(threads)):
        try:
            turl = threads[a]
            msg = messages[a]
        
            driver = uc.Chrome(use_subprocess=True)
            wait = WebDriverWait(driver, 20)
            bump(turl, msg)
            
            i = 0
            a += 1
            while(i < bump_delay):
                i += 1
                time.sleep(1)
                print(f"bumping again in {bump_delay-i} seconds")
        except:
            print("something went wrong! trying again in 60 seconds!")
            time.sleep(60)
            

# Close the webdriver
