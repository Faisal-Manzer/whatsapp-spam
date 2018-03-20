import time
from selenium import webdriver

#configure path of webdriver
#----------------------------------------------------
path = "/Users/faisal_manzer/Downloads/chromedriver"
#----------------------------------------------------

def errOcc(mess):
    print ""
    print mess
    p = input("Enter Any thing to continue... ")
def faisalMessage(message):
        messBox = driver.find_element_by_class_name('_3F6QL')
        messBox.click()
        messBox.send_keys(message)
        clickButton = driver.find_element_by_class_name("_2lkdt")
        clickButton.click()
def getMessage():
    try:
        message = input("What's your message: ")
        times = int(input("Number of times u want to send: "))
        delay = int(input("Set Delay for messages in sec: "))
        for x in range(0, times):
            try:
                faisalMessage(message)
                time.sleep(delay)
            except:
                errOcc("Sorry :( script is unable to send message... Have u done all steps")
    except:
        errOcc("Plz Enter Valid Value")
def intro():
    print "\nFaisal Manzer app just for fun"
    print "\n1. Scan The QR code"
    print "2. Go the the chat u whom want to send message"
    print "3. Enter 'X' to exit"
def clear():
    for x in range(0, 15):
        print("")
driver = webdriver.Chrome(path)
driver.get("https://web.whatsapp.com/")
exitCont = 0;
while not exitCont:
    clear()
    intro()
    doneAll = input("4. Enter 'Y' when done: ")
    if doneAll == 'Y' or doneAll == 'y':
        getMessage()
    if doneAll == 'x' or doneAll == 'X':
        exitCont = 1
print("Faisal Manzer\nThanks for using :)")
