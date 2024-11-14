
from pytest_demo.common.loga import logger
import pytest
from pytest_demo.common.parseData import base_data
test_data = base_data.get_yaml_data()


#testcases文件夹下下面的每一个
@pytest.fixture(scope="function", autouse=True)#用例执行前的一些操作
def run_case_mark():
    """
    执行用例开始前和结束后打印log信息
    :return:
    """
    logger.info("开始执行用例")
    yield#会在这个语句之前执行setup动作，语句之后执行teardown动作
    logger.info("用例执行结束")

def get_base_data():
    """
    获取测试数据
    :return:
    """
    res = base_data.get_yaml_data()
    return res


