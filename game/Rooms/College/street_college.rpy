default streetCollegeMonicaSuffix = 1
default streetCollegeBettySuffix = 1

label street_college:

    $ print "enter_street_college"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_College[day_suffix]"

#    music
    music Groove2_85
    return

label street_college_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_College_Monica_" + cloth + "_[streetCollegeMonicaSuffix]" + day_suffix, "click" : "street_college_environment", "actions" : "l", "zorder" : 10}, scene="street_college")
    $ add_object_to_scene("Betty", {"type":2, "base":"Street_College_Betty[streetCollegeBettySuffix]" + day_suffix, "click" : "street_college_environment", "actions" : "l", "zorder" : 10}, scene="street_college")
    $ add_object_to_scene("College", {"type":2, "base":"Street_College_Building", "click" : "street_college_teleport", "actions" : "lw", "zorder" : 0}, scene="street_college")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_college_teleport:
    if obj_name == "College":
        if act=="l":
            call dialogue_classmate_3_3i() #dialogue_betty_college_1_1s()
        if act=="w":
            if day_time != "evening":
                call dialogue_classmate_3_2d()
            else:
                call dialogue_classmate_3_2c()
    return
label street_college_environment:
    if obj_name == "Monica":
        call dialogue_classmate_3_2e()

    return
