import time,pytest,allure,ddt
from selenium import webdriver
from utils.excel_read import ParseExcel

excel_path = './data/login_excel.xls'
sheetName = 'user'
excel = ParseExcel(excel_path,sheetName)
@allure.feature('测试登录用例')
@ddt.ddt
class Test_login(object):
    test_user_data = [
        {'user': '13177831912', 'password': '123456'},
        {'user': '13100001011', 'password': '123456'}
    ]
    #@pytest.mark.usefixtures("open_url('https://www.kuaixuezaixian.com/login?returnurl=%2F')")
    #@pytest.mark.parametrize(test_user_data)


    @allure.story('打开首页地址')
    @allure.severity('blocker')
    @ddt.data(*excel.getDataFromSheet())
    def test_openUrl(self,data):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.kuaixuezaixian.com/")
        self.driver.maximize_window()
        time.sleep(10)
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/ul/li[2]/span").click()
        time.sleep(10)

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


