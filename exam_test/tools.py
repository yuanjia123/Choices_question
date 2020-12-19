import xlrd
import os
import random
#系统模块
#8
#打印绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def data():
    '''
    读取excel里面的值
    :return:
    '''
    users = []

    # 显示pythonbase.xlsx这个文件的路径 、这个路径要和当前的django项目路径保持一致
    ti = os.path.join(BASE_DIR, 'exam_test\pythonbase.xlsx')
    # print("ti---------",ti)
    book = xlrd.open_workbook(ti)

    #获取teacher  sheet的数据
    sheet = book.sheet_by_name('SheetJS')

    # sheet.nrows获取该sheet当中的有效行数
    for i in range(1, sheet.nrows):
        users.append({"topic": sheet.row_values(i)[0],
                      "a": str(sheet.row_values(i)[2]),
                      "b": str(sheet.row_values(i)[3]),
                      "c": str(sheet.row_values(i)[4]),
                      "d": str(sheet.row_values(i)[5]),
                      "answer": str(sheet.row_values(i)[6]),
                      "think": str(sheet.row_values(i)[7]),
                      })

    # users = random.choices(users, k=50)
    # print("----------",len(users))
    return users

if __name__ == '__main__':
    print(data())
    print(len(data()))