from  Common.Baseui import baseUI

import  time



class Test_mall():
    def test_login(self,driver):
       #  使用baseUI
       base=baseUI(driver)
       #  打开登录页面
       driver.get("http://192.168.60.132/#/login")
       # 输入用户名
       base.send_keys("输入用户名",'''//input[@name="username"]''',"admin")
       # 输入密码
       base.send_keys("输入密码",'''//input[@name="password"]''',"123456")
       # 点击登录
       base.click("点击登录",'''(//span[contains(text(),'登录')])[1]''')
       assert '首页' in driver.page_source

    def test_fahuo(self,driver):
        base = baseUI(driver)
        # 点击订单
        base.click("点击订单",'''//span[@slot="title" and text()="订单"]''')
        # 点击订单列表
        base.click("点击订单列表",'''//span[ text()="订单列表"]''')
        # 点击订单状态
        base.click("点击订单状态",'''//label[contains(text(),'订单状态：')]/following-sibling::div//input''')
        # 选择待发货
        base.click("选择待发货",'''//span[contains(text(),'待发货')]''')
        # 点击查询搜索
        base.click("点击查询搜索",'''//span[contains(text(),'查询搜索')]''')
        # 点击订单的第一笔订单
        base.click("点击订单的第一笔订单",'''//tbody/tr[1]/td[10]//span[contains(text(),'订单发货')]''')
        assert "发货列表" in driver.page_source
        # 点击物流公司
        base.click("点击物流公司",'//input[@placeholder="请选择物流公司"]')
        # 选择圆通快递
        base.click("选择圆通快递",'''//span[contains(text(),'圆通快递')]''')
        # 输入物流单号
        base.send_keys("输订单号",'''(//input[@type="text"])[2]''','153145465')
        # 点击确定
        base.click("点击确认",'''//span[contains(text(),'确定')][1]''')
        # 点击确定
        base.click("点击确认", '''//span[contains(text(),'确定')][2]''')
        # 获取提示文本
        base.get_text("获取提示文本",'''//div[@aria-label="提示"]''')
        # 断言




