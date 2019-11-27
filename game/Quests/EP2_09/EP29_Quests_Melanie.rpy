default ep29_quests_melanie_started = False
default ep29_melanie_refused_visit_victoria = False


label ep29_quests_melanie_check:
    if ep29_quests_melanie_started != False or ep27_melanie_visited_victoria == False or ep27_melanie_refused_victoria_friendship == True or photoshoot8_count < 1:
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
        call process_change_map_location("House")
        call change_scene("street_house_outside", "Fade_long", "highheels_run2")
        return False
    # Переход на управление Мелани
    $ day_time = "day"
    $ day_suffix = ""
    $ move_object("Biff", "empty")
    $ melanie_cloth = "StreetOutfit1"
    $ mapTeleportForcedCarSound = True
    call ep29_quests_melanie_control1_init()
    $ money = 125000.0
    music stop
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0

    return

#    $ add_hook("map_teleport", "ep27_quests_melanie3a_block_melanie_home", scene="global", priority = 2000, label="melanie_home_restrict") # Блокируем дом Мелани
