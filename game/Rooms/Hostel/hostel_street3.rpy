default hostelStreet3MonicaFromSideSuffix = ""

label hostel_street3:
    $ print "enter_hostel_street2"
    $ miniMapData = []

    $ sceneIsStreet = True

    $ scene_image = "scene_Hostel_Street3[day_suffix]"
    return
label hostel_street3_init:

    $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Street3_Monica_[cloth][hostelStreet3MonicaFromSideSuffix][day_suffix]", "click" : "hostel_street3_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Citizen_3", {"type" : 2, "base" : "Hostel_Street3_Citizen_3[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_4", {"type" : 2, "base" : "Hostel_Street3_Citizen_4[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_7", {"type" : 2, "base" : "Hostel_Street3_Citizen_7[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_street3_teleport:

    return
label hostel_street3_environment:

    return
