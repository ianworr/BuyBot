
# Initializing Program ----------------------------------------------------------------- 1.0 -


#import packages for selenium operation -------------------------------------------------1.1
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

#import login and website info module
import info

# Create classes ------------------------------------------------------------------------1.2

class Tabi():
    """docstring for ClassName"""
    def __init__(self,dom):
        # Figuring out what tab this is
        self.tab = '' #  Tab identifier
        self.dom = dom #  The exact URL for the product
        self.url = self.dom.split('/')[2] #  Figuring out what website it is
        
        #  Import site specific information based on the website from info module
        paths = info.paths(self.url) 

        # Assign website specific information to names based on website
        self.loginpage       = paths[0]
        self.addtocrtbtn     = paths[1]
        self.addtocrtbtn2    = paths[2]
        self.crt             = paths[3]
        self.qtyxp           = paths[4]
        self.qtyval          = paths[5]
        self.checkoutxpath  = paths[6]
        self.checkoutxpath2  = paths[7]
        self.emailid         = paths[8]
        self.continueid      = paths[9]
        self.passwid         = paths[10]
        self.passwid2        = paths[11]
        self.loginid         = paths[12]
        self.purcont         = paths[13]
        self.sndto           = paths[14]
        self.cvvinput        = paths[15]
        self.cpchid          = paths[16]
        self.cardinp         = paths[17]
        self.expinp          = paths[18]
        self.zipinf          = paths[19]
        self.revorder        = paths[20]
        self.purchacebtn     = paths[21]


# Create functions ----------------------------------------------------------------------1.3

# Function that opens new tabs and goes to the domain for each object
def openlogin(num,wind,tim):#-------------------------------------------- 1.3.1
    timeout = tim # how long to look for elements

    # For each object
    for n in range(num):
        driver.get(wind[n].dom) # Load the website
        
        # Check if this website has already been logged into by seeing
        # If it is the same website as the previous tab. 
        if wind[n].url != wind[n-1].url: # If it is new...
            try:
                # Look for an email input
                WebDriverWait(driver, timeout).until(
                    EC.element_to_be_clickable((By.ID, wind[n].emailid))
                ).send_keys(info.email(wind[n].url))
                time.sleep(1)
                
                # Look for password input. Some websites change their
                # format occasionally though, so this checks for that.
                try:
                    pssi = WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((By.ID, wind[n].passwid))
                    ).send_keys(info.password(wind[n].url))
                except:
                    pssi = WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((By.ID, wind[n].passwid2))
                    ).send_keys(info.password(wind[n].url))
            except:
                # If it can't find, then there might be a 
                # captcha, so just let user handle it
                print('captcha found, you handle it boss') 
            input("press enter when logged in")
        
        # Store the tab identifier
        wind[n].tab = driver.current_window_handle
        time.sleep(1)
        driver.execute_script("window.open('');") # Open new tab
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[n+1]) # Switch to new tab
        time.sleep(1)


# function that tries to find the add to cart button
def checka2c(num,wind,tim): #-------------------------------------------- 1.3.2
    timeout = tim

    #based on the website, use a different method to find the button.
    if wind[num].url == 'www.amazon.com':
        buybutton = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
        )

    elif wind[num].url == 'www.bestbuy.com':
        buybutton = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )

    else:
        buybutton = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, wind[num].addtocrtbtn))
        )
    print("found it")


# Code to check for captchas and how to respond to them
def capcheck(num,wind): #------------------------------------------------ 1.3.3
    # last is for finding the newest tab
    #last = len(wind)-1
    loopnum = num
    
    # Find the captcha element.  if it doesn't exist, an error will raise and continue the main program.
    driver.find_element_by_id('g-recaptcha-response')
    
    # if it does exist, open a new window and load a new instance of that website
    driver.execute_script("window.open('');")
    driver.close()
    time.sleep(1)
    driver.switch_to_window(driver.window_handles[-1]) #-1 goes to the last opened tab
    time.sleep(2)
    driver.get(wind[loopnum].dom)
    wind[loopnum].tab = driver.current_window_handle


# Code to change the quantity of items purchased
def qty_select(wind,tim):#----------------------------------------------- 1.3.4
    timeout = tim
    # start a loop to look for the quantity button. the while loop will allow for a captcha to be taken care of first
    while True:
        try:
            qty = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, wind[loopnum].qtyxp))
            )
            break #break out of the loop if the button is found
        except:
            # once the captcha or other screen is taken care of
            input('press enter when ready')

    # if the quantity is set to be more than one, then change it.  otherwise do nothing
    if wind[loopnum].qtyval != '1':
        
        # if the quantity indicator is a dropdown menu, select it and go to 2.  
        try:
            Select(qty)
            # update the quantity
            qty.select_by_value(wind[loopnum].qtyval)
        
        except: #otherwise if it is a + button, press it.
            qty.click()


# function to find and press the checkout button
def chkt_btn(wind): #---------------------------------------------------- 1.3.5
    contt = True
    while contt: #keeps going back and forth to find which checkout button is correct
        
        # some websites have their checkout buttons change places occasionally.  this checks both places it can be
        try:
            checkoutBtn = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, wind[loopnum].checkoutxpath))
            )
            contt = False


        except:
            try:
                checkoutBtn = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, wind[loopnum].checkoutxpath2))
                )
                contt = False
            except:
                continue
    #now click the checkout button
    checkoutBtn.click() 

# Antonline functions uniquely, so we need to have a section that runs specifically for it.
def antonline(wind): #--------------------------------------------------- 1.3.6
    input("press enter when captcha is done")
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, cardinp))
    ).send_keys(cardinf('card'))
    driver.find_element_by_xpath(wind[loopnum].expinp).send_keys(info.cardinf('date'))
    driver.find_element_by_xpath(wind[loopnum].cvvinput).send_keys(cardinf('cvv'))
    driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[3]/div/form/div[3]/div[1]/div[2]/input').send_keys('Ian Orr')
    driver.find_element_by_id(wind[loopnum].emailid).send_keys(info.email(urll))
    driver.find_element_by_id('bphone1').send_keys('9197401290')
    driver.find_element_by_id(wind[loopnum].zipinf).send_keys('27609')
    driver.find_element_by_id('baddr1').send_keys(info.cardinf('add1'))
    driver.find_element_by_id('baddr2').send_keys(info.cardinf('add2'))
    driver.find_element_by_id('bcity').send_keys(info.cardinf('city'))
    #/html/body/div[3]/div[5]/div[3]/div/form/div[3]/div[1]/div[18]/select
    Select(driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[3]/div/form/div[3]/div[1]/div[18]/select')).select_by_value('34')
    input('press enter when ready')
# Get initial information -------------------------------------------------------------- 1.4

#if testing, set to true
testing = input("are you testing?")
if testing == 'n':
    testing = False
else:
    testing = True

reloads = int(input("how long to check on each page?"))
# domain,urlll = info.urlz(testing)
# urlsz = len(urlll)

#open up chrome and go to the chosen website
driver = webdriver.Chrome()
#driver.get(loginpage)
# p1 = driver.current_window_handle

wind = [] # Initialize the Window class as a list of objects

# Import all the websites to use into a list, then determine the number of websites in that list
urlll = info.urlz(testing)
urlsz = len(urlll)

# Initialize each object in the list
for n in range(urlsz):
    wind.append(Tabi(urlll[n]))
    # wind[n].impt(urlll[n])

timeout = 15 # determine the time the program will take to look for login inputs

# Start the program--------------------------------------------------------------------- 2.0 -

# Logging in --------------------------------------------------------------------------- 2.1

openlogin(urlsz,wind,timeout)
#line above runs the function that opens each website in the object list to log in
# (tab the line if it needs the if statement)

# Checking For availability------------------------------------------------------------- 2.2

timeout = reloads # Uses the user input from the beginning to determine how long program will wait for each tab to load
search = True # search determines the loop continuing to run
loopnum = 0 # using loopnum to turn the while loop into a for loop. 

# This loop will continuously run until something is found.
while search:
    try:
        # Runs the fuction to check if the ADD TO CART button is functional yet
        checka2c(loopnum,wind,timeout)
    except:
        # If above check fails...
        try:
            # See if the function failed because of a capcha.  If so, try to fix the issue.
            capcheck(loopnum,wind)
        except:
            pass
        # Since button wasn't found, reload the page and move to the next tab.
        driver.refresh()
        print("not found yet")

        loopnum += 1 # loop number determines which tab to go to next
        # if the loop number goes past the total number of tabs, go back to the first one.
        if loopnum == urlsz:
            loopnum = 0
        # Go to the next tab
        driver.switch_to.window(wind[loopnum].tab)  
        continue

    # Check if there is another button that needs to be pressed before adding to cart
    try:
        buybutton = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, wind[loopnum].addtocrtbtn2))
        )
    except :
        pass

    # opens a tab of a youtube video to alert me there is a hit.
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('https://www.youtube.com/watch?v=Tf1DEI2lEe0&ab_channel=ValikShevchenko')
    driver.switch_to.window(wind[loopnum].tab)


    # Start the buying process ------------------------------------------------------------- 2.3

    time.sleep(2) #go to cart after adding item to cart
    driver.get(f"https://{wind[loopnum].url}/{wind[loopnum].crt}cart")

    timeout = 15 # timer for how long to wait for the cart page to load
    
    qty_select(wind,timeout) # run function to change quantity
    time.sleep(1)
    chkt_btn(wind) # run function to click checkout button

    print("Successfully added to cart - beginning check out")

    if urll == 'www.antonline.com':
        antonline(wind)
    else:
        try:
            passBtn = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, wind[loopnum].passwid2))
            )
            passBtn.send_keys(info.password(urll))
            
        except:
            print("no password input button found, continuing")
            timeout = 1
        #timeout = 10
        try:
            purcontBtn = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, wind[loopnum].purcont))
            )
            purcontBtn.click()
            timeout = 15
        except:
            print("no purcont button found, continuing")
            timeout = 1

        try:
            sndtobtn = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, wind[loopnum].sndto))
            )
            sndtobtn.click()
            timeout = 15
        except:
            print("no send to button found, continuing")
            timeout = 1

        try:
            cvvinp  = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, wind[loopnum].cvvinput))
            )
            cvvinp.send_keys(info.cardinf('cvv'))
        except:
            print("no cvv input found, continuing")
            timeout = 1

        try:
            revorderbtn  = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, wind[loopnum].revorder))
            )
            revorderbtn.click()
            timeout = 15
        except:
            print("no review order button found, continuing")
            timeout = 1

    if testing == False:
        buythatbich  = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, wind[loopnum].purchacebtn))
        )
        buythatbich.click()

    #seach = False
    driver.get(wind[loopnum].dom)
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    time.sleep(2)
    driver.switch_to.window(wind[loopnum].tab)

    #break