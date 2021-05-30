default ep255_quests_shinyhole1_init_flag = False
default ep255_quests_shinyhole_claire_private1_day = 0
default ep255_quests_shinyhole_claire_private1_refused = False
default ep255_quests_shinyhole_claire_private1_monica_day = 0
label ep255_quests_shinyhole1_init:
    if ep255_quests_shinyhole1_init_flag == True:
        return
    $ ep255_quests_shinyhole1_init_flag = True
    $ questHelp("shinyhole_62")
    $ add_hook("Teleport_Hostel_Pub", "ep255_quests_shinyhole2_enter_pub", scene="hostel_street", label="ep255_quests_shinyhole2_enter_pub")
    return

label ep255_quests_shinyhole2_enter_pub:
    $ add_hook("before_open", "ep255_quests_shinyhole3_pub", scene="pub", label="ep255_quests_shinyhole3_pub", once=True)
    return

label ep255_quests_shinyhole3_pub:
    if get_active_objects("Pub_StripteaseGirl2", scene="pub") == False or ep218_quests_monica_queen_job1_day == day:
        return
    $ remove_hook(label="ep255_quests_shinyhole2_enter_pub")
    $ ep255_quests_shinyhole_claire_private1_day = day
    # предложение Клэр о привате
    call ep22_5_dialogues5_pub_1()
    if _return == False:
        $ move_object("Pub_StripteaseGirl2", "pub_makeuproom")
        $ questHelp("shinyhole_62", False)
        $ ep255_quests_shinyhole_claire_private1_refused = True
        return
    $ move_object("Pub_StripteaseGirl2", "pub_makeuproom")
    $ add_hook("before_open", "ep255_quests_shinyhole4_monica", scene="pub_makeuproom", label="ep255_quests_shinyhole4_monica")
    return

label ep255_quests_shinyhole4_monica:
    if get_active_objects("Pub_StripteaseGirl2", scene="pub_makeuproom") == False:
        return
    $ remove_hook()
    call ep22_5_dialogues5_pub_2()
    $ ep255_quests_shinyhole_claire_private1_monica_day = day
    $ questHelp("shinyhole_62", True)
    $ add_char_progress("Pub_StripteaseGirl2", 25, "claire_private1_money")
#    $ move_object("Pub_StripteaseGirl2", "empty")
    call refresh_scene_fade_long()
    return





#
