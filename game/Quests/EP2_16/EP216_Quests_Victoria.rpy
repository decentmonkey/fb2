default ep216_victoria_visit_day1 = 0
default ep216_quests_victoria1_init_flag = False

label ep216_quests_victoria1_init: # Юлия сообщает что надо ехать к Виктории на девичник
    $ add_hook("office_work_process", "ep216_quests_victoria2_init", scene="global", label="ep216_quests_victoria2_init", priority = 90)
    $ ep216_quests_victoria1_init_flag = True
    return

label ep216_quests_victoria2_init: # инициализация во время работы
    $ remove_hook()
    $ monicaOfficeWorkedToday = True
    call ep216_dialogues5_victoria_1()
    $ add_objective("go_victoria", t_("Поехать к Виктории."), c_red, 125)
    call locations_init_victoriahome1() # инициализируем локацию Виктории
    $ map_objects ["Teleport_VictoriaHome"] = {"text" : t_("АПАРТАМЕНТЫ ВИКТОРИИ"), "xpos" : 1403, "ypos" : 260, "base" : "map_marker", "state" : "visible"}

    # блокируем перемещения
    $ focus_map("Teleport_VictoriaHome", "ep216_dialogues5_victoria_12b")
    $ move_object("Melanie", "empty")
    $ hudDaySkipToEveningEnabled = False # выключаем телепорт в кровать
    # выключаем сон
    $ add_hook("slums_apartments_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")
    $ add_hook("hostel_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")
    $ add_hook("juliahome_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")
    $ add_hook("basement_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")

    # блокируем перемещения и работу
    $ add_hook("MonicaTable", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep216_victoria_block")
    $ add_hook("MonicaChair", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep216_victoria_block")
    $ add_hook("Julia", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep216_victoria_block")
    $ add_hook("Teleport_Inside", "ep216_dialogues5_victoria_12", scene="street_monica_office", label="ep216_victoria_block")
    $ add_hook("before_open", "ep216_quests_victoria3_street", scene="street_monica_office", label="ep216_victoria_block")
    $ add_hook("Worker1", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker2", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker3", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker4", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker5", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker6", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker7", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker3", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")
    $ add_hook("Worker4", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")
    $ add_hook("Worker6", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")
    $ add_hook("Worker7", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")

    $ add_hook("VictoriaHome_Enter", "ep216_quests_victoria4_enter", scene="street_victoriahome", label="ep216_victoria_visit_day1")
    $ add_hook("enter_scene", "ep216_quests_victoria3_street2", scene="street_victoriahome", label="ep216_victoria_visit_day1", once=True)
    $ autorun_to_object("ep216_dialogues5_victoria_12b", scene="working_office_cabinet")
    call refresh_scene_fade()
    return False

label ep216_quests_victoria3_street: # Моника выходит на улицу и наступает вечер
    $ remove_hook()
    if day_time != "evening":
        $ changeDayTime("evening")
    return

label ep216_quests_victoria3_street2: # Попадаем к Виктории на улицу
    $ unfocus_map()
    return

label ep216_quests_victoria4_enter: # вход к Виктории
    if act=="l":
        return
    if cloth != "CasualDress1":
        call ep216_dialogues5_victoria_8a()
        return False
    $ remove_hook()
    $ remove_hook(label="ep216_victoria_block")
    $ hudDaySkipToEveningEnabled = True
    call ep216_dialogues5_victoria_2()
    call ep216_dialogues5_victoria_4()
    if melanieVictoriaMonicaTable1 == True: # Моника осудила Мелани в гостях у Виктории, воткнула в нее розу
        call ep216_dialogues5_victoria_6()
    else:
        $ autorun_to_object("ep216_dialogues5_victoria_5", scene="street_victoriahome")
    $ add_hook("Melanie", "ep216_dialogues5_victoria_7", scene="monica_office_makeup_room", label="ep216_victoria_visit_day1_after")
    $ move_object("Melanie", "empty")
    $ ep216_victoria_visit_day1 = day
    $ remove_objective("go_victoria")
    call refresh_scene_fade()
    return False
