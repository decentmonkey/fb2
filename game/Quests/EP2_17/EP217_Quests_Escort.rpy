default ep217_quests_escort2_check_start_party_flag = False

label ep217_quests_escort1:
    call ep217_dialogues1_escort_2()
    call ep217_dialogues1_escort_2a()
    $ remove_objective("go_administrator")
    $ add_objective("go_customer", t_("Пойти к клиенту, который ждет Монику у лифта."), c_blue, 105)
    $ move_object("EscortCustomer1", "rich_hotel_lift")

    $ remove_hook(label="escort_scene8_block_lift")

    $ add_hook("Monica", "ep217_dialogues1_escort_3a", scene="rich_hotel_lift", label="escort_scene8")
    $ add_hook("Teleport_Reception", "ep217_dialogues1_escort_3a", scene="rich_hotel_lift", label="escort_scene8")
    $ autorun_to_object("ep217_dialogues1_escort_3a", scene="rich_hotel_lift")
    $ richHotelLiftSceneSuffix = ""

    $ add_hook("Door", "ep217_dialogues1_escort_3b", scene="rich_hotel_reception", label="escort_scene8")
    $ add_hook("Teleport_Restaurant", "ep217_dialogues1_escort_3b", scene="rich_hotel_reception", label="escort_scene8")
    $ add_hook("Teleport_Street_Rich_Hotel", "ep217_dialogues1_escort_3b", scene="rich_hotel_reception", label="escort_scene8")

    $ add_hook("Lift", "ep217_quests_escort1a", scene="rich_hotel_lift", label="escort_scene8")
    $ add_hook("EscortCustomer1", "ep217_dialogues1_escort_3a", scene="rich_hotel_lift", label="escort_scene8")
    $ add_talk("EscortCustomer1", "ep217_quests_escort1a", scene="rich_hotel_lift", label="escort_scene8")
    $ autorun_to_object("ep217_dialogues1_escort_3b", scene="rich_hotel_reception")
    call refresh_scene_fade()
    return

label ep217_quests_escort1a:
    call ep217_dialogues1_escort_3()
    $ questHelp("escort_15", skipIfExists=True)
    $ questHelp("escort_16", skipIfExists=True)
    $ questHelp("escort_17", skipIfExists=True)
    call ep217_dialogues1_escort_4()
    if _return == -1: # Моника убежала
        $ questHelp("escort_14", False, skipIfTrue=True)
        $ questHelp("escort_15", False, skipIfTrue=True)
        $ questHelp("escort_16", False, skipIfTrue=True)
        $ questHelp("escort_17", False, skipIfTrue=True)
        $ autorun_to_object("ep217_dialogues1_escort_5", scene="street_rich_hotel") # мысли если убежала из номера Адриано сразу после того, как фетишист пришел за ней

    if _return == -2: # отказала в сексе
        $ questHelp("escort_14", False)
        $ questHelp("escort_15", True, skipIfTrue=True)
        $ questHelp("escort_16", False, skipIfTrue=True)
        $ questHelp("escort_17", False, skipIfTrue=True)
#        call ep217_dialogues1_escort_5a() # если сказала Адриано, что она не Моника, и был с ним секс или не было секса
        $ autorun_to_object("ep217_dialogues1_escort_5", scene="street_rich_hotel") # мысли если убежала из номера Адриано сразу после того, как фетишист пришел за ней

    if _return == 1:
        # если все ок
        $ questHelp("escort_14", True)
        $ questHelp("escort_15", True)
        $ questHelp("escort_16", True)
        if ep217_quests_escort2_check_start_party_flag == False:
            $ autorun_to_object("ep217_dialogues1_escort_7", scene="street_rich_hotel")
            call ep217_quests_escort2_init_party()
#            $ enter_scene("ep217_quests_escort2_check_start_party")
        call ep217_dialogues1_escort_5a()


    call ep217_dialogues1_escort_6() # разговор с админом

    $ move_object("ReceptionGirl", "rich_hotel_reception")
    $ remove_hook(label="escort_scene8")
    $ remove_objective("go_customer")
    $ richHotelLiftMonicaSuffix = 1
    $ richHotelLiftSceneSuffix = "_Closed"
    $ move_object("EscortCustomer1", "empty")
    call ep211_quests_escort2_end_day()
    call change_scene("street_rich_hotel", "Fade_long", "snd_lift")


    return False


label ep217_quests_escort2_init_party:
    if ep217_quests_escort2_check_start_party_flag == True:
        return
    $ ep217_quests_escort2_check_start_party_flag = True
    m "init party!"
#    "Пойти на девичник к Кэндис и Эбби."
    $ questHelp("escort_17", skipIfTrue=True)
    $ remove_hook()
    return
