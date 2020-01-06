import requests

import app


class EmployeeApi(object):

    def __init__(self):
        self.emp_url = app.Host + "/api/sys/user"
        # 如果调用员工管理模块相关接口时，先调用login.py接口
        # 获取的app.Headers是{"Content-type":"application/json","Authorization":"Bearer xxxxx-xxx-xxxxx"}
        self.headers = app.Headers

    def add_emp(self, username, mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-01-04",
            "formOfEmployment": 1,
            "workNumber": "0005",
            "departmentName": "测试",
            "departmentId": "1210411411066695680"
        }
        # 发送添加员工接口请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        # 返回添加员工接口的响应数据
        return response

    def query_emp(self):
        url = self.emp_url + "/" + app.EMP_ID
        return requests.get(url, headers=self.headers)

    def modify_emp(self, username):
        url = self.emp_url + "/" + app.EMP_ID
        data = {"username": username}
        return requests.put(url, json=data, headers=self.headers)

    def delete_emp(self):
        url = self.emp_url + "/" + app.EMP_ID
        return requests.delete(url, headers=self.headers)
