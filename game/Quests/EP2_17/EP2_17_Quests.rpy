label ep217_quests:
    if ep215_quests_betty_visit2_completed_day > 0: # если Бетти общалась с соседом, инциализируем квест с Бетти
        $ questHelp("house_45")
        $ add_hook("fitness_end", "ep217_quests_betty1_check", scene="global", label="betty_neighbour_check")
    return
