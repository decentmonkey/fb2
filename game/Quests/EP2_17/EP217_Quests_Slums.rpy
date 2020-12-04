default citizen5BlockedByDay = 0
default citizen5BForced = False
default citizen5LastDay = 0

default citizen9BlockedByDay = 0
default citizen9BForced = False
default citizen9LastDay = 0

label ep217_quests_slums1: # клик на Акира Сан
    call ep217_dialogues4_citizens_2()
    if _return == -1: # не стала отходить с ним
        $ questHelp("work_slums_53", False, skipIfTrue=True)
        return
    if _return == -2: # пришли к пилону, но отказалась
        fadeblack 2.5
        $ questHelp("work_slums_53", False, skipIfTrue=True)
        call change_scene("hostel_edge_1_a", "Fade_long")
        return False

    $ citizen5BForced = False
    # идем в апартаменты
    $ questHelp("work_slums_53", True)
    $ citizen5BlockedByDay = day+3
    $ citizen5LastDay = day

    if _return == -3:
        # прогнала
        $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="street_monicahome")
        call change_scene("street_monicahome", "Fade_long")
    call refresh_scene_fade()
    return False
