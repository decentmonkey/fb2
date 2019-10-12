label process_afterload:
    if monicaWorkingAtBiffOffice == False and monicaOutfitsEnabled[6] == True:
        $ remove_hook(label="biff_work_dialogue1")
        $ ep26_quests_biff1_Flag = False
        call ep26_quests_biff1()
        m "here"
    return
