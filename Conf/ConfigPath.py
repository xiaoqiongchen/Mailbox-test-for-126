import os
def dir_path():#获取当前项目路径
    proj_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return proj_dir_path
def test_data_path():#获取测试数据路径
    path=os.path.join(dir_path()+"\\TestData\\test_data.xlsx")
    return path
def ini_path():#获取ini文件路径
    path=os.path.join(dir_path()+"\\Conf\\LocateExpress.ini")
    return path
# print(dir_path())
# print(ini_path())