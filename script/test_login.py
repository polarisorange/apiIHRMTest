import unittest
from api.login_api import LoginApi
import logging
from utils import assert_common


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
    def tearDownClass(cls) -> None:
        pass

    def test01_login_success(self):
        response = self.login_api.login("13800000002", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据，日志输出只能用{}占位符
        logging.info("登录成功接口返回数据为：{}".format(jsonData))

        # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, jsonData.get('success'))  # 断言success的值
        # self.assertEqual(10000, jsonData.get('code'))  # 断言code的值
        # self.assertIn('操作成功', jsonData.get('message'))  # 断言meg的值

        assert_common(self, response, 200, True, 10000, '操作成功')

    def test02_username_is_not_exist(self):
        response = self.login_api.login("13900000002", "123456")

        jsonData = response.json()

        logging.info("账号不存在是输入的数据为：{}".format(jsonData))

        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test03_password_is_error(self):
        response = self.login_api.login("13800000002", "111111")

        jsonData = response.json()

        logging.info("密码错误时输入的数据为：{}".format(jsonData))

        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test04_username_have_special_char(self):
        response = self.login_api.login("@#$%^&*!@#$", "111111")

        jsonData = response.json()

        logging.info("账号输入特殊字符输出的数据为：{}".format(jsonData))

        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test05_username_is_empty(self):
        response = self.login_api.login("", "111111")

        jsonData = response.json()

        logging.info("账号为空输出的数据为：{}".format(jsonData))

        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test06_password_is_empty(self):
        response = self.login_api.login("13800000002", "")

        jsonData = response.json()

        logging.info("密码为空输出的数据为：{}".format(jsonData))

        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test07_username_have_chinese(self):
        response = self.login_api.login("138000000三毛", "123456")

        jsonData = response.json()

        logging.info("账号有中文输出的数据为：{}".format(jsonData))

        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test08_username_have_space(self):
        response = self.login_api.login("138000000 2", "123456")

        jsonData = response.json()

        logging.info("账号有空格输出的数据为：{}".format(jsonData))

        assert_common(self, response, 200, False, 20001, '用户名或密码错误')


if __name__ == '__main__':
    unittest.main()
