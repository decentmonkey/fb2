default ep29_quests_melanie_started = False
default ep29_melanie_refused_visit_victoria = False
default ep29_monica_refused_visit_victoria = False

default ep29_melanie_talk_victoria_stage = 0
default ep29_quests_melanie_monica_stage=1
default ep29_quests_victoria_event_completed = False

default melaniePhotoShootOutfitIdx = -1

label ep29_quests_melanie_check:
    if ep29_quests_melanie_started != False or ep27_melanie_visited_victoria == False or ep27_melanie_refused_victoria_friendship == True or photoshoot8_count < 1 or week_day == 7:
        return
    $ ep29_quests_melanie_started = True
    # Начинаем квест с Мелани
    call ep29_dialogues3_melanie_monica_victoria_3b() # Приходит Мелани и говорит что надо ехать вечером к ней
    $ add_hook("enter_scene", "ep29_quests_melanie_init1", scene="street_monica_office", once=True, label="ep29_quests_melanie")
    $ add_hook("Teleport_Melanie_Home", "ep29_quests_melanie_map1", scene="map", label=["ep29_quests_melanie", "ep29_quests_melanie_map1"])
    $ add_hook("basement_monica_before_sleep", "ep29_quests_melanie_monica_sleep_restrict", scene="global", label="ep29_quests_melanie")
    $ add_hook("before_open", "ep29_quests_melanie_monica_come_melanie", scene="melanie_home", label="ep29_quests_melanie")
    $ remove_hook(label="melanie_home_restrict")
    $ add_objective("go_to_melanie", _("Пойти вечером к Мелани домой на встречу с 'другом'"), c_red, 95)
    return

label ep29_quests_melanie_init1:
    call ep29_dialogues3_melanie_monica_victoria_7()
    if cloth != "Whore":
        $ add_objective("go_to_melanie_dress", _("Нужно переодеться и ехать к Мелани"), c_blue, 105)

    return

label ep29_quests_melanie_monica_sleep_restrict: # Не даем ложиться спать
    call ep29_dialogues3_melanie_monica_victoria_7c()
    if _return == True:
        $ remove_objective("go_to_melanie_dress")
        $ remove_objective("go_to_melanie")
        $ remove_hook(label="ep29_quests_melanie")
        call ep29_quests_melanie_disappearing()
        $ add_hook("map_teleport", "ep27_quests_melanie3a_block_melanie_home", scene="global", priority = 2000, label="melanie_home_restrict") # Блокируем дом Мелани
        $ add_hook("enter_scene", "ep29_quests_melanie_check1", scene="monica_office_entrance", label="ep29_quests_melanie_check1") # Проверка для старта следующих апдейтов квеста
        $ ep29_monica_refused_visit_victoria = True
        return
    return False

label ep29_quests_melanie_map1:
    if cloth == "CasualDress1":
        call ep29_dialogues3_melanie_monica_victoria_7a()
        return False
    if cloth != "Whore":
        call ep29_dialogues3_melanie_monica_victoria_7b()
        return False
    return

label ep29_quests_melanie_monica_come_melanie: # Моника приходит к Мелани
    call ep29_dialogues4_lesbian_threesome_victoria_1()
    # Мелани сидит перед зеркалом днем
    call ep29_dialogues3_melanie_monica_victoria_1()
    if _return == False:
        # Мелани отказалась от посещения Виктории
        $ ep29_melanie_refused_visit_victoria = True
        $ remove_objective("go_to_melanie_dress")
        $ remove_objective("go_to_melanie")
        $ remove_hook(label="ep29_quests_melanie")
        call ep29_quests_melanie_disappearing()
        call process_change_map_location("Monica_Office")
        $ cloth = "WorkingOutfit1"
        $ cloth_type = "WorkingOutfit"
        $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_7d", scene="working_office_cabinet", once=True)
        call change_scene("working_office_cabinet", "Fade_long", "highheels_run2")
        return False
    # Переход на управление Мелани
    call melanie_home_init2() # инициализируем апартаменты Мелани
    $ day_time = "day"
    $ day_suffix = ""
    $ move_object("Biff", "empty")
    $ melanie_cloth = "StreetOutfit1"
    $ cloth = "WorkingOutfit1"
    $ cloth_type = "WorkingOutfit"
    call process_change_map_location("Monica_Office")
    $ mapTeleportForcedCarSound = True
    call ep29_quests_melanie_control1_init()
    $ money = 125000.0
    $ add_objective("go_to_victoria", _("Пойти в офис Дика и узнать, что нужно Виктории"), c_blue, 105)

    music stop
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0

    return

label ep29_quests_melanie_alex1:
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1i()
        return False
    call ep29_dialogues3_melanie_monica_victoria_1j()
    return False

label ep29_quests_melanie_alex2: # фотосессия
    if act=="l":
        return
    $ remove_hook()
    call ep29_dialogues3_melanie_monica_victoria_5()

    music stop
    label ep29_quests_melanie_alex2_loop1:
        call biffInitMelanieOutfitIcons()
        show screen choose_melanie_photoshoot_outfit()
        with Dissolve(0.2)
        $ result = ui.interact()
        if result == -1:
            sound click_denied
            jump ep29_quests_melanie_alex2_loop1
        $ melaniePhotoShootOutfitIdx = result + 1
        sound click1
        hide screen choose_melanie_photoshoot_outfit

    if melaniePhotoShootOutfitIdx == 1:
        call ep29_dialogues3_melanie_monica_victoria_5a1()
        call  ep29_photoshoot_melanie1()
        call ep29_dialogues3_melanie_monica_victoria_5a0()
    $ remove_objective("go_photoshoot")
    $ add_objective("go_home", _("Нужно ехать домой. Скоро придет Виктория"), c_pink, 95)
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_6", scene="monica_office_makeup_room", owner="Melanie", label="melanie_popup_messages", once=True)
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    call change_scene("monica_office_makeup_room", "Fade_long")
    return False

label ep29_quests_melanie_secretary1:
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1l()
        return False
    if get_active_objects("Biff", scene="monica_office_cabinet") != False:
        call ep29_dialogues3_melanie_monica_victoria_1n()
    else:
        call ep29_dialogues3_melanie_monica_victoria_1m()
    call refresh_scene_fade()
    return False

label ep29_quests_melanie_biff_comment1:
    # Мелани заходит в кабинет Бифа, когда его нет
    if get_active_objects("Biff", scene="monica_office_cabinet") == False:
        call ep29_dialogues3_melanie_monica_victoria_1n2()
    return

label ep29_quests_melanie_biff1: # клик на Бифа издалека
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1o()
        return False
    call change_scene("monica_office_cabinet_table")
    return False


label ep29_quests_melanie_biff2: # клик на Бифа рядом
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1o()
        return False
    # диалог с Бифом
    call ep29_dialogues3_melanie_monica_victoria_4()
    if _return == False:
        pass
        $ add_objective("go_home", _("Нужно ехать домой. Скоро придет Виктория"), c_pink, 95)
        $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_6", scene="monica_office_cabinet", owner="Melanie", label="melanie_popup_messages", once=True)
    else:
        $ add_objective("go_photoshoot", _("Провести фотосессию"), c_green, 85)
        $ add_hook("AlexPhotograph", "ep29_quests_melanie_alex2", scene="monica_office_photostudio", owner="Melanie", label=["melanie_dialogues", "melanie_photoshoot"])

    $ remove_objective("go_to_biff")
    $ add_hook("Biff", "ep29_dialogues3_melanie_monica_victoria_1ss", scene="monica_office_cabinet", owner="Melanie", label="melanie_biff_block1")
    call change_scene("monica_office_cabinet")
    return False

label ep29_quests_melanie_monica1: # Клик на Монику в кабинете
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1w()
        return False
    # диалог с Моникой
#    if ep29_quests_melanie_monica_stage == 0:
#        call ep29_dialogues3_melanie_monica_victoria_3d()
#        call refresh_scene_fade()
#        return False
    if ep29_quests_melanie_monica_stage == 1:
        call ep29_dialogues3_melanie_monica_victoria_3a()
        call ep29_dialogues3_melanie_monica_victoria_3c()
#        $ add_hook("Monica", "ep29_dialogues3_melanie_monica_victoria_1rr", scene="working_office_cabinet", owner="Melanie", label="melanie_monica_block1")
#        $ add_hook("exit_scene", "ep29_dialogues3_melanie_monica_victoria_3c", scene="working_office_cabinet", owner="Melanie", label="melanie_popup_messages", once=True)
        $ day_time = "evening"
        $ day_suffix = "_Evening"
        $ set_active(False, group="workers", scene="working_office")
        $ set_active(False, group="workers", scene="working_office2")
        $ remove_objective("go_to_monica")
        $ move_object("Julia", "empty")
        $ move_object("Biff", "monica_office_cabinet")
        $ add_objective("go_to_biff", _("Пойти в кабинет Бифа и поговорить с ним"), c_orange, 85)
        $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_6a", scene="street_monica_office", owner="Melanie", label="melanie_popup_messages", once=True)
        $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_1hh", scene="melanie_home", owner="Melanie", label="melanie_popup_messages", once=True)
        $ add_hook("Teleport_Cabinet", "ep29_dialogues3_melanie_monica_victoria_1rr", scene="working_office", owner="Melanie", label="melanie_teleports_monica_restrict")
        $ add_hook("Teleport_Cabinet", "ep29_dialogues3_melanie_monica_victoria_1rr", scene="working_office2", owner="Melanie", label="melanie_teleports_monica_restrict")
        $ add_hook("Biff", "ep29_quests_melanie_biff2", scene="monica_office_cabinet_table", owner="Melanie", label="melanie_dialogues")
        $ add_hook("Chair", "ep29_quests_melanie_home1_chair", scene="melanie_home", owner="Melanie", label="melanie_victoria_quest")
        $ remove_hook(label="melanie_popup_messages_early")
        $ set_var("Chair", actions="lh", scene="melanie_home")
        $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_3c0", scene="monica_office_makeup_room", owner="Melanie", once=True)
        call change_scene("monica_office_makeup_room", "Fade_long", False)
    return False



label ep29_quests_melanie_dick_Reception: # клик на рецепшин у Дика
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1y()
        return False
    call ep29_dialogues3_melanie_monica_victoria_1z()
    call refresh_scene_fade()
    return False

label ep29_quests_melanie_victoria1: # диалог с Викторией
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1aa()
        return False
    # Диалог с Викторией
    if ep29_melanie_talk_victoria_stage == 0:
        call ep29_dialogues3_melanie_monica_victoria_2()
        $ ep29_melanie_talk_victoria_stage = 1
        call change_scene("dick_office_hall1", "Fade_long")
        call refresh_scene_fade()
        return

    # второй диалог
    call ep29_dialogues3_melanie_monica_victoria_2a0()
    # после диалога с Викторией
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_1ii", scene="street_monica_office", owner="Melanie", label="melanie_popup_messages", once=True)
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_1kk", scene="dick_office_hall1", owner="Melanie", label="melanie_popup_messages", once=True)
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_2a", scene="monica_office_entrance", owner="Melanie", label="melanie_popup_messages", once=True)
    $ set_active("Wine", True, scene="melanie_home")
    $ ep29_quests_melanie_monica_stage = 1
    $ melanieHomeMelanieSuffix = "2"
    $ add_hook("Teleport_Secretary", "ep29_dialogues3_melanie_monica_victoria_1pp", scene="dick_office_hall1", owner="Melanie", label="melanie_block_to_victoria")
    $ remove_objective("go_to_victoria")
    $ add_objective("go_to_monica", _("Вернуться в студию и поговорить с Миссис Бакфетт"), c_orange, 75)
    $ remove_hook(label="melanie_teleports_monica_restrict")
    call change_scene("dick_office_hall1", "Fade_long")
    return False

label ep29_quests_melanie_home1_chair: # старт сцены с Викторией
    if act=="l":
        return
    call ep29_dialogues3_melanie_monica_victoria_1ll()
    call ep29_dialogues4_lesbian_threesome_victoria_1a() # сцена
    $ remove_objective("go_home")
    $ remove_hook(label="melanie_popup_messages")
    # переключаем Монику назад
    $ mapTeleportForcedCarSound = False
    call ep29_quests_melanie_control1_uninit()
    call process_change_map_location("House")
    music stop
    img black_screen
    with diss
    pause 2.0
    $ remove_objective("go_to_melanie_dress")
    $ remove_objective("go_to_melanie")
    $ cloth = "Whore"
    $ cloth_type = "Whore"
    $ add_hook("map_teleport", "ep27_quests_melanie3a_block_melanie_home", scene="global", priority = 2000, label="melanie_home_restrict") # Блокируем дом Мелани
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_6b", scene="street_house_outside", label="monica_comment1", once=True)
    call change_scene("street_house_outside", "Fade_long", False)
    $ add_hook("enter_scene", "ep29_quests_melanie_check1", scene="monica_office_entrance", label="ep29_quests_melanie_check1") # Проверка для старта следующих апдейтов квеста

    # убираем Мелани
    call ep29_quests_melanie_disappearing()
    $ remove_hook(label="ep29_quests_melanie")
    $ ep29_quests_victoria_event_completed = True
    return False

label ep29_quests_melanie_disappearing:
    $ add_hook("Melanie_Life_day", "Melanie_Life_disappeared", scene="global", label="melanie_disappeared_after_victoria")
    $ add_hook("Melanie_Life_evening", "Melanie_Life_disappeared", scene="global", label="melanie_disappeared_after_victoria")
    return

label ep29_quests_melanie_check1:
    return







#    $ add_hook("map_teleport", "ep27_quests_melanie3a_block_melanie_home", scene="global", priority = 2000, label="melanie_home_restrict") # Блокируем дом Мелани
