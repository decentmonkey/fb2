default ep211_julia_second_date_inited = False
default ep211_julia_second_date_aborted = False
default ep211_julia_comment_day1 = 0
default ep211_julia_second_date_completed = False
default ep211_julia_second_date_completed_day = 0

label ep211_quests_julia1:
    # инициализация второго свидания
    call ep211_dialogues4_julia_1()
    $ ep211_julia_second_date_inited = True
    $ add_objective("go_date_julia", _("После работы пойти на свидание с Юлией в кафе."), c_orange, 105)
    $ ep210_julia_evening_at_work = False
    $ ep210_julia_not_at_work = True
    $ move_object("Julia", "empty")
    $ add_hook("enter_scene", "ep210_dialogues5_julia_2a", scene="working_office_cabinet", label="julia_date2")
    $ add_hook("JuliaCafe", "ep211_quests_julia2_check_cafe_enter", scene="street_juliahome", label=["julia_date2", "julia_date2_enter_cafe"])

    return

label ep211_quests_julia2_check_cafe_enter:
    if act=="l":
        return
    if cloth != "CasualDress1":
        call ep210_dialogues5_julia_3_4a()
        return False
    # второе свидание в кафе
    call ep211_dialogues4_julia_11q()
    if _return == False:
        return False
    $ remove_objective("go_date_julia")
    call ep211_dialogues4_julia_2()
    if day_time != "evening":
        $ changeDayTime("evening")
    $ ep210_julia_evening_at_work = True
    $ ep210_julia_not_at_work = False
    $ move_object("Julia", "street_juliahome")
    $ autorun_to_object("ep211_dialogues4_julia_3", scene="street_juliahome")
    $ add_hook("Monica", "ep211_dialogues4_julia_3", scene="street_juliahome", label="julia_date2")
    $ add_hook("Julia", "ep211_dialogues4_julia_3b", scene="street_juliahome", label="julia_date2")
    $ add_hook("JuliaHome", "ep211_quests_julia3_enter_building", scene="street_juliahome", label="julia_date2")
    $ remove_hook(label="julia_date2_enter_cafe")
    $ set_active("Teleport_StreetCorner", False, scene="street_juliahome")
    $ map_enabled = False
    $ streetJuliaHomeMonicaSuffix = 2
    call refresh_scene_fade_long()
    return False

label ep211_quests_julia3_enter_building:
    if act=="l":
        call ep211_dialogues4_julia_3()
        return False
    $ streetJuliaHomeMonicaSuffix = 1
    call locations_init_juliahome()
    $ set_active("Teleport_StreetCorner", False, scene="street_juliahome")
    $ map_enabled = True
    $ move_object("Julia", "juliahome_livingroom")
    $ add_hook("JuliaHome", "ep211_dialogues4_julia_11r", scene="street_juliahome", label="julia_home_block") # Блокируем вход в дом Юлии в дальнейшем
    call ep211_dialogues4_julia_4()
    $ set_active("Teleport_Kitchen", False, scene="juliahome_livingroom")
    $ add_hook("Julia", "ep211_quests_julia4_talk", scene="juliahome_livingroom", label="julia_date2")
    call change_scene("juliahome_livingroom", "Fade_long", False)
    return False

label ep211_quests_julia4_talk:
    if act=="l":
        return
    $ remove_hook()
    call ep211_dialogues4_julia_4a()
    if _return == False:
        $ remove_hook(label="julia_date2")
        $ ep211_julia_second_date_aborted = True
#        $ ep211_julia_second_date_inited = False # Позволяем сходить на свидание вновь
        $ e210_quests_julia_aborted = True
        $ remove_hook(label="julia_dating_regular")
        $ set_active("Teleport_StreetCorner", True, scene="street_juliahome")
        $ add_hook("JuliaHome", "ep211_dialogues4_julia_9", scene="street_juliahome", label="evening_time_temp")
        $ char_info["Julia"]["level"] = 1
        $ char_info["Julia"]["progress"] = 0
        $ char_info["Julia"]["caption"] = _("Юлия боится Монику")
        $ autorun_to_object("ep211_dialogues4_julia_9", scene="street_juliahome")
        $ remove_objective("find_julia_panties_color")
        call change_scene("street_juliahome", "Fade_long")
        return False

    $ add_hook("Julia", "ep211_dialogues4_julia_5", scene="juliahome_livingroom", label="julia_date2")
    $ set_active("Teleport_Kitchen", True, scene="juliahome_livingroom")
    $ add_hook("Teleport_Street", "ep211_dialogues4_julia_11s", scene="juliahome_kitchen", label="julia_home_street_block")
    $ autorun_to_object("ep211_dialogues4_julia_6b", scene="juliahome_bathroom")
    $ add_hook("WashMachine", "ep211_quests_julia5_panties_not_found", scene="juliahome_bathroom", label=["julia_date2", "julia_home_search_panties"])
    $ add_objective("search_panties", _("Осмотреть ванную комнату."), c_blue, 105)
    call juliahome_bathroom_init()

    call refresh_scene_fade()
    return False

label ep211_quests_julia5_panties_not_found:
    $ remove_hook()
    call ep211_dialogues4_julia_6()
    $ remove_objective("search_panties")
    $ add_hook("Julia", "ep211_quests_julia6_talk", scene="juliahome_livingroom", label="julia_date2")
    call refresh_scene_fade()

    return False

label ep211_quests_julia6_talk:
    if act=="l":
        return
    call ep211_dialogues4_julia_7()
    $ add_hook("Julia", "ep211_dialogues4_julia_7a", scene="juliahome_livingroom", label="julia_date2")
    $ remove_hook(label="julia_home_street_block")
    $ add_hook("enter_scene", "ep211_quests_julia7_end", scene="street_juliahome", label="julia_date2")
    $ add_hook("JuliaHome", "ep211_dialogues4_julia_9", scene="street_juliahome", label="evening_time_temp")
    $ add_hook("Monica", "ep211_dialogues4_julia_10", scene="street_juliahome", label="street_juliahome_evening_comment") # Комментарий что вечером здесь опасно
    $ set_active("Teleport_StreetCorner", True, scene="street_juliahome")
    call refresh_scene_fade()
    return False

label ep211_quests_julia7_end:
    $ remove_hook()
    $ ep211_julia_second_date_completed = True
    $ ep211_julia_second_date_completed_day = day
    $ add_char_progress("Julia", 100, "julia_second_date")
    call ep211_dialogues4_julia_8()
    $ remove_hook(label="julia_date2")
    return False




    return False
