default monicaOfficeWhiskeyOnTable = False

label monica_office_cabinet_table:
    $ print "enter_monica_office_cabinet_table"
    $ miniMapData = []

    if monicaOfficeWhiskeyOnTable == False:
        $ scene_image = "scene_Office_Monica_Cabinet_Table[day_suffix]"
    else:
        $ scene_image = "scene_Office_Monica_Cabinet_Table_Whiskey[day_suffix]"
    return

label monica_office_cabinet_table_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Monica_[cloth][day_suffix]", "click" : "monica_office_cabinet_table_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Beef", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Beef[day_suffix]", "click" : "monica_office_cabinet_table_environment", "actions" : "lt", "zorder":10})

    $ add_object_to_scene("Flowers", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Flowers", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":2, "group":"environment"})
    $ add_object_to_scene("Paints", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Paints", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":2, "group":"environment"})
#    $ add_object_to_scene("Water", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Water[day_suffix]", "click" : "monica_office_cabinet_table_environment", "actions" : "l", "zorder":2, "group":"environment"})
#    $ add_object_to_scene("Whiskey", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Whiskey[day_suffix]", "click" : "monica_office_cabinet_table_environment", "actions" : "l", "zorder":2, "group":"environment"})

    $ add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : _("К СЕКРЕТАРЮ"), "larrow" : "arrow_left_2", "base":"Office_Monica_Cabinet_Table_Exit", "click" : "monica_office_cabinet_table_teleport", "xpos" : 723, "ypos" : 166, "zorder":11, "b":0.15, "tint":[1.0, 1.0, 0.85], "teleport":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_cabinet_table_teleport:
    if obj_name == "Teleport_Monica_Office_Secretary":
        call change_scene("monica_office_secretary")
        return
    return
label monica_office_cabinet_table_environment:
    if obj_name == "Beef":
        return
    if obj_name == "Monica":
        return
    if obj_name == "Journal":
        return

    if obj_name == "Water":
        return

    return


#
