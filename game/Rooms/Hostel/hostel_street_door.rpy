label hostel_street_door:
    $ print "enter_hostel_street2"
    $ miniMapData = []
    call miniMapHostelGenerate()

    $ sceneIsStreet = True
    $ scene_image = "scene_hostel_street_door[day_suffix]"
    return

label hostel_street_door_init:
    $ add_object_to_scene("Teleport_hostel_reception", {"type":2, "base":"Hostel_Street2_Door", "click" : "hostel_street_door_teleport", "actions" : "lw", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7], "teleport":True})
    $ add_object_to_scene("Poster", {"type":2, "base":"Hostel_Street2_Poster", "click" : "hostel_street_door_environment", "actions" : "l", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7], "group":"environment"})
#    $ add_object_to_scene("Pipes", {"type":2, "base":"Hostel_Street2_Pipes", "click" : "hostel_street_door_environment", "actions" : "l", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7], "group":"environment"})

#    $ add_object_to_scene("Car", {"type":2, "base":"hostel_street2_Car", "click" : "hostel_street2_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Hostel_Street", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "hostel_street_door_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_street_door_teleport:
    if obj_name == "Teleport_Hostel_Street":
        if cloth_type == "Nude":
            call change_scene("hostel_street", "Fade", "snd_walk_barefoot")
            return
        call change_scene("hostel_street")
        return
    if obj_name == "Teleport_hostel_reception":
        if act == "l":
            mt "Это вход в хостел..."
        if act == "w":
            mt "Я не пойду туда! Там насильники! И я теперь должна $10.000 управляющей этой дыры."
            return
            call change_scene("hostel_reception", "Fade_long", "snd_jail_door")
            return
        return
    return
label hostel_street_door_environment:
    if obj_name == "Poster":
        mt "Я не пойду туда! Там насильники! И я теперь должна $10.000 управляющей этой дыры."
        return
    if obj_name == "Pipes":
        pass

    return
