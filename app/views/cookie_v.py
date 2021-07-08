import tornado
from tornado.web import RequestHandler


class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        # 验证参数中是否存在 name？
        if self.request.arguments.get('name'):
            # 从查询参数中读取Cookie的名称
            name = self.get_query_argument('name')

            # 从cookies中获取name的对象或值
            value = self.get_cookie(name)
            self.write(value)
        else:
            # 查看所有cookie
            cookies: dict = self.request.cookies
            html = '<ul>%s</ul>'
            lis = []
            for key in cookies:
                lis.append('<li>%s: %s</li>' % (key, self.get_cookie(key)))

            html = '显示所以cookie' + html % ''.join(lis)
            html += """
                <form method="post">
                    <input name="name" placeholder="请输入cookie">
                    <button>提交</button>
                </form>
            """
            self.write(html)

    def post(self):
        name = self.get_argument('name')
        if self.request.cookies.get(name, None):
            # 存在的
            self.clear_cookie(name)
            self.write('<h3>删除%s成功</h3>' % name)
        else:
            self.write('<h3>删除%s失败,不存在</h3>' % name)

        # 重定向操作时，不需要再调用self.write()
        self.redirect('/cookie')  # 重定向