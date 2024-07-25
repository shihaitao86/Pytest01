def test_04_interface():
    print('函数')
class TestWeb:
    def test_03_interface(self):
        print('测试接口')

    # 前置-用例执行之前
    def setup_method(self):
        print("用例之前执行的代码")

    # 后置-用例执行之后
    def teardown_method(self):
        print("用例之后执行的代码")
