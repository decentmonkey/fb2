default basement_monica_after_sleep_dialogue1_skip = True

label basement_bed_hook:
    if act == "l":
        return True
    if act == "h":
        if day_time == "day":
            call monica_take_nap()
            return _return
        if day_time == "evening":
            call monica_gosleep1()
            return _return
    return


label monica_wakeup1:
    #Моника встает с утра
    mt "Еще одно утро в этой дыре! Мне надо что-то придумать, чтобы вернуть все назад как было!"

    mt "Я не высыпаюсь на этой кровати."
    "Мне нужна нормальная постель!"

    mt "Такая королева как я не может привыкнуть спать в таких условиях!"
    "Я заслуживаю лучшего!"

    mt "Это мой дом! Я не заслуживаю того чтобы спать в подвале!"

    mt "Мне надо что-то придумать, чтобы вернуть все назад как было!"
    return

label monica_take_nap:
    menu:
        "Лечь и ждать вечера.":
            #транзиция на отдых
            call basement_monica_nap_transition1()
            $ changeDayTime("evening")
            return False
        "Не ложиться.":
            return False
    return

label monica_gosleep1:
    #если Моника голодная
    if monicaEatedLastDay < day:
        if day - monicaEatedLastDay >= 3:
            #если Моника не ела 3 дня
            $ autorun_to_object("basement_monica_hungry_cant_sleep")
            call refresh_scene_fade()
            return False
        else:
            mt "Я сегодня ничего не ела! Лечь спать голодной?"
            menu:
                "Лечь спать голодной.":
                    if cloth != "Nude":
                        $ cloth_type = "Nude"
                        $ cloth = "GovernessPants"
                    call basement_monica_sleep_transition1()
                    $ changeDayTime("day")
                    return False
                "Не ложиться.":
                    return False
    menu:
        "Лечь спать.":
            if cloth != "Nude":
                $ cloth_type = "Nude"
                $ cloth = "GovernessPants"
            call basement_monica_sleep_transition1()
            $ changeDayTime("day")
            return False
        "Не ложиться.":
            return False
    return False

label basement_monica_nap_transition1:
    img black_screen
    with Dissolve(0.5)
    $ basement_bedroom2_MonicaSuffix = 2
    call refresh_scene_fade()
    return
label basement_monica_sleep_transition1:
    img black_screen
    with Dissolve(0.5)
    $ basement_bedroom2_MonicaSuffix = 2
    call refresh_scene_fade()
    return

label basement_monica_after_nap:
    $ autorun_to_object("basement_monica_after_nap_dialogue1")
    return
label basement_monica_after_nap_dialogue1:
    if day - monicaEatedLastDay >= 2:
        mt "Неплохо было бы что-то поесть..."
    else:
        mt "Я передохнула. Что дальше?"
    return

label basement_monica_after_sleep:
    $ autorun_to_object("basement_monica_after_sleep_dialogue1")
    return

label basement_monica_after_sleep_dialogue1:
    #Моника встает с утра
    if basement_monica_after_sleep_dialogue1_skip == True:
        $ basement_monica_after_sleep_dialogue1_skip = False
        return
    $ rnd = rand(1,5)
    if rnd == 1:
        mt "Еще одно утро в этой дыре! Мне надо что-то придумать, чтобы вернуть все назад как было!"

    if rnd == 2:
        mt "Я не высыпаюсь на этой кровати."
        "Мне нужна нормальная постель!"

    if rnd == 3:
        mt "Такая королева как я не может привыкнуть спать в таких условиях!"
        "Я заслуживаю лучшего!"

    if rnd == 4:
        mt "Это мой дом! Я не заслуживаю того чтобы спать в подвале!"

    if rnd == 5:
        mt "Мне надо что-то придумать, чтобы вернуть все назад как было!"
    return

label basement_monica_hungry_cant_sleep:
    #если Моника не ела 3 дня
    mt "{b}Я не ела{/b} уже третий день!"
    "Я не могу лечь спать в таком состоянии!"
    "Я ХОЧУ ЕСТЬ!!!"
    return
