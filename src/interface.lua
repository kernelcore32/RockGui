create_window("title", "600x500")

local function send_message(name)
    print("Hello from " .. name .. "!")
end

create_button("click me", function() send_message("interpreter") end, 100, 100)

local listbox = create_list_box(nil, 200, 200)

local menu_bar = create_menu_bar()

create_menu_child(menu_bar, "File")