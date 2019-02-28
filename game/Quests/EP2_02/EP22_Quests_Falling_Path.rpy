default fallingPathServedCustomers = []
default fallingPathServedCustomersGlobal = {}
default fallingPathServedCustomersTotal = 0
default fallingPathServedCustomersToday = 0
default fallingPathCitizenVisitsData = {"visits":0}

define fallingPathMaxCustomersPerDay = 3 # Количество обслуженных клиентов до того как наступит вечер

init python:
    def store_citizen_action(actionName, amount = 1):
        global fallingPathCitizenVisitsData
        if fallingPathCitizenVisitsData.has_key(actionName) == False:
            fallingPathCitizenVisitsData[actionName] = 0
        fallingPathCitizenVisitsData[actionName] += 1
        return

    def fallingPathGetCitizenData(propertyName):
        global fallingPathCitizenVisitsData
        if fallingPathCitizenVisitsData.has_key(propertyName) == False:
            fallingPathCitizenVisitsData[propertyName] = 0
        return fallingPathCitizenVisitsData[propertyName]


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
    $ fallingPathServedCustomersToday = 0
    return

label ep22_quests_falling_path3:
    python:
#        for citizenName in citizens_list_source:
        citizensArr = get_objects(scene="all", group="citizens")
        for citizenObj in citizensArr:
            add_hook(citizenObj[1], "ep22_quests_falling_path4", scene=citizenObj[2], group="falling_path_dialogues_citizens")
    return
label ep22_quests_falling_path4:
    # Диалоги проституции
    if act=="l":
        return
    if kebabWorkInProgress == True or cloth == "Kebab":
        return
    if day_time == "evening":
        mt "Я боюсь подходить к людям в вечернее время."
        "Это опасно..."
        return False
    if obj_name in fallingPathServedCustomers:
        mt "За такие маленькие деньги я больше ничего не собираюсь показывать ему сегодня..."
        return False
    call citizens_init()
    if obj_name == "Citizen_2":
        $ obj_name = "Citizen_1"
    $ store_music()
    music Hidden_Agenda
    $ monicaHostelEdge1ASuffixOneTime = 2
    $ citizenId = citizens_list_source[obj_name]["id"]
    $ pylonPreset = rand(1,2)
    $ funcName = "citizen" + str(citizenId) + "_dialogue_pilon"
    call falling_path_start_customer()
    call expression funcName
    $ restore_music()
    if _return != False:
        $ notif(_("Моника обслужила 'Клиента'"))
        call falling_path_store_customer()
    return False

label falling_path_start_customer():
    if fallingPathServedCustomersGlobal.has_key("Citizen_" + str(citizenId)) == False:
        $ fallingPathServedCustomersGlobal["Citizen_" + str(citizenId)] = {"visits":0}
    $ fallingPathCitizenVisitsData = fallingPathServedCustomersGlobal["Citizen_" + str(citizenId)]
    return
label falling_path_store_customer():
    $ fallingPathServedCustomers.append("Citizen_" + str(citizenId))
    $ fallingPathServedCustomersGlobal["Citizen_" + str(citizenId)]["visits"] += 1
    $ fallingPathServedCustomersTotal += 1
    $ fallingPathServedCustomersToday += 1
    if fallingPathServedCustomersTotal == 2:
        $ questLog(17, False)
        $ questLog(22, True)
    if fallingPathServedCustomersToday >= fallingPathMaxCustomersPerDay:
        $ changeDayTime("evening")
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
    call falling_path_store_customer()
    call citizens_init_day()
    return

#    call citizens_init()
