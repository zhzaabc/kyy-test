import pytest,allure,ddt
from selenium import webdriver
from utils.excel_read import ParseExcel

excelPath = ''
sheetName = ''
excel = ParseExcel(excelPath,sheetName)

@ddt.ddt
class test_login():

    @ddt.data(*excel.getDataFromSheet())
    def test_login(self,data):
        self.driver.find_elements_by_id('').sendkeys('data')
