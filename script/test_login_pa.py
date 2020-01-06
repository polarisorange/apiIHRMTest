import unittest
from api.login_api import LoginApi
import logging
from utils import assert_common, read_login_data
from parameterized import parameterized


class TestIHRMLogin(unittest.TestCase):
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

    @parameterized.expand(read_login_data)
    def test01_login_success(self, mobile, password, http_code, success, code, message):
        response = self.login_api.login(mobile, password)
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据，日志输出只能用{}占位符
        logging.info("登录接口返回的数据为：{}".format(jsonData))

        assert_common(self, response, http_code, success, code, message)


if __name__ == '__main__':
    unittest.main()
