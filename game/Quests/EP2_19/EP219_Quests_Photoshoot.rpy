default ep219_quests_photoshoot1_init_day = 0
default ep219_quests_photoshoot10_biff_talk_enabled = False
default ep219_quests_work_enabled = True
default ep219_quests_photoshoot10_day = 0
default photoshoot11_count = 0

label ep219_quests_photoshoot1_init:
    if ep219_quests_photoshoot1_init_day > 0:
        return
    $ ep219_quests_photoshoot1_init_day = day
    $ ep219_quests_photoshoot10_biff_talk_enabled = True
    $ questHelp("office_60")
    return

label ep219_quests_photoshoot2_biff:
    $ questHelp("photoshoot_15")
    call ep219_dialogues2_office_1()
    if _return == False:
        $ add_talk("Biff", "ep219_quests_photoshoot3_biff_repeat", scene="monica_office_cabinet_table", label="ep219_quests_photoshoot3_biff_repeat")
        call change_scene("monica_office_secretary", "Fade_long")
        $ questHelp("office_60", False)
        return False
    $ ep219_quests_photoshoot10_biff_talk_enabled = False
    call ep219_quests_photoshoot4_campbell()
    return False

label ep219_quests_photoshoot3_biff_repeat:
    call ep219_dialogues2_office_2()
    if _return == False:
        call change_scene("monica_office_secretary", "Fade_long")
        return False
    $ remove_hook(label="ep219_quests_photoshoot3_biff_repeat")

    $ ep219_quests_photoshoot10_biff_talk_enabled = False
    call ep219_quests_photoshoot4_campbell()
    return False

label ep219_quests_photoshoot4_campbell: # офис Кэмпбелла
    $ questHelp("photoshoot_15a")
    call ep219_dialogues2_office_3()
    if _return == False:
        $ questHelp("office_60", False)
        $ add_talk("Biff", "ep219_quests_photoshoot3_biff_repeat", scene="monica_office_cabinet_table", label="ep219_quests_photoshoot3_biff_repeat")
        call putoff_work_clothes()
        call process_change_map_location("House")
        call change_scene("street_house_outside", "Fade_long")
        return False
    call ep219_dialogues2_office_3_photoshoot()
    if _return == False:
        $ questHelp("office_60", False)
        $ add_talk("Biff", "ep219_quests_photoshoot3_biff_repeat", scene="monica_office_cabinet_table", label="ep219_quests_photoshoot3_biff_repeat")
        call putoff_work_clothes()
        call process_change_map_location("House")
        call change_scene("street_house_outside", "Fade_long")


    $ shotsAmountCompleted = len(list(set(PS11_shoots_array)))
    if shotsAmountCompleted >= shotsTotalAmount:
        $ questHelp("photoshoot_15a", True)
    $ questHelp("photoshoot_15", True)
    $ add_hook("Biff", "ep22_quests_office6", scene="monica_office_cabinet_table", label="photoshoot") #Мне надо получить деньги от Бифа
    $ add_hook("Teleport_Monica_Office_Entrance", "ep22_dialogue6_7a", scene="monica_office_secretary", label="photoshoot", priority = 105) #Блокируем выход пока не получили деньги от Бифа
    call change_scene("monica_office_cabinet", "Fade_long")
    $ monicaOutfitsEnabled[10] = True
    $ autorun_to_object("ep219_dialogues2_office_4", scene="street_monica_office")
    $ questHelp("office_60", True)
    $ ep219_quests_photoshoot10_day = day
    return

label ep219_quests_photoshoot5_regular:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    sound snd_car_door
    $ renpy.pause (1.0, hard=True)
    sound snd_car_turn_on
    $ renpy.pause (1.0, hard=True)
    img scene_Map_Evening
    with fade
    sound snd_car_engine
    $ renpy.pause(6.0, hard=True)
    img black_screen
    with fade
    sound snd_car_door
    $ renpy.pause (2.0, hard=True)
    music Groove2_85
    call ep219_dialogues2_office_3a()
    if _return == False:
        return False
    call ep219_dialogues2_office_3_photoshoot()
    if _return == False:
        return False
    $ shotsAmountCompleted = len(list(set(PS11_shoots_array)))
    if shotsAmountCompleted >= shotsTotalAmount:
        $ questHelp("photoshoot_15a", True)

    return
