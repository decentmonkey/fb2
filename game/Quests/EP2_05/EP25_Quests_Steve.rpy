default monicaMadeBlowjobForSteveChair = False
default monicaSteveCumDealActive = False
default monicaSteveCumDealRejected = False # Моника решила осуществить сделку, но позже отказалась от нее
default monicaSteveCumDealCompleted = False # Моника закрыла сделку

default monicaSteveBlowjobDealCount = 0 # Кол-во сделок со Стивом blowjob

label ep25_quests_steve1:
    # инициализация сцен и входа
    call locations_init_steve_office()
    $ move_object("Steve", "empty")
    $ add_hook("Teleport_Building", "ep25_quests_steve2", scene = "street_steve_office", priority = 200, label="steve_office_check_evening")
    $ add_hook("Teleport_Building", "ep25_quests_steve3", scene="street_steve_office", label = "steve_office_enter")

    $ move_object("Jane", "steve_office_secretary")

    $ add_hook("Jane", "ep25_quests_steve5", scene="steve_office_secretary", label="jane_dialogue_regular1")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve5", scene="steve_office_secretary", label="jane_dialogue_regular1")
    $ add_hook("Jane", "ep25_quests_steve4", scene="steve_office_secretary", label="jane_dialogue1")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve4", scene="steve_office_secretary", label="jane_dialogue1")
    $ add_hook("open", "ep25_quests_steve4a", scene="steve_office_secretary")

    $ add_hook("change_time_day", "ep25_quests_steve6", scene="global")
    return

label ep25_quests_steve2:
    # Вход в здание Стива, проверка на вечер
    if act == "l":
        return
    if week_day == 7:
        mt "Сегодня выходной. Офис Стива закрыт."
        return False
    if day_time == "evening":
        mt "Уже вечер. Офис Стива закрыт."
        return False
    return

label ep25_quests_steve3:
    # Вход в офис Стива
    if act == "l":
        return
    if act == "w":
        if cloth != "CasualDress1":
            call ep25_dialogues2_steve1b()
            return False
        call change_scene("steve_office_secretary", "Fade_long", "snd_lift")
    return False


label ep25_quests_steve4:
    # первый разговор с Джейн
    if act=="l" and obj_name=="Jane":
        return
    $ remove_hook(label="jane_dialogue1")
    call ep25_dialogues2_steve1()
    call change_scene("street_steve_office", "Fade_long", "snd_lift")
    $ questLog(33, False)
    $ questLog(40, True)

    return False

label ep25_quests_steve4a:
    # Музыка входа Моники
    $ remove_hook()
    music m80s_Things
    return

label ep25_quests_steve5:
    # регулярный разговор с Джейн 1
    if act=="l" and obj_name == "Jane":
        return
    call ep25_dialogues2_steve1a()
    call refresh_scene_fade()
    return False

label ep25_quests_steve6:
    # Инициализация второго прихода Моники с утра
    $ remove_hook()
    $ add_hook("Jane", "ep25_quests_steve7", scene="steve_office_secretary", label="jane_dialogue2")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve7", scene="steve_office_secretary", label="jane_dialogue2")
    return

label ep25_quests_steve7:
    # Второй диалог с Джейн (приходит Тиффани)
    if act=="l" and obj_name == "Jane":
        return
    $ remove_hook(label="jane_dialogue2")
    call ep25_dialogues2_steve2()

    $ autorun_to_object("ep25_dialogues2_steve2a", scene="street_steve_office")
    $ add_hook("change_time_day", "ep25_quests_steve8", scene="global") # Третьий приход Моники (инициализация с утра)
    call change_scene("street_steve_office", "Fade_long", "snd_lift")
    return False

label ep25_quests_steve8:
    # Инициализация третьего прихода Моники с утра
    $ remove_hook()
    $ add_hook("Jane", "ep25_quests_steve9", scene="steve_office_secretary", label="jane_dialogue3")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve9", scene="steve_office_secretary", label="jane_dialogue3")
    $ steve_office_secretary_suffix = 2
    return


label ep25_quests_steve9:
    # Третий разговор с Джейн (заходит к Стиву)
    if act=="l" and obj_name == "Jane":
        return
    $ remove_hook(label="jane_dialogue3")
    call ep25_dialogues2_steve3()
    $ monicaHasSexWithSteveBasement = False # debug!!
    if monicaHasSexWithSteveBasement == True: # У Моники был секс со Стивом
        call ep25_dialogues2_steve4()
        $ move_object("Steve", "steve_office_office_table")
        $ add_hook("Steve", "ep25_quests_steve10", scene="steve_office_office_table", label="steve_office_steve_dialogue1")
        $ add_hook("Door", "ep25_quests_steve10", scene="steve_office_office_table", label="steve_office_steve_dialogue1")
        call change_scene("steve_office_office_table", "Fade_long", False)
        return False
    else:
        # Секса со Стивом не было
        call ep25_dialogues2_steve10()
        if _return == True: # Моника сделала минет Стиву
            $ notif("Стив перевел деньги Виктории.")
            $ monicaEarnedWeeklyMoney = True
            $ remove_hook("DickSecretary_Dialogue1_Menu", "ep24_quests_steve28", scene="menu") # Убираем из меню Виктории вопрос про деньги Стива


        $ questLog(40, False)
        $ questLog(42, True)
        # Регулярный приход к Стиву
        $ add_hook("Teleport_Building", "ep25_quests_steve15", scene="street_steve_office", label="steve_office_blocked_today") # Блокируем вход в здание на сегодня
        $ add_hook("change_time_day", "ep25_quests_steve16", scene="global") # Релуярный приход Моники (инициализация с утра)
        call change_scene("street_steve_office", "Fade_long", "snd_lift")
#    $ monicaHasSexWithSteveBasement = True
#            $ monicaSteveBasementOffended = True

    return False

label ep25_quests_steve10:
    # Разговор со Стивом (секс был)
    if act=="l":
        return
    $ remove_hook(label="steve_office_steve_dialogue1")
    call ep25_dialogues2_steve4a()
    if _return == False:
        # Моника не делала минет. Добилась денег угрозой
        $ questLog(40, False)
        $ questLog(42, True)
        $ notif("Стив перевел деньги Виктории.")
        $ monicaEarnedWeeklyMoney = True
        $ remove_hook("DickSecretary_Dialogue1_Menu", "ep24_quests_steve28", scene="menu") # Убираем из меню Виктории вопрос про деньги Стива

        # Регулярный приход к Стиву
        $ add_hook("Teleport_Building", "ep25_quests_steve15", scene="street_steve_office", label="steve_office_blocked_today") # Блокируем вход в здание на сегодня
        $ add_hook("change_time_day", "ep25_quests_steve16", scene="global") # Релуярный приход Моники (инициализация с утра)

        call change_scene("street_steve_office", "Fade_long", "snd_lift")
        return False
    else:
        # Моника сделала минет, но Стив деньги не послал
        $ autorun_to_object("ep25_dialogues2_steve5", scene="street_steve_office")
        call change_scene("street_steve_office", "Fade_long", "snd_lift")
        $ add_hook("Teleport_Building", "ep25_dialogues2_steve5a", scene="street_steve_office", label="need_check_steve_money1") # Блокируем вход в здание пока не проверили деньги
        $ remove_hook("DickSecretary_Dialogue1_Menu", "ep24_quests_steve28", scene="menu") # Убираем из меню Виктории вопрос про деньги Стива
        $ add_hook("DickSecretary_Dialogue1_Menu", "ep25_quests_steve11", scene="menu", label="need_check_steve_money_victoria1", caption=_("Стив прислал деньги."), priority=95) # У Виктории спрашиваем про деньги Стива (новый диалог)

    return

label ep25_quests_steve11:
    # Моника разговаривает с Викторией о деньгах от Стива
    call ep25_dialogues2_steve6()
    $ remove_hook(label="need_check_steve_money1") # Разблокируем вход к Стиву
    $ add_hook("Jane", "ep25_quests_steve12", scene="steve_office_secretary", label="jane_dialogue4")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve12", scene="steve_office_secretary", label="jane_dialogue4")
    return False

label ep25_quests_steve12:
    # Разговор с Джейн в 4-ый раз
    if act=="l" and obj_name == "Jane":
        return
    $ remove_hook(label="need_check_steve_money_victoria1") # Убираем у Виктории вопрос про деньги
    $ add_hook("change_time_day", "ep25_quests_steve13", scene="global") # Пятый приход Моники (инициализация с утра)
    call ep25_dialogues2_steve7()
    return False

label ep25_quests_steve13:
    # Пятый приход Моники (иницилизация с утра)
    $ remove_hook()
    $ remove_hook(label="jane_dialogue4")
    $ add_hook("Jane", "ep25_quests_steve14", scene="steve_office_secretary", label="jane_dialogue5")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve14", scene="steve_office_secretary", label="jane_dialogue5")
    return

label ep25_quests_steve14:
    # Пятый диалог с Джейн (заходит к Стиву) (Стив не прислал деньги за минет)
    if act=="l" and obj_name == "Jane":
        return
    $ remove_hook(label="jane_dialogue5")
    call ep25_dialogues2_steve8()
    if _return == True:
        $ autorun_to_object("ep25_dialogues2_steve9", scene="street_steve_office")
    call change_scene("street_steve_office", "Fade_long", "snd_lift")
    $ add_hook("Teleport_Building", "ep25_quests_steve15", scene="street_steve_office", label="steve_office_blocked_today") # Блокируем вход в здание на сегодня
    $ add_hook("change_time_day", "ep25_quests_steve16", scene="global") # Релуярный приход Моники (инициализация с утра)
    $ monicaSteveCumDealActive = True
    $ questLog(40, False)
    $ questLog(41, True)

    return False

label ep25_quests_steve15:
    # Блок на вход в офис Стива сегодня
    call ep25_dialogues2_steve11()
    return False

label ep25_quests_steve16:
    $ remove_hook()
    $ remove_hook(label="steve_office_blocked_today") # Убираем блок с офиса Стива
    $ steve_office_secretary_suffix = 1 # Джейн сидит
    $ remove_hook(label="jane_dialogue_regular1")
    $ add_hook("Jane", "ep25_quests_steve17", scene="steve_office_secretary", label="jane_dialogue_regular2") # Регулярный диалог с Джейн
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve18", scene="steve_office_secretary", label="jane_dialogue_regular2") # Регулярный телепорт в офис Стива мимо Джейн
    call Steve_init() # Инициализируем Стива
    $ add_hook("steve_office_dialogue", "ep25_quests_steve16a", scene="global", label="steve_first_regular_dialogue_remove_victoria_menu") # При первом регулярном разговоре со Стивом убираем упоминание про деньги у Виктории
    return

label ep25_quests_steve16a:
    # При первом регулярном разговоре со Стивом убираем упоминание про деньги у Виктории
    $ remove_hook()
    $ remove_hook("DickSecretary_Dialogue1_Menu", "ep24_quests_steve28", scene="menu") # Убираем из меню Виктории вопрос про деньги Стива
    return

label ep25_quests_steve17:
    # Регулярный диалог с Джейн 2
    if act == "l" and obj_name == "Jane":
        return
    call getSteveStatus()
    call ep25_dialogues3_steve1(_return)
    if _return == 0:
        call change_scene("street_steve_office", "Fade_long", "snd_lift")
        return False
    call refresh_scene_fade()
    return False

label ep25_quests_steve18:
    # Регулярный вход в офис Стива по телепорту
    call getSteveStatus()
    if _return != 0:
        call ep25_dialogues3_steve1(_return)
        call ep25_dialogues3_steve1aa()
        if _return == True:
            music Groove2_85
            call change_scene("steve_office_office", "Fade_long")
        else:
            call change_scene("street_steve_office", "Fade_long", "snd_lift")
        return False

    # Регулярный разговор со Стивом
    call process_hooks("steve_office_dialogue", "global")
    if _return == False:
        return False
    call ep25_dialogues3_steve1a()
    if _return == 0:
        call change_scene("street_steve_office", "Fade_long", "snd_lift")
        return False
    if _return == 1: # Моника закрывает cum сделку
        call ep25_dialogues3_steve1b()
        if _return == False:
            call ep25_quests_steve19() # Блокируем офис на сегодня (день)
            call change_scene("street_steve_office", "Fade_long", "snd_lift")
            return False

        $ monicaSteveCumDealActive = False
        $ monicaSteveCumDealCompleted = True
        $ notif("Стив перевел деньги Виктории.")
        $ monicaEarnedWeeklyMoney = True
        $ questLog(40, False)
        $ questLog(41, False)
        $ questLog(42, True)
        call ep25_quests_steve19() # Блокируем офис на сегодня (день)
        call change_scene("street_steve_office", "Fade_long", "snd_lift")
        return False

    if _return == 2: # Сделка со Стивом (blowjob)
        call ep25_dialogues3_steve2()
        if _return == False:
            call ep25_quests_steve19() # Блокируем офис на сегодня (день)
            call change_scene("street_steve_office", "Fade_long", "snd_lift")
            return False
        $ choosedMoney = _return
        if monicaSteveBlowjobDealCount == 0:
            # Первый приход Джейн
            call ep25_dialogues3_steve3a()
        if monicaSteveBlowjobDealCount == 1:
            call ep25_dialogues3_steve4a()
        if monicaSteveBlowjobDealCount == 2:
            call ep25_dialogues3_steve3b()
        if monicaSteveBlowjobDealCount == 3:
            call ep25_dialogues3_steve4b()
        if monicaSteveBlowjobDealCount == 4:
            call ep25_dialogues3_steve3c()
        if monicaSteveBlowjobDealCount == 5:
            call ep25_dialogues3_steve4c()
        if monicaSteveBlowjobDealCount > 5:
            # random
            $ rnd1 = rand(1,6)
            if rnd1 == 1:
                call ep25_dialogues3_steve3a()
            if rnd1 == 2:
                call ep25_dialogues3_steve4a()
            if rnd1 == 3:
                call ep25_dialogues3_steve3b()
            if rnd1 == 4:
                call ep25_dialogues3_steve4b()
            if rnd1 == 5:
                call ep25_dialogues3_steve3c()
            if rnd1 == 6:
                call ep25_dialogues3_steve4c()

        $ monicaSteveBlowjobDealCount +=1
        if choosedMoney == 1:
            $ add_money(50.0)
        $ notif("Стив перевел деньги Виктории.")
        $ monicaEarnedWeeklyMoney = True

        call ep25_quests_steve19() # Блокируем офис на сегодня (день)
        call change_scene("street_steve_office", "Fade_long", False)
        return False


    return

label ep25_quests_steve19:
    # Закрываем офис Стива до вечера
    $ add_hook("Teleport_Building", "ep25_quests_steve15", scene="street_steve_office", label="day_time_temp") # Блокировка офиса до вечера
    return




#
