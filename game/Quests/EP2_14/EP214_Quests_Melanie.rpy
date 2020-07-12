default ep214_quests_melanie_day = 0

label ep214_quests_melanie:
    $ remove_hook()
    $ ep214_quests_melanie_day = day
    call ep214_dialogues4_melanie_alex_1()
    call ep214_dialogues4_melanie_alex_2()
    $ move_object("Melanie", "empty")
    return
