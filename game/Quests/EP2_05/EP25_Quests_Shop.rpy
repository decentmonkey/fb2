default ep25_quests_shop1_shop_inited = False
default monicaHasCasualDress1 = False
default monicaBoughtCasualDress1 = False
default monicaStealCasualDress1 = False

default clothShopUsualDayVisitorsAmount = 4
default clothShopUsualEveningVisitorsAmount = 0

label ep25_quests_shop1:
    # Вход в магазин одежды (первый раз)
    $ remove_hook()
    call locations_init_clothing_shop()

    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop2", scene="street_cloth_shop", label=["cloth_shop_enter1", "cloth_shop_quests"])
    $ autorun_to_object("ep25_dialogues1_shop1c", scene="cloth_shop_view1")

    $ add_hook("Cashier", "ep25_quests_shop3", scene="cloth_shop_cashier", label="cloth_shop_quests")

#    call ep25_quests_steve1()
    call ep25_quests_shop2()

    return False

label ep25_quests_shop2:
    # Вход в магазин одежды, обычный

    $ set_active(False, group="cloth_shop_visitors", scene="Cloth_Shop", recursive=True)

    # Скрываем посетителей, кроме 4-х случайных
    $ shopVisitorsList = ["Shop_Visitor1", "Shop_Visitor2", "Shop_Visitor3", "Shop_Visitor4", "Shop_Visitor5", "Shop_Visitor6", "Shop_Visitor7", "Shop_Visitor8", "Shop_Visitor9", "Shop_Visitor10"]
    $ currentVisitorsAmount = clothShopUsualDayVisitorsAmount
    if day_time == "evening":
        currentVisitorsAmount = clothShopUsualEveningVisitorsAmount
    $ activeVisitors = random.sample(set(shopVisitorsList), currentVisitorsAmount)
    python:
        for visitorName in activeVisitors:
            set_active(visitorName, True, scene="cloth_shop_view1", recursive=True)
            set_active(visitorName, True, scene="cloth_shop_view2", recursive=True)

    call change_scene("cloth_shop_view1")

    return False

label ep25_quests_shop3:
    # Разговор с кассиром (поиск платья и покупка)
    if act=="l":
        return
    $ remove_hook()

    call ep25_dialogues1_shop2()
    if _return == False:
        $ clothShopUsualDayVisitorsAmount = 0 # В магазине никого нет
        $ add_hook("Cashier", "ep25_quests_shop6", scene="cloth_shop_cashier", label=["cloth_shop_quests", "steal_dress"]) # Теперь платье можно и украсть
        $ add_hook("open", "ep25_quests_shop5", scene="cloth_shop_view1", label=["cloth_shop_quests", "steal_dress"])
        $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4a", scene="street_cloth_shop", label=["cloth_shop_enter2", "cloth_shop_quests"]) # блокируем вход в магазин
        $ add_hook("change_time_day", "ep25_quests_shop4b", scene="global") # Разблокируем вход в магазин на следующий день

        call change_scene("street_cloth_shop")
        return False

    $ monicaHasCasualDress1 = True
    $ monicaBoughtCasualDress1 = True
    $ remove_objective("find_casual_dress")
    $ cloth = "CasualDress1"
    $ cloth_type = "CasualDress"
    call ep25_quests2()
    $ autorun_to_object("ep25_dialogues1_shop2a", scene="street_cloth_shop") # Комментарий на улице о покупке платья
    call change_scene("street_cloth_shop")

    $ remove_hook(label="cloth_shop_quests")
    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4", scene="street_cloth_shop", label="cloth_shop_enter_refuse")
    return False

label ep25_quests_shop4:
    # Моника не хочет заходить в магазин после покупки платья
    call ep25_dialogues1_shop3()
    return False

label ep25_quests_shop4a:
    # Моника не хочет заходить в магазин сегодня
    call ep25_dialogues1_shop4a()
    return False
label ep25_quests_shop4b:
    # Вход в магазин разблокируется на следующий день
    $ remove_hook()
    $ remove_hook(label="cloth_shop_enter2")
    return

label ep25_quests_shop5:
    # В магазине мало народа. Может быть украсть платье?
    if lastSceneName != "street_cloth_shop":
        return
    call ep25_dialogues1_shop4()
    call ep25_dialogues1_shop5()
    if _return == True:
        call ep25_quests_shop7()
        return False
    call change_scene("cloth_shop_cashier")
    return
label ep25_quests_shop6:
    # Моника может купить или украсть платье
    if act=="l":
        return

    # Говорим о том чтобы купить платье
    call ep25_dialogues1_shop2()
    if _return == False:
        call change_scene("street_cloth_shop")
        return False

    $ monicaHasCasualDress1 = True
    $ monicaBoughtCasualDress1 = True
    $ remove_objective("find_casual_dress")
    $ cloth = "CasualDress1"
    $ cloth_type = "CasualDress"
    call ep25_quests2()
    $ autorun_to_object("ep25_dialogues1_shop2a", scene="street_cloth_shop") # Комментарий на улице о покупке платья
    call change_scene("street_cloth_shop")

    $ remove_hook(label="cloth_shop_quests")
    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4", scene="street_cloth_shop", label="cloth_shop_enter_refuse")
    return

label ep25_quests_shop7:
    # Воруем платье
    m "Воруем платье"
    return

















#
