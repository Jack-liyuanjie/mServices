from tornado.web import RequestHandler, asynchronous
from tornado.httpclient import AsyncHTTPClient, HTTPClient, HTTPResponse, HTTPRequest


# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# 同步请求案例HTTPClient
class DownloadHandler(RequestHandler):
    def get(self):
        # 获取查询参数中的url（下载资源的网址）
        url = self.get_query_argument('url')
        # 参数里面添加filename
        filename = self.get_query_argument('filename', 'index.html')

        # 发起同步请求
        client = HTTPClient()
        # validate_cert 是否验证ssl安全连接的证书
        response: HTTPResponse = client.fetch(url, validate_cert=False)  # validate验证证书为Flase
        # print(response.body)
        # 保存到static/downloads
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)
        self.write('下载成功')


# 异步请求案例AsyncHTTPClient
class AsyncDownloadHandler(RequestHandler):

    def save(self,response: HTTPResponse):
        # print(response.effective_url, '下载成功')
        self.write('<br>下载完成，正在保存')

        # 在回调函数中，可以获取请求的查询参数
        filename = self.get_query_argument('filename', 'index.html')

        # 保存到static/downloads
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)

        self.write('<br>保存文件成功')
        # 调用finish()给它一个响应，手动关闭连接
        self.finish()

    @asynchronous
    def get(self):
        # 获取查询参数中的url（下载资源的网址）
        url = self.get_query_argument('url')

        # 发起异步请求
        client = AsyncHTTPClient()
        # validate_cert 是否验证ssl安全连接的证书
        client.fetch(url,
                     callback=self.save,
                     validate_cert=False)  # validate验证证书为Flase

        self.write('下载中...')
        self.set_status(200)


# 协程处理
class XcDownloadHandler(RequestHandler):

    def save(self,response: HTTPResponse):
        # print(response.effective_url, '下载成功')
        self.write('<br>下载完成，正在保存')

        # 在回调函数中，可以获取请求的查询参数
        filename = self.get_query_argument('filename', 'index.html')

        # 保存到static/downloads
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)

        self.write('<br>保存文件成功')
        # 调用finish()给它一个响应，手动关闭连接
        self.finish()

    @asynchronous
    async def get(self):
        # 获取查询参数中的url（下载资源的网址）
        url = self.get_query_argument('url')

        # 发起异步请求
        client = AsyncHTTPClient()
        # validate_cert 是否验证ssl安全连接的证书
        response = await client.fetch(url, validate_cert=False)  # validate验证证书为Flase
        self.write('下载中...')
        self.save(response)
        self.set_status(200)