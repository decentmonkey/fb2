default bettyVisitedSteve = False
default janeContractCompletedThisWeek = False
default janeContractsCount = 0
default monicaOfferedBoobsToSteve1 = False # Моника предложила сама показать грудь Стиву (контракт с Джейн)
default monicaSteveContractPenaltyActive = False # Действует пенальти на контракты со Стивом
default monicaSteveContractJaneAwaits = False
default monicaJaneTouchedMonicaBoobs = False

# Еженедельный хук (обнуление посещения джейн и тд)
label ep26_quests_steve1:
    $ janeContractCompletedThisWeek = False
    return

label ep26_quests_steve2:
    # Сделка с Джейн
    call ep26_dialogues2_steve1_0() # Выбор контракта
    if _return == 1:
        # Знакомство с Джейн
        call ep26_dialogues2_steve1()
        if _return == 0:
            call ep25_quests_steve19()# Блокируем офис на сегодня (день)
            call change_scene("street_steve_office", "Fade_long", False)
            return False
        if _return == 1:
            $ monicaSteveContractJaneAwaits = True # Стив не будет давать другой работы, пока не будет выполнен контракт с Джейн
            call ep25_quests_steve19()# Блокируем офис на сегодня (день)
            call change_scene("street_steve_office", "Fade_long", False)
            return False
        call ep26_dialogues2_steve3()
        if _return == False:
            $ monicaSteveContractPenaltyActive = True
            call ep25_quests_steve19()# Блокируем офис на сегодня (день)
            call change_scene("street_steve_office", "Fade_long", False)
            return False

#        $ monicaSteveContractPenaltyActive = False
        $ janeContractCompletedThisWeek = True
        $ janeContractsCount += 1
#        $ notif(_("Стив перевел деньги Виктории."))
#        $ monicaEarnedWeeklyMoney = True
#        $ remove_objective("money_for_victoria")
        call ep25_quests_steve19()# Блокируем офис на сегодня (день)
        call change_scene("street_steve_office", "Fade_long", False)
    return False
