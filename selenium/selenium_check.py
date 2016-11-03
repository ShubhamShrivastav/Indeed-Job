
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

##################

#Set up web driver

##################

def set_up_driver():

    return webdriver.Firefox()

######################

#do cool stuff

######################

def run_selenium():

    driver=set_up_driver()

    #this is where it happens

    driver.get('http:google.com')

    elem=driver.find_element_by_name('q')

    elem.send_keys('python programming')

    elem.send_keys(Keys.ENTER)

#######################

#Clean up the driver

#######################

def tear_down(driver):

    time.sleep(4)

    driver.quit()

################################

#Main

################################

if '__main__'==__name__:

    run_selenium()

