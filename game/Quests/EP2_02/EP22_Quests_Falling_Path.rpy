default fallingPathServedCustomers = []
default fallingPathServedCustomersTotal = 0
default fallingPathServedCustomersToday = 0


label ep22_quests_falling_path1: # Инициализация ситизенов перед нападением на Монику
    if questOffendMonicaFlyersCitizen12Completed == True: #если событие уже произошло, то стираем хук
        if questOffendMonicaFlyersCitizen6ThanksGiven == True:
            $ remove_hook()
            return
        if day_time == "evening":
            $ set_active("Citizen_6", False, scene="all")
        else:
            $ set_active("Citizen_6", True, scene="all")
        return
    if monicaKnowAboutKebabWork == False: # Если Моника не знает о кебабах, то ждем
        return
    call citizens_init_monica_offend()
    $ questOffendMonicaFlyersCitizen12Started = True
    return

label ep22_quests_falling_path2:
    $ fallingPathServedCustomers = []
    return

label ep22_quests_falling_path3:
    python:
#        for citizenName in citizens_list_source:
        citizensArr = get_objects(scene="all", group="citizens")
        for citizenObj in citizensArr:
            add_hook(citizenObj[1], "ep22_quests_falling_path4", scene=citizenObj[2], group="falling_path_dialogues_citizens")
    return
label ep22_quests_falling_path4:
    if act=="l":
        return
    if day_time == "evening":
        mt "Я боюсь подходить к людям в вечернее время."
        "Это опасно..."
        return False
    if obj_name in fallingPathServedCustomers:
        mt "Я уже достаточно показала ему сегодня..."
        return False
    return

label falling_path_store_customer():

    $ fallingPathServedCustomers.append("Citizen_" + str(citizenId))
    $ fallingPathServedCustomersTotal += 1
    $ fallingPathServedCustomersToday += 1
    if fallingPathServedCustomersTotal == 2:
        $ questLog(17, False)
        $ questLog(22, True)
    return
#label="monica_kebab_offend"

label ep22_quests_falling_path5:
    $ remove_objective("thanks_for_rescue")
    $ remove_hook(label="monica_kebab_offend")
    $ autorun_to_object("citizen6_dialogue_after_offend4", scene="hostel_edge_1_a")
    $ add_hook("change_time_day", "ep22_quests_falling_path2", scene="global")
    $ notif(_("Falling Path started..."))
    $ questLog(16, False)
    $ questLog(17, True)
    call init_location("hostel_edge_1_a", "hostel_edge_1_a_init")
    call ep22_quests_falling_path3()
    return
