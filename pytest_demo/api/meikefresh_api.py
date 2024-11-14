import json

from pytest_demo.api.api_unit import api_util
from pytest_demo.testcase.conftest import get_base_data
from pytest_demo.common.loga import logger
from pytest_demo.common.httpClient import http_request
from pytest_demo.common.ResponseUtil import process_response
header = json.loads(get_base_data()["headers"])
#用来存放所有的请求，其他地方也可以调用
#登录
def login(account, password ):
    data = {
        'account': account,
        'password': password
    }

    response = api_util.get_login(data=data).json()
    return response

#加入购物车
def add_shopping_cart(userid):
    """
    加入购物车需要先登录
    :param json_data:
    :param token:
    :return:
    """
    # data = {"userId":userid,
    #         "shopCartProducts":[{"quantity":get_base_data()["add_sku"]["quantity"],
    #                              "productSku":get_base_data()["add_sku"]["productSku"]}]}
    # response = api_util.add_shoppig(data=json.dumps(data),headers=header).json()

    data = {"userId": userid,
            "shopCartProducts": [{"quantity": get_base_data()["add_sku"]["quantity"],
                                  "productSku": get_base_data()["add_sku"]["productSku"]}]}
    response = http_request.send_request(path=get_base_data()["add_sku"]["path"], method="post", data=json.dumps(data), headers=header)

    return response.json()
#提交订单
# def order_submit(uesrid):
#     data = {"userId":uesrid,
#             "payType":1,
#             "recName":"臻品口腔门诊部反复复电话号是啥对对对",
#             "recTel":"17877474744",
#             "recAddr":"天津市天津市和平区物业A1楼1",
#             "remark":"",
#             "detailList":[{"productSku":get_base_data()["add_sku"]["productSku"],
#                            "quantity":get_base_data()["add_sku"]["quantity"],"couponId":"null"}],
#             "invoiceId":30901,
#             "invoiceType":"SPECIAL_INVOICE",
#             "channel":"web",
#             "expressFeeFromQuery":"false",
#             "certificateType":"0",
#             "useMaxCoupon":"true",
#             "giftStatus":0,
#             "prmList":[]}
#     response = api_util.send_request(path=get_base_data()["odrder_submit"]["path"],data=json.dumps(data), method="post",headers=header)
#     return response.json()
