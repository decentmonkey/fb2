default ep27_quests_flash_quest1_inited = False
default monicaWorkFlashCardQuestActive = False
default monicaWorkFlashCardNeedReportsAmount = 7 #Кол-во отчетов, которые надо собрать
default monicaWorkFlashCardReportsCollected = 0 # Сколько отчетов собрано
default monicaWorkFlashCardQuestNeedGiveReports = False # отчеты собраны, надо их сдать
default monicaWorkFlashCardQuestReportsNeedTalkBiff = False # после сдачи отчетов надо поговорить с Бифом
default monicaWorkFlashCardQuestReportsCollectedBySelf = False # Сама-ли Моника собирала отчеты последний раз

default monicaWorkFlashCardQuestGoodReportsCount = 0
default monicaWorkFlashCardQuestBadReportsCount = 0



label ep27_quests_office1:
    # Инициализация квестов со флешкой (этап1)

    $ add_hook("Biff", "ep27_quests_office2", scene="monica_office_cabinet_table", label="monica_flash_card_quest1")

    $ ep27_quests_flash_quest1_inited = True
    return

label ep27_quests_office2:
    # Разговор с Бифом о том, что Моника должна приносить флешку с отчетами
    $ remove_hook()
    if act=="l":
        return
    call ep27_dialogues4_biff1()

    $ miniMapEnabledOnly = ["none"]
    $ add_hook_multi("ep26_dialogues5_office1_1a", scene="monica_office_secretary", label="monica_flash_card_quest1_block", filter={"teleport":True})
    $ add_hook("Teleport_Monica_Office_Entrance", "ep26_dialogues5_office1_1a", scene="monica_office_secretary", label="monica_flash_card_quest1_block")
    $ add_hook("Secretary", "ep27_quests_office3", scene="monica_office_secretary", label="monica_flash_card_quest1")


    $ autorun_to_object("ep27_dialogues4_biff2", scene="monica_office_secretary")
    call change_scene("monica_office_secretary", "Fade_long")

    return False

label ep27_quests_office3:
    # Разговор с секретаршей о флешке
    $ remove_hook()
    $ define_inventory_object("flash_card", {"description" : _("Флеш Карта"), "label_suffix" : "_use_flash_card", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/flash_card" + res.suffix + ".png"})

    call ep27_dialogues4_biff3()

    call ep27_quests_office4_reset_reports() # Сбрасываем отчеты

    # Инитим сбор отчетов у воркеров
    $ add_hook_multi("ep27_quests_office_workers1", scene="working_office", label="monica_flash_card_quest1", filter={"group":"workers"})
    $ add_hook_multi("ep27_quests_office_workers1", scene="working_office2", label="monica_flash_card_quest1", filter={"group":"workers"})

    $ add_hook("Teleport_Monica_Office_Cabinet", "ep27_quests_office6_return_reports_teleport", scene="monica_office_secretary", label="monica_flash_card_quest1", priority=151)
    $ add_hook("Secretary", "ep27_quests_office5", scene="monica_office_secretary", label="monica_flash_card_quest1")
    $ add_hook("Biff", "ep27_quests_office7_biff", scene="monica_office_cabinet_table", label="monica_flash_card_quest1")

    $ add_hook("Teleport_Street_Monica_Office", "ep27_quests_office9_check_exit", scene="monica_office_entrance", label="monica_flash_card_quest1", priority=300)
    $ add_hook("before_open", "ep27_quests_office6b", scene="monica_office_cabinet_table", label=["monica_flash_card_quest1", "monica_flash_card_quest1_cabinet_table"], priority=151)

    $ questLog(46, True)
    $ miniMapEnabledOnly = []
    $ remove_hook(label="monica_flash_card_quest1_block")
    $ autorun_to_object("ep27_dialogues4_biff4", scene="monica_office_secretary")
    call refresh_scene_fade()
    return False

label ep27_quests_office4_reset_reports:
    $ monicaWorkFlashCardQuestActive = True
    $ monicaWorkFlashCardReportsCollected = 0
    $ monicaWorkFlashCardQuestNeedGiveReports = False
#    $ monicaWorkFlashCardQuestReportsNeedTalkBiff = False
#    $ monicaWorkFlashCardQuestReportsCollectedBySelf = False
    $ ep27_flash_card_reports_done_arr = [] # сбрасываем список собранных отчетов
    return

label ep27_quests_office5: # Перехват возвращения отчетов (разговор с секретаршей)
    if act=="l":
        return
    jump ep27_quests_office6_return_reports_teleport

label ep27_quests_office6_return_reports_teleport: # Перехват возвращения отчетов
    if monicaWorkFlashCardQuestActive == False or monicaWorkFlashCardQuestNeedGiveReports == False:
        return
    # Разговор с секретаршей
    call ep27_dialogues4_biff8()
    call ep27_quests_office4_reset_reports() # Сбрасываем отчеты
    call change_scene("monica_office_secretary")
    $ remove_objective("reports_to_biff")
    $ add_objective("reports_to_biff", _("Биф просил зайти к нему после сдачи отчетов."), c_orange, 20)
    return False

label ep27_quests_office6b: # Перехват возвращения отчетов в офисе Бифа по миникарте
    jump ep27_quests_office6_return_reports_teleport

label ep27_quests_office7_biff: # Разговор с Бифом после сдачи отчетов
    if act=="l":
        return
    if monicaWorkFlashCardQuestReportsNeedTalkBiff == False: # Нет необходимости общаться по отчетам
        return
    if monicaWorkFlashCardQuestReportsCollectedBySelf == True:
        call ep27_dialogues4_biff5() # Хороший отчет
        $ monicaWorkFlashCardQuestGoodReportsCount += 1
    else:
        call ep27_dialogues4_biff6() # Плохой отчет
        $ monicaWorkFlashCardQuestBadReportsCount += 1
    $ monicaWorkFlashCardQuestReportsNeedTalkBiff = False
    $ remove_objective("reports_to_biff")
    call change_scene("monica_office_cabinet", "Fade_long")
    return False

label ep27_quests_office8_julia: # Моника заставляет собирать отчеты Юлию
    call ep27_dialogues6_julia1()
    $ monicaWorkFlashCardQuestReportsCollectedBySelf = False
    $ monicaWorkFlashCardQuestNeedGiveReports = True
    $ monicaWorkFlashCardReportsCollected = monicaWorkFlashCardNeedReportsAmount
    $ monicaWorkFlashCardQuestReportsNeedTalkBiff = True
    $ monicaWorkFlashCardReportLastDay = day
    $ remove_objective("reports_to_biff")
    $ add_objective("reports_to_biff", _("Отдать собранные отчеты для Бифа."), c_green, 20)
    $ changeDayTime("evening") # Изменяем на вечер
    $ monicaOfficeWorkedToday = True
#    $ move_object("Julia", "empty") # Юлия уходит с работы (обычный день)
    call ep27_quests_julia1_init() # Чекаем инициализацию квеста с Юлией
    $ autorun_to_object("ep27_dialogues6_julia2", scene="working_office_cabinet")
    call refresh_scene_fade()
    return

label ep27_quests_office9_check_exit: # Проверка на выход из офиса, если надо сдать отчет
    if monicaWorkFlashCardQuestActive == True and monicaWorkFlashCardQuestNeedGiveReports == True:
        call ep27_dialogues6_julia3b()
        return False
    return












#
