default basement_monica_after_sleep_dialogue1_skip = True
default basementBedroomMonicaNapGfx = False
default basementBedroomMonicaNapGfxBettyPanties = False
default basementBedroomMonicaSleepGfx = False
default basementBedNapIndex = 0
default basementBedSleepIndex = 0

label basement_bed_hook:
    if act == "l":
        return True
    if act == "h":
        if day_time == "day":
            call monica_take_nap() from _call_monica_take_nap
            return _return
        if day_time == "evening":
            call monica_gosleep1() from _call_monica_gosleep1
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
    if cloth == "GovernessPants" and monicaBettyPanties == True:
        $ basementBedroomMonicaNapGfxBettyPanties = True
    $ basementBedroomMonicaNapGfx = True
    call basement_monica_nap_transition1() from _call_basement_monica_nap_transition1
    $ autorun_to_object("monica_take_nap1")
    return False
label monica_take_nap1:
    $ set_active("BasementBed", True, scene="basement_bedroom2")
    $ basement_bedroom2_MonicaSuffix = 2
    menu:
        "Лечь и ждать вечера.":
            $ basementBedroomMonicaNapGfx = False
            $ basementBedroomMonicaNapGfxBettyPanties = False
            #транзиция на отдых
            call process_hooks("basement_monica_before_nap", "global") from _call_process_hooks_29
            if _return == False:
                $ basement_bedroom2_MonicaSuffix = 2
                call refresh_scene_fade() from _call_refresh_scene_fade_43
                return False
            $ changeDayTime("evening")
            call process_hooks("basement_monica_after_nap", "global") from _call_process_hooks_30
            call refresh_scene_fade() from _call_refresh_scene_fade_44
            return False
        "Не ложиться.":
            $ basementBedroomMonicaNapGfx = False
            $ basementBedroomMonicaNapGfxBettyPanties = False
            call refresh_scene_fade() from _call_refresh_scene_fade_45
            return False
    return

label monica_gosleep1:
    #если Моника голодная
    if monicaEatedLastDay < day:
        if day - monicaEatedLastDay >= 3 and (monicaCantSleepHungry == True or debugMode == False):
            #если Моника не ела 3 дня
            $ autorun_to_object("basement_monica_hungry_cant_sleep")
            call refresh_scene_fade() from _call_refresh_scene_fade_46
            return False
        else:
            $ basement_bedroom2_MonicaSuffix = 2
            $ basementBedroomMonicaSleepGfx = True
            call basement_monica_sleep_transition1() from _call_basement_monica_sleep_transition1
            $ autorun_to_object("monica_gosleep1a")
            return False
    $ basementBedroomMonicaSleepGfx = True
    call basement_monica_sleep_transition1() from _call_basement_monica_sleep_transition1_1
    $ autorun_to_object("monica_gosleep1b")
    return False
label monica_gosleep1a:
    $ set_active("BasementBed", True, scene="basement_bedroom2")
    mt "Я сегодня ничего не ела! Лечь спать голодной?"
    menu:
        "Лечь спать голодной.":
            $ basementBedroomMonicaSleepGfx = False
            call process_hooks("basement_monica_before_sleep", "global") from _call_process_hooks_31
            if _return == False:
                $ basement_bedroom2_MonicaSuffix = 2
                call refresh_scene_fade() from _call_refresh_scene_fade_47
                return False
            call processHouseCleaningEvening() from _call_processHouseCleaningEvening
            if cloth != "Nude":
                $ cloth_type = "Nude"
                $ cloth = "GovernessPants"
            $ changeDayTime("day")
            call process_hooks("basement_monica_after_sleep", "global") from _call_process_hooks_32
            call refresh_scene_fade() from _call_refresh_scene_fade_48
            return False
        "Не ложиться.":
            $ basementBedroomMonicaSleepGfx = False
            call refresh_scene_fade() from _call_refresh_scene_fade_49
            return False

label monica_gosleep1b:
    $ set_active("BasementBed", True, scene="basement_bedroom2")
    $ basement_bedroom2_MonicaSuffix = 2
    menu:
        "Лечь спать.":
            $ basementBedroomMonicaSleepGfx = False
            call process_hooks("basement_monica_before_sleep", "global") from _call_process_hooks_33
            if _return == False:
                $ basement_bedroom2_MonicaSuffix = 2
                call refresh_scene_fade() from _call_refresh_scene_fade_50
                return False
            call processHouseCleaningEvening() from _call_processHouseCleaningEvening_1
            if cloth != "Nude":
                $ cloth_type = "Nude"
                $ cloth = "GovernessPants"
            $ changeDayTime("day")
            call process_hooks("basement_monica_after_sleep", "global") from _call_process_hooks_34
            call refresh_scene_fade() from _call_refresh_scene_fade_51
            return False
        "Не ложиться.":
            $ basementBedroomMonicaSleepGfx = False
            call refresh_scene_fade() from _call_refresh_scene_fade_52
            return False
    return False

label basement_monica_nap_transition1:
#    $ basementBedNapIndex = rand(1,4)
    $ basementBedNapIndex = ((day+1)%4) + 1
    $ set_active("BasementBed", False, scene="basement_bedroom2")
    call refresh_scene("Dissolve_05") from _call_refresh_scene_9
    return
#    img black_screen
#    with Dissolve(0.5)
#    call refresh_scene_fade()
    return
label basement_monica_sleep_transition1:
    $ basementBedSleepIndex = ((day+1)%4) + 1
    $ set_active("BasementBed", False, scene="basement_bedroom2")
    call refresh_scene("Dissolve_05") from _call_refresh_scene_10
#    img black_screen
#    with Dissolve(0.5)
#    call refresh_scene_fade()
    return

label basement_monica_after_nap:
    $ autorun_to_object("basement_monica_after_nap_dialogue")
    return

label basement_monica_after_nap_dialogue:
    call process_hooks("basement_monica_after_nap_dialogue", "global") from _call_process_hooks_35
    return
label basement_monica_after_nap_dialogue1:
    if day - monicaEatedLastDay >= 2:
        mt "Неплохо было бы что-то поесть..."
    else:
        mt "Я передохнула. Что дальше?"
    return

label basement_monica_after_sleep:
    $ autorun_to_object("basement_monica_after_sleep_dialogue")
    return
label basement_monica_after_sleep_dialogue:
    call process_hooks("basement_monica_after_sleep_dialogue", "global") from _call_process_hooks_36
    return

label basement_monica_after_sleep_dialogue1:
    #Моника встает с утра
#    if basement_monica_after_sleep_dialogue1_skip == True:
#        $ basement_monica_after_sleep_dialogue1_skip = False
#        return
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
    mt "{c}Я не ела{/c} уже третий день!"
    "Я не могу лечь спать в таком состоянии!"
    "Я ХОЧУ ЕСТЬ!!!"
    "..."
    mt "Может быть я смогу что-то найти на заправке?"
    mt "Или у кого-нибудь занять деньги на еду?"
    return
