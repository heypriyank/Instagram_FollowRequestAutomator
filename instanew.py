from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def instanew(userid,key):
    new = webdriver.Firefox()
    new.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(3)
    username = new.find_element_by_name('username')
    password = new.find_element_by_name('password')
    username.clear()
    password.clear()
    username.send_keys(userid)
    password.send_keys(key)
    password.send_keys(Keys.RETURN)
    time.sleep(4)
    turn_off = new.find_element_by_css_selector('button.aOOlW:nth-child(2)')
    turn_off.click()
    time.sleep(3)
    
    # /html/body/span/section/nav/div[2]/div/div/div[3]/div/div[2]/a/span

    dil_icon = new.find_element_by_css_selector('._0ZPOP > span:nth-child(1)')
    dil_icon.click()
    time.sleep(4)
    follow_requests = new.find_element_by_class_name('BcJ68')
    follow_requests.click()


instanew('YOUR INSTAGRAM ID HERE','YOUR PASSWORD HERE')
