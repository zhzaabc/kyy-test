import pytest,allure,os,time,datetime,json
from playwright.sync_api import Page
from selenium import webdriver
from utils.excel_read import ParseExcel


excel_path = './../data/login_excel.xlsx'
sheetName = 'user'
excel_login = ParseExcel(excel_path,sheetName)
test_url = "https://www.kuaixuezaixian.com/"
@allure.feature('测试登录用例')
class Test_login(object):

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=1)
    @allure.step(title=u'打开浏览器')
    def test_browser_open(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
#
    @pytest.mark.parametrize('user_name,user_pwd',
                             [(excel_login.getDataFromSheet()[0][0], excel_login.getDataFromSheet()[0][1])])
    @allure.step(title=u'进入登录页面登录')
    @pytest.mark.run(order=2)
    def test_login_user(self,user_name,user_pwd):
        global driver
        driver.get(test_url)
        time.sleep(5)
        driver.find_element_by_class_name("login").click()
        driver.find_element_by_xpath(
            "//*[@id='__layout']/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/ul/li[2]/span").click()
        driver.find_elements_by_tag_name("input")[0].clear()
        driver.find_elements_by_tag_name("input")[0].send_keys(user_name)
        driver.find_elements_by_tag_name("input")[1].clear()
        driver.find_elements_by_tag_name("input")[1].send_keys(user_pwd)
        time.sleep(5)
        driver.find_element_by_class_name("login-submit-btn").click()
        ##登录断言
        time.sleep(0.5)
#
    @pytest.mark.run(order=3)
    @allure.step(title=u'关闭浏览器')
    def test_browser_close(self):
        global driver
        driver.quit()

# if __name__ == '__main__':
#     # 取当前时间
#     now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#     pytest.main(['-s', '-q', 'test_login.py', '--alluredir=report/report_data'])
#     os.system('allure generate report/report_data -o report/html --clean')
#     os.system('allure serve report/report_data')
if __name__ == '__main__':
    # 取当前时间
    #now = strftime("%Y%m%d%H%M%S", localtime(time()))
    #pytest.main(['-s', '-q', 'test_admin_login.py', '--alluredir', 'report{0}'.format(now)])
    pytest.main(['-s', '-q', 'test_login.py', '--alluredir=report/report_data'])
    # pytest.main(['-s', '-q', 'query.py', '--alluredir', 'Reports'])
    #os.system('allure generate report{0}/ -o report{0}/html'.format(now))
    # os.system('allure generate report/report_data -o report/html --clean')
    storage = Page.context.storage_state()
    os.environ["storage"] = json.dumps(storage)
    os.system('allure serve report/report_data')