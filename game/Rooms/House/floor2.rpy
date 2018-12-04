default floor2BettyPositionSuffix = 0

label floor2:
    $ print "enter_floor2"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_image = "scene_Floor2_Evening"

    $ floor2BettyPositionSuffix = str(renpy.random.randint(1,3))
    return

label floor2_init:
    $ monica_tint = [1.0, 1.0, 1.0]

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Monica_[cloth][day_suffix]", "click" : "floor2_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, {"bettyLocation": {"v":"floor2", "base" : "Floor2_Monica_[cloth]_Evening"}, "monicaCleaningInProgress":{"v":True, "base":"Floor2_Monica_[cloth]_Cleaning_[monicaCleaningObject]"}})
    $ add_object_to_scene("Betty", {"type" : 2, "base" : "Floor2_Betty_[floor2BettyPositionSuffix]_Evening", "click" : "bettyInteract1", "actions" : "lt", "zorder":10})

    $ add_object_to_scene("Carpet", {"type" : 2, "active":False, "base" : "Floor2_Carpet", "click" : "floor2_environment", "actions" : "l", "zorder":10, "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "active":True}})
    $ add_object_to_scene("Sofa", {"type":2, "active":False, "base":"Floor2_Sofa", "click" : "floor2_environment", "actions" : "l", "zorder" : 0, "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "active":True}})

    $ add_object_to_scene("Spot", {"type" : 2, "base" : "Floor2_Spot", "click" : "floor2_environment", "actions" : "lh", "zorder":10, "group":"environment"}, {"monicaCleaningInProgress":{"v":True, "active":False}})

    $ add_object_to_scene("Teleport_BedroomBardie", {"type":3, "text" : _("КОМНАТА БАРДИ"), "larrow" : "arrow_left_2", "base":"Floor2_Teleport_BedroomBardie", "click" : "floor2_teleport", "xpos" : 341, "ypos" : 454, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_BedroomSecond", {"type":3, "text" : _("СПАЛЬНЯ ДЛЯ ГОСТЕЙ"), "larrow" : "arrow_left_2", "base":"Floor2_Teleport_BedroomSecond", "click" : "floor2_teleport", "xpos" : 420, "ypos" : 916, "zorder":15, "b":0.15, "tint":[1.0, 1.0, 0.9], "teleport":True})
    $ add_object_to_scene("Teleport_Bedroom", {"type":3, "text" : _("СПАЛЬНЯ ХОЗЯЕВ"), "larrow" : "arrow_down_2", "base":"Floor2_Teleport_Bedroom", "click" : "floor2_teleport", "xpos" : 1570, "ypos" : 1006, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Bathroom", {"type":3, "text" : _("ВАННАЯ КОМНАТА"), "larrow" : "arrow_left_2", "base":"Floor2_Bathroom", "click" : "floor2_teleport", "xpos" : 350, "ypos" : 250, "zorder":15, "b":0.15, "tint":[1.0, 1.0, 0.9], "teleport":True})
    $ add_object_to_scene("Teleport_Floor2_Stairs", {"type":3, "text" : _("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Floor2_Stairs_Object", "click" : "floor2_teleport", "xpos" : 1030, "ypos" : 58, "zorder":9, "teleport":True})
    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors_Object", "click" : "floor2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})


    $ add_object_to_scene("Flower1", {"type":2, "base":"Floor2_Flower1", "click" : "floor2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Flower2", {"type":2, "base":"Floor2_Flower2", "click" : "floor2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Floor2_Lamps", "click" : "floor2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

    return

label floor2_teleport:
    if obj_name == "Teleport_Floor2_Stairs":
        call change_scene("floor2_stairs")
    if obj_name == "Teleport_Bedroom":
        call change_scene("bedroom2")
    if obj_name == "Teleport_Bathroom":
        call change_scene("bathroom_bath")
    if obj_name == "Teleport_BedroomBardie":
        call change_scene("bedroom_bardie")
        return
    if obj_name == "Teleport_BedroomSecond":
        call change_scene("bedroom_second")
        return

    return

label floor2_environment:
    if name == "Lamps":
        mt "Мне всегда нравилось когда много света."
        "Ничего, скоро я снова буду радоваться этому!"
        return

    if name == "Flower1":
        mt "Это мои цветы!"
        "МОИ!!!"
        return
    if name == "Flower2":
        mt "Это мои цветы!"
        "МОИ!!!"
        return

    if name == "Mirrors":
        if obj_data["action"] == "l":
            mt "Это мои зеркала с косметикой..."
            "Сейчас их захватила эта сучка Бетти."
            "Но это ненадолго!"
            return

        if obj_data["action"] == "w":
            call change_scene("floor2_mirrors")
            return


    if name == "Monica":
        m "Они захватили мой дом, но я верну его!"
        return

    if name == "Spot":
        if obj_data["action"] == "l":
            mt "Пятно на ковре все еще здесь..."
            "Может быть эта Бетти не заметила его?"
            "Я уж точно не собираюсь его убирать!"
            "Этому ковру нужна химчистка!"
            return
        if act == "h":
            call spot_monica_comment1()
            return
    return
