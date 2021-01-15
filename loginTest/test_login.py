import time,pytest,allure,ddt
from selenium import webdriver
from utils.excel_read import ParseExcel
from ddt import ddt,data,unpack

excel_path = './../data/login_excel.xlsx'
sheetName = 'user'
excel = ParseExcel(excel_path,sheetName)
@allure.feature('测试登录用例')
@ddt
class Test_login(object):

    @allure.story('打开首页地址')
    @allure.severity('blocker')
    @data(*excel.getDataFromSheet())
    def test_openUrl(self,data):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.kuaixuezaixian.com/")
        self.driver.maximize_window()
        time.sleep(10)
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/ul/li[2]/span").click()
        time.sleep(10)
        print(data)

    # @allure.story('进入登录页面')
    # @allure.severity('blocker')
    # def test_login_page(self):
    #     driver = webdriver.Chrome()
    #     #driver.find_element("class","login").click()

    @pytest.fixture(scope='module')
    def login_t(request1):
        user=request1.param['user']
        pwd = request1.param['password']
        print('\n用户名:%s,密码:%s'%(user,pwd))
        if pwd:
            return True
        else:
            return False


