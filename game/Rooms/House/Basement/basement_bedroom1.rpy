default basementBedroom1MonicaSuffix = 2

label basement_bedroom1:
    $ print "enter_basement_bedroom1"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_image = "scene_basement_bedroom1"

    $ basementHoleIncomingDirection = "Bedroom"
    return

label basement_bedroom1_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[cloth]_[basementBedroom1MonicaSuffix]", "click" : "basement_bedroom1_environment", "actions" : "l", "zorder":10, "tint": [1.0, 1.0, 0.9]})

    $ add_object_to_scene("Cupboard", {"type":2, "base":"Basement_Bedroom1_Cupboard", "click" : "basement_bedroom1_environment", "actions" : "lw", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("BasementWardrobe", {"type":2, "base":"Basement_Bedroom1_Wardrobe", "click" : "basement_bedroom1_environment", "actions" : "lh", "zorder" : 0})
    $ add_object_to_scene("Picture1", {"type":2, "base":"basement_bedroom1_Picture1", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Picture2", {"type":2, "base":"basement_bedroom1_Picture2", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Picture3", {"type":2, "base":"basement_bedroom1_Picture3", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Picture4", {"type":2, "base":"basement_bedroom1_Picture4", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Picture5", {"type":2, "base":"basement_bedroom1_Picture5", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Picture6", {"type":2, "base":"basement_bedroom1_Picture6", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Picture7", {"type":2, "base":"basement_bedroom1_Picture7", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Table", {"type":2, "base":"basement_bedroom1_Table", "click" : "basement_bedroom1_environment", "actions" : "lw", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Basement_Hole", {"type":3, "text" : _("КОРИДОР"), "larrow" : "arrow_left_2", "base":"Basement_Bedroom1_Teleport_Hole", "click" : "basement_bedroom1_teleport", "xpos" : 459, "ypos" : 877, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Basement_Bedroom2", {"type":3, "text" : _("КРОВАТЬ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_bedroom1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover":True})

    return

label basement_bedroom1_teleport:
    if obj_name == "Teleport_Basement_Hole":
        call change_scene("basement_hole")
        return
    if obj_name == "Teleport_Basement_Bedroom2":
        call change_scene("basement_bedroom2")
        return
    return

label basement_bedroom1_environment:
    if obj_name == "BasementWardrobe":
        if act == "l":
            mt "В этот старый шкаф можно повесить одежду..."
            "Если это можно назвать одеждой..."
        if act == "h":
            call wardrobeBasement()
            return
        return

    if obj_name == "Monica":
        mt "Здесь я теперь сплю..."
        "(хмык)"
        "Но это временно!!!"
        "Это какое-то недоразуменее, которое скоро разрешится!"

    if obj_name == "Cupboard":
        if act == "l":
            mt "Старый шкаф..."
        if act == "w":
            $ basementBedroom2CupboardReturnScene = "basement_bedroom1"
            call change_scene("basement_bedroom2_cupboard")
            return

    if obj_name == "Picture1" or obj_name == "Picture2" or obj_name == "Picture3" or obj_name == "Picture4" or obj_name == "Picture5" or obj_name == "Picture6" or obj_name == "Picture7" or obj_name == "Picture8" or obj_name == "Picture9":
        mt "Живопись..."
        "Я не знала что Юлия увлекается этим."
        "Она пыталась быть похожей на меня?"
        "..."
    if obj_name == "Table":
        if act == "l":
            mt "Этот старый яркий пестрый стол пытается скрасить уныние этой каморки..."
            "Тщетно..."
        if act == "w":
            call change_scene("basement_bedroom_table")
            return
    return
