import time,pytest,allure,requests
from selenium import webdriver
from utils.excel_read import ParseExcel

excel_path = './../data/login_excel.xlsx'
sheetName = 'user'
excel_login = ParseExcel(excel_path, sheetName)
test_url = "https://www.kuaixuezaixian.com/"
headers = {'content-type': "application/json", 'charset': "UTF-8"}
@allure.feature('测试登录用例')
class Test_login(object):

    @allure.story('打开首页地址')
    @allure.severity('blocker')
    @pytest.mark.parametrize('user_name,user_pwd',[(excel_login.getDataFromSheet()[0][0],excel_login.getDataFromSheet()[0][1])])
    def test_openUrl(self,user_name,user_pwd):
        # self.driver = webdriver.Chrome()
        # self.driver.get(test_url)
        # self.driver.maximize_window()
        # time.sleep(10)
        # self.driver.find_element_by_class_name("login").click()
        # self.driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/ul/li[2]/span").click()
        # self.driver.find_elements_by_tag_name("input")[0].clear()
        # self.driver.find_elements_by_tag_name("input")[0].send_keys(user_name)
        # self.driver.find_elements_by_tag_name("input")[1].clear()
        # self.driver.find_elements_by_tag_name("input")[1].send_keys(user_pwd)
        # time.sleep(5)
        # self.driver.find_element_by_class_name("login-submit-btn").click()
        #####登录请求接口
        requests_login = requests.post(test_url+'api/v1/login/password',json={'username':str(user_name),"password":str(user_pwd)},headers=headers )
        # assert requests_login.status_code == 200
        pytest.main(['-s', '-v', '--alluredir', './../report/html/allure-results'])

# if __name__ == '__main__':
#     pytest.main(['-s','-v','--alluredir','./../report/html/allure-results'])
    # def test_assert(self,status_code):
    #     if status_code == 200:
    #         assert

