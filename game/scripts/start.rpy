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
default storedMusic = False
default day_time = "day"

label start:
#    jump credits
    $ debugMode = True

    $ cloth_type = "Whore"
    $ cloth = "Whore"

    $ gameStage = 0
    $ gameSubStage = 0
    $ afterJail = True
    $ rain = False
    $ sceneIsStreet = False

    $ game_version1_screen_ready_to_render = True
    $ zoom_factor = 1

    $ day_time = "evening"
    $ day_suffix = "_Evening"
    $ day = 1
    $ week_day = (day-1)%7
    $ money = 0.0
    $ scenes_data = {"objects": {}, "substs" : {}, "autorun": {}, "hooks": {}}
    $ hooks_stack = []
    $ inventory_objects = {}
    $ inventory = []

    $ hud_preset_current = "default"
    $ bitchmeterValue = 280

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

    $ add_hook("exit_scene", "hook_basement_bedroom2_change_view_to_suffix3", scene="basement_bedroom2")

    call change_scene("basement_bedroom2")

    $ scene_transition = "Fade_long"
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
