default ep213_quests_victoria1_init_flag = False
default ep213_quests_victoria_completed_day = 0

label ep213_quests_victoria1_init:
    if ep213_quests_victoria1_init_flag == True:
        return
    $ add_hook("before_open", "ep213_quests_victoria2_check", scene="monica_office_entrance", label="victoria_office_scene")
    $ ep213_quests_victoria1_init_flag = True
    return

label ep213_quests_victoria2_check:
    if day - ep212_quests_melanie_completed_day > 1 and week_day != 7 and day_time != "evening": # Запускается через день после событий с Мелани, не в воскресенье и днем
        $ remove_hook()
        call ep213_quests_victoria3()
    return False

label ep213_quests_victoria3:
    $ define_inventory_object("victoria_pomade", {"description" : t_("Помада Виктории"), "label_suffix" : "_use_victoria_pomade", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/victoria_pomade" + res.suffix + ".png"})
    call ep213_dialogues1_victoria_1()
    call ep213_dialogues1_victoria_2()
    call ep213_dialogues1_victoria_3()
    $ visited_list = [2]
label ep213_quests_victoria3_loop1:
    if len(visited_list) >= 4:
        jump ep213_quests_victoria3_loop2
    call ep213_dialogues1_victoria_3a()
    if _return in visited_list:
        call ep213_dialogues1_victoria_4()
        jump  ep213_quests_victoria3_loop1
    $ visited_list.append(_return)
    if _return == 1:
        call ep213_dialogues1_victoria_5()
        jump ep213_quests_victoria3_loop1
    if _return == 3:
        call ep213_dialogues1_victoria_6()
        jump ep213_quests_victoria3_loop1
    if _return == 4:
        call ep213_dialogues1_victoria_7()
        jump ep213_quests_victoria3_loop1

label ep213_quests_victoria3_loop2:
    call ep213_dialogues1_victoria_8()
    call ep213_dialogues1_victoria_9()
    call ep213_dialogues1_victoria_10()
    call ep213_dialogues1_victoria_11()
    call ep213_dialogues1_victoria_12()
    call ep213_dialogues1_victoria_13()
    call ep213_dialogues1_victoria_14()
    call put_work_clothes()
    call change_scene("working_office_cabinet2", "Fade_long")
    $ add_hook("change_time_day", "ep213_quests_victoria4_checknext", scene="global", label="ep213_quests_victoria4_checknext")
    $ ep213_quests_victoria_completed_day = day
    return

label ep213_quests_victoria4_checknext:
    return
