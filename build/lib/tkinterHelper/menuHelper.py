from tkinter import Menu
from tkinter import Tk


class MenuItem:
    """Menu item to be used with MenuHelper class"""
    def __init__(self, label, command=None):
        """class constructor

        :param label: Menu item label
        :type label: str
        :param command: callback function pointer
        :type command: function | Callable
        """
        self._label = label if label is not None else ''
        self._command = command if command is not None else False
        self._children = []
        self._is_subitem = False

    @property
    def label(self):
        """Get item label

        :return: item label
        :rtype: str
        """
        return self._label

    @property
    def command(self):
        """Get callback for menu entry

        :return: item callback
        :rtype: function
        """
        return self._command

    @property
    def children(self):
        """Get sub items of this items

        :return: List of sub items
        :rtype: list
        """
        return self._children

    @property
    def is_parent(self):
        """Check if item is parent of other items

        :return: True if item has children, otherwise False
        :rtype: bool
        """
        return len(self._children) > 0

    def add_child(self, item):
        """Add a sub item

        :param item: Item to be added as child
        :type item: MenuItem
        :return: Count of added sub items
        :rtype: int
        """
        if self._is_subitem:
            raise Exception('ItemDepthError: Only one level of sub items is supported.')
        item._is_subitem = True
        self._children.append(item)
        return len(self._children)


class MenuHelper:
    """MenuHelper to easily create Tk menus"""
    def __init__(self, mainframe):
        """class constructor

        :param mainframe: Frame item (Tk frame)
        :type mainframe: Tk
        """
        if mainframe is not None and not isinstance(mainframe, Tk):
            raise Exception('TypeError: param mainframe must be instance of tkinter.Tk')
        self._mainframe = mainframe
        self._items = {}
        self._menu = None

    def add_item(self, item):
        """Add a new item to main menu

        :param item: Item to be added to the menu
        :type item: MenuItem
        """
        self._items[item.label] = item

    def add_create_item(self, label, command=None):
        """Add a new item to main menu, by label and command.

        Recommendation: use add_item method

        :param label: Menu item label
        :type label: str
        :param command: callback function pointer
        :type command: function | Callable
        """
        self._items[label] = MenuItem(label=label, command=command)

    def add_subitem(self, key, item):
        """Add a sub item to an existing menu main item

        :param item: Item to be added
        :type item: MenuItem
        :param key: Key of main item to add sub item to
        :type key: str
        :return: True if sub item could be added, otherwise False
        :rtype: bool
        """
        if key in self._items:
            self._items[key].add_child(item)
            return True
        else:
            return False

    def add_create_subitem(self, key, label, command=None):
        """Add a sub item to an existing menu main item, by label and command.

        Recommendation: use add_item method

        :param key: Key of main item to add sub item to
        :type key: str
        :param label: Menu item label
        :type label: str
        :param command: callback function pointer
        :type command: function | Callable
        :return: True if sub item could be added, otherwise False
        :rtype: bool
        """
        if key in self._items:
            self._items[key].add_child(MenuItem(label=label, command=command))
            return True
        else:
            return False

    def create(self):
        """Create the menu and add to mainframe"""
        self._menu = Menu(self._mainframe)
        for key in self._items:
            print('key:', key)
            print('item:', self._items[key])
            m = Menu(self._menu)
            if self._items[key].is_parent:
                print(key, 'is_parent')
                # continue
                for item in self._items[key].children:
                    print(item)
                    m.add_command(label=item.label, command=item.command)
            else:
                m.add_command(label=self._items[key].label, command=self._items[key].command)
            self._menu.add_cascade(label=key, menu=m)
        self._mainframe.config(menu=self._menu)
