# Бетти, Моника и еда на кухне
label ep26_quests_betty1:
    # Инициализация
    $ add_hook_multi("ep26_quests_betty2", scene="kitchen", label=["kitchen_betty_bardie_food1"], filter={"group":"environment"})
    $ add_hook_multi("ep26_quests_betty2", scene="kitchen2", label=["kitchen_betty_bardie_food1"], filter={"group":"environment"})
    $ add_hook("enter_scene", "ep26_quests_betty3", scene="kitchen", label="kitchen_betty_bardie_food1_enter")
    return

label ep26_quests_betty2:
    # Моника трогает на кухне предметы
    return

label ep26_quests_betty3:
    # Моника заходит на кухню
    if day_time == "evening":
        call ep26_dialogues1_bardie12a()
        return False
    call ep26_dialogues1_bardie6()
    if _return == 0: # Моника просто ушла
        call change_scene("floor1", "Fade_long")
        return False
    return False

#Я могу питаться в доме. Если буду соблюдать условие...
#$ questLog(45, True)
