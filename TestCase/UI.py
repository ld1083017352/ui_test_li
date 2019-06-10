from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    # driver.get 打开一个指定网页
    driver.get("http://192.168.60.146:8080/demo1.html")
    # # 等待几秒
    # time.sleep(5)
    # input_el=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/input")
    # input_el.send_keys("只要你很俩家坡")
    # time.sleep(5)
    # # # clear 清除
    # input_el.clear()
    #
    #
    # time.sleep(5)
    # file_el=driver.find_element_by_id('file1')
    # file_el.send_keys('C:/Users/Administrator/Pictures/DAY1.png')
    #
    #
    #
    # radio_els=driver.find_elements_by_name('radio')
    # print(type(radio_els))
    # radio_els[0].click()
    # time.sleep(1)
    # radio_els[1].click()
    # time.sleep(2)
    #
    #
    # checkbox_els=driver.find_elements_by_class_name('checkbox')
    # print(checkbox_els)
    # checkbox_els[0].click()
    # time.sleep(1)
    # checkbox_els[1].click()
    # time.sleep(1)
    # checkbox_els[2].click()
    # time.sleep(1)

    button_els=driver.find_element_by_xpath('//input[@value="普通按钮"]')
    button_els.click()
    time.sleep(1)
    # 确认弹框
    driver.switch_to.alert.accept()
    time.sleep(2)
    # 取消弹框
    # driver.switch_to.alert.dismiss()






    mima_els=driver.find_element_by_xpath('/html/body/table/tbody/tr[7]/td[2]/input')
    mima_els.send_keys('123456')
    time.sleep(3)

    select_el=driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(12) > td:nth-child(2) > select')
    s=Select(select_el)
    s.select_by_index(1)
    time.sleep(3)
    s.select_by_value('z1')
    time.sleep(3)
    s.select_by_visible_text('周龙3')
    time.sleep(3)



    driver.find_element_by_link_text('当当').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.find_element_by_partial_link_text('度娘').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.refresh()




    # 关闭浏览器quit
    driver.quit()
    # driver.close() 也可以关闭浏览器，但无法关闭进程


