default ep210_quests_escort_stage = 0

label ep210_quests_escort_eat_process:
    if ep210_quests_escort_stage == 0 and ep22_quests_monica_presentation_completed == True:
        call ep210_quests_escort1_philip1()
        return False
    return


label ep210_quests_escort1_philip1: # Первая встреча с Филиппом в ресторане
    # Приходит Филипп
    $ add_hook("Teleport_Street_Rich_Hotel", "ep210_quests_escort_reception1", scene="rich_hotel_reception", label="ep210_quests_escort_reception1")
    $ add_hook("ReceptionGirl", "ep210_quests_escort_reception1", scene="rich_hotel_reception", label="ep210_quests_escort_reception1")

    call ep210_dialogues2_escort_start_Phillip_1()
    if _return == False:
        $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_4", scene="street_rich_hotel")
        call change_scene("rich_hotel_reception", "Fade_long")
        return

    # Секс в туалете
    call ep210_dialogues2_escort_start_Phillip_2()
    if _return == 1:
    if _return == 2:

    $ questLog(61, True)
    $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_3", scene="street_rich_hotel")
    $ add_money(300.0)
    call change_scene("rich_hotel_reception", "Fade_long")

    return


label ep210_quests_escort_reception1: # Рецепшин перехватывает Монику
    $ remove_hook(label="ep210_quests_escort_reception1")
    call ep210_dialogues2_escort_start_Phillip_5()
    return False
