import logging
import os
import time


project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#项目根目录
log_path = os.path.join(project_path,"logs") #日志存放路径
if not os.path.exists(log_path):os.mkdir(log_path)# 不存在log文件夹，则自动创建

class Logger(object):
    default_formats = {# 终端输出格式
        'console_fmt': '%(log_color)s%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-[日志信息]: %(message)s',
        # 日志输出格式
        'file_fmt': '%(asctime)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-[日志信息]: %(message)s'}

    def __init__(self,name=None,log_level=logging.DEBUG):
        self.name = name
        # ①创建一个记录器
        self.logger = logging.getLogger((self.name))
        self.logger.setLevel("INFO")# 设置日志级别为 'level'，即只有日志级别大于等于'level'的日志才会输出
        self.log_formatter = logging.Formatter(self.default_formats["file_fmt"])  # 创建formatter
        self.console_formatter = logging.Formatter(self.default_formats["file_fmt"])  # 创建formatter
        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setLevel("DEBUG")     # ③创建log文件，设置输出等级
        time_now = time.strftime('%Y_%m%d_%H', time.localtime()) + '.log'  # log文件命名：2024_0402_21.log
        self.fileHandler = logging.FileHandler(os.path.join(log_path, time_now), 'a', encoding='utf-8')
        self.fileHandler.setLevel("DEBUG") # ④用formatter渲染这两个Handler
        self.streamHandler.setFormatter(self.console_formatter)
        self.fileHandler.setFormatter(self.log_formatter)# ⑤将这两个Handler加入logger内
        if not self.logger.handlers:  # 在新增handler时判断是否为空,解决log重复打印的问题
            self.logger.addHandler(self.streamHandler)
            self.logger.addHandler(self.fileHandler)


logger = Logger().logger

if __name__ == '__main__':
    logger.warning("warning")
    logger.error("error")
    logger.info("info")
    logger.debug("debug")
    logger.critical("critical")
