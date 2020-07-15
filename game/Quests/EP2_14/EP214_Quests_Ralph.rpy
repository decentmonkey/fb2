default ep214_stored_cloth = ""
default ep214_stored_cloth_type = ""
default stored_map_objects = False
default ep214_ralph_blowjob_day = 0
default ep214_ralph_last_regular_meeting_day = 0

label ep214_quests_ralph1:
    call ep214_dialogues5_bardie_ralph_1()
    $ add_objective("go_fitness", t_("Поехать с Бетти на фитнес во вторник или четверг."), c_white, 15)
    return

label ep214_quests_ralph2:
    # берем одежду Бетти и едем домой
    $ remove_objective("go_fitness")
    call ep214_dialogues5_bardie_ralph_2b()
    $ ep214_stored_cloth = cloth
    $ ep214_stored_cloth_type = cloth_type
    $ cloth = "BettyCloth"
    $ cloth_type = "BettyCloth"
    $ enter_scene("ep214_dialogues5_bardie_ralph_2c", once=True)
    $ move_object("Bardie", "empty")

    python:
        rooms_list = get_rooms_recursive("House")
        for room_name1 in rooms_list:
            add_hook("Monica", "ep214_dialogues5_bardie_ralph_2b1", scene=room_name1, label="Monica_Ralph_Quest")

    $ map_enabled = False
    $ miniMapEnabledOnly = ["Bedroom", "Bathroom", "Floor1", "Floor2", "Basement", "Laundry"]
    $ add_hook("BasementWardrobe", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_bedroom1", label="Monica_Ralph_Quest")
    $ add_hook("Table", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_bedroom2", label="Monica_Ralph_Quest")
    $ add_hook("BasementBed", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_bedroom2", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box1", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box2", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box3", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box4", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box5", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box6", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Panties_Box", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Street", "ep214_dialogues5_bardie_ralph_2b1", scene="floor1", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Kitchen", "ep214_dialogues5_bardie_ralph_2b1", scene="floor1", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Basement_Side", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_hole", label="Monica_Ralph_Quest")
    if monicaBardieRalphSeducingStage == 5:
        $ move_object("Ralph", "living_room")
        $ add_talk("Ralph", "ep214_quests_ralph6_regular", scene="living_room", label="Monica_Ralph_Quest_regular")
        $ add_talk("Ralph", "ep214_quests_ralph3", scene="living_room", label="Monica_Ralph_Quest")
    if monicaBardieRalphSeducingStage == 6:
        $ move_object("Ralph", "empty")
        $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_2b4", scene="bedroom_bardie", label="Monica_Ralph_Quest")
        $ add_hook("Teleport_Street", "ep214_dialogues5_bardie_ralph_2b3", scene="floor1", label="Monica_Ralph_Quest")
        $ add_hook("Teleport_Kitchen", "ep214_dialogues5_bardie_ralph_2b2", scene="floor1", label="Monica_Ralph_Quest")
        $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_4", scene="floor1", label="Monica_Ralph_Quest", once=True)
        $ add_hook("before_open", "ep214_quests_ralph8_meeting_regular", scene="bedroom2", label="Monica_Ralph_Quest")
        $ add_hook("before_open", "ep214_quests_ralph7_search_ralph", scene="living_room", once=True, label="Monica_Ralph_Quest")

    call change_scene("basement_bedroom1", "Fade_long")

    return

label ep214_quests_ralph3: # первая сцена с Ральфом
    call ep214_dialogues5_bardie_ralph_5()
    $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_6", scene="floor1", label="Monica_Ralph_Quest", once=True)
    $ add_objective("go_fitness", t_("Вернуться в фитнес зал."), c_orange, 125)
    $ stored_map_objects = map_objects
    $ map_objects = {
            "Teleport_Fitness" : {"text" : t_("ФИТНЕСС"), "xpos" : 356, "ypos" : 411, "base" : "map_marker", "state" : "visible"},
            "Teleport_House" : {"text" : t_("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active"}
    }
    $ map_enabled = True
    $ add_hook("before_open", "ep214_quests_ralph4", scene="street_fitness", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Street", "ep214_quests_ralph4", scene="floor1", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_LivingRoom", "ep214_dialogues5_bardie_ralph_6a", scene="floor1", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Kitchen", "ep214_dialogues5_bardie_ralph_6a", scene="floor1", label="Monica_Ralph_Quest")
    $ add_hook("BasementWardrobe", "ep214_dialogues5_bardie_ralph_6a", scene="basement_bedroom1", label="Monica_Ralph_Quest")
    $ add_hook("Table", "ep214_dialogues5_bardie_ralph_6a", scene="basement_bedroom2", label="Monica_Ralph_Quest")
    $ add_hook("BasementBed", "ep214_dialogues5_bardie_ralph_6a", scene="basement_bedroom2", label="Monica_Ralph_Quest")
    $ add_hook("Panties_Box", "ep214_dialogues5_bardie_ralph_6a", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Basement_Side", "ep214_quests_ralph4", scene="basement_hole", label="Monica_Ralph_Quest")
    $ ep214_ralph_blowjob_day = day
    call change_scene("floor1", "Fade_long")
    return False

label ep214_quests_ralph4:
    $ remove_objective("go_fitness")
    $ remove_hook(label="Monica_Ralph_Quest")
    $ miniMapEnabledOnly = []
    imgf scene_Map
    sound highheels_run1
    pause 3.0
    call ep214_dialogues5_bardie_ralph_7()
    $ map_objects = stored_map_objects
    $ stored_map_objects = False
    $ add_objective("talk_bardie", t_("Поговорить с Барди."), c_blue, 125)
    $ add_hook("before_open", "ep214_quests_ralph5_bardie", scene="bedroom_bardie", label="Monica_Ralph_Quest")
    $ cloth = ep214_stored_cloth
    $ cloth_type = ep214_stored_cloth_type
    sound highheels_short_walk
    img black_screen
    with Dissolve(0.5)
    pause 2.0
    $ map_enabled = False
    $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Monica_2_[cloth][day_suffix]", "click" : "street_fitness_environment2", "actions" : "l", "zorder" : 10}, scene="street_fitness")
    $ add_hook("open", "EP22_Quests_Betty6a", scene="street_fitness")
    $ autorun_to_object("ep22_dialogues4_7a", scene="street_fitness")
    $ ep22_dialogues4_7a_flag1 = False
    call change_scene("street_fitness", "Fade_long", False)
    return False

label ep214_quests_ralph5_bardie: # разговор с Барди
    $ remove_hook()
    call ep214_dialogues5_bardie_ralph_8()
    $ enter_scene("ep214_dialogues5_bardie_ralph_9", once=True)
    $ remove_objective("talk_bardie")
    $ questLog(72, False)
    $ questLog(79, True)
#    $ add_objective("go_fitness", t_("Поехать с Бетти на фитнес во вторник или четверг."), c_blue, 125)
    $ monicaBardieRalphSeducingStage = 6
    call change_scene("floor2", "Fade_long")
    return False

label ep214_quests_ralph6_regular: # подход к Ральфу в обычное время
    if cloth == "Governess":
        call ep214_dialogues5_bardie_ralph_9a()
        return False
    return
label ep214_quests_ralph7_search_ralph:
    call ep214_dialogues5_bardie_ralph_10()
    if ep214_ralph_last_regular_meeting_day == 0:
        $ add_hook("Teleport_Kitchen", "ep214_dialogues5_bardie_ralph_11a", scene="floor1", label="Monica_Ralph_Quest")
        $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_11b", scene="basement_bedroom2", label="Monica_Ralph_Quest", once=True)
        $ add_hook("Teleport_Basement_Pool", "ep214_dialogues5_bardie_ralph_11b", scene="floor1_stairs", label="Monica_Ralph_Quest")
        $ add_hook("Teleport_Street", "ep214_dialogues5_bardie_ralph_11c", scene="floor1", label="Monica_Ralph_Quest")
        $ add_hook("Teleport_BedroomBardie", "ep214_dialogues5_bardie_ralph_11d", scene="floor2", label="Monica_Ralph_Quest")
        $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_11e", scene="bathroom_bath", once=True, label="Monica_Ralph_Quest")
        $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_11f", scene="bedroom_second", once=True, label="Monica_Ralph_Quest")

    call refresh_scene_fade()
    return
label ep214_quests_ralph8_meeting_regular: # регулярные встречи с Ральфом
    $ remove_hook(label="Monica_Ralph_Quest")
    m "here"
    $ miniMapEnabledOnly = []
    imgf scene_Map
    sound highheels_run1
    pause 3.0
    $ cloth = ep214_stored_cloth
    $ cloth_type = ep214_stored_cloth_type
    sound highheels_short_walk
    img black_screen
    with Dissolve(0.5)
    pause 2.0
    $ map_enabled = False
    $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Monica_2_[cloth][day_suffix]", "click" : "street_fitness_environment2", "actions" : "l", "zorder" : 10}, scene="street_fitness")
    $ add_hook("open", "EP22_Quests_Betty6a", scene="street_fitness")
    $ autorun_to_object("ep22_dialogues4_7a", scene="street_fitness")
    $ ep22_dialogues4_7a_flag1 = False
    call change_scene("street_fitness", "Fade_long", False)
    return





#
