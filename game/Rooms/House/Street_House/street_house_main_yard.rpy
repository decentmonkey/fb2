default driverOnHouseYard = True

label street_house_main_yard:
    $ print "enter_street_house_main_yard"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_House[day_suffix]"
    if day_time == "day":
        music Mandeville
    else:
        music night_ambience
    return

label street_house_main_yard_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Monica_[cloth][day_suffix]", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
    $ add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15})
    $ add_object_to_scene("Driver", {"type" : 2, "base" : "Street_House_Driver[day_suffix]", "click" : "street_house_main_yard_environment", "actions" : "lt", "zorder":10, "b":0.15, "icon_t":"/Icons/talk" + res.suffix +".png"})

    $ add_object_to_scene("Teleport_House", {"type":3, "text" : _("В ДОМ"), "rarrow" : "arrow_up_2", "base":"Street_House_Teleport_House", "click" : "street_house_main_yard_teleport", "xpos" : 1683, "ypos" : 858, "zorder":11, "b":-0.05, "tint":[1.0, 1.0, 0.85], "teleport":True})

    $ add_object_to_scene("Bardie", {"type" : 2, "base" : "Street_House_Bardie[day_suffix]", "click" : "bardieInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png", "active":False})

    $ add_object_to_scene("Teleport_Fence", {"type":3, "text" : _("К ЗАБОРУ"), "larrow" : "arrow_left_2", "base":"Street_House_Teleport_Fence", "click" : "street_house_main_yard_teleport", "xpos" : 758, "ypos" : 154, "zorder":11, "b":0.15, "tint":[1.0, 1.0, 0.9], "active":False})

    $ add_object_to_scene("Teleport_Gate", {"type":3, "text" : _("К ВОРОТАМ"), "larrow" : "arrow_left_2", "base":"Street_House_Teleport_Gate", "click" : "street_house_main_yard_teleport", "xpos" : 433, "ypos" : 660, "zorder":11, "b":0.15, "tint":[1.0, 1.0, 0.85], "teleport":True})


    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_house_main_yard_teleport:
    if obj_name == "Teleport_Fence":
        call change_scene("street_house_fence", "Fade", "highheels_run2")
        return
    if obj_name == "Teleport_Gate":
        call change_scene("street_house_gate", "Fade", "highheels_run2")
        return
    if obj_name == "Teleport_House":
#        music casualMusic
        call change_scene("floor1", "Fade_long", "highheels_run2")
        return
    return
label street_house_main_yard_environment:
    if obj_name == "Car":
        mt "Моя бывшая машина..."
        "Но я верну все назад, клянусь!"
        "Я устроим им всем АД!!!"
        return
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            mt "Фред... Мой бывший водитель..."
            "Редкий ублюдок..."
            "Он не избежит своей участи!"
            return
        if obj_data["action"] == "t":
            mt "Мне не о чем разговаривать с ним!!!"
            return
    if obj_name == "Monica":
        mt "(хмык)"
        return
    return

















#
