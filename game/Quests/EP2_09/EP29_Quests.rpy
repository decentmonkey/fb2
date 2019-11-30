default ep29_quests_initialized = False

label ep29_quests_init:
    if ep29_quests_initialized == False:
        $ ep29_quests_initialized = True
        $ set_active ("Pub_Washbasin", False, scene="pub")
    return
