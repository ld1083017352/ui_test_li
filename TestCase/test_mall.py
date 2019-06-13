


from  Common.Baseui import baseUI
import pytest

import  time






class Test_mall():
    @pytest.mark.fahuo
    def test_fahuo(self, base):
     base.driver.get("http://192.168.60.132/#/oms/order")
        # 点击订单状态

     base.click("点击订单状态", '''//label[contains(text(),'订单状态：')]/following-sibling::div//input''')
    # 选择待发货
     base.click("选择待发货", '''//span[contains(text(),'待发货')]''')
    # 点击查询搜索
     base.click("点击查询搜索", '''//span[contains(text(),'查询搜索')]''')
    # 点击订单的第一笔订单
     base.click("点击订单的第一笔订单", '''//tbody/tr[1]/td[10]//span[contains(text(),'订单发货')]''')
    # 点击物流公司
     base.click("点击物流公司", '//input[@placeholder="请选择物流公司"]')
    # 选择圆通快递
     base.click("选择圆通快递", '''//span[contains(text(),'圆通快递')]''')
    # 输入物流单号
     base.send_keys("输订单号", '''(//input[@type="text"])[2]''', '153145465')
    # 点击确定
     base.click("点击确认", '''(//span[contains(text(),'确定')])[1]''')
    # 点击确定
     base.click("点击确认", '''(//span[contains(text(),'确定')])[2]''')
    # 获取提示文本
     base.get_text("获取提示文本", '''//div[@aria-label="提示"]''')
    # # 断言



    @pytest.mark.tuihuo
    def test_tuihuo(self, base):
        base.driver.get("http://192.168.60.132/#/oms/returnApply")
        # 点击处理状态//label[contains(text(),'处理状态')]
        base.click("点击处理状态",'''//label[contains(text(),"处理状态：")]/following-sibling::div/div/div/input''')
        # 选择为待处理//span[contains(text(),'待处理')]
        base.click("选择为待处理",'''//span[contains(text(),'待处理')]''')
        # 点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索", '''//span[contains(text(),"查询搜索")]''')
        # 点击第一个订单查看详情(//span[contains(text(),'查看详情')])[1]
        base.click("点击第一个订单查看详情",'''(//span[contains(text(),'查看详情')])[1]''')
        # 获取订单金额
        money = base.get_text("获取订单金额", '''//div[contains(text(),'订单金额')]/following-sibling::div''')
        money=money[1:]
        # 输入退款金额//div[contains(text(),'确认退款金额')]/following-sibling::div/div/input

        base.send_keys("输入退款金额", '''//div[contains(text(),'确认退款金额')]/following-sibling::div//input''', str(money))
        # 点击确认退货//span[contains(text(),'确认退货')]
        base.click("点击确认退货",'''//span[contains(text(),'确认退货')]''')
        # 点击确认//span[contains(text(),'确定')]
        base.click("点击确认",'''//span[contains(text(),'确定')]''')
        # 获取提示文本
        base.get_text("获取提示文本", '''//div[@aria-label="提示"]''')
        # 断言








