import json
from pytest_demo.common.loga import logger
from pytest_demo.api.ResultBase import ResultResponse
#处理response
def process_response(response):
    if response.status_code == 200:
        # 构造字典{success:True} ResultResponse用来存储response的值
        ResultResponse.success = True
        ResultResponse.body = response.json()
        # logger.info("组装的ResultResponse是",ResultResponse)
    else:
        #用于表示某个操作或请求没有成功完成
        ResultResponse.success = False
        logger.info("接口报错")
    # response.status_code不是200和时候，打印log信息
    logger.info("接口返回内容是>>{}:".format(response.json,ensure_ascii=False,indent=2))
    return ResultResponse
