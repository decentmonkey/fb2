default ep26_quests_bardie_day1 = 0
default monicaShowedBoobsToBardie = False
default monicaMadeTitjobBardie = False

label ep26_quests_bardie1:
    # Инициализация квестов 0.6
    if monicaCleaningInProgressEngineWorkingFlag == True: # Если идет уборка, вешаем эту функцию на событие после окончания уборки
        $ add_hook("monica_cleaning_end", "ep26_quests_bardie1", scene="global")
        return

    # Барди шантажирует Бетти. Может быть я могу использовать это?
    $ questLog(44, True)
    $ add_hook("Bardie_Life_day", "Bardie_Life_Day6", scene="global", label="bardie_day_street_yard") # Барди днем все время во дворе
    $ add_hook("before_open", "ep26_quests_bardie2", scene="bedroom_bardie") # Разговор с Барди в комнате
    $ add_hook("Bardie", "ep26_quests_bardie2b", scene="bedroom_bardie", label="ep26_bardie_pre_dialogue1")
    return

label ep26_quests_bardie1a:
    $ remove_hook()
    call ep26_quests_bardie1()
    return

label ep26_quests_bardie2:
    # Первый разговор с Барди по поводу еды в доме, Барди дрочит
    if day_time == "day":
        return
    if cloth != "Governess":
        $ autorun_to_object("ep26_quests_bardie2a", scene="bedroom_bardie")
        return
    $ remove_hook()
    $ remove_hook(label="ep26_bardie_pre_dialogue1")
    call ep26_dialogues1_bardie1()
    $ autorun_to_object("ep26_dialogues1_bardie1a", scene="floor2")
    $ add_hook("Bardie", "ep26_quests_bardie3", scene="bedroom_bardie")
    call change_scene("floor2")
    return

label ep26_quests_bardie2a:
    mt "Мне лучше переодеться сначала."
    mt "В таком виде Барди от меня точно попросит чего-нибудь неприличного..."
    return

label ep26_quests_bardie2b:
    call ep26_quests_bardie2a()
    return False

label ep26_quests_bardie3:
    # Моника заходит к Барди второй раз. После того как увидела что он дрочит.
    if cloth != "Governess":
        call ep26_quests_bardie2a()
        return False
    call ep26_dialogues1_bardie2()
    if _return == 0: # Моника ушла вначале
        $ autorun_to_object("ep26_dialogues1_bardie3a", scene="floor2")
        call change_scene("floor2")
        return False
    if _return == 1 or _return == 2: # Наказание
        call ep24_dialogues4_bardie4()
        if _return != False:
            $ basement_bedroom2_MonicaSuffix = 2
            call change_scene("basement_bedroom2", "Fade_long", False)
        return False
    if _return == 3:
        $ autorun_to_object("ep26_dialogues1_bardie3", scene="floor2")
        call change_scene("floor2")
        $ remove_hook("Bardie", "ep26_quests_bardie3", scene="bedroom_bardie")
        $ add_hook("Bardie", "ep26_quests_bardie4", scene="bedroom_bardie", label="ep26_bardie_dialogue3")
        $ ep26_quests_bardie_day1 = day


    return False

label ep26_quests_bardie4:
    # Моника заходит третий раз и делает titjob
    if ep26_quests_bardie_day1 == day:
        call ep26_dialogues1_bardie3()
        return False
    if cloth != "Governess":
        call ep26_quests_bardie2a()
        return False
    call ep26_dialogues1_bardie4()
    if _return == 0 or _return == 1: # Просто ушла вначале
        call change_scene("floor2", "Fade_long")
        return False
    if _return == 2: # Все завершено
        $ move_object("Bardie", "empty")
        call change_scene("floor2", "Fade_long", "snd_runaway")
        $ remove_hook(label="ep26_bardie_dialogue3")
        $ add_hook("Bardie", "ep26_quests_bardie5", scene="bedroom_bardie", label="ep26_bardie_dialogue4")
        return False


    return False

label ep26_quests_bardie5:
    # Моника заходит четвертый раз и узнает какое условие питания в доме
    if cloth != "Governess":
        call ep26_quests_bardie2a()
        return False
    call ep26_dialogues1_bardie5()
    if _return == 1: # Наказание
        call ep24_dialogues4_bardie4()
        if _return != False:
            $ basement_bedroom2_MonicaSuffix = 2
            call change_scene("basement_bedroom2", "Fade_long", False)
        return False

    if _return == 2: # Все ок, инициализируем Бетти
        $ questLog(44, False)
        $ remove_hook(label="ep26_bardie_dialogue4")
        $ add_hook("Bardie", "ep26_quests_bardie6", scene="bedroom_bardie", label="ep26_bardie_dialogue5_betty_kitchen")
        $ autorun_to_object("ep26_dialogues1_bardie5a", scene="floor2")
        call ep26_quests_betty1() # Инициализация питания на кухне
        call change_scene("floor2", "Fade_long")
        return False
    return False

label ep26_quests_bardie6:
    # Приход к Барди из-за Бетти на кухне
    return









#
