default debugMode = False

default gameStage = 0
default gameSubStage = 0
default afterJail = False
default rain = False
default rainIntencity = 0
default lightning = False
default sceneIsStreet = False
default objectives_list = []
default currentMusic = False
default storedMusic = []
default day_time = "day"
default episode = 1

label start:
    #new game
    $ episode = 2
    $ debugMode = True

    $ cloth_type = "Nude"
    $ cloth = "Nude"
    $ bitchmeterValue = 280
    $ scenes_data = {"objects": {}, "substs" : {}, "autorun": {}, "hooks": {}}
    $ hooks_stack = []
    $ inventory_objects = {}
    $ inventory = []

#    call intro_questions()
    call start_game()
    return

label start_saved_game:
    $ episode = 2
    $ scenes_data = {"objects": {}, "substs" : {}, "autorun": {}, "hooks": {}}
    $ hooks_stack = []
    $ inventory_objects = {}
    $ inventory = []
    call start_game()
    return

label start_game:
    $ gameStage = 0
    $ gameSubStage = 0
    $ afterJail = True
    $ rain = False
    $ sceneIsStreet = False

    $ game_version1_screen_ready_to_render = True
    $ zoom_factor = 1

    $ day = 10
    $ week_day = (day)%7
    $ day_time = "day"
    $ day_suffix = ""
    $ money = 0.0

    $ hud_preset_current = "default"

    call game_init()
#    python:
#        for i in renpy.exports.get_image_load_log():
#            print i

    $ map_objects = {
            "Teleport_Monica_Office" : {"text" : _("ОФИС МОНИКИ"), "xpos" : 882, "ypos" : 320, "base" : "map_marker", "state" : "visible"},
            "Teleport_Street_Corner" : {"text" : _("УГОЛ УЛИЦЫ"), "xpos" : 124, "ypos" : 476, "base" : "map_marker", "state" : "visible"},
            "Teleport_Dick_Office" : {"text" : _("ОФИС ДИКА"), "xpos" : 1370, "ypos" : 127, "base" : "map_marker", "state" : "visible"},
            "Teleport_Gas_Station" : {"text" : _("ЗАПРАВКА"), "xpos" : 1125, "ypos" : 910, "base" : "map_marker", "state" : "visible"},
            "Teleport_Police" : {"text" : _("ПОЛИЦИЯ"), "xpos" : 912, "ypos" : 809, "base" : "map_marker", "state" : "visible"},
            "Teleport_Rich_Hotel" : {"text" : _("ОТЕЛЬ ЛЯ ГРАНД"), "xpos" : 1782, "ypos" : 593, "base" : "map_marker", "state" : "visible"},
            "Teleport_Fitness" : {"text" : _("ФИТНЕСС"), "xpos" : 356, "ypos" : 411, "base" : "map_marker", "state" : "visible"},
            "Teleport_Steve_Office" : {"text" : _("ОФИС СТИВА"), "xpos" : 1333, "ypos" : 724, "base" : "map_marker", "state" : "visible"},
            "Teleport_Bank" : {"text" : _("БАНК"), "xpos" : 1212, "ypos" : 439, "base" : "map_marker", "state" : "visible"},
            "Teleport_Cloth_Shop" : {"text" : _("МАГАЗИН ОДЕЖДЫ"), "xpos" : 340, "ypos" : 901, "base" : "map_marker", "state" : "visible"},
            "Teleport_Street_Corner" : {"text" : _("УГОЛ УЛИЦЫ"), "xpos" : 88, "ypos" : 942, "base" : "map_marker", "state" : "visible"},
            "Teleport_Hostel2" : {"text" : _("ГРЯЗНАЯ УЛИЦА"), "xpos" : 259, "ypos" : 1046, "base" : "map_marker", "state" : "visible"},
            "Teleport_House" : {"text" : _("ДОМ МОНИКИ"), "xpos" : 95, "ypos" : 798, "base" : "map_marker_house", "state" : "active"}
    }
#mousedown_3, hide_windows
#    $ print(config.keymap["game_menu"])
#    $ config.keymap["hide_windows"] = []
#    $ print(config.keymap)
#    pause

    $ bFredFollowingMonica = False

    $ scene_refresh_flag = True
    $ map_scene = "House"
    $ map_enabled = True
    $ map_disabled_forced = False
    $ scene_name = "none"
    $ api_scene_name = "none"
    call locations_init()
    call citizens_init()

    $ add_hook("exit_scene", "hook_basement_bedroom2_change_view_to_suffix3", scene="basement_bedroom2")
    # Запрет Бетти ходить по дому
    $ add_hook("enter_scene", "afterJailHouse_dialogue10", scene="bathroom_bath", label="betty_forbidden")
    $ add_hook("enter_scene", "afterJailHouse_dialogue15", scene="kitchen", label="betty_forbidden")
    $ add_hook("enter_scene", "afterJailHouse_dialogue15b", scene="kitchen2", label="betty_forbidden")
    $ add_hook("enter_scene", "afterJailHouse_dialogue16a", scene="bedroom2", label="betty_forbidden")

    # Проверка одежды при хождении по дому и покидании его
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom1")
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom2")
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom_cupboard")
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom_table")
    $ add_hook("map_teleport", "hook_basement_bedroom_check_exit_cloth_map", scene="global")
    $ add_hook("Gates", "hook_basement_bedroom_check_exit_cloth_gates", scene="street_house_gate")

    # Жизнь персонажей
    $ add_hook("change_time_day", "citizens_init_day", scene="global")
    $ add_hook("change_time_evening", "citizens_init_evening", scene="global")
    $ add_hook("change_time_day", "Beef_Life_day", scene="global")
    $ add_hook("change_time_evening", "Beef_Life_evening", scene="global")
    $ add_hook("change_time_day", "Bardie_Life_day", scene="global")
    $ add_hook("change_time_evening", "Bardie_Life_evening", scene="global")
    $ add_hook("change_time_day", "Betty_Life_day", scene="global")
    $ add_hook("change_time_evening", "Betty_Life_evening", scene="global")
    $ add_hook("change_time_day", "Ralph_Life_day", scene="global")
    $ add_hook("change_time_evening", "Ralph_Life_evening", scene="global")
    $ add_hook("change_time_day", "Fred_Life_day", scene="global")
    $ add_hook("change_time_evening", "Fred_Life_evening", scene="global")

    # Уборка в доме
    $ add_hook("enter_scene", "house_cleaning", scene="floor1")
    $ add_hook("enter_scene", "house_cleaning", scene="floor2")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom_bardie")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom_second")
    $ add_hook("enter_scene", "house_cleaning", scene="living_room")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom1")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom2")
    $ add_hook("monica_cleaning_start", "Bardie_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Bardie_Life_Monica_Cleaning_End", scene="global")
    $ add_hook("monica_cleaning_start", "Betty_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Betty_Life_Monica_Cleaning_End", scene="global")
    $ add_hook("monica_cleaning_start", "Ralph_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Ralph_Life_Monica_Cleaning_End", scene="global")
    $ add_hook("monica_cleaning_start", "Fred_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Fred_Life_Monica_Cleaning_End", scene="global")
    # Офис Моники
    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue4a", scene="monica_office_secretary")


#    $ remove_hook(label="betty_forbidden", scene="House", recursive=True)
    call change_scene("basement_bedroom2", "Fade_long", False)

    $ scene_transition = "Fade_long"

#    $ changeDayTime("evening")
#    $ scene_data = process_scene_objects_list(scene_name) #парсим содержимое свойств объектов перед выводом
#    $ print scene_data

#    $ renpy.pause(100, hard=True)

#    $ autorun_to_object("intro_scene", "intro_scene_start")
    music stop

    jump show_scene

label start_new_game:
    music casualMusic
#    $ map_enabled = True
#    $ add_objective("dress_homecloth", _("Одеть домашнюю одежду"), c_blue, 0)

#    $ miniMapDisabled = ["Basement"]


#    $ add_inventory("phone", 1, True)
    return

label empty_label:
    return























#
