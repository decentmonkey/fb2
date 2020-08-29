default ep215_quests_pub1_inited = False
default ep215_quests_vest_only_active = False
default ep215_quests_pub2_lastday = 0
default ep215_quests_ashley_dialogue1_active = False
default ep215_quests_ashley_dialogue2_active = False
default ep215_quests_molly_monica_fight_day = 0
default monica_shiny_hole_queen_day = 0

label ep215_quests_pub1:
    if ep215_quests_pub1_inited == True:
        return
    $ ep215_quests_pub1_inited = True
    $ ep215_quests_vest_only_active = True
    $ add_hook("Teleport_Pub", "ep215_quests_pub2", scene="pub_makeuproom", label="ep215_quests_pub2")

    return

label ep215_quests_pub2:
    if cloth_type != "StripOutfit" or get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False:
        return
    if day - ep215_quests_pub2_lastday < 4: # не показываем слишком часто
        return
    $ ep215_quests_pub2_lastday = day
    call ep215_dialogues1_pub_1()
    $ add_hook("before_open", "ep215_quests_pub3_molly1", scene="pub_makeuproom", label="ep215_quests_pub3_molly1")
#    $ add_talk("Pub_StripteaseGirl1", "ep215_quests_pub3_molly1", scene="pub_makeuproom", label="ep215_quests_pub3_molly1")
    return

label ep215_quests_pub3_molly1:
    if ep215_quests_pub2_lastday == day:
        return
    $ remove_hook(label="ep215_quests_pub3_molly1")
    $ remove_hook(label="ep215_quests_pub2")
    $ ep215_quests_vest_only_active = False
    call ep215_dialogues1_pub_2()
    $ add_talk("Pub_StripteaseGirl1", "ep215_quests_pub3_molly2", scene="pub_makeuproom", label="ep215_quests_pub3_molly2")
    return

label ep215_quests_pub3_molly2:
    if cloth_type != "Whore":
        $ cloth = "Whore"
        $ cloth_type = "Whore"
        sound snd_fabric1
        fadeblack 2.0
    call ep215_dialogues1_pub_3() # предложение баттла
    if _return == False:
        return False
    # баттл
    $ remove_hook()
    call ep215_dialogues1_pub_4()
    call ep215_dialogues1_pub_5()
    call ep215_dialogues1_pub_7()
    $ move_object("Pub_StripteaseGirl1", "empty")
    $ monicaDancedLastDay = day
    $ ep215_quests_ashley_dialogue1_active = True
    $ add_talk("Pub_StripteaseGirl1", "ep215_quests_pub3_molly3", scene="pub_makeuproom", label="ep215_quests_pub3_molly2")

    return False

label ep215_quests_pub3_molly3:
    if ep215_quests_molly_monica_fight_day == day:
        return
    call ep215_dialogues1_pub_9()
    if _return == False:
        return False
    # драка
    $ ep215_quests_molly_monica_fight_day = day
    call ep215_dialogues1_pub_9_loop1()
    if _return == 0: # уйти
        return False
    if _return == -2: # Моника отказалась на второй баттл
        return False
    if _return == 1: # второй баттл
        $ monicaDancedLastDay = day
        $ move_object("Pub_StripteaseGirl1", "empty")
        call ep215_dialogues1_pub_10()
        if _return == False:
            return False
        $ remove_hook(label="ep215_quests_pub3_molly2")
        # Моника королева Shiny Hole
        $ monica_shiny_hole_queen_day = day
        call ep215_dialogues1_pub_11()
        $ questLog(84, True)
        $ add_talk("Pub_StripteaseGirl1", "ep215_dialogues1_pub_12", scene="pub_makeuproom", label="monica_queen_molly_talk_refuse")
        $ add_talk("Pub_StripteaseGirl2", "ep215_quests_pub4_claire", scene="pub_makeuproom", label="ep215_quests_pub4_claire")
        return False

    return False


label ep215_quests_pub4_claire:
    $ remove_hook()
    call ep215_dialogues1_pub_13()
    $ ep215_quests_ashley_dialogue1_active = False
    $ ep215_quests_ashley_dialogue2_active = True
    return False











#
