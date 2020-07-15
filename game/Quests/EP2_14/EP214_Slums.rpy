default ep214_slums_offer_activated = False
default ep214_slums_offer_day = 0
default ep214_slums_citizen4_aborted = False
default ep214_slums_monnica_licked_perry_last_day = 0
default ep214_slums_monnica_licked_perry_first_day = 0
default ep214_slums_monnica_licked_perry_count = 0
default ep214_slums_monica_perry_talk_count = 0
default ep214_slums_monica_rent_hostel_last_day = 0
default ep214_slums_monica_paid_money_this_week = False
default ep214_perry_debt = 50000.0


label ep214_slums1_offer:
    $ ep214_slums_offer_day = day
    call ep214_dialogues2_citizens_1()
    if _return == -1:
        return False
    if _return == -2: # Укусила
        $ ep214_slums_citizen4_aborted = True
        $ enter_scene("ep214_dialogues2_citizens_5", once=True)
        call bitch(20, "ep214_slums_citizen4_aborted")
        fadeblack 2.0
        call change_scene("street_corner", "Fade_long")
        return True
    if _return == -3: # Убежала от Перри
        $ enter_scene("ep214_dialogues2_citizens_2", once=True)
        call whores_place_init2()
        $ street_whores_perry_active = True
        $ add_hook("Perry", "ep214_slums2_perry_repeat", scene="whores_place", label="ep214_slums2_perry_repeat")
        $ add_hook("Perry", "ep214_dialogues2_citizens_7", scene="whores_place", act="l", label="ep214_slums2_perry_repeat")
        $ add_hook("Teleport_Hostel_1_a", "ep214_dialogues2_citizens_4", act="w", scene="hostel_edge_1_c", label=["day_time_temp", "ep214_slums2_perry_repeat"])
        fadeblack 2.0
        call change_scene("street_corner", "Fade_long")
        return True
    if _return == 1:
        call ep214_slums3_start_fp_part2()
        $ autorun_to_object("ep214_dialogues2_citizens_3", scene="hostel_edge_1_a")
        call refresh_scene_fade()
        call change_scene("hostel_edge_1_a", "Fade_long")
        return True
    return

label ep214_slums2_perry_repeat:
    if act=="l":
        return
    $ remove_hook(label="ep214_slums2_perry_repeat")
    $ set_active("Perry", False, scene="whores_place")
    call ep214_dialogues2_citizens_1b()
    call ep214_slums3_start_fp_part2()
    $ enter_scene("ep214_dialogues2_citizens_3", once=True)
    call change_scene("hostel_edge_1_a", "Fade_long")
    return False

label ep214_slums3_start_fp_part2: # Начало новой части квестов в трущобах (старые неактивны)
    $ questLog(82, True)
    call locations_init_hostel_inside()
    $ add_hook("Teleport_Hostel_Street_Door", "ep214_dialogues2_citizens_7", act="l", scene="hostel_street", label="Perry_Debt")
    $ add_hook("Poster", "ep214_dialogues2_citizens_7", scene="hostel_street_door", label="Perry_Debt")
    $ add_hook("Teleport_hostel_reception", "ep214_slums4_enter_hostel", scene="hostel_street_door", label="Perry_Debt")
    $ add_hook("Perry", "ep214_dialogues2_citizens_7", scene="hostel_reception", label="Perry_Debt")

    $ add_hook_multi("ep214_citizens_click", scene="Street_Corner", recursive=True, label="citizens_interact2", filter={"group":"citizens"})
    $ add_talk("Perry", "ep214_slums5_talk_perry_first_time", scene="hostel_reception", label="Perry_Debt_talk")
    $ add_hook("Teleport_Hostel_Bedroom", "ep214_slums5_talk_perry_first_time", scene="hostel_reception", label="Perry_Debt_talk")

    $ add_hook_day("ep214_slums6_weekly", week_day = 6, label="Perry_Debt_check") #каждую субботу утром будет проверка на отдачу долга Перри
    return

label ep214_slums4_enter_hostel:
    if act=="l":
        call ep214_dialogues2_citizens_7()
        return False
    call change_scene("hostel_reception", "Fade", "snd_jail_door")
    return False

label ep214_slums5_talk_perry_first_time: # первый разговор с Перри
    $ remove_hook(label="Perry_Debt_talk")
    call ep214_dialogues2_citizens_8()
    if _return == 1: # Моника отдала часть денег. полизала и может ночевать, осталась ночевать
        pass
    if _return == -1: # Моника отдала часть денег. полизала и может ночевать, но ушла
        pass
    if _return == -2: # Моника не стала ничего отдавать, уходит
        pass
    if _return == -3: # Моника полизала, может ночевать, но злая
        pass
    if _return == -4: # Моника отдала часть денег. но не лизала (нет жилья)
        pass
    return False

label ep214_slums6_weekly: # вызывается по субботам
    if ep214_perry_debt > 0:
        if ep214_slums_monica_paid_money_this_week == True:
            $ ep214_slums_monica_paid_money_this_week = False
            return
        $ ep214_perry_debt += 1000.0
        $ notif(t_("Долг Перри увеличился на $ 1000"))
    return

label ep214_citizens_click:
    if act=="l":
        return
    m "here"
    return False






#
