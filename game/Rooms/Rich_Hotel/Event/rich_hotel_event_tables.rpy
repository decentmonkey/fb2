label rich_hotel_event_tables:
    $ print "rich_hotel_event_tables"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_rich_hotel_event_tables"
    return

label rich_hotel_event_tables_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "rich_hotel_event_tables_Monica_[cloth]", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Philip", {"type" : 2, "base" : "rich_hotel_event_tables_Philip", "click" : "rich_hotel_event_tables_environment", "actions" : "lt", "zorder":10})

#    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3], "group":"environment"})

    $ add_object_to_scene("Teleport_Rich_Hotel_Hall", {"type":3, "text" : _("ИДТИ КО СЦЕНЕ"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "rich_hotel_event_sofa_teleport", "xpos" : 780, "ypos" : 956, "zorder":11, "teleport":True})
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

    return
