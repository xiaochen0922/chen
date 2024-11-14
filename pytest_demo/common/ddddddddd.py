import requests
import json
from pytest_demo.common import loga
from pytest_demo.common import parseData
yaml_data = parseData.base_data.get_yaml_data()
url = yaml_data["host"]["url"]

class HttpClient:
    def __init__(self):
        self.url = url
        self.logger = loga.logger

    def send_request(self, path, method, **kwargs):
        return self.request(path, method, **kwargs)

    def get(self, path, **kwargs):
        return self.request(path, 'GET', **kwargs)

    def post(self, path, **kwargs):
        return self.request(path, 'POST', **kwargs)

    def request(self, path, method, **kwargs):
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


http_request = HttpClient()

if __name__ == '__main__':
    url_path = '/user/login'
    data = {"account": 18711971689, "password": 123456}
    response = http_request.send_request(url_path,method="POST" ,data=data)
    print(response.text)  # 使用response.text打印响应文本
    # 如果响应是JSON格式，并且您想将其解析为Python对象，可以使用：
    # response_json = response.json()
    # print(response_json)