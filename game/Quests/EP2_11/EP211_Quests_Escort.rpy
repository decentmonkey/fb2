default ep211_quests_escort1_inited = False

default ep211_quests_stored_cloth = False
default ep211_quests_stored_cloth_type = False

default monicaEscortLastDay = 0 # Когда крайний раз Моника работала в эскорте

default monicaEscortScene1Day = 0
default monicaEscortScene2Day = 0

label ep211_quests_escort1:
    if ep211_quests_escort1_inited == False:
        call locations_init_rich_hotel_restaurant2()
        call rich_hotel_reception_init3()
        $ add_hook("Teleport_Lift", "ep211_quests_escort3_lift_check", scene="rich_hotel_reception", label="rich_hotel_lift_block")
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep211_quests_escort1_enter", scene="street_rich_hotel", label="rich_hotel_escort_enter_check")
        $ add_hook("Door", "ep211_quests_escort3_door_check", scene="rich_hotel_reception", label="rich_hotel_door_block")
        $ ep211_quests_escort1_inited = True
    $ richHotelLiftMonicaSuffix = 1
    $ richHotelLiftSceneSuffix = "_Closed"

    call ep210_dialogues7_escort_hotel_8a()
    $ ep211_quests_stored_cloth = cloth
    $ ep211_quests_stored_cloth_type = cloth_type
    $ cloth = "EscortDress1"
    $ cloth_type = "EscortDress"
    $ add_hook("ReceptionGirl", "ep211_quests_escort2_exit_dialogue", scene="rich_hotel_reception", quest="work_escort")
    $ add_hook("Teleport_Street_Rich_Hotel", "ep211_quests_escort2_exit", scene="rich_hotel_reception", quest="work_escort")
    $ add_hook("Teleport_Restaurant", "ep211_quests_escort4_restaurant", scene="rich_hotel_reception", quest="work_escort")
    $ add_hook("MonicaTable", "ep211_quests_escort5_restaurant_wait_customer", scene="rich_hotel_restaurant", quest="work_escort")
    $ monicaEscortLastDay = day
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    call refresh_scene_fade()
    return

label ep211_quests_escort1_enter: # проверка на вход в отель
    if monicaEscortLastDay == day:
        call ep210_dialogues7_escort_hotel_7d()
        return False
    return

label ep211_quests_escort2_exit:
    call ep211_escort_scene1_14()
    if _return == 1:
        $ remove_hook(quest="work_escort")
        $ cloth = ep211_quests_stored_cloth
        $ cloth_type = ep211_quests_stored_cloth_type
        call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1")
    return False

label ep211_quests_escort2_exit_dialogue:
    if act=="l":
        return
    call ep211_escort_scene1_14()
    if _return == 1:
        $ remove_hook(quest="work_escort")
        $ remove_hook(quest="work_escort")
        $ cloth = ep211_quests_stored_cloth
        $ cloth_type = ep211_quests_stored_cloth_type
        call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1")
    return False

label ep211_quests_escort3_lift_check: # Проверка на вход в лифт
    if cloth_type != "EscortDress":
        call ep211_escort_scene1_13()
        return False
    return

label ep211_quests_escort3_door_check:
    if act=="l":
        call ep211_escort_scene1_13a()
        return False
    call ep211_escort_scene1_13()
    return False

label ep211_quests_escort4_restaurant: # Вход в ресторан
    music stop
    img black_screen
    with diss
    pause 1.5
    $ rnd1 = rand(1,4)
    if rnd1 == 1:
        call ep210_dialogues7_escort_hotel_8a2()
    if rnd1 == 2:
        call ep210_dialogues7_escort_hotel_8b()
    if rnd1 == 3:
        call ep210_dialogues7_escort_hotel_8c()
    if rnd1 == 4:
        call ep210_dialogues7_escort_hotel_8d()
    call change_scene("rich_hotel_restaurant", "Fade_long")
    return False

label ep211_quests_escort5_restaurant_wait_customer:
    call ep211_escort_scene1_1a()
    return
