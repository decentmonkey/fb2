default monicaOfficeBeefMelanie = True

label monica_office_cabinet:
    $ print "enter_monica_office_cabinet"
    $ miniMapData = []

    if monicaOfficeWhiskeyOnTable == False:
        $ scene_image = "scene_Office_Monica_Cabinet[day_suffix]"
    else:
        $ scene_image = "scene_Office_Monica_Cabinet_Whiskey[day_suffix]"

    if monicaOfficeBeefMelanie == True:
        $ scene_image = "scene_Office_Monica_Cabinet_Beef_Melanie_Monica_Whore_Evening"

    return

label monica_office_cabinet_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_Cabinet_Monica_[cloth]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Beef", {"type" : 2, "base" : "Office_Monica_Cabinet_Beef[day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":5}, {"monicaOfficeBeefMelanie":{"v":True, "base" : "Office_Monica_Cabinet_Beef_Melanie_Monica_Beef[day_suffix]"}})
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "Office_Monica_Cabinet_Beef_Melanie_monica_Melanie[day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":6, "active":False})

    $ add_object_to_scene("Flowers", {"type" : 2, "base" : "Office_Monica_Cabinet_Flowers", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Paints", {"type" : 2, "base" : "Office_Monica_Cabinet_Paints", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Table", {"type" : 2, "base" : "Office_Monica_Cabinet_Table", "click" : "monica_office_cabinet_environment", "actions" : "lw", "zorder":1, "group":"environment"})
    $ add_object_to_scene("Windows", {"type" : 2, "base" : "Office_Monica_Cabinet_Windows", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Projector", {"type" : 2, "base" : "Office_Monica_Cabinet_Projector", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":0, "group":"environment"})

    $ add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : _("К СЕКРЕТАРЮ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monica_office_cabinet_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_cabinet_teleport:
    if obj_name == "Teleport_Monica_Office_Secretary":
        call change_scene("monica_office_secretary")
        return
    return
label monica_office_cabinet_environment:
    if obj_name == "Beef":
        return
    if obj_name == "Melanie":
        return
    if obj_name == "Monica":
        m "Мой... Офис..."
    if obj_name == "Projector":
        return

    if obj_name == "Flowers":
        return
    if obj_name == "Paints":
        return
    if obj_name == "Windows":
        return
    if obj_name == "Table":
        if obj_data["action"] == "l":
            m "Мой... Стол..."
        if obj_data["action"] == "w":
            call change_scene("monica_office_cabinet_table")
            return
    return








#
