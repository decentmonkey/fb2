label rich_hotel_event_scene:
    $ print "rich_hotel_event_scene"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_rich_hotel_event_scene_melanie_beef_monica_photodress"
    return

label rich_hotel_event_scene_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "rich_hotel_event_scene_Monica_[cloth]", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Beef", {"type" : 2, "base" : "rich_hotel_event_scene_Beef", "click" : "rich_hotel_event_scene_environment", "actions" : "lt", "zorder":9})
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "rich_hotel_event_scene_Melanie", "click" : "rich_hotel_event_scene_environment", "actions" : "lt", "zorder":10})

#    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3], "group":"environment"})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_event_scene_teleport:
    return
label rich_hotel_event_scene_environment:
    if obj_name == "Monica":
        return
    if obj_name == "Beef":
        return
    if obj_name == "Melanie":
        return


    return
