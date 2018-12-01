default hostelStreet2MonicaFromSideSuffix = ""

label hostel_street2:
    $ print "enter_hostel_street2"
    $ miniMapData = []

    $ sceneIsStreet = True

    $ scene_image = "scene_Hostel_Street2[day_suffix]"
    return
label hostel_street2_init:

    $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Street2_Monica_[cloth][hostelStreet2MonicaFromSideSuffix][day_suffix]", "click" : "hostel_street2_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Citizen_6", {"type" : 2, "base" : "Hostel_Street2_Citizen_6[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_8", {"type" : 2, "base" : "Hostel_Street2_Citizen_8[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_10", {"type" : 2, "base" : "Hostel_Street2_Citizen_10[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_12", {"type" : 2, "base" : "Hostel_Street2_Citizen_12[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_13", {"type" : 2, "base" : "Hostel_Street2_Citizen_13[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_street2_teleport:

    return
label hostel_street2_environment:

    return
