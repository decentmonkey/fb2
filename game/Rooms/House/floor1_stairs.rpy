default floor1_stairs_Teleport_Basement_Pool_offset = False

label floor1_stairs:
    $ print "enter_floor1_stairs"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_image = "scene_Floor1_Stairs[day_suffix]"

    $ floor1_stairs_Teleport_Basement_Pool_offset = False
    if get_active_objects("Bardie") != False:
        $ floor1_stairs_Teleport_Basement_Pool_offset = True

    return

label floor1_stairs_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Floor1_Stairs_Monica_[cloth]", "click" : "floor1_stairs_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
    $ add_object_to_scene("Bardie", {"type" : 2, "base" : "Floor1_Stairs_Bardie[day_suffix]", "click" : "bardieInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png", "active":False})

    $ add_object_to_scene("Flower", {"type":2, "base":"Floor1_Stairs_Flower", "click" : "floor1_stairs_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Furniture", {"type":2, "base":"Floor1_Stairs_Furniture", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Floor1_Stairs_Lamps", "click" : "floor2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Basement_Pool", {"type":3, "text" : _("ЛЕСТНИЦА В ПОДВАЛ"), "rarrow" : "arrow_down_2", "base":"Floor1_Stairs_StairsDown", "click" : "floor1_stairs_teleport", "xpos" : 635, "ypos" : 365, "zorder":9, "teleport":True}, {"floor1_stairs_Teleport_Basement_Pool_offset":{"v":True, "xpos" : 535, "ypos" : 365}})

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : _("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "floor1_stairs_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Floor2_Stairs", {"type":3, "text" : _("ЛЕСТНИЦА ВВЕРХ"), "rarrow" : "arrow_up_2", "base":"Floor1_Stairs_StairsUp", "click" : "floor1_stairs_teleport", "xpos" : 857, "ypos" : 250, "zorder":9, "teleport":True}, {"floor1_stairs_Teleport_Basement_Pool_offset":{"v":True, "xpos" : 857, "ypos" : 240}})
    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label floor1_stairs_teleport:
    if obj_name == "Teleport_Floor2_Stairs":
        call change_scene("floor2_stairs", "Fade_long", "highheels_run2")
        return
    if obj_name == "Teleport_Basement_Pool":
        call change_scene("basement_pool")
        return
    if obj_name == "Teleport_Floor1":
        call change_scene("floor1")
        return
    return

label floor1_stairs_environment:
    if obj_name == "Monica":
        mt "Они ничего не собираются делать с лестницей."
        "Конечно, с какой стати им что-то делать с ней?"
        "У них, очевидно, нет такого вкуса как у меня!"
        "Они счастливы жить в том что создала Я!!!"
        "ЭТО НЕСПРАВЕДЛИВО!!!"
        return

    if obj_name == "Flower":
        mt "Это мои цветы!"
        "МОИ!!!"
        return
    return
