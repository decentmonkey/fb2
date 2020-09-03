default p215_slums1_alcoholic_last_day = 0

label ep215_slums1_dialogue_alcoholic:
    # Алкоголик подзывает Монику
    call ep215_dialogues6_citizens_1()
    if _return == 0:
        call refresh_scene_fade()
        return False
    $ move_object("Citizen_14", "empty")
    if _return == -1: # отказалась вести домой
        call change_scene("hostel_edge_1_a", "Fade_long")
        return False
    $ citizen14BlockedByDay = day + 3
    if _return == -2:# отказалась пить
        $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="street_monicahome")
        call change_scene("street_monicahome", "Fade_long")
        call refresh_scene_fade()
        return False
    if _return == -3: # выпила одну и остановилась
        $ cloth = "HomeCloth4"
        $ cloth_type = "HomeCloth"
        fadeblack 1.0
        $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="monicahome_livingroom")
        call change_scene("monicahome_livingroom", "Fade", False)
        $ changeDayTime("evening")
        $ set_rest_place("slums_apartments")
        $ changeDayTime("day")
        return False

    # выпила все и проснулась с алкашом
    $ p215_slums1_alcoholic_last_day = day

    $ changeDayTime("evening")
    $ set_rest_place("none")
    $ changeDayTime("day")

    call ep215_dialogues6_citizens_1b()
    fadeblack 2.0
    $ move_object("Citizen_14", "empty")
    $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="street_monicahome")
    call change_scene("street_monicahome", "Fade_long")
    return False
