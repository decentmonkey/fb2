default ep218_quests_victoria_init_flag = False

label ep218_quests_victoria_init:
    if ep218_quests_victoria_init_flag == True or ep27_melanie_visited_victoria != True:
        return
    $ ep218_quests_victoria_init_flag = True
    # стартуем в ближайший рабочий день
    $ add_hook("office_work_process", "ep218_quests_victoria1_start", scene="global", label="ep218_quests_victoria1_start", priority = 50)
    $ questHelp("victoria_17")
    return

label ep218_quests_victoria1_start:
    $ remove_hook()
    m "here"
    call office_work_begin1_end()
    return False
