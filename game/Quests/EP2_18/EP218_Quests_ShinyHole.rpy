default ep218_quests_shinyhole_init_flag = False
default ep218_quests_claire_danced_nude_last_day = 0

label ep218_quests_shinyhole_check:
    if ep218_quests_shinyhole_init_flag == True:
        return
    if ep217_quests_shinyhole16_molly_after_private_flag == True and questHelpGetStatus("shinyhole_57a") == 1 and questHelpGetStatus("shinyhole_57") == 1:
        $ ep218_quests_shinyhole_init_flag = True
        $ questHelp("shinyhole_59")
        $ add_talk("Pub_StripteaseGirl2", "ep218_quests_shinyhole1_claire", scene="pub_makeuproom", label="ep218_claire")

    return

label ep218_quests_shinyhole1_claire:
    if ep217_quests_shinyhole15_claire_after_private_day == day:
        return
    if cloth != "Whore":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "Whore"
        $ cloth_type = "Whore"
    call ep218_dialogues1_pub_1()
    if _return == False: # отказала
        call refresh_scene_fade()
        return False

    call pub_dance2_claire_dance2()
    if ep218_quests_claire_danced_nude_last_day == 0:
        call ep218_dialogues1_pub_3()
    $ questHelp("shinyhole_59", True)
    call change_scene("pub", "Fade_long")
    $ notif(t_("Клэр ушла домой."))
    $ move_object("Pub_StripteaseGirl2", "empty")
    $ monicaDancedLastDay = day
    $ ep218_quests_claire_danced_nude_last_day = day
    return False











#
