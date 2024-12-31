import os

import pytest

# 运行pytest测试框架的主函数
if __name__ == '__main__':
    pytest.main()
    # 调用allure生成报告
    os.system("allure generate ./temps -o ./report --clean")
