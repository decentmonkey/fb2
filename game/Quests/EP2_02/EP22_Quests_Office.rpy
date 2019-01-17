label ep22_quests_office_init:
    $ biffDisabled = True
    if monkeysOffended2 == True:
        $ biffMonicaCastingsEnabled = True
#        $ notif(_("Моника заставляла моделей проходить обнаженный кастинг"))
    $ add_hook_day("ep22_quests_office2", week_day = 6, label="photoshoot_regular") #Обновляем возможность фотосессии раз в неделю по субботам
    $ add_hook("Biff", "ep22_quests_office1", scene="monica_office_cabinet_table")
    $ add_hook("AlexPhotograph", "ep22_quests_office3", scene="monica_office_photostudio", label="photoshoot_regular")
    return

label ep22_quests_office1: #регулярный разговор с Бифом на работе
    if act=="l":
        return
    call ep22_dialogue6_3()
    if _return == False:
        call change_scene("monica_office_cabinet")
#        call refresh_scene_fade()
        return
    # Инициализируем фотосессию
    $ add_hook("Teleport_Monica_Office_Entrance", "monica_office_secretary_dialogue6", scene="monica_office_secretary", label="photoshoot") #Блокируем выход пока идет фотосессия
    $ add_hook("AlexPhotograph", "ep22_quests_office4", scene="monica_office_photostudio", label="photoshoot_alex") # Алекс стартует фотосессию
    $ add_hook("Biff", "ep22_quests_office5", scene="monica_office_cabinet_table", label="photoshoot") # Мне надо идти в фотостудию, блок на Биффа
    call refresh_scene_fade()
    return

label ep22_quests_office2: # Обновляем возможность фотосессии раз в неделю
    $ biffWeeklyPhotoShootEnabled = True
    return
label ep22_quests_office3: # Регулярный разговор с Алексом
    if act=="l":
        return
    call ep22_dialogue6_4()
    call refresh_scene_fade()
    return False
label ep22_quests_office4: # Алекс стартует фотосессию
    if act == "l":
        return
#    $ monicaPhotoShootOutfitIdx = 1
#    jump ep22_quests_office4_l1
    call ep22_dialogue6_5()
    if _return == False:
        call refresh_scene_fade()
        return False
    $ monicaPhotoShootInProgress = True
    # Выбор наряда
    label ep22_quests_office4_loop1:
        show screen choose_photoshoot_outfit()
        with Dissolve(0.2)
        $ result = ui.interact()
        if result == -1:
            sound click_denied
            jump ep22_quests_office4_loop1
        $ monicaPhotoShootOutfitIdx = result + 1
        sound click1
        hide screen choose_photoshoot_outfit

    call ep22_dialogue6_5a()

label ep22_quests_office4_l1:
    if monicaPhotoShootOutfitIdx == 1:
        call ep22_photoshoot1()
        call ep22_photoshoot1_end()
    if monicaPhotoShootOutfitIdx == 2:
        call ep22_photoshoot2()
        call ep22_photoshoot2_end()
        if monicaSecretaryOutfit1EnforcementPlanned == False: # После фотосессии в костюме #2 планируем переодевание секретарши
            $ monicaSecretaryOutfit1EnforcementPlanned = True
            $ add_hook("before_open", "ep22_quests_office9", scene="monica_office_secretary") # Планируем инициализацию outfit1 для секретарши
    if monicaPhotoShootOutfitIdx == 3:
        call ep22_photoshoot3()
        call ep22_photoshoot3_end()
    #конец фотосессии
    sound snd_fabric1
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    $ remove_hook(label="photoshoot_alex")
    $ add_hook("Biff", "ep22_quests_office6", scene="monica_office_cabinet_table", label="photoshoot") #Мне надо получить деньги от Бифа
    $ add_hook("Teleport_Monica_Office_Entrance", "ep22_dialogue6_7a", scene="monica_office_secretary", label="photoshoot") #Блокируем выход пока не получили деньги от Бифа
    call change_scene("monica_office_cabinet", "Fade_long")
    return False
label ep22_quests_office5: # Мне надо идти в фотостудию, блок на Биффа
    if act=="l":
        return
    call monica_office_secretary_dialogue6()
    return False

label ep22_quests_office6: #Биф, где мои деньги?
    if act=="l":
        return
    call ep22_dialogue6_7()
    if _return == True:
        if monicaPhotoShootOutfitIdx == 1:
            $ add_char_progress("Biff", PS1_BiffProgress, "PS1_BiffProgress_day" + str(day))
        if monicaPhotoShootOutfitIdx == 2:
            $ add_char_progress("Biff", PS2_BiffProgress, "PS2_BiffProgress_day" + str(day))
        if monicaPhotoShootOutfitIdx == 3:
            $ add_char_progress("Biff", PS3_BiffProgress, "PS3_BiffProgress_day" + str(day))

    if monicaBiffFirstPhotoShoot == True:
        $ monicaBiffFirstPhotoShoot = False
        $ questLog(8, True)
    $ biffWeeklyPhotoShootEnabled = False
    $ monicaPhotoShootInProgress = False
    $ remove_objective("money_for_victoria")
    $ remove_hook(label="photoshoot")
    call change_scene("monica_office_secretary", "Fade_long")
    return False

label ep22_quests_office7: #enable Biff
    $ biffDisabled = False
    $ biffOnlyFridayEvening = False
    $ add_hook("Secretary", "ep22_quests_office8a", scene="monica_office_secretary", label="secretary_last_request")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep22_quests_office8", scene="monica_office_secretary", label="secretary_last_request")
    return
label ep22_quests_office8a:
    if act=="l":
        return
    jump ep22_quests_office8
label ep22_quests_office8: # Последний раз секретарша просит о помощи
    call monica_office_secretary_dialogue3()
    $ remove_hook(label="secretary_last_request")
    call refresh_scene_fade()
    return False
label ep22_quests_office9:
    if biffWeeklyPhotoShootEnabled == False or day_time != "evening":
        return
    $ remove_hook()
    # инициализируем outfit1 на секретарше
    $ monicaOfficeSecretarySecretarySuffix = 4
    $ remove_hook("Secretary", "monica_office_secretary_dialogue2", scene="monica_office_secretary")
    $ add_hook("Secretary", "ep22_quests_office12", scene="monica_office_secretary", label="secretary_regular_talk")
    $ add_hook("Secretary", "ep22_quests_office10", scene="monica_office_secretary", label="secretary_last_request")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep22_quests_office11", scene="monica_office_secretary", label="secretary_last_request")
    $ replace_hook("ep22_dialogue6_2b", scene="monica_office_secretary", label="check_bill_at_place")
    return
label ep22_quests_office10: # Последний запрос о помощи со стороны секретарши
    if act=="l":
        return
    call ep22_dialogue6_1()
    $ remove_hook(label="secretary_last_request")
    call refresh_scene_fade()
    return False
label ep22_quests_office11:
    call ep22_dialogue6_1()
    $ remove_hook(label="secretary_last_request")
    call refresh_scene_fade()
    return False
label ep22_quests_office12: # Регулярный разговор с секретаршей
    if act=="l":
        call ep22_dialogue6_2a()
        return False
    call ep22_dialogue6_2()
    call refresh_scene_fade()
    return


label ep22_quests_office13:
    return
label ep22_quests_office14:
    return
label ep22_quests_office15:
    return
