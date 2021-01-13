from openpyxl import load_workbook

class ParseExcel():
    def __init__(self,excel_path):
        self.wb = load_workbook(excel_path)
        self.sheet = self.wb.active


    def getDataFromSheet(self):
        datalist = []
        for line in self.sheet:
            datalist.append(line)
        return datalist

if  __name__ == '__main__':
    excel_path = './../data/login_excel.xls'
    sheetName = 'user'
    parse = ParseExcel(excel_path)
    print(parse.getDataFromSheet())