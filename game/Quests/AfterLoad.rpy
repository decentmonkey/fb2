label process_afterload:
    if monicaWorkingAtBiffOffice == False and monicaOutfitsEnabled[6] == True:
        $ remove_hook(label="biff_work_dialogue1")
        $ ep26_quests_biff1_Flag = False
        call ep26_quests_biff1() from _call_ep26_quests_biff1_1

    call ep28_quests() from _call_ep28_quests
    call ep29_quests_init() from _rcall_ep29_quests_init
    call ep29_revenge_quest1_init() from _rcall_ep29_revenge_quest1_init
    call monica_cheats_init() from _rcall_monica_cheats_init
    call ep210_quests_load_init() from _rcall_ep210_quests_load_init
    call ep211_quests_load_init() from _rcall_ep211_quests_load_init
    call ep212_quests_load_init() from _rcall_ep212_quests_load_init
    call ep213_quests_load_init() from _rcall_ep213_quests_load_init
    call ep214_quests_load_init() from _rcall_ep214_quests_load_init
    call ep215_quests_load_init() from _rcall_ep215_quests_load_init
    call ep216_quests_load_init() from _rcall_ep216_quests_load_init
    return

label process_afterload_part2:
    m "here"
    call questHelp_init()
    $ questHelp("house1")
    $ questHelp("house2")
    $ questHelp("house3")
    $ questHelp("house4")
    $ questHelp("fitness1")
    $ questHelp("fitness2")
    $ questHelpDesc("house_desc1")

    $ questHelp("house2", True)
    $ questHelp("house3", False)

    $ questHelp("dick1")
    $ questHelp("dick2")
    $ questHelp("dick3")
    $ questHelp("dick4")
    $ questHelp("dick5")
    $ questHelp("dick6")

    m "here2"
    return

label quest_test1:
    $ questHelp("fitness1", True)
    $ questHelp("fitness2", True)
    return

label quest_test2:
    $ questHelp("dick3", True)
    $ questHelp("dick4", True)
    $ questHelp("dick1", False)
    $ questHelp("dick2", False)
#    $ questHelp("dick5", False)
#    $ questHelp("dick6", False)
    return
