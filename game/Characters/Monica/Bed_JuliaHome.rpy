label juliahome_bed:
    if act=="l":
        return
    if act == "h":
        $ monicaRestJuliaHome = True
        $ monicaRestJuliaHomeDay = day
        $ monicaRestHouse = False
        $ monicaRestApartments = False
        if day_time == "day":
            call juliahome_bed_take_nap()
            return _return
        if day_time == "evening":
            call juliahome_bed_gosleep()
            return _return

    return

label juliahome_bed_take_nap:
    $ juliaHomeNapSuffixStored = juliaHomeLivingRoomMonicaSuffix
    $ set_active("Bed1", False)
    $ juliaHomeLivingRoomMonicaSuffix = 4
    $ autorun_to_object("juliahome_bed_take_nap1")
    call refresh_scene("Dissolve_05")
    return

label juliahome_bed_take_nap1:
    menu:
        "Лечь и ждать вечера.":
            music stop
            img black_screen
            with Dissolve(0.2)
            #транзиция на отдых
            call process_hooks("juliahome_monica_before_nap", "global")
            $ set_active("Bed1", True)
            if _return == False:
                $ juliaHomeLivingRoomMonicaSuffix = juliaHomeNapSuffixStored
                call refresh_scene_fade()
                return False
            $ changeDayTimeJuliaHome("evening")
            $ juliaHomeLivingRoomMonicaSuffix = 3
            call process_hooks("juliahome_monica_after_nap", "global")
            call refresh_scene_fade()
            return False
        "Не ложиться.":
            $ juliaHomeLivingRoomMonicaSuffix = juliaHomeNapSuffixStored
            $ set_active("Bed1", True)
            call refresh_scene_fade()
            return False
    return


label juliahome_bed_gosleep:
    $ juliaHomeNapSuffixStored = juliaHomeLivingRoomMonicaSuffix
    $ juliaHomeNapJuliaSuffixStored = juliaHomeLivingRoomJuliaSuffix
    if get_active_objects("Julia", scene="juliahome_livingroom") != False:
        $ juliaHomeLivingRoomMonicaSuffix = 1
        $ juliaHomeLivingRoomJuliaSuffix = 1
    else:
        $ juliaHomeLivingRoomMonicaSuffix = 4

    $ set_active("Bed1", False)
    $ autorun_to_object("juliahome_bed_gosleep1")
    call refresh_scene("Dissolve_05")
    return

label juliahome_bed_gosleep1:
    if monicaEatedLastDay < day:
        if day - monicaEatedLastDay >= 3 and (monicaCantSleepHungry2 == True or debugMode == False) and debugMode == False:
            #если Моника не ела 3 дня
            mt "{c}Я не ела{/c} уже третий день!"
            "Я не могу лечь спать в таком состоянии!"
            "Я ХОЧУ ЕСТЬ!!!"
            $ set_active("Bed1", True)
            $ juliaHomeLivingRoomMonicaSuffix = juliaHomeNapSuffixStored
            $ juliaHomeLivingRoomJuliaSuffix = juliaHomeNapJuliaSuffixStored
            call refresh_scene_fade()
            return False

        else:
            mt "Я сегодня ничего не ела! Лечь спать голодной?"


label juliahome_bed_gosleep1_loop1:
    menu:
        "Поцелуй перед сном." if juliahome_evening_sleep_event_active == True and get_active_objects("Julia", scene="juliahome_livingroom") != False:
            call ep213_quests_julia19_evening_scene()
            call juliahome_bed_gosleep2()
            return

        "Лечь спать." if monicaEatedLastDay == day:
            call juliahome_bed_gosleep2()
            return
        "Поесть и лечь спать." if monicaEatedLastDay < day:
            call juliahome_kitchen_eat_before_sleep()
            call juliahome_bed_gosleep2()
            return
        "Лечь спать голодной." if monicaEatedLastDay < day:
            call juliahome_bed_gosleep2()
            return
        "Пропустить до..." if basementBedSkipUntilFridayEnabled == True and week_day != 5 and week_day != 4:
            menu:
                "Пропустить до Понедельника." if basementBedSkipUntilFridayEnabled == True and week_day > 5 and week_day < 7:
                    $ skipUntilFridayTargetDay = 1
                    jump juliahome_bed_skip_until_day1
                "Пропустить до Вторника." if basementBedSkipUntilFridayEnabled == True and (week_day > 5):
                    $ skipUntilFridayTargetDay = 2
                    jump juliahome_bed_skip_until_day1
                "Пропустить до Среды." if basementBedSkipUntilFridayEnabled == True and (week_day > 5 or week_day < 2):
                    $ skipUntilFridayTargetDay = 3
                    jump juliahome_bed_skip_until_day1
                "Пропустить до Четверга." if basementBedSkipUntilFridayEnabled == True and (week_day > 5 or week_day < 3):
                    $ skipUntilFridayTargetDay = 4
                    jump juliahome_bed_skip_until_day1
                "Пропустить до Пятницы." if basementBedSkipUntilFridayEnabled == True and week_day != 5 and week_day != 4:
                    img black_screen
                    with Dissolve(0.2)
                    $ skipUntilFridayTargetDay = 5
                    call juliahome_skip_until_friday()
                    return False
                "Не ложиться.":
                    $ juliaHomeLivingRoomMonicaSuffix = juliaHomeNapSuffixStored
                    $ set_active("Bed1", True)
                    call refresh_scene_fade()
                    return False
        "Не ложиться.":
            $ juliaHomeLivingRoomMonicaSuffix = juliaHomeNapSuffixStored
            $ juliaHomeLivingRoomJuliaSuffix = juliaHomeNapJuliaSuffixStored
            $ set_active("Bed1", True)
            call refresh_scene_fade()
            return False

    return

label juliahome_bed_gosleep2:
    music stop
    img black_screen
    with Dissolve(0.2)
    #транзиция на отдых
    call process_hooks("juliahome_monica_before_sleep", "global")
#    $ set_active("Bed1", True)
    if _return == False:
        $ juliaHomeLivingRoomMonicaSuffix = juliaHomeNapSuffixStored
        $ juliaHomeLivingRoomJuliaSuffix = juliaHomeNapJuliaSuffixStored
        call refresh_scene_fade()
        return False
    $ juliaHomeLivingRoomMonicaSuffix = 1
    $ juliaHomeLivingRoomJuliaSuffix = 1
    $ changeDayTimeJuliaHome("day")
    call process_hooks("juliahome_monica_after_sleep", "global")
    call refresh_scene_fade()
    return

label juliahome_bed_skip_until_day1:
    img black_screen
    with Dissolve(0.2)
    call slums_monica_skip_until_friday()
    return

label juliahome_skip_until_friday: # Пропуск дней до пятницы
    img black_screen
    with Dissolve(0.5)
    $ skipDaysInterrupted = False
    $ skipDaysActiveFlag = True
    label juliahome_skip_until_friday_loop1:
        if day_time == "day":
            call process_hooks("juliahome_monica_before_nap", "global")
            if _return == False:
                $ juliaHomeLivingRoomMonicaSuffix = 1
                $ juliaHomeLivingRoomJuliaSuffix = 1
                $ skipDaysInterrupted = True
            else:
                $ changeDayTimeJuliaHome("evening")
                call process_hooks("juliahome_monica_after_nap", "global")
        if day_time == "evening":
            call process_hooks("slums_apartments_monica_before_sleep", "global")
            if _return == False:
                $ juliaHomeLivingRoomMonicaSuffix = 1
                $ juliaHomeLivingRoomJuliaSuffix = 1
                $ skipDaysInterrupted = True
            else:
                #call processHouseCleaningEvening()
                $ changeDayTimeJuliaHome("day")
                call process_hooks("juliahome_monica_after_sleep", "global")
        if week_day != skipUntilFridayTargetDay and skipDaysInterrupted == False:
            jump juliahome_skip_until_friday_loop1

    if skipDaysInterrupted == True:
        $ add_hook("juliahome_monica_after_sleep_dialogue", "monica_skip_until_friday_interrupted", scene="global", label="monica_skip_until_friday_interrupted", priority = 10000)
        $ add_hook("juliahome_monica_after_nap_dialogue", "monica_skip_until_friday_interrupted", scene="global", label="monica_skip_until_friday_interrupted", priority = 10000)
    $ juliaHomeLivingRoomMonicaSuffix = 1
    $ juliaHomeLivingRoomJuliaSuffix = 1
#    $ set_active("Bed1", True)
    $ skipDaysActiveFlag = False
    $ skipDaysInterrupted = False
    call refresh_scene_fade()
    return False

label juliahome_monica_after_nap:
    $ autorun_to_object("juliahome_monica_after_nap_dialogue")
    return

label juliahome_monica_after_nap_dialogue:
    if scene_name != "juliahome_livingroom":
        return
    call process_hooks("juliahome_monica_after_nap_dialogue", "global")
    return
label juliahome_monica_after_nap_dialogue1:
    $ rnd = rand(1,3)
#    if rnd == 1:
#        mt "Как же хорошо, что я теперь сама себе хозяйка. Никакая провинциальная дура теперь не командует мною."
#    if rnd == 2:
#        mt "Здесь так шумно. Не могу привыкнуть к этому."
#    if rnd == 3:
#        mt "Я немного задремала, а на улице уже вечер. Что мне сегодня еще нужно сделать?"

    mt "Я немного задремала, а на улице уже вечер. Что мне сегодня еще нужно сделать?"
    if day - monicaEatedLastDay >= 2:
        mt "Неплохо было бы что-то поесть..."
    return

label juliahome_monica_after_sleep:
    $ autorun_to_object("juliahome_monica_after_sleep_dialogue")
    return

label juliahome_after_sleep_dialogue:
    if scene_name != "juliahome_livingroom":
        return
    call process_hooks("juliahome_monica_after_sleep_dialogue", "global")
    return
label juliahome_monica_after_sleep_dialogue1:
    $ rnd = rand(1,3)
#    if rnd == 1:
#        mt "Еще один день в этой ужасной дыре... С другой стороны, здесь все МОЕ. И это не может не радовать."
#    if rnd == 2:
#        mt "Ужасно неудобное спальное место! У меня такое чувство, что я спала на полу."
#    if rnd == 3:
#        mt "Если бы у меня получилось сделать здесь ремонт и обновить мебель, здесь стало бы довольно уютно."
    return

label juliahome_kitchen_eat_before_sleep:
    imgf 30842
    sound snd_eating
    w
#        pause 1.5
    $ monica_eated()
    return
