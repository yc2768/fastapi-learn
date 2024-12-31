import pytest
import requests
import allure

BASE_URL="http://127.0.0.1:8000/user"

@allure.feature("用户CRUD测试")
class TestUserCRUD:

    # @allure.story("创建用户")
    # def test_create_user(self):
    #     user_data={"username":"testUser1","email":"testUser1@qq.com"}
    #     response=requests.post(BASE_URL,json=user_data)
    #     assert response.status_code==200

    # @allure.story("获取所有用户")
    # def test_get_users(self):
    #     response = requests.get(BASE_URL)
    #     assert response.status_code == 200
    #     assert len(response.json()) > 0

    # @allure.story("根据id获取用户信息")
    # def test_get_user(self):
    #     response = requests.get(BASE_URL + "/5")
    #     assert response.status_code == 200

    # @allure.story("更新用户")
    # def test_update_user(self):
    #     updated_data = {"username": "testUpdateUser", "email": "testUpdateUser@qq.com"}
    #     response = requests.put(BASE_URL + "/5", json=updated_data)
    #     assert response.status_code == 200

    @allure.story("删除指定用户")
    def test_delete_user(self):
        response = requests.delete(BASE_URL + "/5")
        assert response.status_code == 200
