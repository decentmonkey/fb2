default ep25_quests1Flag1 = False
default ep25_quests1Flag2 = False

label ep25_quests1:
    # Моника пытается зайти в здание Стива
    if ep25_quests1Flag1 == False:
        $ ep25_quests1Flag1 = True
        $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_dialogues1_shop1b", scene="street_cloth_shop", label="cloth_shop_closed")
    if monicaAskedVictoriaAboutSteveMoney == False:
        call ep25_dialogues1_shop1()
        return False
    if ep25_quests1Flag2 == False:
        $ ep25_quests1Flag2 = True
        $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop1", scene="street_cloth_shop")

    $ add_objective("find_casual_dress", _("Найти нормальную одежду"), c_orange, 15)
    call ep25_dialogues1_shop1a()
    return False
