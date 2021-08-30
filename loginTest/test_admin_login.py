from selenium.webdriver import *
import pytest
import allure,datetime
from time import *
import os


class Test_admin_login(object):

    @pytest.mark.run(order=1)
    @allure.step(title=u'打开浏览器')
    def test_browser_open(self):
        global driver
        driver = Chrome()

    @pytest.mark.parametrize('url, input_box_id, search_btn_id, keyword, expected',
                             [('https://cn.bing.com', 'sb_form_q', 'sb_form_go', u'赵丽颖', u'冯绍峰'),
                              ('https://www.sogou.com/', 'query', 'stb', u'冯绍峰', u'赵丽颖'),
                              ])
    @pytest.mark.run(order=2)
    @allure.step(title=u'搜索')
    def test_search(self, url, input_box_id, search_btn_id, keyword, expected):
        global driver
        # 最大化窗口
        driver.maximize_window()
        # 设置默认的等待时长
        driver.implicitly_wait(15)
        # 打开网页
        driver.get(url)
        # 点击搜索框
        driver.find_element_by_id(input_box_id).click()
        # 输入关键字
        driver.find_element_by_id(input_box_id).send_keys(keyword)
        sleep(3)
        # 点击搜索按钮
        driver.find_element_by_id(search_btn_id).click()
        sleep(5)
        assert expected in driver.page_source

    @pytest.mark.run(order=3)
    @allure.step(title=u'关闭浏览器')
    def test_browser_close(self):
        global driver
        driver.quit()


if __name__ == '__main__':
    # 取当前时间
    now = strftime("%Y%m%d%H%M%S", localtime(time()))
    #pytest.main(['-s', '-q', 'test_admin_login.py', '--alluredir', 'report{0}'.format(now)])
    pytest.main(['-s', '-q', 'test_admin_login.py', '--alluredir=report/report_data'])
    # pytest.main(['-s', '-q', 'query.py', '--alluredir', 'Reports'])
    #os.system('allure generate report{0}/ -o report{0}/html'.format(now))
    # os.system('allure generate report/report_data -o report/html --clean')
    os.system('allure serve report/report_data')


    # os.system(u'allure generate Reports -o Reports/html --clean')

