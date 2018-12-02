label rich_hotel_event_sofa:
    $ print "rich_hotel_event_sofa"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_rich_hotel_event_sofa_Monica_Melanie_Beef"
    return

label rich_hotel_event_sofa_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "rich_hotel_event_sofa_Monica_[cloth]", "click" : "rich_hotel_event_sofa_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Beef", {"type" : 2, "base" : "rich_hotel_event_sofa_Philip", "click" : "rich_hotel_event_sofa_environment", "actions" : "lt", "zorder":10})
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "rich_hotel_event_sofa_Melanie", "click" : "rich_hotel_event_sofa_environment", "actions" : "lt", "zorder":11})

    $ add_object_to_scene("Komode", {"type" : 2, "base" : "rich_hotel_event_sofa_Komode", "click" : "rich_hotel_event_sofa_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Lamp", {"type" : 2, "base" : "rich_hotel_event_sofa_Lamp", "click" : "rich_hotel_event_sofa_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("TV1", {"type" : 2, "base" : "rich_hotel_event_sofa_TV1", "click" : "rich_hotel_event_sofa_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("TV2", {"type" : 2, "base" : "rich_hotel_event_sofa_TV2", "click" : "rich_hotel_event_sofa_environment", "actions" : "l", "zorder":0, "group":"environment"})

#    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3], "group":"environment"})

    $ add_object_to_scene("Teleport_Rich_Hotel_Hall", {"type":3, "text" : _("ИДТИ КО СЦЕНЕ"), "larrow" : "arrow_left_2", "base":"Rich_Hotel_Event_Sofa_Teleport_Hall", "click" : "rich_hotel_event_sofa_teleport", "xpos" : 767, "ypos" : 1014, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_event_sofa_teleport:
    if obj_name == "Teleport_Rich_Hotel_Hall":
        call change_scene("rich_hotel_event_hall")
        return
    return
label rich_hotel_event_sofa_environment:
    if obj_name == "Monica":
        return
    if obj_name == "Beef":
        if act == "l":
            return
        if act == "t":
            return
    if obj_name == "Melanie":
        if act == "l":
            return
        if act == "t":
            return

    if obj_name == "Komode":
        return
    if obj_name == "Lamp":
        return
    if obj_name == "TV1" or obj_name == "TV2":
        return
    return
