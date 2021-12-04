from selenium import webdriver
"""
browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read Online for Free')
try:
    linkElem.click()
except:
    print('Was not able to find an element with that name.')
"""

"""
browser = webdriver.Chrome()
browser.get('https://login.metafilter.com')
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('ahihiduy')

passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('123')
try:
    passwordElem.submit()
    print("OK")
except:
    print("ERROR")
"""

from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('https://tienganhb1.com/chu-de-thi-noi-tieng-anh-b1')
htmlElem = browser.find_element_by_tag_name("html")
htmlElem.send_keys(Keys.END)
#htmlElem.send_keys(Keys.HOME)
#browser.quit()