default juliaOfficeOffended1 = False # Моника заставляла Юлию работать допоздна
default juliaOfficeOffended2 = False # Моника заставляла Юлию собирать отчеты вместо себя и ругалась при этом

default juliaQuestInited = False

default juliaQuestStarted = False
default juliaQuestRefused = False # Моника отказалась от квеста с Юлией (прогнала Фреда)
default juliaQuestStage = 0
default juliaQuestStage0_Progress = 0

default juliaQuestLastDay = 0

label ep27_quests_julia1_init: # Инит квеста с Юлией
    if juliaQuestInited == True:
        return
    $ add_hook("office_work_process", "ep27_quests_julia2", scene="global", label="ep27_quests_julia1_a")
    $ juliaQuestInited = True
    return

label ep27_quests_julia2: # Проверка на первый приход Фреда
    if juliaOfficeOffended1 == False or juliaOfficeOffended2 == False: # Если Моника хорошо общается с Юлией, то Фред не приходит
        return
    $ remove_hook()
    # Фред приходит!
    call ep27_dialogues6_julia3()
    if _return == True:
        $ autorun_to_object("ep27_dialogues6_julia4", scene="working_office_cabinet")
        $ questLog(47, True)
        $ juliaQuestStage0_Progress = 1
        $ juliaQuestStarted = True
    else:
        $ juliaQuestRefused = True
    return False

label ep27_quests_julia3: # Юлия, ты сегодня хорошо выглядишь
    call ep27_dialogues6_julia5()
    $ juliaQuestLastDay = day
    #fred
    return
