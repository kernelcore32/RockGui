# Rock Gui
Rock gui is a python tkinter library wrapped around lua to create graphical user interfaces.

## Table of Contents
- [Installation](#installation)
- [Usage & Functions](#usage--functions)
- [Versions](#versions)
- [Donate](#donate)
- [License](#license)

## Installation
To install RockGui you'll have to download the source files or clone the github repository to your local computer. Locate the directory to RockGui and open the src folder.
Drag the 'main.py' file from the src folder to your project's directory. Execute the 'main.py' file whenever you are using the provided functions from Rock Gui in lua. 
To execute the 'main.py' file you are required to own Python and the Lupa library which you can download at https://python.org and https://pypi.org/project/lupa/. 
If you find any issues or you have any questions you want to ask, you can do so at the Issues tab located in our github repository or at our email teamkernelcore64@proton.me.

### Execution Command

Windows 11, Windows 10
```bash
py -m main
```

MacOS, Linux
```bash
python3 -m main
```

Makefile
```bash
make run
```

## Usage & Functions
These are the functions provided by Rock Gui v2.5.

The create_window function is used to create the window for your application where widgets will be inserted.
```lua
create_window("title of window", "size of window in the y and x axis: 500x500", "/icon/path/to/ico/file"):
```

The create_button function is used to create a button widget for the window which can be used to complete tasks and call functions on click.
```lua
create_button("button text", function() your_button_event() end, x axis placement, y axis plasement, width of button, height of button, "background color of button", "cursor style of button")
```

The create_text_box function is used to create a text box widget for the window which can be used to write and inserting contents from files.
```lua
create_text_box("state of the text box", x axis placement, y axis placement, width of text box, height of text box, "cursor style of text box", "background color of text box")
```

The create_scrolled_text function is used to create a text box with a scroll bar for the window. 
```lua
create_scrolled_text(x axis placement, y axis placement, width of scrolled text box, height of scrolled text box)
```

The create_entry function is used to create an entry for the window which can be used for password entries and file path entries.
```lua
create_entry("state of the entry", x axis placement, y axis placement, width of entry, "cursor style of entry", "background color of entry")
```

The create_separator function is used to create a line between a widget for the window. 
```lua
create_separator("style of the separator", x axis placement, y axis placement, --[[if you want it to takefocus either {true} or {false}--]], "cursor style of separator", "orient position of the separator either horizontal or vertical", width of separator)
```

Creates a new parent menu for the window. 
```lua
create_menu_bar()
```

Creates a new child menu and cascade for the parent menu.
```lua
create_menu_child(the parent menu, "cascade label")
```

Adds a command to the child menu.
```lua
add_menu_command(the child menu, "command label", function() your_menu_event() end)
```

The create_check_button function is used to create a check button for the window which can be used for option systems and settings frames.
```lua
create_check_button("state of the check button", function() your_check_button_event() end, x axis placement, y axis placement, "text displayed on check button", "cursor style of check button", "font of check button", "background color of check button", height of check button, width of check button)
```

The create_radio_button function is used to create a radio button for the window which can be used for one-selection systems and on/off options.
```lua
create_radio_button("state of the radio button", function() your_radio_button_event() end, x axis placement, y axis placement, "text displayed on radio button", "cursor style of radio button", "font of radio button", "background color of radio button", height of radio button, width of radio button)
```

The create_list_box function is used to create a list box for the window which can be used for displaying files, processes, directories, items and objects.
```lua
create_list_box("state of list box", y axis placement, x axis placement, "background color of list box", height of list box, width of list box, "active style of list box", "relief of list box")
```

Adds a list box item to a list box.
```lua
add_list_box_item(the listbox, "Item to add")
```

Deletes the index of a list box item.
```lua
remove_list_box_item(the listbox, "Item to remove")
```

## Versions
These are the supported versions of Rock Gui.

| Version 1.0.0 | Version 2.0.0 | Version 3.0.0 |
| -------- | -------- | -------- |
| ✅      | ✅       | ❌      |
|  |  |  |

## Donate
You can send a financial contribution to Rock Gui 
over at https://github.com/sponsors/TuberAsk.

## License
Rock Gui is licensed under the redistribution terms 
of the Apache License v2.0. Read more over at
https://apache.org/licenses/LICENSE-2.0.