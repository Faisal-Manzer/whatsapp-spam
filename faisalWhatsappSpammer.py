from selenium import webdriver
import time
path = "/Users/faisal_manzer/Downloads/chromedriver"
driver = webdriver.Chrome(path)

def intro():
    print("\n\nCopyright Faisal Manzer")
    print("\n\nTo exit enter 'N'")
    print("\n1. Scan the QR Code")
    print("\n2. Go to the chat whom u want to send message")

def execute():
    message = raw_input("What's your message: ")
    times = int(raw_input("Number of times u want to send: "))
    delay = int(raw_input("Set Delay for messages in sec: "))
    for x in range(0, times):
        messBox = driver.find_element_by_class_name('_3F6QL')
        messBox.click()
        messBox.send_keys(message)
        clickButton = driver.find_element_by_class_name("_2lkdt")
        clickButton.click()
        time.sleep(delay)
exitCont = 1
driverCont = 1
while exitCont:
    intro()
    if driverCont:
        driver.get("https://web.whatsapp.com/")
        driverCont = 0
    yorn = raw_input("\n3. Enter 'Y' When Done: ")
    if yorn=='Y' or yorn=='y':
        execute()
    else:
        exitCont = 0