default ep219_quests_load_init_flag = False

label ep219_quests_load_init:
    if ep219_quests_load_init_flag == False:
        $ ep219_quests_load_init_flag = True
        if char_info["Biff"]["level"] == 4:
            $ char_info["Biff"]["caption"] = t_("Цыпочке надо развлекать папочку, чтобы он продолжал давать ей работу.")
            $ char_info["Biff"]["enabled"] = True
        if char_info["Biff"]["level"] < 5:
            $ questHelp("office_58")

        if ep218_quests_betty_completed_day > 0:
            call ep219_quests_ralph_init1()
        else:
            if bettyFredLaundryHasSex == False or ep215_quests_betty_refused == True or ep217_quests_betty_refused == True or (ep218_quests_betty_day > 0 and ep218_quests_betty_completed_day == 0):
                # если квесты с Бетти прерваны
                if monicaBardieRalphSeducingStage > 0: # если встречается с Ральфом
                    if monicaBettyRalphSeduction7 == True: # если открыты все действия с Ральфом
                        call ep219_quests_ralph_init1()

        if fallingPathStarted == True:
            $ questHelp("work_slums_54")
            $ citizen4BForced = True
    return
