import allure
import pytest
from pytest_demo.common.DB_Uilt import db
from pytest_demo.api.meikefresh_api import *
header = json.loads(get_base_data()["headers"])
from pytest_demo.testcase.conftest import *
test_data = base_data.get_yaml_data()


@pytest.fixture(scope="module", autouse=True)
def userid(self):
    result = login(test_data['user_login']['account'], test_data['user_login']['password'])
    return result["body"]["userId"]
@allure.feature("用户数据")  # 用来给测试报告分组
class TestUser:
    #获取用户id，每个类里面执行一次

    # 参数化实现登录
    @allure.title("用户登录测试")
    @allure.description("测试用户登录功能是否正常")
    # @pytest.mark.parametrize("account,password",get_base_data()["user_login_new"])#用于为测试函数提供多组参数和对应的预期结果
    def test_user_login(self):
        with allure.step("执行登录操作"):
            result = login(test_data['user_login']['account'], test_data['user_login']['password'])
        with allure.step("验证登录结果"):
            # 假设userId是登录成功的标志
            assert "userId" in result["body"], "登录失败，未找到userId"


            # @pytest.mark.skipif(True)#为true的时候跳过该用例
    # @pytest.mark.parametrize("data", get_base_data()["shopping_cart"])
    #加入购物车，需要用到userid
    @allure.title("加入购物车")
    @allure.description("测试")
    def test_shopping_cart(self,userid):
        result = add_shopping_cart(userid)
        with allure.step("判断是否加入购物车成功"):
            assert "code" in result

    # # @pytest.mark.skipif(True)#为true的时候跳过该用例
    # def test_order_submit(self，userid):
    #     result = order_submit(userid)
    #     orderid = result["body"]["orderId"]
    #     db(orderid)
    #     logger.info(f"执行完删除订单，订单单号为: {orderid}")
    #
    #     assert "code" in result




