import os

from tornado.web import Application

from app.views.cookie_v import CookieHandler
from app.views.index_v import IndexHandler
from app.views.order_v import OrderHandler
from app.views.search_v import SearchHandler
from app.ui.nav import NavModule
from app.ui.menu import MenuModule
from app.views.download import DownloadHandler, AsyncDownloadHandler, XcDownloadHandler
from app.views.message import RobbitHandler, MessageHandler, MessagexinHandler
from app.views.user import UseHandler
# 配置settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
settings = {
    'debug': True,
    'template_path': os.path.join(BASE_DIR, 'templates'),
    'static_path': os.path.join(BASE_DIR, 'static'),
    'static_url_prefix': '/s/',
    'ui_modules': {
        'Nav': NavModule,
        'Menu': MenuModule
    },
    'cookie_secret': '64ejhas8dfsd71208d'
}


def make_app(host='localhost'):
    return Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        ('/download', DownloadHandler),
        ('/asdownload', AsyncDownloadHandler),
        ('/xcdownload', XcDownloadHandler),
        ('/message', MessageHandler),
        ('/robbit', RobbitHandler),
        ('/msg', MessagexinHandler),
        ('/login', UseHandler),
        (r'/order/(?P<action_code>\d+)/(?P<order_id>\d+)', OrderHandler)
    ], default_host=host, **settings)