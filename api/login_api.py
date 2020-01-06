import requests
import app


class LoginApi(object):
    """登录类"""

    def __init__(self):
        self.login_url = app.Host + "/api/sys/login"
        self.headers = app.Headers

    def login(self, mobile, password):
        # 要发送的数据
        data = {"mobile": mobile, "password": password}
        # 发送登录请求
        response = requests.post(self.login_url, json=data, headers=self.headers)
        # 返回响应数据
        return response
