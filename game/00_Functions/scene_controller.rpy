default pause_enter = 0
default pause_exit = 0
default sceneStages = []
default lastSceneName = False
default refreshed_scene_name = False
default game_version1_screen_ready_to_render = False
default scene_caption = ""
default exitHookCalled = False

label show_scene:
    $ exitHookCalled = False
    $ show_scene_loop_flag = False
    if scene_refresh_flag == False:
        jump show_scene_loop
    $ hide_screens_for_scene()
#    if dialogue_active_flag == True:
#        $ renpy.show_screen("dialogue_down_arrow")
#        $ renpy.pause()
#        $ renpy.hide_screen("dialogue_down_arrow")

label show_scene_now:
    if define_version_current != define_version:
        call define_autorun() from _call_define_autorun
#    $ print "pause_enter"
#    $ print pause_enter
#    $ print "pause_exit"
#    $ print pause_exit
    if rain != True or sceneIsStreet != True:
        hide screen Rain

    $ interface_blocked_flag = True
    $ list_files_scene_drop_flag = False
    if scene_sound != False:
        $ sound_to_play = get_filename(scene_sound)
        play sound sound_to_play
        $ scene_sound = False
    $ print "Bitchiness"
    $ print bitchmeterValue
    hide screen sprites_hover_dummy_screen

#    window hide
#    window show
    $ config.keymap["hide_windows"] = []
#    config.keymap["hide_windows"] = ["mouseup_3", "mouseup_2", "h"]

    if scene_transition != False and gui.scenes_transitions == True:
#        $ _dismiss_pause = False
        if scene_transition == "Fade" or scene_transition == "Fade_fast":
            if refreshed_scene_name == scene_name and scene_transition != "Fade_fast":
                scene black_screen at convert_resolution_transform
                with Dissolve(0.2)
#                $ renpy.pause(0.2, hard=True)
            else:
                scene black_screen at convert_resolution_transform
                with Dissolve(0.1)
    #            $ renpy.pause(0.2, hard=True)
        if scene_transition == "Fade_long":
            scene black_screen at convert_resolution_transform
            with Dissolve(0.7)
#            $ renpy.pause(0.7, hard=True)
#        $ _dismiss_pause = True

    $ renpy.scene()
    $ scene_image_file = get_image_filename(parse_str(scene_image), True)
    $ scene_refresh_flag = False
    show screen show_image_screen(scene_image_file)
    $ image_screen_scene_flag = True
    call map_street_scene_visibility_check() from _call_map_street_scene_visibility_check
    show screen hud_screen(hud_presets[hud_preset_current])
    show screen hud_minimap(miniMapData)
    if rain == True and sceneIsStreet == True:
        show screen Rain
        stop music fadeout 1.0

    define idle_len = 0.0
    $ parse_transition_flag = True
    $ interface_blocked_flag = False

    $ makeDump()
    $ scene_data = process_scene_objects_list(scene_name) #парсим содержимое свойств объектов перед выводом
    $ scene_data = process_character_info_buttons(scene_data) #добавляем кнопки info для персонажей со свойствами
    show screen screen_sprites(scene_data)
    if parse_transition_flag == True:
#        $ _dismiss_pause = False
        if scene_transition != False and gui.scenes_transitions == True:
            if scene_transition == "Fade":
                if refreshed_scene_name == scene_name:
                    with Dissolve(0.2)
                else:
                    with Dissolve(0.1)
            if scene_transition == "Fade_long":
                with Dissolve(0.7)
            if scene_transition == "Dissolve_fast":
                with Dissolve(0.3)
            if scene_transition == "Dissolve_05":
                with Dissolve(0.5)
            if scene_transition == "Dissolve_07":
                with Dissolve(0.7)
            if scene_transition == "Dissolve_10":
                with Dissolve(1.0)
#        $ _dismiss_pause = True
    $ scene_transition = False

    if refreshed_scene_name != scene_name:
        $ refreshed_scene_name = scene_name
        call process_hooks("enter_scene", scene_name) from _call_process_hooks_13 #хук вызывается после входа на сцену и отрисовки (как autorun)
        call remove_dialogue() from _call_remove_dialogue_2
    if scene_refresh_flag == True:
        jump show_scene

    if scenes_data["autorun"].has_key(scene_name) and scenes_data["autorun"][scene_name].has_key("scene"):
        $ autorunFunc = scenes_data["autorun"][scene_name]["scene"]
        $ del scenes_data["autorun"][scene_name]["scene"]
        show screen sprites_hover_dummy_screen()
        call expression autorunFunc from _call_expression_6
#        hide screen sprites_hover_dummy_screen
        $ scene_refresh_flag = True
        jump show_scene



label show_scene_loop:
    $ pause_enter += 1
    pause
    $ pause_exit += 1
    if show_scene_loop_flag == False:
        jump show_scene_loop
    else:
        jump show_scene


label change_scene(new_scene_name, in_transition_name="Fade", in_sound_name="highheels_short_walk"):
    $ target_scene_name = new_scene_name
    $ target_scene_parent = scene_get_parent(target_scene_name)
    $ _return = None
    if exitHookCalled == False:
        call process_hooks("exit_scene", scene_name) from _call_process_hooks_14 #хук выхода со сцены
        $ exitHookCalled = False
    if _return == False: #Если False, то прерываем смену сцены
        return
    if scenes_data["objects"].has_key(new_scene_name) == False or scenes_data["objects"][new_scene_name].has_key("data") == False:
        $ notif ("No scene found! : " + new_scene_name)
        $ makeDump()
        return
    $ sceneIsStreet = False
    $ scene_transition = in_transition_name
    $ scene_sound = in_sound_name
    $ scene_refresh_flag = True
#    $ scene_label = get_scene_label(scene_label)
    $ lastSceneName = scene_name
    $ scene_name = new_scene_name
    $ refreshed_scene_name = False
    $ scene_caption = scenes_data["objects"][scene_name]["data"]["caption"]
    $ scene_label = scenes_data["objects"][scene_name]["data"]["label"]
    $ api_scene_name = new_scene_name

    call process_hooks("before_open", scene_name) from _call_process_hooks_15 #хук до инициализации сцены
    call expression scene_label from _call_expression_7
    call process_hooks("open", scene_name) from _call_process_hooks_16 #хук сразу после инициализации сцены
    return

label refresh_scene(fade_param = False):
    if fade_param != False:
        $ scene_transition = fade_param

    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    $ lastSceneName = scene_name
    call expression scene_name from _call_expression_8
    return

label refresh_scene_fade():
    $ scene_transition = "Fade"
    $ lastSceneName = scene_name
    call refresh_scene() from _call_refresh_scene
    return
label refresh_scene_fade_long():
    $ scene_transition = "Fade_long"
    $ lastSceneName = scene_name
    call refresh_scene() from _call_refresh_scene_1
    return

label remove_dialogue():
    python:
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        dialogue_active_flag = False
    return


label after_load():
    $ refresh_list_files_forced()
    if episode < 2:
        call start_saved_game() from _call_start_saved_game
        return
    if game_version1_screen_ready_to_render == False:
        $ game_version1_screen_ready_to_render = True
        call refresh_scene() from _call_refresh_scene_2
    $ imagesSizesCache = {}
    $ scene_refresh_flag = True #???
    $ show_scene_loop_flag = True
    call run_after_load()
    jump show_scene
#    return

label call_save():
    if interface_blocked_flag == True:
        return
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    call screen save()
    return
    return
