import requests
import pytest

corpid = "ww21a86872a6b23839"
corpsecret = "FDe_8P8Fg_PtsGIgzcaAkDPX07tW0pOJaXXczodcJtI"


def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    result = requests.get(url).json()
    return result["access_token"]


def test_depart_add():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={get_token()}"
    data = {
        "name": "深圳研发中心",
        "parentid": 1
    }
    print(requests.post(url, json=data).json())


def test_depart_updata():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={get_token()}"
    data = {
        "id": 2,
        "name": "珠海研发中心"
    }
    print(requests.post(url, json=data).json())


def test_depart_delete():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={get_token()}&id=2"
    print(requests.get(url).json())


def test_depart_list():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={get_token()}&id=1"
    print(requests.get(url).json())
