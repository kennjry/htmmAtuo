from base.base import Base
import page
from time import sleep

from base.web_base import WebBase
from tools.get_log import GetLog

log=GetLog.get_logger()

class PageMpLogin(WebBase):
    #输入用户名
    def page_input_username(self,username):
        #调用父类中输入方法,page中的数据在__init__.py文件中
        self.base_input(page.mp_username,username)

    #输入验证码
    def page_input_code(self,code):
        self.base_input(page.mp_code,code)

    #点击登录按钮
    def page_click_login_btn(self):
        sleep(1)
        self.base_click(page.mp_login_btn)

    #获取昵称封装---》在测试脚本中断言使用
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    #组合业务方法-->在测试脚本层使用
    def page_mp_login(self,username,code):
        log.info("正在调用自媒体用户名的密码")
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

#组合业务方法-->发布文章依赖使用
    def page_mp_login_success(self,username="13812345678",code="246810"):
        log.info("正在调用自媒体用户名的密码")
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()