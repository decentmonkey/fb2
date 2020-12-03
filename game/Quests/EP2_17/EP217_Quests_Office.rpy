default ep217_quests_office_menu_enabled = False
default ep217_quests_office1_last_day = 0

default ep217_quests_presentation_completed_day = 0
default ep217_quests_presentation_completed2_day = 0

label ep217_quests_office1:
    if ep217_quests_office1_last_day == 0:
        call ep217_dialogues6_office_1()
    else:
        call ep217_dialogues6_office_3()
    if _return == -1: # отказалась, не получит никакой другой работы
        $ remove_hook(label="ep217_quests_office1")
        $ add_talk("Biff", "ep217_quests_office1", scene="monica_office_cabinet_table", label="ep217_quests_office1")
        $ add_hook("enter_scene", "ep217_dialogues6_office_2a", scene="street_monica_office", label="ep217_quests_office1")
        $ ep217_quests_office1_last_day = day
        $ autorun_to_object("ep217_dialogues6_office_2", scene="street_monica_office")
        $ questHelp("office_53", False)
        call putoff_work_clothes()
        call change_scene("street_monica_office", "Fade_long")
        return False

    $ add_hook("basement_monica_after_sleep_dialogue", "ep217_quests_office2_after_sleep", scene="global", label="ep217_quests_office1")
    $ add_hook("slums_basement_monica_after_sleep_dialogue", "ep217_quests_office2_after_sleep", scene="global", label="ep217_quests_office1")
    $ add_hook("juliahome_monica_after_sleep_dialogue", "ep217_quests_office2_after_sleep", scene="global", label="ep217_quests_office1")

    $ add_hook("change_time_day", "ep217_quests_office3_after_sleep", scene="global", label="ep217_quests_office1_nextday", once=True)
    $ add_talk("Biff", "ep217_dialogues6_office_4a", scene="monica_office_cabinet_table", label="private_presentation1")

    $ questHelp("office_53", True)
    $ questHelp("office_53a")
    call putoff_work_clothes()
    call change_scene("street_monica_office", "Fade_long")

    return False

label ep217_quests_office2_after_sleep:
    $ remove_hook(label="ep217_quests_office1")
    call ep217_dialogues6_office_4()
    return False

label ep217_quests_office3_after_sleep:
    $ add_objective("go_hotel", t_("Идти в отель Ле Гранд для проведения приватной презентации."), c_white, 55)
    $ questHelp("office_53a", True)
    $ questHelp("office_54", skipIfExists=True)
    $ add_hook("Teleport_Rich_Hotel_Reception", "ep217_quests_office4_enter_hotel", scene="street_rich_hotel", label="private_presentation1")
    return

label ep217_quests_office4_enter_hotel:
    if act=="l":
        return
    # презентация
    $ questHelp("office_54", True)
    $ remove_objective("go_hotel")
    call ep217_dialogues6_office_5()
    call ep217_dialogues6_office_6()
    $ questHelp("office_55", True)
    $ questHelp("office_56", True)
    $ questHelp("office_57")
    $ add_talk("Biff", "ep217_quests_office5_biff_after_presentation", scene="monica_office_cabinet_table", label="private_presentation1_after")
    $ ep217_quests_presentation_completed_day = day

    if _return == -2: # Моника не работала в эскорте, убежала
        if day_time != "evening":
            $ changeDayTime("evening")
        $ remove_hook(label="private_presentation1")
        $ autorun_to_object("ep217_dialogues6_office_8", scene="street_rich_hotel")
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep217_dialogues6_office_8", scene="street_rich_hotel", label=["evening_time_temp", "private_presentation1_after_block"])
        $ move_object("Biff", "empty")
        call change_scene("street_rich_hotel", "Fade_long")
        call refresh_scene_fade_long()
        $ questHelp("philip_8", False)
        return False

    if _return == 1: # Моника уехала с Филиппом
        $ questHelp("philip_8")
        if day_time != "evening":
            $ changeDayTime("evening")
        $ remove_hook(label="private_presentation1")
        call ep217_quests_philip1()
        return False

    return False

label ep217_quests_office5_biff_after_presentation:
    $ remove_hook()
    call ep217_dialogues6_office_9()
    call ep213_dialogues4_biff_12() # кастинг

    $ ep217_quests_presentation_completed2_day = day
    $ ep217_quests_office_menu_enabled = False
    $ questHelp("office_57", True)
    call change_scene("monica_office_secretary", "Fade_long")
    return False












#
