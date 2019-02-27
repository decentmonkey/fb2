default ep23_quests_initialized = False

label ep23_Quests_init:
    $ ep23_quests_initialized = True
    $ remove_hook(label="food_basement_room_init") #страховка
    $ add_hook("before_open", "food_basement_room_init", scene="basement_bedroom2", label="food_basement_room_init", priority = 200)
    $ add_hook("before_open", "food_basement_room_init", scene="basement_bedroom_table", label="food_basement_room_init", priority = 200)
    call basement_bedroom_table_init()
    call basement_bedroom2_init()
    $ define_inventory_object("food_package", {"description" : _("Еда"), "label_suffix" : "_use_food", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/food_package" + res.suffix + ".png"})

    return
