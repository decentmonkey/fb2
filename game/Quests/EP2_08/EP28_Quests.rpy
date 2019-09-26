label ep28_quests:

    # Проверка на баг с отсутствием диалога с Бифом о работе
    if ep26_quests_biff1_Flag == True and monicaWorkingAtBiffOffice == False:
        call ep26_quests_biff1()
    return
