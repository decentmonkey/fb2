label rich_hotel_event_sittable:
    $ print "rich_hotel_event_sittable"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_rich_hotel_event_sittable_Philip_Monica"
    return

label rich_hotel_event_sittable_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "rich_hotel_event_sittable_Monica", "click" : "rich_hotel_event_sittable_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Philip", {"type" : 2, "base" : "rich_hotel_event_sittable_Philip", "click" : "rich_hotel_event_sittable_environment", "actions" : "lt", "zorder":10})

    $ add_object_to_scene("Teleport_Rich_Hotel_Hall", {"type":3, "text" : _("ИДТИ КО СЦЕНЕ"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "rich_hotel_event_sofa_teleport", "xpos" : 780, "ypos" : 956, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_event_sittable_teleport:
    return
label rich_hotel_event_sittable_environment:
    if obj_name == "Monica":
        return
    if obj_name == "Philip":
        if act == "l":
            return
        if act == "t":
            return

    return
