default ep27_quests_initialized = False
label ep27_quests1:
    # Инициализация v0.7
    if char_info.has_key("Bartender") == False:
        call characters_pub_init()
    $ char_info["Bartender"]["enabled"] = True

    if photoshoot7_count > 0:
        $ monicaOutfitsEnabled[7] = True # Открываем следующий костюм (черный лебедь)

    # Мелани
    call ep27_quests_melanie1_init()

    $ currentMusicPriority = 0
    $ ep27_quests_initialized = True
    return
