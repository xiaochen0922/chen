import logging

import requests
import json
from pytest_demo.common import loga
from pytest_demo.common import parseData
# from pytest_demo.common.ResponseUtil import process_response
from pytest_demo.testcase.conftest import *
yaml_data = parseData.base_data.get_yaml_data()
url = yaml_data["host"]["url"]
class  HttpClient:
        def __init__(self):#初始化方法,构造方法,构造函数 作用:当我们创建好一个实例对象之后,会自动调用这个方法
            self.url = url
            self.logger = loga.logger

        def send_request(self, path, method, **kwargs):#总的一个请求传入地址，请求方法和其他参数，先写一些基本请求再写这个
            return self.request(path, method, **kwargs)

        def get(self, path, **kwargs): #path是路径加在url后面，**kwargs包含其他参数
            return self.request(path, 'GET', **kwargs)

        def post(self, path, **kwargs):
            return self.request(path, 'POST', **kwargs)

        def request(self, path, method, **kwargs):#负责发送 HTTP 请求并处理响应,把返回信息写入日志文件
            response = requests.request(method, self.url + path, **kwargs)
            self.request_log(path, method, response, **kwargs)
            return response

        def request_log(self, path, method, response, **kwargs):
            data = kwargs.get("data")
            json_data = kwargs.get("json")
            params = kwargs.get("params")
            headers = kwargs.get("headers")

            self.logger.info("请求地址>>{}".format(self.url + path))
            self.logger.info("请求方法>>{}".format(method))
            try:
                self.logger.info("响应内容>>{}".format(response.json()))
            except (ValueError, json.JSONDecodeError):
                self.logger.info("响应内容无法解析为JSON")

            if data is not None:
                self.logger.info("data参数>>>\n{}".format(json.dumps(data, indent=2)))
            if params is not None:
                self.logger.info("params参数>>>\n{}".format(json.dumps(params, indent=2)))
            if json_data is not None:
                self.logger.info("json_data参数>>>\n{}".format(json.dumps(json_data, indent=2)))
            if headers is not None:
                self.logger.info("headers参数>>>\n{}".format(json.dumps(headers, indent=2)))

# header = {"Content-Type":"application/json;chars"}params={"pdCode":"PDC0555","productSku":300445,"coupon":"true","channel":"APP"},
http_request = HttpClient()
if __name__ == '__main__':
    url_path = '/user/login'
    data = {"account": 18711971689, "password": 123456}
    response = http_request.send_request(url_path,method="POST" ,data=data)
    # url_path2="/product/single/detail?pdCode=PDC0555&productSku=300445&coupon=true&channel=APP"
    # response2 = http_request.send_request(url_path2,method="GET",headers='{"Content-Type": "application/json;chars"}')

    print(response.text)  # 使用response.text打印响应文本


