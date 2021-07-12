from tornado.web import UIModule
from app.models.menu import Menu
from utils.conn import session


class MenuModule(UIModule):
    def render(self):
        data = {
            # 'menus': [
            #     {'title': '百度', 'url': 'https://www.baidu.com'},
            #     {'title': '京东', 'url': 'https://jd.com'},
            #     {'title': '阿里', 'url': 'https://www.aliyun.com'}
            # ]
            'menus': session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        }
        return self.render_string('ui/menu.html', **data)
