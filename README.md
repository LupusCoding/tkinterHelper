# tkinterHelper ![LICENSE](https://img.shields.io/github/license/LupusCoding/tkinterHelper)

The package tkinterHelper let you easily create tkinter objects.

This package is not part of the standard tkinter package nor created or proven by the 
original creators of tkinter.

This package requires: tkinter

## implemented helper
* [MenuHelper](#menuhelper)

## MenuHelper
![MenuHelper Tests](https://img.shields.io/github/workflow/status/LupusCoding/tkinterHelper/CI)

Create menus in a simple way, by using the MenuHelper and its' methods like add_item() 
or add_subitem().

You can use three different ways to create the menu.

### 1. way to create
```python
from tkinterHelper import MenuHelper, MenuItem
from tkinter import Tk

window = Tk()

# create MenuHelper
menu = MenuHelper(window)
# create main menu item
mmenu_1 = MenuItem('Main Item 1')
# create sub menu item on main menu item
mmenu_1.add_child(MenuItem('Sub Item 1', method1))
# create another sub menu item on main menu item
mmenu_1.add_child(MenuItem(label='Sub Item 2', method2))
# add the items to stack
menu.add_item(mmenu_1)
# create another main menu item
mmenu_2 = MenuItem(label='Main Item 2', command=method3)
# add the second main menu item to stack
menu.add_item(mmenu_2)
# create tkinter menu
menu.create()
```

### 2. way to create
```python
from tkinterHelper import MenuHelper, MenuItem
from tkinter import Tk

window = Tk()

# create MenuHelper
menu = MenuHelper(window)
# create main menu item
menu.add_item(MenuItem('Main Item 1'))
# create sub menu item on main menu item
menu.add_subitem('Main Item 1', MenuItem('Sub Item 1', method1))
# create another sub menu item on main menu item
menu.add_subitem(key='Main Item 1', item=MenuItem('Sub Item 2', method2))
# create another main menu item
menu.add_item(item=MenuItem(label='Main Item 2', command=method3))
# create tkinter menu
menu.create()
```

### 3. way to create
```python
from tkinterHelper import MenuHelper
from tkinter import Tk

window = Tk()

# create MenuHelper
menu = MenuHelper(window)
# create main menu item
menu.add_create_item('Main Item 1')
# create sub menu item on main menu item
menu.add_create_subitem('Main Item 1', 'Sub Item 1', method1)
# create another sub menu item on main menu item
menu.add_create_subitem(key='Main Item 1', label='Sub Item 2', command=method2)
# create another main menu item
menu.add_create_item(label='Main Item 2', command=method3)
# create tkinter menu
menu.create()
```
