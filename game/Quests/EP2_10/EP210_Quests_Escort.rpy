default ep210_quests_escort_stage = 0
default monica_philip_visits = 0
default monica_philip_visits_stage = 1
default ep210_quests_escort1_philip3_map_flag = False
default monica_philip_visited_last_day = 0
default monica_philip_visit_whore1_exists = False
default monica_philip_visits_blowjobs = 0
default monica_philip_visits_sex = 0
default monica_philip_visits_swallowed = 0

label ep210_quests_escort_eat_process:
    if ep210_quests_escort_stage == 0 and ep22_quests_monica_presentation_completed == True:
        call ep210_quests_escort1_philip1()
        return False
    return


label ep210_quests_escort1_philip1: # Первая встреча с Филиппом в ресторане
    # Приходит Филипп
    $ add_hook("Teleport_Street_Rich_Hotel", "ep210_quests_escort_reception1", scene="rich_hotel_reception", label="ep210_quests_escort_reception1")
    $ add_hook("ReceptionGirl", "ep210_quests_escort_reception1", scene="rich_hotel_reception", label="ep210_quests_escort_reception1")
    call rich_hotel_reception_init2() # Инициализация локации рецепшина
    call ep210_dialogues2_escort_start_Phillip_1()
    if _return == False:
        $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_4", scene="street_rich_hotel")
        $ move_object("Philip", "rich_hotel_reception")
        $ add_hook("Philip", "ep210_quests_escort1_philip2", scene="rich_hotel_reception", label="ep210_quests_escort1_philip2")
        $ ep210_quests_escort_stage = -1
        call change_scene("rich_hotel_reception", "Fade_long")
        return

    # Секс в туалете
    music stop
    img black_screen
    with diss
    pause 2.0
    call ep210_dialogues2_escort_start_Phillip_2()
    if _return == 1: # Моника отказалась, но возможен возврат
        $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_4", scene="street_rich_hotel")
        $ move_object("Philip", "rich_hotel_reception")
        $ add_hook("Philip", "ep210_quests_escort1_philip2", scene="rich_hotel_reception", label="ep210_quests_escort1_philip2")
        $ ep210_quests_escort_stage = -1
        call change_scene("rich_hotel_reception", "Fade_long")
        return

    if _return == 2: # Моника ударила Филиппа
        $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_4", scene="street_rich_hotel")
        $ ep210_quests_escort_stage = -1
        call change_scene("rich_hotel_reception", "Fade_long")
        return

    $ questLog(61, True)
    $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_3", scene="street_rich_hotel")
    $ add_money(300.0)
    sound2 fx_coins
    # Инициализируем дом Филиппа
    call locations_init_philip_home()
    $ map_objects ["Teleport_PhilipHome"] = {"text" : _("ДОМ ФИЛИППА"), "xpos" : 1767, "ypos" : 242, "base" : "map_marker", "state" : "visible"}
    $ add_hook("map_teleport", "ep210_quests_escort1_philip3_map", scene="global", label="philiphome_outfit_restrict")
    $ add_hook("Teleport_Building", "ep210_quests_escort1_philip4_enter", scene="street_philiphome")
#    $ map_objects ["Teleport_JuliaHome"] = {"text" : _("ДОМ ЮЛИИ"), "xpos" : 521, "ypos" : 1014, "base" : "map_marker", "state" : "visible"}
#    call street_corner_init2()
#    call locations_init_julia_street()

    call change_scene("rich_hotel_reception", "Fade_long")
    return

label ep210_quests_escort1_philip2: # Повторный квест с Филиппом
    call ep210_dialogues2_escort_start_Phillip_3a()
    $ move_object("Philip", "empty")
    $ ep210_quests_escort_stage = 0
    call refresh_scene_fade()
    return


label ep210_quests_escort_reception1: # Рецепшин перехватывает Монику
    $ remove_hook(label="ep210_quests_escort_reception1")
    call ep210_dialogues2_escort_start_Phillip_5()
    call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1")
    return False

label ep210_quests_escort1_philip3_map: # Проверка на одежду на карте у Филиппа
    if obj_name == "Teleport_PhilipHome":
        if cloth_type != "CasualDress":
            call ep210_dialogues2_escort_start_Phillip_11()
            return False
        if ep210_quests_escort1_philip3_map_flag == False:
            call ep210_dialogues2_escort_start_Phillip_6()
            $ ep210_quests_escort1_philip3_map_flag = True
        $ streetPhilipHomeMonicaSuffix = 1
    return

label ep210_quests_escort1_philip4_enter: # Вход к Филиппу домой
    if week_day != 6:
        call ep210_dialogues2_escort_start_Phillip_8()
        return False
    if day_time != "evening":
        call ep210_dialogues2_escort_start_Phillip_9()
        return False
    call ep210_dialogues2_escort_start_Phillip_7()
    if _return == False:
        call refresh_scene_fade()
        return False

    if monica_philip_visits_stage == 1:
        if monica_philip_visits % 2 == 1:
            # У Филиппа другая шлюха
            $ monica_philip_visit_whore1_exists = True
        else:
            $ monica_philip_visit_whore1_exists = False

        $ monica_philip_visits += 1
        call ep210_dialogues2_escort_start_Phillip_12()
        if _return == False:
            $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_13b", scene="street_philiphome")
            $ add_hook("Teleport_Building", "ep210_dialogues2_escort_start_Phillip_19", scene="street_philiphome", label=["philip_restict_day", "evening_time_temp"]) # Блок на вход к Филиппу в этот день
            $ streetPhilipHomeMonicaSuffix = 2
            call refresh_scene_fade_long()
            return False
        if monica_philip_visit_whore1_exists == True:
            music stop
            img black_screen
            with diss
            sound highheels_short_walk
            pause 1.5
            $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_13a", scene="street_philiphome")
            $ add_hook("Teleport_Building", "ep210_dialogues2_escort_start_Phillip_19", scene="street_philiphome", label=["philip_restict_day", "evening_time_temp"]) # Блок на вход к Филиппу в этот день
            $ streetPhilipHomeMonicaSuffix = 2
            $ move_object("Bitch1", "street_philiphome")
            $ add_hook("Bitch1", "ep210_quests_escort1_philip5_bitch1_street", scene="street_philiphome", label="ep210_quests_escort1_philip5_bitch1_street")
            $ add_hook("exit_scene", "ep210_quests_escort1_philip5_bitch1_street_leave", scene="street_philiphome", label="ep210_quests_escort1_philip5_bitch1_street")
            call refresh_scene_fade_long()
            return False


        # Выбор действия
        call ep210_dialogues2_escort_start_Phillip_14()
        if _return == 1:
            # Минет
            call ep210_dialogues2_escort_start_Phillip_15()
            if _return == True:
                $ monica_philip_visits_blowjobs += 1
                $ add_corruption(monicaPhilipVisitBlowjobCorruption, "monicaPhilipVisitBlowjobCorruption" + str(day))
                $ add_money(100.0)
                $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_17", scene="street_philiphome")
            else:
                $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_13b", scene="street_philiphome")
            $ add_hook("Teleport_Building", "ep210_dialogues2_escort_start_Phillip_19", scene="street_philiphome", label=["philip_restict_day", "evening_time_temp"]) # Блок на вход к Филиппу в этот день
            $ streetPhilipHomeMonicaSuffix = 2
            call refresh_scene_fade_long()
            return
        if _return == 2:
            # Секс
            call ep210_dialogues2_escort_start_Phillip_16()
            if _return == True:
                $ monica_philip_visits_sex += 1
                $ add_corruption(monicaPhilipVisitSexCorruption, "monicaPhilipVisitBlowjobCorruption" + str(day))
                $ add_money(100.0)
                $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_17", scene="street_philiphome")
            else:
                $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_13b", scene="street_philiphome")
            $ add_hook("Teleport_Building", "ep210_dialogues2_escort_start_Phillip_19", scene="street_philiphome", label=["philip_restict_day", "evening_time_temp"]) # Блок на вход к Филиппу в этот день
            $ streetPhilipHomeMonicaSuffix = 2
            call refresh_scene_fade_long()
            return


    $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_13b", scene="street_philiphome")
    $ add_hook("Teleport_Building", "ep210_dialogues2_escort_start_Phillip_19", scene="street_philiphome", label=["philip_restict_day", "evening_time_temp"]) # Блок на вход к Филиппу в этот день
    $ streetPhilipHomeMonicaSuffix = 2
    call refresh_scene_fade_long()
    return False


label ep210_quests_escort1_philip5_bitch1_street: # Шлюха окликает Монику на улице
    if act=="l":
        return
    $ remove_hook(label="ep210_quests_escort1_philip5_bitch1_street")
    call ep210_dialogues2_escort_start_Phillip_13()
    if _return == False:
        $ move_object("Bitch1", "empty")
        call refresh_scene_fade_long()
    return False

label ep210_quests_escort1_philip5_bitch1_street_leave:
    $ remove_hook(label="ep210_quests_escort1_philip5_bitch1_street")
    $ move_object("Bitch1", "empty")
    return
















#
