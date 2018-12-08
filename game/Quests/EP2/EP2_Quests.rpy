default dickDoorBlockedDay = 0
default biffWaitingForMonicaToWork = False
default monicaTalkedSecretary1 = False
default monica_office_cabinet_biff_dialogue3Flag = False

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
#    $ add_hook_day("dick_secretary_time_to_pay1", day = nextFriday, evening=True)
    $ add_hook_day("dick_secretary_time_to_pay1", day = nextFriday)
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
    $ add_hook("Teleport_Inside", "monica_dick_office_refuse_dialogue1", scene="street_dick_office", label="dick_blocked")
    $ add_hook("BasementBed", "basement_bed_hook", scene="basement_bedroom2")
    $ add_hook("basement_monica_before_sleep", "dick_secretary_time_to_pay2", scene="global")
    $ add_hook("basement_monica_after_sleep_dialogue", "dick_secretary_time_to_pay1a", scene="global")
    $ remove_hook()
#    if biffWaitingForMonicaToWork == False:
#        "но пока не надо!"
#        $ nextFriday = getNextDayByWeekDay(5)
#        $ remove_hook()
#        $ add_hook_day("dick_secretary_time_to_pay1", day = nextFriday, evening=True)
#        return
    return
label dick_secretary_time_to_pay1a:
    mt "Сегодня пятница. Мне надо {b}найти $ 5000 до вечера{/b}!"
    "Тогда Дик убедится в моей лояльности и вытащит меня из этой ситуации, в которую я попала!"
    $ remove_hook()
    return
label dick_secretary_time_to_pay2:
    mt "Я не могу идти спать. Я должна {b}принести сегодня $ 5000 Дику{/b}!"
    return False

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
    $ monicaOfficeSecretaryMonicaSuffix_forced = ""
    if _return == False:
        return False
    call change_scene("monica_office_secretary")
    $ autorun_to_object("monica_office_secretary_dialogue5", scene="monica_office_secretary")
    if nextFriday != day:
        $ biffOnlyFridayEvening = True
        $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_cabinet_biff_dialogue2", scene="monica_office_secretary", label="biff_refuse1") # Если не пятница, то блокируем Бифа на сегодня
        $ add_hook("enter_scene", "monica_office_secretary_dialogue5a", scene="monica_office_secretary", label="biff_comment1") #При входе в офис Моника думает все-же согласиться на фотосессию
        $ add_hook("change_time_day", "monica_office_biff_talk_about_work1_next_day", scene="global")
    $ remove_hook(label="monica_secretary2")
    if nextFriday == day: # уже пятница, активируем
        $ replace_hook("monica_office_biff_talk_about_work2", scene="monica_office_cabinet_table", label="biff2") # Разговариваем с Бифом в 3-ий раз, соглашаясь на обнажение постепенно

#    $ biffOnlyFridayEvening = True # Бифф будет только в пятницу вечером
    return False

label monica_office_biff_talk_about_work1_next_day: # Если вчера была не пятница, то вешаем хуки об отсутствии Бифа до пятницы (хрень какая-то, так и есть :) )
    m "monica_office_biff_talk_about_work1_next_day"
    $ remove_hook()
    $ remove_hook(label="biff_refuse1")
    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue4", scene="monica_office_secretary", label="biff_refuse1", priority=160)
#    $ remove_hook(label="biff_refuse1")
    $ replace_hook("monica_office_biff_talk_about_work2", scene="monica_office_cabinet_table", label="biff2")  # Разговариваем с Бифом в 3-ий раз, соглашаясь на обнажение постепенно

    return

label monica_office_biff_talk_about_work2: #Моника разговаривает с Бифом третий раз.
    if act == "l":
        return
    call monica_office_cabinet_biff_dialogue4()
    if _return == False:
        return False
    $ remove_hook(label="biff_comment1")
    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue6", scene="monica_office_secretary", label="photoshot_exit_refuse")
    $ add_hook("Teleport_Monica_Office_Entrance", "monica_office_secretary_dialogue6", scene="monica_office_secretary", label="photoshot_exit_refuse")
    $ add_hook("AlexPhotograph", "monica_office_photoshot1", scene="monica_office_photostudio")
    $ remove_hook()
    call change_scene("monica_office_secretary")
    return False

label monica_office_photoshot1:
    if act == "l":
        return
    call monica_office_photostudio_alex_dialogue2()
    if _return == False:
        return False
    $ cloth_type = "PhotoDress"
    $ cloth = "PhotoDress"
    $ remove_hook()
    $ remove_hook(label="photoshot_exit_refuse")

    $ add_hook("AlexPhotograph", "monica_office_dialogue9", scene="monica_office_photostudio", label="after_photoshot")
    $ add_hook("Secretary", "monica_office_secretary_dialogue7", scene="monica_office_secretary", label="after_photoshot") # Комментарий Моники в платье
    $ add_hook("Teleport_Monica_Office_Entrance", "monica_office_dialogue9", scene="monica_office_secretary", label="after_photoshot")
    $ add_hook("Biff", "monica_office_photoshot1_biff_talk1", scene="monica_office_cabinet_table", label="biff3")
    return False

label monica_office_photoshot1_biff_talk1:
    if act=="l":
        return
    call monica_office_cabinet_biff_dialogue5()
    $ remove_hook()
    $ remove_hook(label="after_photoshot")
    m "EVENT"
    # идем на эвент
    return False
