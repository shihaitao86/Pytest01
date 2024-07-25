import time
import pytest

class TestWeb3:
    @pytest.mark.run(order=2)
    def test_03_interface_1(self):
        time.sleep(3)
        print('第一个接口')
    @pytest.mark.run(order=1)
    def test_03_interface_3(self):
        time.sleep(3)
        print('第三个接口')
    @pytest.mark.run(order=3)
    def test_03_interface_2(self):
        time.sleep(3)
        print('第二个接口')
