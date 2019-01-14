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
        call refresh_scene_fade()
        return
    # Инициализируем фотосессию
    $ add_hook("Teleport_Monica_Office_Entrance", "monica_office_secretary_dialogue6", scene="monica_office_secretary", label="photoshoot") #Блокируем выход пока идет фотосессия
    $ add_hook("AlexPhotograph", "ep22_quests_office4", scene="monica_office_photostudio", label="photoshoot_alex") # Алекс стартует фотосессию
    $ add_hook("Biff", "ep22_quests_office5", scene="monica_office_cabinet_table", label="photoshoot") # Мне надо идти в фотостудию, блок на Биффа
    return

label ep22_quests_office2: # Обновляем возможность фотосессии раз в неделю
    $ biffWeeklyPhotoShootEnabled = True
    return
label ep22_quests_office3: # Регулярный разговор с Алексом
    if act=="l":
        return
    call ep22_dialogue6_4()
    call refresh_scene_fade()
    return
label ep22_quests_office4: # Алекс стартует фотосессию
    if act == "l":
        return
    call ep22_dialogue6_5()
    if _return == False:
        call refresh_scene_fade()
        return False
    $ monicaPhotoShootInProgress = True
    # Выбор наряда
    call ep22_dialogue6_5a()
    if monicaPhotoShootOutfitIdx == 1:
        call ep22_photoshoot1()
        call ep22_photoshoot1_end()
    if monicaPhotoShootOutfitIdx == 1:
        call ep22_photoshoot2()
        call ep22_photoshoot2_end()
    if monicaPhotoShootOutfitIdx == 1:
        call ep22_photoshoot3()
        call ep22_photoshoot3_end()
    #конец фотосессии
    $ monicaPhotoShootInProgress = False
    $ remove_hook(label="photoshoot_alex")
    $ add_hook("Biff", "ep22_quests_office6", scene="monica_office_cabinet_table", label="photoshoot") #Мне надо получить деньги от Бифа
    $ add_hook("Teleport_Monica_Office_Entrance", "ep22_dialogue6_7a", scene="monica_office_secretary", label="photoshoot") #Блокируем выход пока не получили деньги от Бифа

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
    $ biffWeeklyPhotoShootEnabled = False
    $ remove_hook(label="photoshoot")
    return
    
label ep22_quests_office7:
    return
label ep22_quests_office8:
    return
label ep22_quests_office9:
    return
label ep22_quests_office10:
    return
label ep22_quests_office11:
    return
label ep22_quests_office12:
    return
label ep22_quests_office13:
    return
label ep22_quests_office14:
    return
label ep22_quests_office15:
    return
