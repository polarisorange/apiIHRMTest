import time
import unittest
import app
from script.login import Login
from script.test_employee import TestIHRMEmp
from tools.HTMLTestRunner import HTMLTestRunner

# 实例化测试套件对象
suite = unittest.TestSuite()

# 将测试用例添加到测试套件
# suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))
# 使用HTMLTestRunner执行测试套件，生成测试报告
# report_path = app.base_dir + "/report/ihrm{}.html".format(time.strftime('%Y%m%d_%H%M%S'))
report_path = app.base_dir + "/report/ihrm.html"
with open(report_path, mode='wb') as f:
    # 实例化HTMLTestrunner
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源接口测试", description="v1.0.0")
    # 使用runner执行测试套件
    runner.run(suite)
