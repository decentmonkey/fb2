label rich_hotel_event_hall:
    $ print "rich_hotel_event_hall"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Rich_Hotel_Event_Hall"
    return

label rich_hotel_event_hall_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Monica_[cloth]", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Philip", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Philip", "click" : "rich_hotel_event_hall_environment", "actions" : "lt", "zorder":10})
    $ add_object_to_scene("HotelStaff", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_HotelStaff", "click" : "rich_hotel_event_hall_environment", "actions" : "lt", "zorder":10})

    $ add_object_to_scene("Chair1", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Chair1", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Chair2", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Chair2", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Chair3", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Chair3", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Chair4", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Chair4", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Lamp", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Lamp", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Palm", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Palm", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("People", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_People", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Poster", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Poster", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("PosterMelanie", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_PosterMelanie", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Scene", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Scene", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Table", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Table", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})

#    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3], "group":"environment"})

    $ add_object_to_scene("Teleport_Rich_Hotel_Reception", {"type":3, "text" : _("ЛИФТ"), "rarrow" : "arrow_right_2", "base":"Rich_Hotel_Event_Hall_Exit", "click" : "rich_hotel_event_hall_teleport", "xpos" : 319, "ypos" : 230, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Rich_Hotel_Tables", {"type":3, "text" : _("СТОЛИКИ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow", "click" : "rich_hotel_event_hall_teleport", "xpos" : 334, "ypos" : 431, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Rich_Hotel_Sofa", {"type":3, "text" : _("ВИП ЗОНА"), "rarrow" : "arrow_right_2", "base":"Rich_Hotel_Event_Hall_Teleport_Sofa", "click" : "rich_hotel_event_hall_teleport", "xpos" : 1517, "ypos" : 1038, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_event_hall_teleport:
    if obj_name == "Teleport_Rich_Hotel_Reception":
#            call change_scene("rich_hotel_reception")
        return
    if obj_name == "Teleport_Rich_Hotel_Tables":
            call change_scene("rich_hotel_event_tables")
        return
    if obj_name == "Teleport_Rich_Hotel_Sofa":
            call change_scene("rich_hotel_event_sofa")
        return
    return
label rich_hotel_event_hall_environment:

    if obj_name == "Monica":
        return
    if obj_name == "Philip":
        if act == "l":
            return
        if act == "t":
            return
    if obj_name == "HotelStaff":
        if act == "l":
            return
        if act == "t":
            return

    if obj_name == "Chair1" or obj_name == "Chair2" or obj_name == "Chair3" or obj_name == "Chair4":
        return
    if obj_name == "Lamp":
        return
    if obj_name == "Palm":
        return
    if obj_name == "People":
        return
    if obj_name == "Poster":
        return
    if obj_name == "PosterMelanie":
        return
    if obj_name == "Scene":
        return
    if obj_name == "Table":
        return

    return
