import os
import time
import tkinter as tk
from tkinter.ttk import Separator
from tkinter import scrolledtext
from lupa import LuaRuntime

"""
╔═══╗        ╔╗      ╔═══╗      
║╔═╗║        ║║      ║╔═╗║      
║╚═╝║╔══╗╔══╗║║╔╗    ║║ ╚╝╔╗╔╗╔╗
║╔╗╔╝║╔╗║║╔═╝║╚╝╝    ║║╔═╗║║║║╠╣
║║║╚╗║╚╝║║╚═╗║╔╗╗    ║╚╩═║║╚╝║║║
╚╝╚═╝╚══╝╚══╝╚╝╚╝    ╚═══╝╚══╝╚╝

Rock Gui is developed by TuberAsk and KernelCore32 over at (https://github.com)
-------------------------------------------------------------------------------

Rock Gui is licensed under the redistribution terms of the Apache License v2.0 (c)

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.

"""

global root

def wait(s):
    time.sleep(s)

def create_window(title=None, geometry=None, iconbitmap=None):
    global root
    root = tk.Tk()
    root.title(title)
    root.geometry(geometry)
    root.iconbitmap(iconbitmap)

def create_button(text=None, command=None, x=None, y=None, width=None, height=None, bg_color=None, cursor=None):
    global root
    button = tk.Button(root, text=text, command=command, width=width, height=height, bg=bg_color, cursor=cursor)
    button.place(x=x, y=y)
    return button

def create_text_box(state=None, x=None, y=None, width=None, height=None, cursor=None, bg_color=None):
    global root
    text_box = tk.Text(root, state=state, width=width, height=height, cursor=cursor, bg=bg_color)
    text_box.place(x=x, y=y)
    return text_box

def create_scrolled_text(x=None, y=None, width=None, height=None):
    global root
    scrolled_text_box = scrolledtext.ScrolledText(root, width=width, height=height)
    scrolled_text_box.place(x=x, y=y)
    return scrolled_text_box

def create_entry(state=None, x=None, y=None, width=None, cursor=None, bg_color=None):
    global root
    entry = tk.Entry(root, state=state, width=width, bg=bg_color, cursor=cursor)
    entry.place(x=x, y=y)
    return entry

def create_separator(style=None, x=None, y=None, takefocus=None, cursor=None, orient=None, width=None):
    global root
    separator = Separator(root, style=style, takefocus=takefocus, cursor=cursor, orient=orient)
    separator.place(x=x, y=y, width=width)
    return separator

def create_menu_bar():
    global root
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    return menu_bar

def create_menu_child(menu_bar, label):
    child_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=label, menu=child_menu)
    return child_menu

def add_menu_command(menu, label, command):
    menu.add_command(label=label, command=command)

def create_list_box(state=None, y=None, x=None, bg_color=None, height=None, width=None, activestyle=None, relief=None):
    global root
    list_box = tk.Listbox(root, state=state, bg=bg_color, height=height, width=width, activestyle=activestyle, relief=relief)
    list_box.place(x=x, y=y)
    return list_box

def add_list_box_item(list_box, item):
    list_box.insert(tk.END, item)
    return list_box

def remove_list_box_item(list_box, item):
    try:
        index = list_box.get(0, tk.END).index(item)
        list_box.delete(index)
    except ValueError:
        pass

def create_check_button(state=None, command=None, x=None, y=None, text=None, cursor=None, font=None, bg_color=None, height=None, width=None):
    global root
    check_button = tk.Checkbutton(root, state=state, command=command, text=text, cursor=cursor, font=font, bg=bg_color, height=height, width=width)
    check_button.place(x=x, y=y)
    return check_button

def create_radio_button(state=None, command=None, x=None, y=None, text=None, cursor=None, font=None, bg_color=None, height=None, width=None):
    global root
    radio_button = tk.Radiobutton(root, state=state, command=command, text=text, cursor=cursor, font=font, bg=bg_color, height=height, width=width)
    radio_button.place(x=x, y=y)
    return radio_button

lua = LuaRuntime(unpack_returned_tuples=True)
lua.globals().create_window = create_window
lua.globals().create_button = create_button
lua.globals().create_text_box = create_text_box
lua.globals().create_entry = create_entry
lua.globals().create_separator = create_separator
lua.globals().create_menu_bar = create_menu_bar
lua.globals().create_menu_child = create_menu_child
lua.globals().add_menu_command = add_menu_command
lua.globals().create_list_box = create_list_box
lua.globals().add_list_box_item = add_list_box_item
lua.globals().remove_list_box_item = remove_list_box_item
lua.globals().create_scrolled_text = create_scrolled_text
lua.globals().create_radio_button = create_radio_button
lua.globals().create_check_button = create_check_button
lua.globals().wait = wait

current_dir = os.path.dirname(os.path.abspath(__file__))
for file_name in os.listdir(current_dir):
    if file_name.endswith(".lua"):
        lua_script_path = os.path.join(current_dir, file_name)
        lua.execute(open(lua_script_path).read())

root.mainloop()