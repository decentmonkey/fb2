default ep218_quests_shinyhole_init_flag = False

label ep218_quests_shinyhole_check:
    if ep218_quests_shinyhole_init_flag == True:
        return
    if ep217_quests_shinyhole16_molly_after_private_flag == True and questHelpGetStatus("shinyhole_57a") == 1 and questHelpGetStatus("shinyhole_57") == 1:
        m "init!"
        pass
    return
