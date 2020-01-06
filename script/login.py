import unittest

import app
from api.login_api import LoginApi
import logging
from utils import assert_common, read_login_data


class Login(unittest.TestCase):
    """登录测试类"""

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClassPa(cls) -> None:
        pass

    def test_login(self):
        response = self.login_api.login("13800000002", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据，日志输出只能用{}占位符
        logging.info("登录成功接口返回数据为：{}".format(jsonData))

        assert_common(self, response, 200, True, 10000, '操作成功')
        # 获取令牌，并拼接成以Bearer 开头的令牌字符
        token = jsonData.get("data")
        # 保存令牌到全局变量
        app.Headers['Authorization'] = "Bearer " + token
        logging.info("保存的令牌是：{}".format(app.Headers))


if __name__ == '__main__':
    unittest.main()
