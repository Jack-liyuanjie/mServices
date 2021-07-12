from unittest import TestCase

from utils.conn import session, Base
from app.models.menu import Menu


class TestBase(TestCase):
    def test_base(self):
        Base.metadata.drop_all()
        Base.metadata.create_all()


class TestMenuORM(TestCase):
    # 增
    def test_add(self):
        m1 = Menu()
        m1.title = '用户管理'

        session.add(m1)
        session.commit()

    def test_adds(self):
        session.add_all([
            Menu(title='订单管理'),
            Menu(title='会员管理', url='/user1', parent_id=1),
            Menu(title='派件员', url='/user2', parent_id=1),
            Menu(title='合作商', url='/user3', parent_id=1),
            Menu(title='订单统计', url='/order_cnt', parent_id=2)
        ])

        session.commit()

    # 查
    def test_get(self):
        # 查询—session.query(模型类)
        m = session.query(Menu).get(1)
        print(m.title)
        print('----子菜单----')
        for cm in m.childs:
            print(cm)

    # 查看一级菜单,判断parent_id不为空则为以及菜单
    def test_query_root_menu(self):
        ms = session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        for menu in ms:
            print(menu)
            for secondayr in menu.childs:
                print('-'*3, secondayr)

    # 改
    def test_update(self):
        menu = session.query(Menu).get(5)
        menu.title = '合作伙伴'
        session.commit()

    # 删
    def test_delete(self):
        menu = session.query(Menu).get(5)
        session.delete(menu)
        session.commit()

