

label street_house_outside:
    $ print "enter_street_house_outside"
    $ miniMapData = []
    if miniMapTurnedOff == False:
        call miniMapHouseGenerate() from _call_miniMapHouseGenerate_20

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_House_Outside[day_suffix]"
    music night_ambience
    return

label street_house_outside_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Outside_Monica_[cloth][day_suffix]", "click" : "street_house_outside_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Teleport_House_Outside_Outside", {"type":3, "text" : _("ИДТИ ПО ДОРОГЕ"), "rarrow" : "arrow_down_2", "base":"Street_House_Outside_Teleport_Outside", "click" : "street_house_outside_teleport", "xpos" : 200, "ypos" : 790, "zorder":11, "teleport":True, "house_out_teleport":True})
    $ add_object_to_scene("Teleport_House_Gate", {"type":3, "text" : _("НАЗАД К ВОРОТАМ"), "larrow" : "arrow_left_2", "base":"Street_House_Outside_Teleport_Gate", "click" : "street_house_outside_teleport", "xpos" : 1531, "ypos" : 605, "zorder":9, "b":0.2, "tint":[1.0, 1.0, 0.7], "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_house_outside_teleport:
    if obj_name == "Teleport_House_Gate":
        call change_scene("street_house_gate") from _call_change_scene_149
        return
    if obj_name == "Teleport_House_Outside_Outside":
        call map_show() from _call_map_show_1
        return
    return
label street_house_outside_environment:
    if obj_name == "Monica":
        mt "Я помню как стучалась в эти ворота недавно..."
        "Это все какой-то кошмар!"
        "Скоро это все должно закончиться!"
        return
    return
