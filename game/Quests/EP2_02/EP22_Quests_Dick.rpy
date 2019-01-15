default monicaEarnedWeeklyMoneySkip = False

label ep22_quests_Dick1:
    if act=="l":
        return
    $ remove_hook()
    $ remove_hook(lable="hurry_to_dick")
    call ep22_dialogues5_2()
    $ add_hook("DickSecretary", "ep22_dialogues5_3")
    $ add_hook("change_time_day", "ep22_quests_Dick3", scene="global")
    $ add_hook("basement_monica_after_sleep_dialogue", "ep22_dialogues2_3a", scene="global")
    $ add_hook("Dick_Life_evening", "Dick_Life_evening2", scene="global", lable="dick_no_evening")
    $ questLog(21, True)
    $ remove_objective("dick_money_tomorrow")
    $ map_enabled = True
    $ unfocus_map()
    call refresh_scene_fade()
    return

label ep22_quests_Dick2:
    if act == "l":
        return
    call ep22_dialogues5_4()
#    $ add_object_to_scene("DickSecretary", {"type":2, "base":"Office_Dick_Cabinet_Dick_Secretary_Monica_Whore_1_Secretary", "click" : "dick_office_cabinet_environment", "actions" : "lt", "zorder" : 11}, scene="dick_office_cabinet")
    $ move_object("DickSecretary", "dick_office_cabinet")
    $ add_hook("Door", "ep22_dialogues5_5", scene="dick_office_secretary", label="dicksecretary_stage2")
    $ add_hook("Teleport_Entrance", "ep22_quests_Dick4", scene="dick_office_hall1", label="dicksecretary_stage2")
    call change_scene("dick_office_secretary", "Fade_long")
    return

label ep22_quests_Dick3: #открываем дверь у Дика
    $ remove_hook()
    $ remove_hook(label="dicksecretary_stage1")
    return

label ep22_quests_Dick4:
    $ store_music()
    call ep22_dialogues5_6()
    $ remove_hook(label="dicksecretary_stage2")
    $ move_object("DickSecretary", "dick_office_secretary")
    $ add_hook("Teleport_Entrance", "ep22_dialogues5_6a", label="dicksecretary_stage3")
    $ add_hook("DickSecretary", "ep22_dialogues5_6a", scene="dick_office_secretary", label = "dicksecretary_stage3")
    $ add_hook("DickTheLawyer", "ep22_quests_Dick5", scene="dick_office_cabinet", label = "dicksecretary_stage3")
    $ dickOfficeHallMonicaSuffix = 2 #default 1
    $ dickOfficeSecretaryMonicaSuffix = 3 #default1
    $ dickOfficeMonicaState = 3
    call refresh_scene_fade()
    return False

label ep22_quests_Dick5:
    if act=="l":
        return
    $ restore_music()
    call ep22_dialogues5_7()
    $ remove_hook(label="dicksecretary_stage3")
    $ add_hook("Door", "ep22_dialogues5_8", scene="dick_office_secretary", label="dick_resticted_for_monica")
    $ add_hook("Teleport_Hall", "ep22_dialogues5_8a", scene="dick_office_secretary", label="dicksecretary_stage4")
    $ add_hook("DickSecretary", "ep22_dialogues5_8b", scene="dick_office_secretary")
    $ add_hook("DickSecretary", "ep22_quests_Dick6", scene="dick_office_secretary", label="dicksecretary_stage4")

    call change_scene("dick_office_secretary")
    return
label ep22_quests_Dick6:
    if act=="l":
        return
    call ep22_dialogues5_9()
    $ remove_hook(label="dicksecretary_stage4")
    $ autorun_to_object("ep22_dialogues5_9a", scene="street_dick_office")
    $ dickOfficeHallMonicaSuffix = 1
    $ dickOfficeSecretaryMonicaSuffix = 4

    $ add_objective("money_for_victoria", _("Заработать $ 5000 для Виктории до Пятницы!"), c_pink, 10)

    #Инициализация регулярного поведения Виктории
    $ add_hook_day("ep22_quests_Dick7", week_day = 6) #каждую субботу утром будет проверка на деньги для Виктории
    if week_day == 7:
        $ monicaEarnedWeeklyMoneySkip = True
    $ add_hook("DickSecretary", "ep22_quests_Dick8", scene="dick_office_secretary")
    $ add_hook("open", "ep22_quests_Dick9", scene="dick_office_secretary")
    $ add_hook("Monica", "ep22_dialogues5_13a", scene="dick_office_hall1")
    $ add_hook("change_time_day", "ep22_quests_Dick10", scene="global")
    $ add_hook("open", "ep22_quests_Dick11", scene="street_house_main_yard")
    $ add_hook("map_teleport", "ep22_quests_Dick12", scene="global")
    $ remove_hook(lable = "dick_no_evening")
    $ rain = True
    $ rainIntencity = 3
    $ lightning = False
    $ questLog(21, False)
    $ questLog(12, True)
    $ monicaNeedToAskMelanieForHelp = True
    call refresh_scene_fade()
    return False

label ep22_quests_Dick7:
    # Пятничная проверка на деньги для Виктории
    if monicaEarnedWeeklyMoneySkip == True:
        $ monicaEarnedWeeklyMoneySkip = False
        return
    if monicaEarnedWeeklyMoney == True: #если деньги для Виктории заработаны
        $ monicaEarnedWeeklyMoney = False #Виктория их тратит
        $ monicaWeeklyMoneySpent = True
        $ notif(_("Виктория потратила деньги Моники на шоппинг. Она ждет деньги снова до следующей пятницы."))
        $ add_char_progress("DickSecretary", monicaVictoriaEarnedWeeklyMoneyProgress, "monicaVictoriaEarnedWeeklyMoneyProgress " + str(day))
        $ add_objective("money_for_victoria", _("Заработать $ 5000 для Виктории до Пятницы!"), c_pink, 10)
    else:
        #если деньги не заработаны
        $ monicaVictoriaPunishmentPlanned = True # Моника заслужила наказание
        $ monicaWeeklyMoneySpent = False # Виктория не потратила деньги, потому что их нет

    return

label ep22_quests_Dick8: #регулярный разговор с Викторией
    if act=="l":
        return
    if monicaVictoriaPunishmentPlanned == True: #наказание
        $ monicaVictoriaPunishmentPlanned = False
        call ep22_dialogues5_12()
        call refresh_scene_fade()
        return False
    if week_day != 5:
        call ep22_dialogues5_10()
        call refresh_scene_fade()
        return False
    else:
        call ep22_dialogues5_11()
        call refresh_scene_fade()
        return False
    return

label ep22_quests_Dick9: #поза Моники перед Викторией
    if monicaVictoriaPunishmentPlanned == True: #наказание
        $ dickOfficeSecretaryMonicaSuffix = 3
    else:
        $ dickOfficeSecretaryMonicaSuffix = 4
    return

label ep22_quests_Dick10: #rain off and enable Biff
    call ep22_quests_office7()
    $ rain = False
    $ rainIntencity = 1
    $ lightning = False
    $ basementBedSkipUntilFridayEnabled = True #включаем возможность пропускания дней до пятницы
    $ remove_hook()
    return

label ep22_quests_Dick11: #уменьшение дождя в доме
    if rain == True:
        $ rainIntencity = 1
        $ lightning = False
    return

label ep22_quests_Dick12: #сцена секса Виктории с Диком
    $ remove_hook()
    call ep22_dialogues5_14()
    $ lightning = True
    $ changeDayTime("evening")
    return True
