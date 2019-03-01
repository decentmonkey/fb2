default ep23_quests_initialized = False

default melanieWaitingOpenedOutfits = False # Мелани ждет, чтобы октрылись костюмы у Моники для фотосессии

label ep23_Quests_init:
    $ ep23_quests_initialized = True
    $ remove_hook(label="food_basement_room_init") #страховка
    $ add_hook("before_open", "food_basement_room_init", scene="basement_bedroom2", label="food_basement_room_init", priority = 200)
    $ add_hook("before_open", "food_basement_room_init", scene="basement_bedroom_table", label="food_basement_room_init", priority = 200)
    call basement_bedroom_table_init()
    call basement_bedroom2_init()
    $ define_inventory_object("food_package", {"description" : _("Еда"), "label_suffix" : "_use_food", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/food_package" + res.suffix + ".png"})
    if str(13) in questLogDataEnabled:
        $ questLog(13, False)
        $ questLog(13, True)
    if monicaOutfitsEnabled[2] == True:
        $ monicaOutfitsEnabled[3] = True # Открываем следующий костюм



    return
