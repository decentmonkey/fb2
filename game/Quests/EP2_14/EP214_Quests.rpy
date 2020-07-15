default ep214_quests_load_init_flag = False
label ep214_quests_load_init:
    if ep214_quests_load_init_flag == False:
        $ ep214_quests_load_init_flag = True
        if char_info["Ralph"]["level"] == 1:
            $ char_info["Ralph"]["enabled"] = True
            $ char_info["Ralph"]["caption"] = t_("Ральф примерный семьянин.")
