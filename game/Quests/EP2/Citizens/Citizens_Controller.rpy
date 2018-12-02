default citizensAmountDay = 8
default citizensAmountEvening = 5

default citizen1_offered_last_day = 0
default citizen2_offered_last_day = 0
default citizen3_offered_last_day = 0
default citizen4_offered_last_day = 0
default citizen5_offered_last_day = 0
default citizen6_offered_last_day = 0
default citizen7_offered_last_day = 0
default citizen8_offered_last_day = 0
default citizen9_offered_last_day = 0
default citizen10_offered_last_day = 0
default citizen11_offered_last_day = 0
default citizen12_offered_last_day = 0
default citizen13_offered_last_day = 0
default citizen14_offered_last_day = 0
default citizen15_offered_last_day = 0


label citizens_dialogue:
    if kebabWorkInProgress == False:
        mt "Я не собираюсь с ним разговаривать без надобности!"
        "Мне противны эти люди!"
        "Они не соответствуют моему статусу!"
        return

    $ citizenObjName = obj_name

    if citizenObjName == "Citizen_1" or citizenObjName == "Citizen_2":
        call citizen1_dialogue()

    if citizenObjName == "Citizen_3":
        call citizen3_dialogue()
    if citizenObjName == "Citizen_4":
        call citizen4_dialogue()
    if citizenObjName == "Citizen_5":
        call citizen5_dialogue()
    if citizenObjName == "Citizen_6":
        call citizen6_dialogue()
    if citizenObjName == "Citizen_7":
        call citizen7_dialogue()
    if citizenObjName == "Citizen_8":
        call citizen8_dialogue()
    if citizenObjName == "Citizen_9":
        call citizen9_dialogue()
    if citizenObjName == "Citizen_10":
        call citizen10_dialogue()
    if citizenObjName == "Citizen_11":
        call citizen11_dialogue()
    if citizenObjName == "Citizen_12":
        call citizen12_dialogue()
    if citizenObjName == "Citizen_13":
        call citizen13_dialogue()
    if citizenObjName == "Citizen_14":
        call citizen14_dialogue()
    if citizenObjName == "Citizen_15":
        call citizen15_dialogue()

    call refresh_scene_fade()
    return

label citizens_init:
    $ citizens_list_source = {
        "Citizen_1":{},
        "Citizen_2":{},
        "Citizen_3":{},
        "Citizen_4":{},
        "Citizen_5":{},
        "Citizen_6":{},
        "Citizen_7":{},
        "Citizen_8":{},
        "Citizen_9":{},
        "Citizen_10":{},
        "Citizen_11":{},
        "Citizen_12":{},
        "Citizen_13":{},
        "Citizen_14":{},
        "Citizen_15":{},
    }
    return

label citizens_init_day:

    return
label citizens_init_evening:
    python:
        citizensEveningList = random.sample(set(list(citizens_list_source.keys())), citizensAmountEvening)
        if "Citizen_1" in citizensEveningList:
            citizensEveningList.append("Citizen_2")
        if "Citizen_2" in citizensEveningList:
            citizensEveningList.append("Citizen_1")
        if "Citizen_3" in citizensEveningList:
            citizensEveningList.append("Citizen_9")
        if "Citizen_9" in citizensEveningList:
            citizensEveningList.append("Citizen_3")
        citizensEveningList = list(set(citizensEveningList)) #unique
        set_active(False, scene="all", group="citizens")
        for var1 in citizensEveningList:
            print var1
            set_active(var1, True, scene="all")
    $ print citizensEveningList
    return
