default ep28_quests_police_day1_cage1_flag = False
default ep28_quests_police_day1_bed1_flag = False
default ep28_quests_monica_offended_day1 = False # Монику использовали заключенные день1
default ep28_quests_monica_offended_prisoners = False # Моника сама наехала на заключенных
default ep28_quests_monica_kicked_prisoners = False # Моника ударила и укусила заключенных
default ep28_quests_monica_called_monicapubname = False

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
    $ add_hook("cage_interact", "ep28_dialogues_jail3a", scene="police", label="cage_interact_nobody")
    call refresh_scene_fade_long()
    return
