#用来取ini和yaml文件的内容
import os
import configparser
import yaml
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_path, "data", "data.yaml")# 项目数据文件的路径
ini_path = os.path.join(project_path, "config", "setting.ini")



class ParseData:
    def __init__(self):#初始化路径,每次都会先获取文件路径
        self.data_path = data_path
        self.ini_path = ini_path

    def get_yaml_data(self):
        """
        读取yaml文件内容
        :return: 返回yaml读取的数据
        """
        with open(self.data_path,mode='r',encoding='utf-8')as file: #打开yaml文件
            data = yaml.safe_load(file)#解析yaml文件里面的内容
            return data

    def get_ini_data(self):
            """
            获取数据文件的内容
            :return:
            """
            config = configparser.ConfigParser()
            config.read(self.ini_path, encoding="utf8")
            return config

base_data = ParseData()

