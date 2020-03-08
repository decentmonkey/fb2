default monicaHomeLivingRoomMonicaSuffixStored = 0

label slums_basement_bed:
    if act=="l":
        return
    if act == "h":
        $ monicaRestApartments = True
        $ monicaRestApartmentsDay = day
        $ monicaRestHouse = False
        if day_time == "day":
            call slums_basement_bed_take_nap()
            return _return
        if day_time == "evening":
            call slums_basement_bed_gosleep()
            return _return

    return False

label slums_basement_bed_take_nap:
    $ monicaHomeLivingRoomMonicaSuffixStored = monicaHomeLivingRoomMonicaSuffix
    $ monicaHomeLivingRoomMonicaSuffix = "Nap" + str(day%4 + 1)
    $ set_active("Bed1", False)
    $ autorun_to_object("slums_basement_bed_take_nap1")
    call refresh_scene("Dissolve_05")
    return

label slums_basement_bed_take_nap1:
    menu:
        "Лечь и ждать вечера.":
            music stop
            $ afterNapSuffix = day%2 + 3
            img black_screen
            with Dissolve(0.2)
            #транзиция на отдых
            call process_hooks("slums_apartments_monica_before_nap", "global")
            $ set_active("Bed1", True)
            if _return == False:
                $ monicaHomeLivingRoomMonicaSuffix = monicaHomeLivingRoomMonicaSuffixStored
                call refresh_scene_fade()
                return False
            $ monicaHomeLivingRoomMonicaSuffix = afterNapSuffix
            $ changeDayTimeSlumsApartments("evening")
            call process_hooks("slums_apartments_monica_after_nap", "global")
            call refresh_scene_fade()
            return False
        "Не ложиться.":
            $ monicaHomeLivingRoomMonicaSuffix = monicaHomeLivingRoomMonicaSuffixStored
            $ set_active("Bed1", True)
            call refresh_scene_fade()
            return False
    return

label slums_basement_bed_gosleep:
    $ monicaHomeLivingRoomMonicaSuffixStored = monicaHomeLivingRoomMonicaSuffix
    $ monicaHomeLivingRoomMonicaSuffix = "Sleep" + str(day%4 + 1)
    $ monicaHomeLivingRoomSceneSuffix2 = "Night"
    $ set_active("Bed1", False)
    $ autorun_to_object("slums_basement_bed_gosleep1")
    call refresh_scene("Dissolve_05")
    return

label slums_basement_bed_gosleep1:
    if monicaEatedLastDay < day:
        if day - monicaEatedLastDay >= 3 and (monicaCantSleepHungry2 == True or debugMode == False) and debugMode == False:
            #если Моника не ела 3 дня
            mt "{c}Я не ела{/c} уже третий день!"
            "Я не могу лечь спать в таком состоянии!"
            "Я ХОЧУ ЕСТЬ!!!"
            $ set_active("Bed1", True)
            $ monicaHomeLivingRoomSceneSuffix2 = ""
            $ monicaHomeLivingRoomMonicaSuffix = monicaHomeLivingRoomMonicaSuffixStored
            call refresh_scene_fade()
            return False

        else:
            mt "Я сегодня ничего не ела! Лечь спать голодной?"

    menu:
        "Лечь спать." if monicaEatedLastDay == day:
            call slums_basement_bed_gosleep2()
            return
        "Поесть и лечь спать." if monicaEatedLastDay < day:
            call slums_basement_kitchen_eat_before_sleep()
            call slums_basement_bed_gosleep2()
            return
        "Лечь спать голодной." if monicaEatedLastDay < day:
            call slums_basement_bed_gosleep2()
            return
        "Пропустить до..." if basementBedSkipUntilFridayEnabled == True and week_day != 5 and week_day != 4:
            menu:
                "Пропустить до Понедельника." if basementBedSkipUntilFridayEnabled == True and week_day > 5 and week_day < 7:
                    $ skipUntilFridayTargetDay = 1
                    jump slums_basement_bed_skip_until_day1
                "Пропустить до Вторника." if basementBedSkipUntilFridayEnabled == True and (week_day > 5):
                    $ skipUntilFridayTargetDay = 2
                    jump slums_basement_bed_skip_until_day1
                "Пропустить до Среды." if basementBedSkipUntilFridayEnabled == True and (week_day > 5 or week_day < 2):
                    $ skipUntilFridayTargetDay = 3
                    jump slums_basement_bed_skip_until_day1
                "Пропустить до Четверга." if basementBedSkipUntilFridayEnabled == True and (week_day > 5 or week_day < 3):
                    $ skipUntilFridayTargetDay = 4
                    jump slums_basement_bed_skip_until_day1
                "Пропустить до Пятницы." if basementBedSkipUntilFridayEnabled == True and week_day != 5 and week_day != 4:
                    img black_screen
                    with Dissolve(0.2)
                    $ skipUntilFridayTargetDay = 5
                    call slums_monica_skip_until_friday()
                    return False
                "Не ложиться.":
                    $ monicaHomeLivingRoomMonicaSuffix = monicaHomeLivingRoomMonicaSuffixStored
                    $ monicaHomeLivingRoomSceneSuffix2 = ""
                    $ set_active("Bed1", True)
                    call refresh_scene_fade()
                    return False
        "Не ложиться.":
            $ monicaHomeLivingRoomMonicaSuffix = monicaHomeLivingRoomMonicaSuffixStored
            $ monicaHomeLivingRoomSceneSuffix2 = ""
            $ set_active("Bed1", True)
            call refresh_scene_fade()
            return False

    return

label slums_basement_bed_gosleep2:
    music stop
    $ afterSleepSuffix = day%2 + 3
    img black_screen
    with Dissolve(0.2)
    #транзиция на отдых
    call process_hooks("slums_apartments_monica_before_sleep", "global")
    $ set_active("Bed1", True)
    if _return == False:
        $ monicaHomeLivingRoomSceneSuffix2 = ""
        $ monicaHomeLivingRoomMonicaSuffix = monicaHomeLivingRoomMonicaSuffixStored
        call refresh_scene_fade()
        return False
    $ monicaHomeLivingRoomSceneSuffix2 = ""
    $ monicaHomeLivingRoomMonicaSuffix = afterNapSuffix
    $ changeDayTimeSlumsApartments("day")
    call process_hooks("slums_apartments_monica_after_sleep", "global")
    call refresh_scene_fade()
    return

label slums_basement_bed_skip_until_day1:
    img black_screen
    with Dissolve(0.2)
    call slums_monica_skip_until_friday()
    return

label slums_monica_skip_until_friday: # Пропуск дней до пятницы
    img black_screen
    with Dissolve(0.5)
    $ skipDaysInterrupted = False
    $ skipDaysActiveFlag = True
    label slums_monica_skip_until_friday_loop1:
        if day_time == "day":
            call process_hooks("slums_apartments_monica_before_nap", "global")
            if _return == False:
                $ monicaHomeLivingRoomSceneSuffix2 = ""
                $ monicaHomeLivingRoomMonicaSuffix = afterNapSuffix
                $ skipDaysInterrupted = True
            else:
                $ changeDayTimeSlumsApartments("evening")
                call process_hooks("slums_apartments_monica_after_nap", "global")
        if day_time == "evening":
            call process_hooks("slums_apartments_monica_before_sleep", "global")
            if _return == False:
                $ monicaHomeLivingRoomSceneSuffix2 = ""
                $ monicaHomeLivingRoomMonicaSuffix = afterNapSuffix
                $ skipDaysInterrupted = True
            else:
                #call processHouseCleaningEvening()
                $ changeDayTimeSlumsApartments("day")
                call process_hooks("slums_apartments_monica_after_sleep", "global")
        if week_day != skipUntilFridayTargetDay and skipDaysInterrupted == False:
            jump slums_monica_skip_until_friday_loop1

    if skipDaysInterrupted == True:
        $ add_hook("slums_basement_monica_after_sleep_dialogue", "monica_skip_until_friday_interrupted", scene="global", label="monica_skip_until_friday_interrupted", priority = 10000)
        $ add_hook("slums_basement_monica_after_nap_dialogue", "monica_skip_until_friday_interrupted", scene="global", label="monica_skip_until_friday_interrupted", priority = 10000)
    $ monicaHomeLivingRoomSceneSuffix2 = ""
    $ monicaHomeLivingRoomMonicaSuffix = day%2 + 3
    $ set_active("Bed1", True)
    $ skipDaysActiveFlag = False
    $ skipDaysInterrupted = False
    call refresh_scene_fade()
    return False

label slums_basement_monica_after_nap:
    $ autorun_to_object("slums_basement_monica_after_nap_dialogue")
    return

label slums_basement_monica_after_nap_dialogue:
    if scene_name != "monicahome_livingroom":
        return
    call process_hooks("slums_basement_monica_after_nap_dialogue", "global")
    return
label slums_basement_monica_after_nap_dialogue1:
    $ rnd = rand(1,3)
    if rnd == 1:
        mt "Как же хорошо, что я теперь сама себе хозяйка. Никакая провинциальная дура теперь не командует мною."
    if rnd == 2:
        mt "Здесь так шумно. Не могу привыкнуть к этому."
    if rnd == 3:
        mt "Я немного задремала, а на улице уже вечер. Что мне сегодня еще нужно сделать?"

    if day - monicaEatedLastDay >= 2:
        mt "Неплохо было бы что-то поесть..."
    return

label slums_basement_monica_after_sleep:
    $ autorun_to_object("slums_basement_monica_after_sleep_dialogue")
    return

label slums_basement_monica_after_sleep_dialogue:
    if scene_name != "monicahome_livingroom":
        return
    call process_hooks("slums_basement_monica_after_sleep_dialogue", "global")
    return
label slums_basement_monica_after_sleep_dialogue1:
    $ rnd = rand(1,3)
    if rnd == 1:
        mt "Еще один день в этой ужасной дыре... С другой стороны, здесь все МОЕ. И это не может не радовать."
    if rnd == 2:
        mt "Ужасно неудобное спальное место! У меня такое чувство, что я спала на полу."
    if rnd == 3:
        mt "Если бы у меня получилось сделать здесь ремонт и обновить мебель, здесь стало бы довольно уютно."
    return


label slums_basement_kitchen_eat:
    # Моника ест на кухне
    if act=="l":
        return
    if day == monicaEatedLastDay:
        call ep211_dialogues6_slum_apartment_37()
    else:
        call ep211_dialogues6_slum_apartment_36()
        $ monica_eated()
    $ set_active("Cocktail", True, scene="monicahome_livingroom")
    call refresh_scene_fade()
    return False

label slums_basement_kitchen_eat_before_sleep:
    call ep211_dialogues6_slum_apartment_36()
    $ monica_eated()
    $ set_active("Cocktail", True, scene="monicahome_livingroom")
    return
