from selenium import webdriver
from selenium.webdriver.support.select import Select
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
driver.get("http://192.168.60.146:8080/demo1.html")
import time
if __name__ == '__main__':
    action_chains=ActionChains(driver)
    a=driver.find_element_by_link_text('当当')
    b=driver.find_element_by_partial_link_text('度娘')
    c=driver.find_element_by_link_text('京东')
    action_chains.key_down(Keys.CONTROL).click(a).key_up(b).perform()
    time.sleep(3)
    d=driver.window_handles
    for i in d:
        driver.switch_to.window(i)
        if driver.title.__contains__('当当'):
            break
    time.sleep(5)
    driver.quit()

