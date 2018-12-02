label street_steve_office:

    $ print "enter_street_steve_office"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_Steve_Office[day_suffix]"
    return

label street_steve_office_init:
    $ add_object_to_scene("Teleport_Building", {"type":2, "base":"Street_Steve_Office_Building", "click" : "street_steve_office_teleport", "actions" : "lw", "zorder" : 1, "b":0.05})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_steve_office_teleport:
    if obj_name == "Teleport_Building":
        if obj_data["action"] == "l":
            m "Неплохо устроился Стив!"
            "НА МОИ ДЕНЬГИ!!!"
        if obj_data["action"] == "w":
            if day_time == "evening":
                mt "Уже вечер. Офис Стива закрыт."
                return
            mt "Стив урод."
            "Я разберусь с ним позже."
            "Сейчас мне не до того..."
            return
            call change_scene("steve_office_secretary", "Fade_long", "snd_lift")
            return
    return
label street_steve_office_environment:

    return
