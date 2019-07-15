default monicaKissedBiff = False

label ep26_quests_biff1:
    # Инициализируем разговор о работе в офисе
    $ add_hook("Biff", "ep26_quests_biff2", scene="monica_office_cabinet_table", label="biff_work_dialogue1")
    return

label ep26_quests_biff2:
    # Разговор с Бифом о работе
    if act=="l":
        return
    if cloth != "CasualDress1":
        call ep26_dialogues5_office1_1a2() # Говорим о том что надо одеть платье
        return

    call process_hooks("photoshoots_work_available_check", "global")
    if biffWeeklyPhotoShootEnabled == False or _return == False:
        return

    call ep26_dialogues5_office1_2()
    if _return == False:
        call change_scene("monica_office_secretary")
        return False
    # Начинаем подготовку к работе
    # Моника идет к секретарше

    $ remove_hook(label="biff_work_dialogue1")

    # блокируем выходы
    $ add_hook("Teleport_Monica_Office_Entrance", "ep26_dialogues5_office1_1a", scene="monica_office_secretary", label="biff_work_block1")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep26_dialogues5_office1_1a", scene="monica_office_secretary", label="biff_work_block1")
    $ add_hook("Secretary", "ep26_quests_biff3", scene="monica_office_secretary")
    call change_scene("monica_office_secretary")

    return False

label ep26_quests_biff3:
    # Говорим с секретаршей
    if act=="l":
        return
    $ remove_hook()
    call ep26_dialogues5_office1_2b()
    $ remove_hook(label="biff_work_block1")
    # блокируем выходы
    $ add_hook("Teleport_Monica_Office_Entrance", "ep26_dialogues5_office1_2a", scene="monica_office_secretary", label="biff_work_block2")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep26_dialogues5_office1_2a", scene="monica_office_secretary", label="biff_work_block2")
    $ add_hook("Secretary", "ep26_dialogues5_office1_2a", scene="monica_office_secretary", label="biff_work_block2")

    $ add_hook("AlexPhotograph", "ep26_quests_biff4", scene="monica_office_photostudio")
    return False

label ep26_quests_biff4:
    # Говорим с Алексом
    if act=="l":
        return
    $ remove_hook()
    call ep26_dialogues5_office1_3()
    $ remove_hook(label="biff_work_block2")
    $ add_hook("Teleport_Monica_Office_Entrance", "ep26_dialogues5_office1_1a", scene="monica_office_secretary", label="biff_work_block3")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep26_dialogues5_office1_1a", scene="monica_office_secretary", label="biff_work_block3")

    $ add_hook("Secretary", "ep26_quests_biff5", scene="monica_office_secretary")
    call put_work_clothes() # Одеваем Монику в рабочую одежду

    return False

label ep26_quests_biff5:
    # Говорим с секретаршей
    if act=="l":
        return
    $ remove_hook()
    call ep26_dialogues5_office1_4()
    $ remove_hook(label="biff_work_block3")

    # возвращаем Мелани
    call ep26_quests_melanie1()

    $ monicaWorkingAtBiffOffice = True

    # инициализируем работу в офисе
    call office_work_init()
    call ep26_quests_office1()

    $ add_hook("before_open", "ep26_quests_biff6", scene="monica_office_cabinet_table", label=["check_bill_at_place", "check_bill_at_place_cabinet_table"], priority=150)
    return False

label ep26_quests_biff6:
    # Проверяем наличие Бифа в офисе днем при переходе по миникарте
    call ep22_dialogue6_2b()
    if _return == False:
        call change_scene("monica_office_secretary")
    return








#
