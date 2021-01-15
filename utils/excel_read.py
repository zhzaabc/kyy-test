from openpyxl import load_workbook

class ParseExcel():
    def __init__(self,excel_path,sheetName):
        self.wb = load_workbook(excel_path)
        self.sheet = self.wb[sheetName]


    def getDataFromSheet(self):
        datalist = []
        for line in self.sheet:
            datalist.append(line[0].value)
        datalist.pop(0)
        return datalist

# if  __name__ == '__main__':
#     excel_path = './../data/login_excel.xlsx'
#     sheetName = 'user'
#     parse = ParseExcel(excel_path,sheetName)
#     print(parse.getDataFromSheet())