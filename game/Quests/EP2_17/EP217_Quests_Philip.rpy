default ep217_quests_philip_visited_day = 0
default ep217_quests_philip_refused = 0

label ep217_quests_philip1: # едут к Филиппу
    $ ep217_quests_philip_visited_day = day
    $ questHelp("philip_8", True)
    call ep217_dialogues5_phillip_1()
    if _return == False: # убежала не спустившись в подвал
        $ ep217_quests_philip_refused = 1
        $ questHelp("philip_10", False)
        $ autorun_to_object("ep217_dialogues5_phillip_6", scene="street_philiphome")
        $ add_hook("Teleport_Building", "ep217_dialogues5_phillip_6", scene="street_philiphome", label=["private_presentation1_philip_block_after", "evening_time_temp"])
        call change_scene("street_philiphome", "Fade_long")
        return False


    call ep217_dialogues5_phillip_2() #БДСМ комната
    if _return == False: # убежала из комнаты
        $ ep217_quests_philip_refused = 2
        $ questHelp("philip_10", False)
        $ autorun_to_object("ep217_dialogues5_phillip_6", scene="street_philiphome")
        $ add_hook("Teleport_Building", "ep217_dialogues5_phillip_6", scene="street_philiphome", label=["private_presentation1_philip_block_after", "evening_time_temp"])
        call change_scene("street_philiphome", "Fade_long")
        return False

    # сцена завершена успешно

    $ questHelp("philip_10", True)
    $ autorun_to_object("ep217_dialogues5_phillip_3", scene="street_philiphome")
    $ add_hook("Teleport_Building", "ep217_dialogues5_phillip_4", scene="street_philiphome", label="private_presentation1_philip_block_after")
    call change_scene("street_philiphome", "Fade_long")
    return
