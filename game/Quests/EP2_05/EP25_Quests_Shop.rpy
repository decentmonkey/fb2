default ep25_quests_shop1_shop_inited = False


label ep25_quests_shop1:
    # Вход в магазин одежды (первый раз)
    $ remove_hook()
    call locations_init_clothing_shop()
    $ set_active(False, group="cloth_shop_visitors", scene="Cloth_Shop", recursive=True)

    $ shopVisitorsList = ["Shop_Visitor1", "Shop_Visitor2", "Shop_Visitor3", "Shop_Visitor4", "Shop_Visitor5", "Shop_Visitor6", "Shop_Visitor7", "Shop_Visitor8", "Shop_Visitor9", "Shop_Visitor10"]
    $ activeVisitors = random.sample(set(shopVisitorsList), 4)
    python:
        for visitorName in activeVisitors:
            set_active(visitorName, True, scene="Cloth_Shop", recursive=True)


    call change_scene("cloth_shop_view1")

    call ep25_quests_steve1()

    return False
