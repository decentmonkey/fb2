label rich_hotel_event_tables:
    $ print "rich_hotel_event_tables"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_rich_hotel_event_tables"
    return

label rich_hotel_event_tables_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "rich_hotel_event_tables_Monica_[cloth]", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Philip", {"type" : 2, "base" : "rich_hotel_event_tables_Philip", "click" : "rich_hotel_event_tables_environment", "actions" : "lt", "zorder":10})

    $ add_object_to_scene("Philip", {"type" : 2, "base" : "rich_hotel_event_tables_Philip", "click" : "rich_hotel_event_tables_environment", "actions" : "lt", "zorder":10})

    $ add_object_to_scene("Chair1", {"type" : 2, "base" : "rich_hotel_event_tables_Chair1", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair2", {"type" : 2, "base" : "rich_hotel_event_tables_Chair2", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair3", {"type" : 2, "base" : "rich_hotel_event_tables_Chair3", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair4", {"type" : 2, "base" : "rich_hotel_event_tables_Chair4", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair5", {"type" : 2, "base" : "rich_hotel_event_tables_Chair5", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair6", {"type" : 2, "base" : "rich_hotel_event_tables_Chair6", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair7", {"type" : 2, "base" : "rich_hotel_event_tables_Chair7", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair8", {"type" : 2, "base" : "rich_hotel_event_tables_Chair8", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})

    $ add_object_to_scene("Drinks", {"type" : 2, "base" : "rich_hotel_event_tables_Drinks", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Flower", {"type" : 2, "base" : "rich_hotel_event_tables_Flower", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("People", {"type" : 2, "base" : "rich_hotel_event_tables_People", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Table1", {"type" : 2, "base" : "rich_hotel_event_tables_Table1", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Table2", {"type" : 2, "base" : "rich_hotel_event_tables_Table2", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})

#    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3], "group":"environment"})

    $ add_object_to_scene("Teleport_Rich_Hotel_Hall", {"type":3, "text" : _("ИДТИ КО СЦЕНЕ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow", "click" : "rich_hotel_event_sofa_teleport", "xpos" : 1633, "ypos" : 997, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_event_tables_teleport:
    if obj_name == "Teleport_Rich_Hotel_Hall":
            call change_scene("rich_hotel_event_hall")
        return
    return
label rich_hotel_event_tables_environment:
    if obj_name == "Monica":
        return
    if obj_name == "Philip":
        if act == "l":
            return
        if act == "t":
            return

    if obj_name == "Chair1" or obj_name == "Chair2" or obj_name == "Chair3" or obj_name == "Chair4":
        return
    if obj_name == "Chair5" or obj_name == "Chair6" or obj_name == "Chair7" or obj_name == "Chair8":
        return
    if obj_name == "Drinks":
        return
    if obj_name == "Flower":
        return
    if obj_name == "People":
        return
    if obj_name == "Table1":
        return
    if obj_name == "Table2":
        return

    return
