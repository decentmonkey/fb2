label street_corner:
    $ print "enter_street_corner"
    $ miniMapData = []
    call miniMapHostelGenerate() from _call_miniMapHostelGenerate_1

    $ sceneIsStreet = True
    $ scene_image = "scene_street_Whores_Place_Car_Stop[day_suffix]"

    $ hostelStreet3MonicaFromSideSuffix = ""
    if day_time == "day":
        music street5
    else:
        if rand(1,4) > 1:
            music street_evening3
        else:
            music street13_ambulance
    return

label street_corner_init:

    $ add_object_to_scene("Monica", {"type":2, "base":"Street_Whores_Place_Car_Stop_Monica_[cloth][day_suffix]", "click" : "street_corner_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Citizen_5", {"type":2, "base":"Street_Whores_Place_Car_Stop_Citizen_5[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})

    $ add_object_to_scene("Teleport_Street1", {"type":3, "text" : _("ВНИЗ ПО УЛИЦЕ"), "larrow" : "arrow_left_2", "base":"Street_Whores_Place_Car_Stop_Teleport_Street1", "click" : "street_corner_teleport", "xpos" : 200, "ypos" : 644, "zorder":15, "teleport":True})
    $ add_object_to_scene("Teleport_Hostel_Street3", {"type":3, "text" : _("БЕДНЫЙ РАЙОН"), "rarrow" : "arrow_up_2", "base":"Street_Whores_Place_Car_Stop_Teleport_Hostel_Street3", "click" : "street_corner_teleport", "xpos" : 1713, "ypos" : 768, "zorder":15, "teleport":True, "high_sprite_hover":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_corner_teleport:
    if obj_name == "Teleport_Street1":
        if cloth_type == "Nude":
            call change_scene("whores_place_street1", "Fade", "snd_walk_barefoot") from _call_change_scene_10
            return
        call change_scene("whores_place_street1", "Fade", "highheels_run2") from _call_change_scene_11
        return
    if obj_name == "Teleport_Hostel_Street3":
        if cloth_type == "Nude":
            call change_scene("hostel_street3", "Fade", "snd_walk_barefoot") from _call_change_scene_12
            return
        call change_scene("hostel_street3", "Fade", "highheels_run2") from _call_change_scene_13
        return
    return
label street_corner_environment:
    if obj_name == "Monica":
        mt "Что за грязное место?"
        "Мне противно находиться здесь!"
        return

    return
