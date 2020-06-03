default ep213_quests_julia_stage = 0
default monica_living_at_juliahome = False
default monica_juliahome_outside_cloth = False
default monica_juliahome_outside_cloth_type = False

default monica_juliahome_cloth = "JuliaCloth1"

default juliahome_evening_sleep_event_active = False
default juliahome_julia_shower_day = 0
default juliahome_work_action_day = 0
default juliahome_work_action_evening_day = 0
default julia_progress_list = [False, False, False, False, False, False, False, False, False, False, False]

label ep213_quests_julia1: # Моника предлагает Юлии жить вместе
    call ep213_dialogues5_julia_16()
    $ ep213_quests_julia_stage = 1
    $ ep210_julia_evening_at_work = False # Вечером Юлия не на работе (а дома)
    $ add_hook("JuliaHome", "ep213_quests_julia2", scene="street_juliahome", label="juliahome1")
    $ add_objective("come_julia_evening", t_("Прийти к Юлии домой вечером."), c_pink, 105)

    return

label ep213_quests_julia2: # Заходит вечером в дом
    if act=="l" or day_time != "evening":
        return
    $ remove_hook()
    call ep213_dialogues5_julia_7()
    # Инициализируем жизнь в доме
    python:
        remove_objective("come_julia_evening")
        ep213_quests_julia_stage = 2
        monica_living_at_juliahome = True
        ep210_julia_evening_at_work = True # Вечером Юлия на работе
        move_object("Julia", "juliahome_livingroom")
        set_var("Julia", base="JuliaHome_LivingRoom_Julia_[juliaHomeLivingRoomJuliaCloth]_[juliaHomeLivingRoomJuliaSuffix][day_suffix]", scene="juliahome_livingroom")
        set_var("Wardrobe", actions="lh", scene="juliahome_livingroom")
        set_var("Bed1", actions="lh", scene="juliahome_livingroom")
        set_var("Julia", base="JuliaHome_Bathroom_Julia_[juliaHomeLivingRoomJuliaCloth]_[juliaHomeBathroomJuliaSuffix]", scene="juliahome_bathroom")
        set_var("Julia", base="JuliaHome_Kitchen_Julia_[juliaHomeLivingRoomJuliaCloth]_[juliaHomeKitchenJuliaSuffix]", scene="juliahome_kitchen")
        set_var("Julia", base="JuliaHome_Kitchen_Julia_[juliaHomeLivingRoomJuliaCloth]_[juliaHomeKitchenJuliaSuffix]", scene="juliahome_bathroomshower")
        juliaHomeLivingRoomMonicaSuffix = 3
        juliaHomeLivingRoomJuliaSuffix = 3
        monica_juliahome_outside_cloth = cloth
        monica_juliahome_outside_cloth_type = cloth_type
        cloth = monica_juliahome_cloth
        cloth_type = "juliahome"
        juliaHomeLivingRoomJuliaCloth = "JuliaCloth1"
        minimapJuliaGenerateEnabled = True
    call juliahome_kitchen_init2()
    call juliahome_bathroomshower_init2()

    $ add_hook("Monica", "ep213_quests_julia21_monica_click", scene="juliahome_bathroom", label="juliahome_shower", quest="juliahome")

    $ add_hook("Shower", "ep213_quests_julia3_shower", scene="juliahome_bathroomshower", label="juliahome_shower", quest="juliahome")
    $ add_hook("Kitchen", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Kitchen_Item1", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Kitchen_Item2", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Kitchen_Item3", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Kitchen_Item4", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Kitchen_Item5", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Teleport_Street", "ep213_quests_julia5_exit_street", scene="juliahome_kitchen", label="juliahome_exit", quest="juliahome")
    $ add_hook("Wardrobe", "ep213_quests_julia6_wardrobe", scene="juliahome_livingroom", label="juliahome_wardrobe", quest="juliahome")
    $ add_hook("Toilet", "ep213_quests_julia7_toilet", scene="juliahome_bathroom", label="juliahome_toilet", quest="juliahome")
    $ add_hook("JuliaHome", "ep213_quests_julia9_enter_building", scene="street_juliahome", label="juliahome_enter", quest="juliahome")
    $ add_hook("Julia", "ep213_quests_julia11_julia", scene="juliahome_livingroom", label="juliahome_julia_regular1", quest="juliahome")
    $ add_hook("Julia", "ep213_quests_julia11_julia", scene="juliahome_kitchen", label="juliahome_julia_regular1", quest="juliahome")
    $ add_hook("Julia", "ep213_quests_julia11_julia", scene="juliahome_bathroom", label="juliahome_julia_regular1", quest="juliahome")
    $ add_hook("Bed1", "juliahome_bed", scene="juliahome_livingroom", label="juliahome_bed", quest="juliahome")
    $ add_location("World", caption=("World"), label="world", init_label="world_init", parent="none")

    $ add_hook("exit_scene", "ep213_quests_julia12_exit_livingroom", scene="juliahome_livingroom", label="juliahome_livingroom_exit", quest="juliahome")
    $ add_hook("before_open", "ep213_quests_julia13_enter_livingroom", scene="juliahome_livingroom", label="juliahome_livingroom_enter", quest="juliahome")
    $ add_hook("before_open", "ep213_quests_julia20_check_julia_movement", scene="juliahome_kitchen", label="juliahome_kitchen_enter", quest="juliahome")

    $ add_hook("map_teleport", "ep213_quests_julia14_map_teleport", scene="global", label="juliahome_map_teleport", priority=10000, quest="juliahome")
    $ add_hook("map_teleport_after", "ep213_quests_julia16_exit_house", scene="global", label="juliahome_map_teleport", priority=10000, quest="juliahome")
    $ add_hook("exit_scene", "ep213_quests_julia3_shower_exit", scene="juliahome_bathroom", label="juliahome_bathroom_exit", quest="juliahome")
    $ add_hook("change_time_evening", "ep213_quests_julia17_life_evening", scene="global", label="juliahome_julia_life_evening", quest="juliahome")

    $ add_hook("juliahome_monica_after_sleep", "ep213_quests_julia21_monica_after_sleep", scene="global", label="juliahome_julia_life_after_sleep", quest="juliahome")
    $ add_hook("Julia", "ep213_quests_julia22_work_julia_regular", scene="working_office_cabinet", label="juliawork_lovestory_regular", quest="juliahome")

    $ questLog(74, True)

    call change_scene("juliahome_livingroom", "Fade_long", False)
    return False


label ep213_quests_julia3_shower: # клик на душ
    if act=="l":
        return

    if monicaLastShowerDay == day and monicaLastShowerDayTime == day_time:
        mt "Я уже принимала душ недавно..."
        return False
    call ep213_dialogues5_julia_15c2()
    $ monicaLastShowerDay = day # Последний день, когда Моника принимала душ
    $ monicaLastShowerDayTime = day_time
    $ juliaHomeBathroomMonicaSuffix = 3
    if day_time != "evening":
        call ep213_quests_julia17_life()
    call change_scene("juliahome_bathroom")

    return False

label ep213_quests_julia3_shower_exit: # выход из ванной (где туалет)
    if get_active_objects("Julia", scene="juliahome_bathroom") != False and juliaHomeBathroomJuliaSuffix == 2:
        $ move_object("Julia", "juliahome_livingroom")
        call ep213_quests_julia17_life()
    return

label ep213_quests_julia4_kitchen: # клик на кухню (еда)
    if act=="l":
        return

    if get_active_objects("Julia", scene="street_juliahome", recursive=True) != False and juliaHomeLivingRoomJuliaSuffix == 2: # Если Юлия дома и спит
        call ep213_dialogues5_julia_9()
        if _return != False:
            $ monica_eated()
#            call ep213_quests_julia17_life()
        $ move_object("Julia", "juliahome_bathroom")
        $ juliaHomeLivingRoomMonicaSuffix = 3
        $ juliaHomeLivingRoomJuliaSuffix = 3
        $ juliaHomeBathroomMonicaSuffix = 1
        $ juliaHomeBathroomJuliaSuffix = 2
        call refresh_scene_fade()
        return False

    if monicaEatedLastDay != day:
        fadeblack
        imgf 30842
        sound snd_eating
        w
#        pause 1.5
        $ monica_eated()
        call refresh_scene_fade()
    else:
        call ep213_dialogues5_julia_15b()
    return False

label ep213_quests_julia5_exit_street: # Моника выходит на улицу
    $ cloth = monica_juliahome_outside_cloth
    $ cloth_type = monica_juliahome_outside_cloth_type
#    $ juliaHomeLivingRoomJuliaSuffix = 3
    if scene_name == "juliahome_kitchen":
        $ autorun_to_object("ep213_dialogues5_julia_15e", scene="street_juliahome")

    if get_active_objects("Julia", scene="street_juliahome", recursive=True) != False and ep213_dialogues5_julia_13_day != day and day_time == "day":
        if cloth == "CasualDress1":
            if week_day != 7:
                call ep213_dialogues5_julia_13()
            else:
                call ep213_dialogues5_julia_13a()
            $ ep213_dialogues5_julia_13_day = day

    call ep213_quests_julia17_life()
    call change_scene("street_juliahome", "Fade_long", "snd_door_close1")
    return False

label ep213_quests_julia6_wardrobe: # гардероб
    if act=="l":
        call ep213_dialogues5_julia_17()
        return False
    call ep213_dialogues5_julia_18_wardrobe()
    if _return == 0:
        call refresh_scene_fade()
        return False
    $ monica_juliahome_outside_cloth = cloth
    $ monica_juliahome_outside_cloth_type = cloth_type
    call ep213_quests_julia5_exit_street()
    return False

label ep213_quests_julia7_toilet: # Моника писает
    if act=="l":
        return
    if get_active_objects("Julia", scene="juliahome_bathroom") != False and juliaHomeBathroomJuliaSuffix == 1:
        mt "Я - Леди!"
        mt "И я не собираюсь писать на глазах у своей гувернантки!"
        mt "Тем более, не знаю, что этой дуре может еще прийти в голову..."
        return False
    if monicaLastPissedDay == day and day_time == monicaLastPissedDayTime:
        mt "Я уже писала недавно. Я пока не хочу."
        return False
    call ep213_dialogues5_julia_15d()
    $ monicaLastPissedDay = day # Последний день, когда Моника писала
    $ monicaLastPissedDayTime = day_time
    call refresh_scene_fade()
    return False

label ep213_quests_julia8_minimap_teleport: # Телепорт по миникарте
    if minimapTeleportButtonName == "JuliaHome_Street":
        if scene_name != "street_juliahome":
            call ep213_quests_julia5_exit_street()
        return
    if scene_name == "street_juliahome":
        call ep213_quests_julia10_check_enter_home()
        fadeblack
        $ monica_juliahome_outside_cloth = cloth
        $ monica_juliahome_outside_cloth_type = cloth_type
        $ cloth = monica_juliahome_cloth
        $ cloth_type = "juliahome"
        sound snd_fabric1
        pause 1.0

    if minimapTeleportButtonName == "JuliaHome_LivingRoom":
        call change_scene("juliahome_livingroom", "Fade", "snd_walk_barefoot")
    if minimapTeleportButtonName == "JuliaHome_Kitchen":
        call change_scene("juliahome_kitchen", "Fade", "snd_walk_barefoot")
    if minimapTeleportButtonName == "JuliaHome_Bathroom":
        call change_scene("juliahome_bathroom", "Fade", "snd_walk_barefoot")

    call ep213_quests_julia20_check_julia_movement()

    return

label ep213_quests_julia9_enter_building: # входит с улицы через вход
    if act=="l":
        return
    call ep213_quests_julia10_check_enter_home()
    fadeblack
    $ monica_juliahome_outside_cloth = cloth
    $ monica_juliahome_outside_cloth_type = cloth_type
    $ cloth = monica_juliahome_cloth
    $ cloth_type = "juliahome"
    sound snd_fabric1
    pause 1.0
    call change_scene("juliahome_livingroom", "Fade", "snd_walk_barefoot")
    return False

label ep213_quests_julia10_check_enter_home: # события при входе в дом
    $ juliaHomeLivingRoomMonicaSuffix = 3
    $ juliaHomeLivingRoomJuliaSuffix = 3
    if day_time == "evening":
        $ move_object("Julia", "juliahome_livingroom")
    return

label ep213_quests_julia11_julia: # регулярный разговор с Юлией (везде)
    if act=="l":
        call ep210_dialogues5_julia_3_2()
        return False

    if scene_name == "juliahome_bathroom" and juliaHomeBathroomJuliaSuffix == 1: # Юлия принимает душ
#        if # хватает уровня
        call ep213_dialogues5_julia_10()
        if _return == False:
            call change_scene("juliahome_kitchen", "Fade_long", "snd_walk_barefoot")
            return False

        $ move_object("Julia", "juliahome_livingroom")
        $ juliaHomeBathroomMonicaSuffix = 3
        call change_scene("juliahome_bathroomshower", "Fade_long", False)
        call change_scene("juliahome_bathroom", "Fade_long", False)
        return False

    if scene_name == "juliahome_kitchen": # Регулярный разговор на кухне
        call ep213_dialogues5_julia_9b()
        call refresh_scene_fade()
        return False

    if scene_name == "juliahome_livingroom" and juliaHomeLivingRoomJuliaSuffix == 1:
        call ep213_dialogues5_julia_8()
        if _return == 0: # Просыпается только Моника
            $ juliaHomeLivingRoomMonicaSuffix = 2
            $ juliaHomeLivingRoomJuliaSuffix = 2
            call refresh_scene_fade()
            return False

        if _return == 1: # Просыпаются
            $ juliaHomeLivingRoomMonicaSuffix = 3
            $ juliaHomeLivingRoomJuliaSuffix = 3
            call ep213_quests_julia17_life()
            call refresh_scene_fade()
            return False

        if _return == 2: # Поспать еще (Моника спит, Юлия уходит, либо остается если выходной)
            $ juliaHomeLivingRoomMonicaSuffix = 3
            $ juliaHomeLivingRoomJuliaSuffix = 3
            call ep213_quests_julia17_life()
            call refresh_scene_fade()
            return False

    call ep213_dialogues5_julia_16a()
    return False

label ep213_quests_julia12_exit_livingroom:
    if juliaHomeLivingRoomMonicaSuffix == 1:
        if day_time == "day":
            $ juliaHomeLivingRoomMonicaSuffix = 2
            $ juliaHomeLivingRoomJuliaSuffix = 2
    return

label ep213_quests_julia13_enter_livingroom:
    if cloth_type != "juliahome":
        $ monica_juliahome_outside_cloth = cloth
        $ monica_juliahome_outside_cloth_type = cloth_type
        $ cloth = monica_juliahome_cloth
        $ cloth_type = "juliahome"

    if juliaHomeLivingRoomJuliaSuffix == 1 or juliaHomeLivingRoomJuliaSuffix == 2:
        $ juliaHomeLivingRoomJuliaSuffix = 2
        $ juliaHomeLivingRoomMonicaSuffix = 2
    if juliaHomeLivingRoomJuliaSuffix != 1 and juliaHomeLivingRoomJuliaSuffix != 2:
        $ set_active("Bed1", True, scene="juliahome_livingroom")

    return

label ep213_quests_julia14_map_teleport: # вызов перед уходом по карте
    # переодеваем Монику назад
    if lastSceneName == "juliahome_livingroom":
        $ cloth = monica_juliahome_outside_cloth
        $ cloth_type = monica_juliahome_outside_cloth_type
    return


label ep213_quests_julia16_exit_house: # Жизнь Юлии при выходе из дома
    if previous_map_scene == "JuliaHome":
        if check_scene_parent(scene_name, "street_juliahome") == True:
            return
        call ep213_quests_julia17_life()
    return

label ep213_quests_julia17_life:
    if week_day != 7 and day_time != "evening":
        if get_active_objects("Julia", scene="street_juliahome", recursive=True) != False:
            $ notif(t_("Юлия ушла на работу."))
        $ juliaHomeLivingRoomJuliaSuffix = 3
        $ move_object("Julia", "working_office_cabinet") # Юлия уходит на работу
    return

label ep213_quests_julia17_life_evening:
    if check_scene_parent(scene_name, "street_juliahome", recursive = True) != False:
        $ move_object("Julia", "juliahome_livingroom")
#        $ juliaHomeLivingRoomMonicaSuffix = 3
        $ juliaHomeLivingRoomJuliaSuffix = 3

    return


label ep213_quests_julia18_progress(scene_idx, status):
    python:
        if status != julia_progress_list[scene_idx]:
            julia_progress_list[scene_idx] = status
            if status == True:
                add_char_progress("Julia", 10, "julia_relations_progress_idx_" + str(scene_idx), duplicate = True)
            else:
                add_char_progress("Julia", -10, "julia_relations_progress_idx_" + str(scene_idx), duplicate = True)
    return


label ep213_quests_julia19_evening_scene: # вечерняя сцена
    call ep213_dialogues5_julia_11()
    return

label ep213_quests_julia20_check_julia_movement:
    if day_time == "evening" and get_active_objects("Julia", scene="juliahome_livingroom") != False and juliahome_julia_shower_day != day and scene_name != "juliahome_livingroom":
        $ notif(t_("Юлия ушла в душ."))
        $ juliahome_julia_shower_day = day
        $ move_object("Julia", "juliahome_bathroom")
        $ juliaHomeBathroomJuliaSuffix = 1

    return

label ep213_quests_julia21_monica_click:
    if act=="l":
        call ep211_dialogues4_julia_11l()
        return False
    return

label ep213_quests_julia21_monica_after_sleep:
    $ move_object("Julia", "juliahome_livingroom")
    return


label ep213_quests_julia22_work_julia_regular:
    if monica_living_at_juliahome == False:
        return
    if act == "l":
        return
    if day_time != "evening":
        call ep213_dialogues5_julia_1()
    else:
        call ep213_dialogues5_julia_1a()
    if _return == 0:
        if day_time != "evening":
            call ep210_dialogues5_julia_4_1()
            $ ep210_julia_kissed_day_day = day
        else:
            call ep210_dialogues5_julia_4_3()
            $ ep210_julia_kissed_day_evening = day

    if _return == 1: # Массаж для Юлии
        call ep213_dialogues5_julia_2()
        $ juliahome_work_action_day = day
    if _return == 2: # На рабочем столе Моники.
        call ep213_dialogues5_julia_3()
        $ juliahome_work_action_day = day
    if _return == 3: # На диване в комнате отдыха
        call ep213_dialogues5_julia_4()
        $ juliahome_work_action_day = day
    if _return == 4: # Под столом Юлии
        call ep213_dialogues5_julia_5()
        $ juliahome_work_action_day = day
    if _return == 5: # В отделе отчетов
        call ep213_dialogues5_julia_6()
        $ move_object("Julia", "juliahome_livingroom")
        $ juliahome_work_action_evening_day = day
        call change_scene("working_office2", "Fade_long", False)
        return False


    call refresh_scene_fade()
    return False
