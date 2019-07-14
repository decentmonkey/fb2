default ep26_quests_initialized = False
label ep26_quests1:
    # Инициализация v0.6
    $ ep26_quests_initialized = True
    $ add_hook_day("ep26_quests_steve1", week_day = 6) # вешаем сброс посещений офиса Стива каждую субботу утром

    return
