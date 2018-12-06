default kebabWorkInProgress = True
default monicaKnowAboutKebabWork = False #Знает-ли Моника об этой работе
default kebabWorkFirstTime = True
default kebabWorkFlyersLeft = 0

label kebab_work_init:
    $ add_hook("Shawarma_Trader", "kebab_work_trader_interact1", scene="whores_place_shawarma", label="kebab_dialogue")
    return

label reduce_flyers:
    $ kebabWorkFlyersLeft = kebabWorkFlyersLeft - 1
    call kebab_work_objective_refresh()
    return

label kebab_work_trader_interact1: # первый разговор о кебабах
    if act == "l":
        return
    if act == "t":
        if day_time == "evening":
            # нет вечерних рендеров разговора о работе
            call monica_shawarma_dialogue0() # он уже закрывается
            call refresh_scene_fade()
            return False
        call kebab_work_start()
        return
        call monica_shawarma_dialogue1()
        if monicaKnowAboutKebabWork == True:
            $ replace_hook("kebab_work_trader_interact2", scene="all", label="kebab_dialogue")
            call kebab_work_start()

    return

label kebab_work_start:
    $ kebabWorkFlyersLeft = monicaKebabWorkFlyersAmount
    $ rnd1 = rand(0, monicaKebabWorkFlyersAmountRandomDiff)
    if rand(0,1) == 1:
        $ rnd1 = rnd1 * -1
    $ kebabWorkFlyersLeft = kebabWorkFlyersLeft + rnd1

    $ add_hook("Teleport_Clothing_Shop", "monica_shawarma_dialogue5", scene="whores_place_shawarma", label="kebab_work")
    if kebabWorkFirstTime == True:
        $ add_hook("enter_scene", "monica_shawarma_dialogue6", scene="hostel_street", label="kebab_work")
        $ add_hook("enter_scene", "monica_shawarma_dialogue7", scene="hostel_street2", label="kebab_work")
        $ add_hook("enter_scene", "monica_shawarma_dialogue9", scene="hostel_street3", label="kebab_work")
        $ add_hook("enter_scene", "monica_shawarma_dialogue8", scene="hostel_edge_1_c", label="kebab_work")
        $ rooms_list = get_rooms_recursive("Street_Corner")
        python:
            for room_name in rooms_list:
                add_hook("Monica", "monica_shawarma_dialogue11", scene=room_name, label="kebab_work")

        #monica_shawarma_dialogue10 mt "В этом районе одни наркоманы и извращенцы!"

    $ map_enabled = False

    $ cloth_type = "Kebab"
    $ cloth = "Kebab"
    call kebab_work_objective_refresh()
    $ kebabWorkFirstTime = False
    return

label kebab_work_objective_refresh:
    if kebabWorkFlyersLeft > 0:
        $ remove_objective("give_flyers")
        $ add_objective("give_flyers", _("Осталось флаеров") + " " + str(kebabWorkFlyersLeft), c_orange, 20)
    else:
        $ remove_objective("give_flyers")
    return

label kebab_work_trader_interact2:
    if act == "l":
        return
    if act == "t":
        if monicaEatedLastDay == day:
            call monica_shawarma_dialogue4() #Моника сыта
            return
    m "interact2"
    return
