# encoding=utf-8
import xlrd
class ExcelUtil():
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)# 获取第一行作为key值，返回列表例如:["序号","搜索词","期望结果","测试时间","测试结果"]
        self.rowNum = self.table.nrows # 获取总行数
        self.colNum = self.table.ncols  # 获取总列数

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):#遍历所有行
                s = {}
                s['rowNum'] = i+2#从第二行取对应values值
                values = self.table.row_values(j)#获取第j行的数据，返回列表
                #print(values)
                for x in list(range(self.colNum)):#遍历所有列
                    if isinstance(values[x],float):
                      s[self.keys[x]]=str(int(values[x]))
                    else:
                      s[self.keys[x]] = values[x]#存储到字典里
                r.append(s)#每行对应的每列数据存储到列表里
                j += 1
            return r
if __name__ == "__main__":
    filepath = "test_data.xlsx"
    sheetName = "login"
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())