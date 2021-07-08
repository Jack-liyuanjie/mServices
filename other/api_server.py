import json
import uuid

import tornado.web
from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_command_line


class LoginHandler(RequestHandler):

    users = [{
        'id': 1,
        'name': 'liyuanjie',
        'pwd': '1234',
        'last_login_device': 'Android 5.1 OnePlus5'
    }]

    def set_default_headers(self):
        # 所有的请求方式执行后，默认设置的响应头的信息
        # 以下设置响应头都是解决跨域问题
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type,x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE')

    def get(self):
        # 读取json数据
        bytes = self.request.body  # 字节码类型
        print(bytes)
        print(self.request.headers.get('Content-Type'))

        # 从请求头中读取请求上传的数据类型
        content_type = self.request.headers.get('Content-Type')
        if content_type.startswith('application/json'):
            # self.write('upload json ok')
            # 字节码类型转字符串
            json_str = bytes.decode('utf-8')
            # 反序列化
            json_data = json.loads(json_str)

            resp_data = {}
            login_user = None
            # 查询用户名和口令是否正确
            for user in self.users:
                if user['name'] == json_data['name']:
                    if user['name'] == json_data['name']:
                        if user['pwd'] == json_data['pwd']:
                            login_user = user
                            break
            if login_user:
                resp_data['msg'] = 'success'
                resp_data['token'] = uuid.uuid4().hex
            else:
                resp_data['msg'] = '查无此人'
            self.write(resp_data)  # wirte()函数可接受str, dict, list
            self.set_header('Content-Type', 'application/json')
        else:
            self.write('upload data 必须是json格式')

    def post(self, *args, **kwargs):
        # 读取数据类型
        bytes = self.request.body # 字节类型
        print(bytes)

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def options(self):
        # 跨域请求时，会被客户端请求，用来表示服务器是否支持跨域请求
        self.set_status(200)

def make_app():
    return tornado.web.Application(
        handlers=[
            ('/user', LoginHandler),
        ],
        default_host=options.port)


if __name__ == '__main__':
    # 定义命令行参数
    define('port',
           default=8000,
           type=int,
           help='绑定的端口')
    define('host',
           default='localhost',
           type=str,
           help='绑定的主机ip')
    # 解析命令行参数
    parse_command_line()

    app = make_app()
    app.listen(options.port)
    print('Running https://%s:%s' % (options.host, options.port))
    IOLoop.current().start()
