default ep214_slums_offer_activated = False
default ep214_slums_offer_day = 0
default ep214_slums_citizen4_aborted = False
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
        fadeblack 2.0
        call change_scene("street_corner", "Fade_long")
        return True
    if _return == 1:
        call ep214_slums3_start_fp_part2()
        return True
    return

label ep214_slums2_perry_repeat:
    if act=="l":
        return
    $ remove_hook()
    $ set_active("Perry", False, scene="whores_place")
    call ep214_dialogues2_citizens_1b()
    call ep214_slums3_start_fp_part2()
    return False

label ep214_slums3_start_fp_part2: # Начало новой части квестов в трущобах (старые неактивны)
    $ questLog(82, True)
    call locations_init_hostel_inside()
    $ add_hook("Teleport_Hostel_Street_Door", "ep214_dialogues2_citizens_7", act="l", scene="hostel_street", label="Perry_Debt")
    $ add_hook("Poster", "ep214_dialogues2_citizens_7", scene="hostel_street_door", label="Perry_Debt")
    $ add_hook("Teleport_hostel_reception", "ep214_slums4_enter_hostel", scene="hostel_street_door", label="Perry_Debt")
    $ add_hook("Perry", "ep214_dialogues2_citizens_7", scene="hostel_reception", label="Perry_Debt")
    return

label ep214_slums4_enter_hostel:
    if act=="l":
        call ep214_dialogues2_citizens_7()
        return False
    call change_scene("hostel_reception", "Fade", "snd_jail_door")
    return False
