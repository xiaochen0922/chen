from pytest_demo.common.httpClient import HttpClient
from pytest_demo.common.parseData import base_data
from pytest_demo.common.loga import logger
yaml_data = base_data.get_yaml_data()
class ApiUtil(HttpClient):
    """
    Api继承HttpClient
    API主要是各个api的调用，主要是添加path和method不用在meikefresh_api里面再去添加
    """
    def __init__(self):
        #super()继承父类的构造方法
        super().__init__()

    def get_login(self,**kwargs):
        #因为继承了HttpClient，所以可以调用HttpClient的post方法
        return self.post("/user/login",**kwargs)

    def add_shoppig(self,**kwargs):#加入购物车
        logger.info("aaaaa{}".format("llllllll"))
        #因为继承了HttpClient，所以可以调用HttpClient的post方法
        return self.post("/shop-cart/add",**kwargs)
    def order_submit(self,**kwargs):#提交订单
        #因为继承了HttpClient，所以可以调用HttpClient的post方法
        return self.post("/order/submit",**kwargs)
api_util = ApiUtil()

