default melanie_control_active = False

label ep29_quests_melanie_control1_init:
    # Переход управления на Мелани
    $ remove_hook(label="change_owner_default_hook")
    $ add_hook("change_owner", "change_owner_default", scene="global", label="change_owner_default_hook")

    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Dick_Entrance_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="dick_office_entrance")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Dick_Hall1_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="dick_office_hall1")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Dick_Secretary_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="dick_office_secretary")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Entrance_Monica_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="monica_office_entrance")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Monica_Cabinet_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="monica_office_cabinet")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Monica_Cabinet_Table_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="monica_office_cabinet_table")
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "Office_Monica_MakeupRoom_Melanie[makeupRoomMelanieSuffix]", "click" : "monica_office_photostudio_environment", "actions" : "lt", "zorder":10, "active":False}, {"melanie_control_active":{"v":True, "base":"Office_Monica_MakeupRoom_Melanie_[melanie_cloth]", "actions" : "l"}}, scene="monica_office_makeup_room")
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Melanie[photostudioMelanieSuffix]", "click" : "monica_office_photostudio_environment", "actions" : "lt", "zorder":10}, {"melanie_control_active":{"v":True, "base":"Office_Monica_PhotoStudio_Melanie_[melanie_cloth]", "actions" : "l"}}, scene="monica_office_photostudio")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Monica_Secretary_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="monica_office_secretary")
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "WorkingOffice_Melanie_[melanie_cloth]", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":10}, scene="working_office")
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "WorkingOfficeCabinet_Melanie_[melanie_cloth]", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":10}, scene="working_office_cabinet")

    $ set_active("Melanie", True, scene="World", recursive=True)

    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="dick_office_entrance", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="dick_office_hall1", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="dick_office_secretary", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="monica_office_entrance", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="monica_office_cabinet", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="monica_office_cabinet_table", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="monica_office_makeup_room", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="monica_office_photostudio", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="monica_office_secretary", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="working_office", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="working_office_cabinet", owner="Melanie", label="melanie_play_interact")

    # хождение
    $ add_hook("Teleport_Monica_Office_Photostudio", "ep29_quests_melanie_teleport_photostudio", scene="monica_office_makeup_room", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_MakeupRoom", "ep29_quests_melanie_teleport_makeuproom", scene="monica_office_photostudio", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Secretary", "ep29_quests_melanie_teleport_secretary", scene="monica_office_photostudio", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Photostudio", "ep29_quests_melanie_teleport_photostudio", scene="monica_office_secretary", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep29_quests_melanie_teleport_monica_cabinet", scene="monica_office_secretary", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Entrance", "ep29_quests_melanie_teleport_lift", scene="monica_office_secretary", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Secretary", "ep29_quests_melanie_teleport_secretary", scene="monica_office_cabinet", owner="Melanie", label="melanie_teleports")
    $ add_hook("Biff", "ep29_quests_melanie_teleport_monica_cabinet_table", scene="monica_office_cabinet", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Secretary", "ep29_quests_melanie_teleport_secretary", scene="monica_office_cabinet_table", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Lift", "ep29_quests_melanie_teleport_lift", scene="working_office", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_WorkingOffice2", "ep29_quests_melanie_teleport_melanie_workingoffice2", scene="working_office", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Cabinet", "ep29_quests_melanie_teleport_melanie_workingoffice_cabinet", scene="working_office", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Cabinet", "ep29_quests_melanie_teleport_melanie_workingoffice_cabinet", scene="working_office2", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_WorkingOffice", "ep29_quests_melanie_teleport_melanie_workingoffice", scene="working_office2", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_WorkingOffice", "ep29_quests_melanie_teleport_melanie_workingoffice", scene="working_office_cabinet", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Secretary", "ep29_quests_melanie_teleport_lift", scene="monica_office_entrance", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Street_Monica_Office", "ep29_quests_melanie_teleport_monica_office_street", scene="monica_office_entrance", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Inside", "ep29_quests_melanie_teleport_monica_office_entrance", scene="street_monica_office", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Inside", "ep29_quests_melanie_teleport_dick_office_entrance", scene="street_dick_office", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Street", "ep29_quests_melanie_teleport_dick_office_street", scene="dick_office_entrance", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Inside", "ep29_quests_melanie_teleport_dick_office_hall1", scene="dick_office_entrance", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Entrance", "ep29_quests_melanie_teleport_dick_office_entrance2", scene="dick_office_hall1", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Secretary", "ep29_quests_melanie_teleport_dick_secretary", scene="dick_office_hall1", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Hall", "ep29_quests_melanie_teleport_dick_office_hall1b", scene="dick_office_secretary", owner="Melanie", label="melanie_teleports")


    call change_owner("Melanie")
    $ map_objects = {
            "Teleport_Monica_Office" : {"text" : _("ОФИС МОНИКИ"), "xpos" : 882, "ypos" : 320, "base" : "map_marker", "state" : "visible", "owner":"Melanie"},
            "Teleport_Dick_Office" : {"text" : _("ОФИС ДИКА"), "xpos" : 1370, "ypos" : 127, "base" : "map_marker", "state" : "visible", "owner":"Melanie"},
            "Teleport_Melanie_Home" : {"text" : _("АПАРТАМЕНТЫ МЕЛАНИ"), "xpos" : 1726, "ypos" : 791, "base" : "map_marker", "state" : "visible", "owner":"Melanie"}
    }
    $ hudDaySkipToEveningEnabled = False
    $ miniMapTurnedOff = True # выключаем minimap
    call change_scene("monica_office_makeup_room", "Fade_long", False)
#    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f"
    return


label ep29_quests_melanie_teleport_photostudio:
    call change_scene("monica_office_photostudio")
    return False

label ep29_quests_melanie_teleport_makeuproom:
    call change_scene("monica_office_makeup_room")
    return False

label ep29_quests_melanie_teleport_secretary:
    call change_scene("monica_office_secretary")
    return False

label ep29_quests_melanie_teleport_monica_cabinet:
    call change_scene("monica_office_cabinet")
    return False

label ep29_quests_melanie_teleport_lift:
    menu:
        "Модный Журнал.":
            call change_scene("monica_office_secretary", "Fade_long", "snd_lift")
        "Офисы.":
            call change_scene("working_office", "Fade_long", "snd_lift")
        "Вестибюль.":
            call change_scene("monica_office_entrance", "Fade_long", "snd_lift")
    return False


label ep29_quests_melanie_teleport_monica_cabinet_table:
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1o()
        return False
    call change_scene("monica_office_cabinet_table")
    return False

label ep29_quests_melanie_teleport_melanie_workingoffice:
    call change_scene("working_office")
    return False

label ep29_quests_melanie_teleport_melanie_workingoffice2:
    call change_scene("working_office2")
    return False

label ep29_quests_melanie_teleport_melanie_workingoffice_cabinet:
    call change_scene("working_office_cabinet", "Fade_long", "snd_door_open1")
    return False


label ep29_quests_melanie_teleport_monica_office_street:
    call change_scene("street_monica_office", "Fade_long")
    return False

label ep29_quests_melanie_teleport_monica_office_entrance:
    call change_scene("monica_office_entrance", "Fade_long")
    return False

label ep29_quests_melanie_teleport_dick_office_entrance:
    call change_scene("dick_office_entrance", "Fade_long")
    return False

label ep29_quests_melanie_teleport_dick_office_entrance2:
    call change_scene("dick_office_entrance", "Fade_long", "snd_lift")
    return False

label ep29_quests_melanie_teleport_dick_office_street:
    call change_scene("street_dick_office", "Fade_long")
    return False

label ep29_quests_melanie_teleport_dick_office_hall1:
    call change_scene("dick_office_hall1", "Fade_long", "snd_lift")
    return False

label ep29_quests_melanie_teleport_dick_office_hall1b:
    call change_scene("dick_office_hall1")
    return False

label ep29_quests_melanie_teleport_dick_secretary:
    call change_scene("dick_office_secretary")
    return False






#
