default ep28_quests_police_day1_cage1_flag = False
default ep28_quests_police_day1_bed1_flag = False
default ep28_quests_monica_offended_day1 = False # Монику использовали заключенные день1
default ep28_quests_monica_offended_day2 = False # Монику использовали заключенные день2
default ep28_quests_monica_offended_day3 = False # Монику использовали заключенные день3
default ep28_quests_monica_offended_prisoners = False # Моника сама наехала на заключенных
default ep28_quests_monica_kicked_prisoners = False # Моника ударила и укусила заключенных
default ep28_quests_monica_called_monicapubname = False
default ep28_quests_bob_dick = False # Боб запихнул член Монике в рот
default marcus_visit1_completed = False
label ep28_quests_police1:
    # Инициализация
    call ep28_dialogues_jail1()
    $ money = 0 # отбираем деньги
    $ add_hook("Sortir", "ep28_quests_police1_sortir", scene="police_cell1", label="cell_sortir") # туалет
    $ remove_hook(label="cage_interact1")
    $ add_hook("cage_interact", "ep28_quests_police_day1_cage1", scene="police", label="cage_interact_day1a")
    $ add_hook("Bed", "ep28_quests_police_bed_regular", scene="police_cell1", label="cell_bed") # кровать
    $ add_hook("Bed", "ep28_quests_police_bed_regular", scene="police_cell2", label="cell_bed") # кровать
    $ add_hook("Bed", "ep28_quests_police_day1_bed1", scene="police_cell1", label="cell_bed_day1") # кровать
    $ add_hook("Bed", "ep28_quests_police_day1_bed1", scene="police_cell2", label="cell_bed_day1") # кровать
    call change_scene("police_cell1", "Fade_long", False)
    return

label ep28_quests_police1_sortir: # клик на сортир
    if act=="l":
        return
    call ep28_dialogues_jail1_piss()
    call refresh_scene_fade()
    return False

label ep28_quests_police_day1_cage1:
    $ ep28_quests_police_day1_cage1_flag = True
    call ep28_dialogues_jail3b()
    call change_scene("police_cell2", "Fade_long")
    return False

label ep28_quests_police_day1_bed1:
    if act=="l":
        return
    if ep28_quests_police_day1_bed1_flag == False:
        call ep28_dialogues_jail3()
        $ ep28_quests_police_day1_bed1_flag = True
    if ep28_quests_police_day1_cage1_flag == False:
        if ep28_quests_police_day1_bed1_flag == True:
            call ep28_dialogues_jail1_bed()
        call refresh_scene_fade()
        return False
    $ remove_hook(label="cage_interact_day1a")
    $ remove_hook(label="cell_bed_day1")
    call ep28_quests_police_day1_prisoners1()
    call refresh_scene_fade()
    return False

label ep28_quests_police_bed_regular:
    if act=="l":
        return
    call ep28_dialogues_jail1_bed()
    return False

label ep28_quests_police_day1_prisoners1: # Приходят заключенные, день1
    $ remove_hook()
    call ep28_dialogues_jail4()
    if _return == False:
        $ ep28_quests_monica_offended_prisoners = True
    else:
        $ ep28_quests_monica_offended_day1 = True
        $ add_corruption(monicaJailDay1AddCorruption, "monicaJailDay1AddCorruption")
    $ add_hook("cage_interact", "ep28_dialogues_jail3a", scene="police", label="cage_interact_nobody")
    $ add_hook("cage_interact", "ep28_dialogues_jail5", scene="police", label="cage_day1")
    $ add_hook("Bed", "ep28_quests_police_day1_bed2", scene="police_cell1", label="cell_bed_day1") # кровать
    $ add_hook("Bed", "ep28_quests_police_day1_bed2", scene="police_cell2", label="cell_bed_day1") # кровать
    call refresh_scene_fade_long()
    return

label ep28_quests_police_day1_bed2: # Моника ложится спать день 1
    if act=="l":
        return
    call ep27_dialogues_marcus1_10()
    if _return == False:
        call refresh_scene_fade_long()
        return False
    call ep28_dialogues_jail6()
    call ep28_dialogues_jail7()
    $ day = day + 1
    $ remove_hook(label="cage_day1")
    $ remove_hook(label="cell_bed_day1")

    $ add_hook("cage_interact", "ep28_quests_police_day2_cage1", scene="police", label="cage_day2")
    call change_scene("police_cell1", "Fade_long", False)
    return False

label ep28_quests_police_day2_cage1: # День2, решетка
    $ remove_hook()
    if ep28_quests_monica_offended_prisoners == True: # конец квеста
        $ remove_hook(label="cell_bed_day1")
        $ remove_hook(label="cage_day1")
        $ remove_hook(label="cage_day2")
        call ep28_quests_police_final()
        return False
    call ep28_dialogues_jail8()
    $ add_hook("Bed", "ep28_quests_police_day2_bed1", scene="police_cell1", label="cage_day2") # кровать
    $ add_hook("Bed", "ep28_quests_police_day2_bed1", scene="police_cell2", label="cage_day2") # кровать
    call change_scene("police_cell2", "Fade_long", False)
    return False

label ep28_quests_police_day2_bed1: # Кровать день2, приходят заключенные
    if act=="l":
        return
    call ep27_dialogues_marcus1_10()
    if _return == False:
        call refresh_scene_fade_long()
        return False
    call ep28_dialogues_jail9()
    if _return == False:
        $ ep28_quests_monica_offended_prisoners = True
    else:
        $ ep28_quests_monica_offended_day2 = True
        $ add_corruption(monicaJailDay2AddCorruption, "monicaJailDay2AddCorruption")

    $ remove_hook(label="cage_day2")
    $ add_hook("Bed", "ep28_quests_police_day2_bed2", scene="police_cell1", label="cage_day2") # кровать
    $ add_hook("Bed", "ep28_quests_police_day2_bed2", scene="police_cell2", label="cage_day2") # кровать


    call change_scene("police_cell1", "Fade_long", False)
#    call refresh_scene_fade_long()
    return False

label ep28_quests_police_day2_bed2: # Кровать день2, после заключенных (сон)
    if act=="l":
        return
    call ep27_dialogues_marcus1_10()
    if _return == False:
        call refresh_scene_fade_long()
        return False

    call ep28_dialogues_jail10()

    $ day = day + 1
    call ep28_dialogues_jail11()
    $ remove_hook(label="cage_day2")
    $ add_hook("cage_interact", "ep28_quests_police_day3_cage1", scene="police", label="cage_day3")
    call change_scene("police_cell1", "Fade_long", False)
    return False

label ep28_quests_police_day3_cage1: # День3, решетка
    $ remove_hook()
    if ep28_quests_monica_offended_prisoners == True: # конец квеста
        $ remove_hook(label="cell_bed_day1")
        $ remove_hook(label="cage_day1")
        $ remove_hook(label="cage_day2")
        $ remove_hook(label="cage_day3")
        call ep28_quests_police_final()
        return False
    call ep28_dialogues_jail12()
    $ add_hook("Bed", "ep28_quests_police_day3_bed1", scene="police_cell1", label="cage_day3") # кровать
    $ add_hook("Bed", "ep28_quests_police_day3_bed1", scene="police_cell2", label="cage_day3") # кровать
    call change_scene("police_cell2", "Fade_long", False)
    return False

label ep28_quests_police_day3_bed1: # Ден3, кровать, приход заключенных
    if act=="l":
        return
    call ep27_dialogues_marcus1_10()
    if _return == False:
        call refresh_scene_fade_long()
        return False
    call ep28_dialogues_jail13()
    call ep28_dialogues_jail14()
    if _return == False:
        $ ep28_quests_monica_offended_prisoners = True
    else:
        $ ep28_quests_monica_offended_day3 = True
        $ add_corruption(monicaJailDay3AddCorruption, "monicaJailDay3AddCorruption")
    $ remove_hook(label="cage_day2")
    $ remove_hook(label="cage_day3")
    $ add_hook("Bed", "ep28_quests_police_day3_bed2", scene="police_cell1", label="cage_day3") # кровать
    $ add_hook("Bed", "ep28_quests_police_day3_bed2", scene="police_cell2", label="cage_day3") # кровать

    music stop
    img black_screen
    with diss
    pause 1.5
    call change_scene("police_cell1", "Fade_long", False)
    return False

label ep28_quests_police_day3_bed2: #День3, кровать, сон
    if act=="l":
        return
    call ep28_dialogues_jail15()
    $ day = day + 1
    call ep28_dialogues_jail16()
    $ remove_hook(label="cage_day3")
    $ add_hook("cage_interact", "ep28_quests_police_day4_cage1", scene="police", label="cage_day3")
    call change_scene("police_cell2", "Fade_long")
    return False

label ep28_quests_police_day4_cage1: #День4, решетка, завершение квеста
    $ remove_hook()
    call ep28_quests_police_final()
    return False


label ep28_quests_police_final: # Завершение тюремного квеста
    call ep28_dialogues_jail17()
    if ep28_quests_monica_offended_prisoners == True:
        # Моника наехала на заключенных
        call ep28_dialogues_jail18()
    else:
        # Моника подчинилась заключенным до конца
        call ep28_dialogues_jail19()

    # Разговор с Маркусом
    call ep28_dialogues_jail2_marcus1()
    call ep28_dialogues_jail2_marcus2()
    $ cloth = "CasualDress1"
    $ cloth_type = "CasualDress"
    $ rain = True
    $ rainIntencity = 3
    $ lightning = True
    $ day_time = "evening"
    $ day_suffix = "_Evening"
    $ add_hook("enter_scene", "ep28_dialogues_jail2_marcus3", scene="street_police", once=True)

    $ define_inventory_object("butt_plug", {"description" : _("Анальная пробка"), "label_suffix" : "_use_butt_plug", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/butt_plug" + res.suffix + ".png"})
    $ questLog(54, False)
    $ questLog(56, True)
    $ add_inventory("butt_plug", 1, True)
    $ add_hook("enter_scene", "ep28_quests_police_final_home", scene="basement_bedroom2", once=True)
    $ add_hook("Building", "ep28_dialogues_jail2_marcus5", scene="street_police", label="marcus_block1")
    music stop
    img black_screen
    with diss
    pause 2.0
    call change_scene("street_police", "Fade_long", False)
    $ marcus_visit1_completed = True
    return

label ep28_quests_police_final_home:
    call ep28_dialogues_jail2_marcus4()
    $ remove_inventory("butt_plug", 1, True)
    $ rain = False
    $ lightning = False

    return







#
