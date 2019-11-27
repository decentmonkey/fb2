default ep29_quests_melanie_started = False

label ep29_quests_melanie_check:
    if ep29_quests_melanie_started != False or ep27_melanie_visited_victoria == False or ep27_melanie_refused_victoria_friendship == True:
        return
    $ ep29_quests_melanie_started = True
    # Начинаем квест с Мелани
    m "here"
    return
