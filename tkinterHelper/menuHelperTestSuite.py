import unittest
from .menuHelper import MenuHelper, MenuItem
from tkinter import Tk, Menu


class TestMenuHelper(unittest.TestCase):
    def test_init_menuhelper(self):
        window = Tk()
        menu = MenuHelper(window)

        self.assertIsInstance(menu, MenuHelper)

    def test_init_menuitem(self):
        item = MenuItem('Item')

        self.assertIsInstance(item, MenuItem)

    def test_menu_build_way1(self):
        def sample_method():
            x = 1
        window = Tk()
        menu = MenuHelper(window)

        mmenu_1 = MenuItem('main_item_1')
        mmenu_1.add_child(MenuItem('sub_item_1', sample_method))
        mmenu_1.add_child(MenuItem('sub_item_2', command=sample_method))
        menu.add_item(mmenu_1)

        self.assertEqual(1, len(menu._items))
        self.assertEqual(2, len(menu._items['main_item_1'].children))

        mmenu_2 = MenuItem(label='main_item_2', command=sample_method)
        menu.add_item(mmenu_2)

        self.assertEqual(2, len(menu._items))
        self.assertEqual(0, len(menu._items['main_item_2'].children))

    def test_menu_build_way2(self):
        def sample_method():
            x = 1
        window = Tk()
        menu = MenuHelper(window)

        menu.add_item(MenuItem('main_item_1'))

        self.assertEqual(1, len(menu._items))

        menu.add_subitem('main_item_1', MenuItem('sub_item_1', sample_method))
        menu.add_subitem(key='main_item_1', item=MenuItem('sub_item_2', sample_method))

        self.assertEqual(2, len(menu._items['main_item_1'].children))

        menu.add_item(item=MenuItem(label='main_item_2', command=sample_method))

        self.assertEqual(2, len(menu._items))
        self.assertEqual(0, len(menu._items['main_item_2'].children))

    def test_menu_build_way3(self):
        def sample_method():
            x = 1
        window = Tk()
        menu = MenuHelper(window)

        menu.add_create_item('main_item_1')

        self.assertEqual(1, len(menu._items))

        menu.add_create_subitem('main_item_1', 'sub_item_1', sample_method)
        menu.add_create_subitem(key='main_item_1', label='sub_item_2', command=sample_method)

        self.assertEqual(2, len(menu._items['main_item_1'].children))

        menu.add_create_item(label='main_item_2', command=sample_method)

        self.assertEqual(2, len(menu._items))
        self.assertEqual(0, len(menu._items['main_item_2'].children))

    def test_create_method(self):
        window = Tk()
        menu = MenuHelper(window)
        menu.add_create_item('main_item_1')

        menu.create()

        self.assertIsInstance(menu._menu, Menu)
