from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):
    base_url = 'http://localhost:8000'

    def test_index_post(self):
        url = self.base_url + '/'
        # 发起post请求，表单参数使用data来指定
        resp = requests.post(url, data={
            'name': 'disen',
            'city': '西安'
        })
        print(resp.text)

    def test_index_get(self):
        url = self.base_url + '/'
        # 发起get请求，查询参数使用params来指定
        resp = requests.get(url, params={
            'wd': 'disen',
            'title': '20'
        })
        print(resp.text)


class TestCookieRequest(TestCase):
    url = 'http://localhost:8000/cookie'

    def test_search(self):
        resp = requests.get('http://localhost:8000/search', params={
            'wd': 'python'
        })
        print(resp.text)
        print(resp.cookies)
        for key, cookie in resp.cookies.itme():
            print(key, resp.cookies.get(key))

    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_delete(self):
        resp = requests.delete(self.url, params={
            'name': 'token'
        })
        print(resp.text)


class TestOrderRequest(TestCase):
    url = 'http://localhost:8000/order/3/2'

    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_post(self):
        resp = requests.post(self.url)
        print(resp.text)


class TestUserLoginRequest(TestCase):
    url = 'http://192.168.124.11:8000/user'

    # 上传json数据
    def test_login(self):
        resp = requests.get(self.url,
                            json={
                                'name': 'disen',
                                'pwd': '1234'
                            })

        # 响应json数据
        print(resp.json())