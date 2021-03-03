default ep219_quests_photoshoot1_init_day = 0
default ep219_quests_photoshoot10_biff_talk_enabled = True
label ep219_quests_photoshoot1_init:
    if ep219_quests_photoshoot1_init_day > 0:
        return
    $ ep219_quests_photoshoot1_init_day = day
    $ questHelp("office_60")
    return
