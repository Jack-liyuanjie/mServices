import tornado
from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 1.请求参数获取
        wd = self.get_argument('wd')
        print(wd)
        # 2.读取多个参数名相同的参数值
        titles = self.get_arguments('title')
        print(titles)
        # 3.从查询参数中读取url路径参数
        wd2 = self.get_query_argument('wd')
        print(wd2)
        titles2 = self.get_query_arguments('title')
        print(titles2)
        # 4.从请求对象中读取参数
        req: HTTPServerRequest = self.request

        # request请求中的数据都是dict字典类型
        wd3 = req.arguments.get('wd')
        print(wd3)  # 字典key对应的value都是bytes字节类型

        wd4 = req.query_arguments.get('wd')
        print(wd4)
        self.write('<h3>我是主页</h3>')

    def post(self):
        name = self.get_argument('name')
        city = self.get_argument('city')
        self.write('<h3>我是POST：%s %s</h3>' % (name, city))
        # 新增数据
        # 读取表单参数
        name = self.get_body_arguments('name')
        city = self.get_body_arguments('city')
        print(name, city)

    def put(self, *args, **kwargs):
        self.write('<h3>我是PUT</h3>')

    def delete(self):
        self.write('<h3>我是del/h3>')