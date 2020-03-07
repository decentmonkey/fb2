default slumsApartmentsStatus = 0
default slumsApartmentsInited1 = False

default slumsApartmentsRentStarted = False
default slumsApartmentsRentActive = False
default slumsApartmentsMonicaKnow = False

default slumsApartmentsSkipFirstSaturdayActive = False

label ep211_slums_apartments_quest1_menu:
    if slumsApartmentsStatus == 0: # Первый разговор
        call ep211_dialogues6_slum_apartment_3()
        if _return == 0:
            return True
        if _return == -1:
            return False
        if slumsApartmentsInited1 == False:
            call ep211_quests_slums_apartments1_init()
            call ep211_quests_slums_apartments1_inita()
        else:
            call ep211_quests_slums_apartments1_inita()
        $ slumsApartmentsMonicaKnow = True
        $ remove_objective("ask_kebab")
        $ add_hook("HomeEnter", "ep211_slums_apartments_quest2_enter_home", scene="street_monicahome", label="jack_apartments1")
        $ add_hook("MonicaWindow", "ep211_slums_apartments_quest2_enter_home", scene="street_monicahome", label="jack_apartments1")
        $ add_hook("Shawarma_Trader", "ep211_slums_apartments_quest1_jack", scene="street_monicahome", label="jack_apartments1")
        $ set_active("Street_MonicaHome_TeleportSlums", False, scene="street_monicahome")

        $ autorun_to_object("ep211_dialogues6_slum_apartment_5", scene="street_monicahome")
        #$ move_object("Shawarma_Trader", "whores_place_shawarma")
        $ move_object("Shawarma_Trader", "street_monicahome")
        $ streetMonicaHomeMonicaSuffix = 0
        $ cloth = "Whore"
        $ cloth_type = "Whore"
        $ map_enabled = False
        $ monicaHomeMiniMapEnabled = False
        music stop
        img black_screen
        with diss
        pause 2.0
        call change_scene("street_monicahome", "Fade_long", False)
    return False

label ep211_slums_apartments_quest1_jack:
    if act=="l":
        return
    call ep211_dialogues6_slum_apartment_5()
    return False

label ep211_slums_apartments_quest2_enter_home:
    if act=="l":
        call ep211_dialogues6_slum_apartment_4()
        return False
    $ set_active("Teleport_Bathroom", False, scene="monicahome_livingroom")
    $ set_active("Teleport_Kitchen", False, scene="monicahome_livingroom")
    $ set_active("Teleport_Wardrobe", False, scene="monicahome_livingroom")
    $ set_active(False, teleport=True, scene="monicahome_livingroom")
    $ set_active(False, group="environment", scene="monicahome_livingroom")
    $ set_active("Cocktail", True, scene="monicahome_livingroom")
    $ move_object("Shawarma_Trader", "monicahome_livingroom")
    $ add_hook("Cocktail", "ep211_dialogues6_slum_apartment_4", scene="monicahome_livingroom", label="jack_apartments1")
    $ add_hook("Monica", "ep211_dialogues6_slum_apartment_4", scene="monicahome_livingroom", label="jack_apartments1")
    $ add_hook("Shawarma_Trader", "ep211_slums_apartments_quest3_jack", scene="monicahome_livingroom", label="jack_apartments1")
    call change_scene("monicahome_livingroom", "Fade_long", "snd_door_open1")
    return False

label ep211_slums_apartments_quest3_jack:
    if act=="l":
        return
    call ep211_dialogues6_slum_apartment_6()
    if _return == 0 or _return == -1:
        if _return == -1:
            $ slumsApartmentsStatus = 1
        $ remove_hook(label="jack_apartments1")
        $ del(map_objects["Teleport_Slums_Apartments"])
        $ set_active("Teleport_Slums_Apartments", False, scene="hostel_street")
        $ move_object("Shawarma_Trader", "whores_place_shawarma")
        $ slumsApartmentsMiniMapActive = False
        $ slumsDirtyStreetMiniMapActive = True
        $ map_enabled = True
        call change_scene("hostel_street", "Fade_long")
        return False
    $ slumsApartmentsStatus = 1
    $ slumsApartmentsRentStarted = True
    $ slumsApartmentsRentActive = True
    $ questLog(71, True)
    $ add_objective("earn_money_rent_apartments", _("Заработать $ 300 за аренду апартаментов до субботы."), c_green, 30)
    $ remove_hook(label="jack_apartments1")
    $ set_active("Teleport_Bathroom", True, scene="monicahome_livingroom")
    $ set_active("Teleport_Kitchen", True, scene="monicahome_livingroom")
    $ set_active("Teleport_Wardrobe", True, scene="monicahome_livingroom")
    $ set_active("Street_MonicaHome_TeleportSlums", True, scene="street_monicahome")
    $ set_active(True, teleport=True, scene="monicahome_livingroom")
    $ set_active(True, group="environment", scene="monicahome_livingroom")
    $ move_object("Shawarma_Trader", "whores_place_shawarma")
    $ cloth = "HomeCloth4"
    $ cloth_type = "HomeCloth"
    $ map_enabled = True
    $ autorun_to_object("ep211_dialogues6_slum_apartment_7", scene="monicahome_livingroom")
    if week_day > 3:
        $ slumsApartmentsSkipFirstSaturdayActive = True
    $ add_hook_day("ep211_slums_apartments_quest4_check_payment", week_day = 6)
    call refresh_scene_fade_long()
    return False


label ep211_slums_apartments_quest4_check_payment:
    if slumsApartmentsSkipFirstSaturdayActive == True:
        $ slumsApartmentsSkipFirstSaturdayActive = False
        return
    if monicaRestApartments == False:
        $ notif(_("Оплата за апартаменты в трущобах."))
        $ slumsApartmentsRentActive = True
        $ add_money(-slumsApartmentsRentPrice)
    else:
        # сцена оплаты
        call ep211_dialogues6_slum_apartment_10()
        if _return == -1: # нет денег
            pass
        if _return == 1:
            # оплата полностью
            pass
        if _return == 2: #скидка 10%
            pass
        m "here"

    return
