default ep219_quests_load_init_flag = False

label ep219_quests_load_init:
    if ep219_quests_load_init_flag == False:
        if char_info["Biff"]["level"] == 4:
            $ char_info["Biff"]["caption"] = t_("Цыпочке надо развлекать папочку, чтобы он продолжал давать ей работу.")
            $ char_info["Biff"]["enabled"] = True
        if char_info["Biff"]["level"] < 5:
            $ questHelp("office_58")


    return
