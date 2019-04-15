default bettyBardieFitnessStage = 0

label ep24_quests_bardie1:
    # Барди зовет Монику после уборки (после первого застолья со Стивом)
    $ restore_music()
    $ remove_hook()
    call ep24_dialogues1_bardie()
    if _return == False:
        $ add_hook("Bardie", "ep24_quests_bardie2", scene="bedroom_bardie")
    else:
        $ questLog(34, True)
        $ add_hook("floor2_betty_fitness_dialogue", "ep24_quests_bardie3", scene="menu", caption=_("Согласиться и предупредить Барди..."), priority=95, active=True)
    call change_scene("basement_bedroom2", "Fade_long", False)
    return

label ep24_quests_bardie2:
    # Моника отказалась от помощи Барди, повтор диалога начинается у Барди в комнате
    if act=="l":
        return
    if cloth != "Governess":
        return
    call ep24_dialogues2_bardie()
    if _return == True:
        $ remove_hook()
        call ep24_quests_bardie1()
        return False
    return False

label ep24_quests_bardie3:
    # Нажато меню Согласиться и предупредить Барди...
    $ EP22_Quests_Betty3Flag1 = True
    call ep24_dialogues5_betty0()
    $ move_object("Bardie", scene="bedroom_bardie")
    $ add_hook("Bardie", "ep24_quests_bardie4", scene="bedroom_bardie", label=["day_time_temp", "bardie_fitness"])
    call refresh_scene_fade()
    return

label ep24_quests_bardie4:
    # Моника сообщает Барди о том что они едут на фитнесс
#    $ remove_hook()
    if cloth != "Governess":
        return
    call ep24_dialogues3_fitness1()
    if _return == True:
        $ add_hook("Betty", "ep24_quests_bardie5", scene="floor2", label=["day_time_temp", "bardie_fitness"])

    call refresh_scene_fade()
    return False

label ep24_quests_bardie5:
    # Моника говорит Бетти что она вернулась от Барди и можно ехать на фитнесс
    call ep22_dialogues4_1a0()
    if _return == False:
        return False

    $ remove_hook(label="bardie_fitness")
    $ add_cleaning(True)
    $ add_hook("open", "EP22_Quests_Betty4", scene="street_fitness")
    $ add_hook("fitness_end", "ep24_quests_bardie6", scene="global")
    call change_scene("street_fitness", "Fade_long", "snd_car_engine")
    return False

label ep24_quests_bardie6:
    # Моника говорит Барди что Бетти осталась одна
    call ep24_dialogues3_fitness2()
    if bettyBardieFitnessStage == 0:
        $ bettyBardieFitnessStage = 1
        call ep24_dialogues3_fitness3()
        return False

    return
