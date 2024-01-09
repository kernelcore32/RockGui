create_window("title", "600x550")

local toggle = false

function toggleState()
    toggle = not toggle
    if toggle then
        print("Hello from interpreter!")
    else
        print("Not hello")
    end
end

create_button("click me", function() print("interpreter") end, 100, 100)

local listbox = create_list_box(nil, 200, 200)

local menu_bar = create_menu_bar()

create_menu_child(menu_bar, "File")

create_check_button("normal", function() toggleState() end, 300, 400)

show_message_box("Error", "what", "info")