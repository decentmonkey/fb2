default dickDoorBlockedDay = 0
default biffWaitingForMonicaToWork = False
default monicaTalkedSecretary1 = False

label fred_talk_monica1:
    $ add_hook("before_open", "fred_talk_monica1a", scene="street_house_main_yard", label="fred_talk1")
    $ add_hook("map_teleport", "fred_talk_monica1aMap", scene="global", label="fred_talk1")
    $ add_hook_multi("fred_talk_monica1b", scene="street_house_main_yard", filter={"teleport":True})
    $ remove_hook()
    return

label fred_talk_monica1aMap:
    if day_time != "day":
        return
    call fred_talk_monica1a()
    return False

label fred_talk_monica1a:
    if day_time != "day":
        return
    $ miniMapEnabledOnly = ["none"]
    $ map_enabled = False
    $ cloth = "Whore"
    $ cloth_type = "Whore"

    $ add_hook("Driver", "fred_talk_monica1c", scene="street_house_main_yard", label="fred_talk1a")

    $ map_source_scene = "street_house_main_yard"
    $ autorun_to_object("fred_talk_monica1b", scene="street_house_main_yard")
    return

label fred_talk_monica1b:
    if day_time != "day":
        return
    call monica_fred_about_dick_dialogue1()
    return False

label fred_talk_monica1c:
    if act == "l":
        return
    $ miniMapEnabledOnly = []
    $ map_enabled = True
    $ remove_hook(label="fred_talk1")
    $ remove_hook("fred_talk_monica1b")
    $ replace_hook("Driver", "fred_talk_monica1c", "fred_talk_monica1d")
    call ep2_open_dick1()
    call fred_talk_monica1d()
    return _return

label fred_talk_monica1d:
    call monica_fred_about_dick_dialogue2()
    $ add_objective("go_dick", _("Отправиться на встречу с Диком"), c_green, 30)
    call refresh_scene_fade()
    return False

label ep2_open_dick1:
    $ move_object("DickTheLawyer", "dick_office_cabinet")
    $ add_hook("DickSecretary", "dick_secretary_talk1", scene="dick_office_secretary", label="secretary1")
    $ add_hook("Door", "dick_secretary_talk1", scene="dick_office_secretary", label="secretary1")
    return

label dick_secretary_talk1:
    $ remove_hook(label="fred_talk1a")
    if act == "l":
        return
    if obj_name == "DickSecretary":
        call monica_dick_secretary_dialogue1()
        $ monicaTalkedSecretary1 = True
    else:
        if monicaTalkedSecretary1 == False:
            call monica_dick_secretary_dialogue1()
            $ monicaTalkedSecretary1 = True
        call monica_dick_secretary_dialogue1a()
        $ remove_hook("Door", "dick_secretary_talk1")
        $ add_hook("enter_scene", "dick_the_lawyer_enter1", scene="dick_office_cabinet")
        $ add_hook("DickTheLawyer", "dick_the_lawyer_talk1", scene="dick_office_cabinet")

    return

label dick_the_lawyer_enter1:
    $ remove_objective("go_dick")
    $ remove_hook()
    call monica_dick_dialogue1a()
    return

label dick_the_lawyer_talk1:
    if act == "l":
        return
    call monica_dick_dialogue1()
    $ dickDoorBlockedDay = day
    $ add_hook("Door", "monica_dick_secretary_dialogue4a", scene="dick_office_secretary", label="dick_blocked")
    $ replace_hook("dick_secretary_talk2", scene="dick_office_secretary", label="secretary1")
    $ add_hook("Teleport_Hall", "monica_dick_secretary_dialogue2a", scene="dick_office_secretary", label="secretary1")
    $ autorun_to_object("monica_dick_secretary_dialogue2a", scene="dick_office_secretary")
    $ autorun_to_object("monica_dick_office_dialogue2", scene="street_dick_office")
    $ nextFriday = getNextDayByWeekDay(5)
    $ add_hook_day("dick_secretary_time_to_pay1", day = nextFriday, evening=True)
    $ remove_hook(label="biff_refuse1") # очищаем дорогу к Бифу
    $ add_hook("Secretary", "monica_office_secretary_talk_before_work_request", scene="monica_office_secretary", label="monica_secretary2")
    $ add_hook_multi("monica_office_secretary_talk_before_work_request", scene="monica_office_secretary", filter={"teleport":True}, label="monica_secretary2_teleport", priority=160)
    $ add_hook("Biff", "monica_office_biff_talk_about_work1", scene="monica_office_cabinet_table", label="biff2")
    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_cabinet_biff_dialogue2a", scene="monica_office_secretary", priority=120)
    call change_scene("dick_office_secretary")
    return

label dick_secretary_talk2:
    if act == "l":
        return
    call monica_dick_secretary_dialogue2()
    $ add_objective("dicksecretary_find_money", _("Принести Виктории $ 5000 до вечера пятницы"), c_red, 30)
    $ add_char_progress("DickSecretary", 20, "dick_secretary_talk2")
    $ remove_hook(label="secretary1")
    $ add_hook("DickSecretary", "dick_secretary_talk3", scene="dick_office_secretary")
    return

label dick_secretary_talk3: #регулярный
    if act == "l":
        return
    call monica_dick_secretary_dialogue3()
    return False


label dick_secretary_time_to_pay1:
    m "Время платить!"
    if biffWaitingForMonicaToWork == False:
        "но пока не надо!"
        $ nextFriday = getNextDayByWeekDay(5)
        $ remove_hook()
        $ add_hook_day("dick_secretary_time_to_pay1", day = nextFriday, evening=True)

        return
    return

label monica_office_secretary_talk_before_work_request:
    if obj_name == "Secretary" and act == "l":
        return
    call monica_office_secretary_dialogue3()
    $ remove_hook(label="monica_secretary2_teleport")
    return False

label monica_office_biff_talk_about_work1: #Моника разговаривает с Бифом второй раз, уже о работе.
    if act == "l":
        return
    call monica_office_cabinet_biff_dialogue3()
    $ monicaOfficeSecretaryMonicaSuffix = ""
    $ autorun_to_object("monica_office_secretary_dialogue5", scene="monica_office_secretary")
    if nextFriday != day:
        $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_cabinet_biff_dialogue2", scene="monica_office_secretary", label="biff_refuse1")
    $ remove_hook(label="monica_secretary2")
    $ biffWaitingForMonicaToWork = True
    $ add_hook("change_time_day", "monica_office_biff_talk_about_work1_next_day", scene="global")
#    $ biffOnlyFridayEvening = True # Бифф будет только в пятницу вечером
    return False

label monica_office_biff_talk_about_work1_next_day:
    m "monica_office_biff_talk_about_work1_next_day"
    $ remove_hook()
    $ replace_hook("monica_office_secretary_dialogue4", scene="monica_office_secretary", label="biff_refuse1")
    $ remove_hook(label="biff_refuse1")
    $ replace_hook("monica_office_biff_talk_about_work1", scene="monica_office_cabinet_table", label="biff2")

    return

label monica_office_biff_talk_about_work2: #Моника разговаривает с Бифом третий раз.
    if act == "l":
        return
    call monica_office_cabinet_biff_dialogue4()
    $ remove_hook()
    return
