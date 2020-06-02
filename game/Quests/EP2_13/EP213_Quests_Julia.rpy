default ep213_quests_julia_stage = 0
default monica_living_at_juliahome = False
default monica_juliahome_outside_cloth = False
default monica_juliahome_outside_cloth_type = False

default monica_juliahome_cloth = "JuliaCloth1"

label ep213_quests_julia1: # Моника предлагает Юлии жить вместе
    call ep213_dialogues5_julia_16()
    $ ep213_quests_julia_stage = 1
    $ ep210_julia_evening_at_work = False # Вечером Юлия не на работе (а дома)
    $ add_hook("JuliaHome", "ep213_quests_julia2", scene="street_juliahome", label="juliahome1")
    $ add_objective("come_julia_evening", t_("Прийти к Юлии домой вечером."), c_pink, 105)

    return

label ep213_quests_julia2: # Заходит вечером в дом
    if act=="l" or day_time != "evening":
        return
    $ remove_hook()
    call ep213_dialogues5_julia_7()
    # Инициализируем жизнь в доме
    python:
        remove_objective("come_julia_evening")
        ep213_quests_julia_stage = 2
        monica_living_at_juliahome = True
        ep210_julia_evening_at_work = True # Вечером Юлия на работе
        move_object("Julia", "juliahome_livingroom")
        set_var("Julia", base="JuliaHome_LivingRoom_Julia_[juliaHomeLivingRoomJuliaCloth]_[juliaHomeLivingRoomJuliaSuffix][day_suffix]", scene="juliahome_livingroom")
        set_var("Wardrobe", actions="lh", scene="juliahome_livingroom")
        set_var("Bed1", actions="lh", scene="juliahome_livingroom")
        set_var("Julia", base="JuliaHome_Bathroom_Julia_[juliaHomeLivingRoomJuliaCloth][juliaHomeBathroomJuliaSuffix]", scene="juliahome_bathroom")
        set_var("Julia", base="JuliaHome_Kitchen_Julia_[juliaHomeLivingRoomJuliaCloth][juliaHomeKitchenJuliaSuffix]", scene="juliahome_kitchen")
        set_var("Julia", base="JuliaHome_Kitchen_Julia_[juliaHomeLivingRoomJuliaCloth][juliaHomeKitchenJuliaSuffix]", scene="juliahome_bathroomshower")
        juliaHomeLivingRoomMonicaSuffix = 3
        juliaHomeLivingRoomJuliaSuffix = 3
        monica_juliahome_outside_cloth = cloth
        monica_juliahome_outside_cloth_type = cloth_type
        cloth = monica_juliahome_cloth
        cloth_type = "juliahome"
        juliaHomeLivingRoomJuliaCloth = "JuliaCloth1"
        minimapJuliaGenerateEnabled = True
    call juliahome_kitchen_init2()
    call juliahome_bathroomshower_init2()
    $ add_hook("Shower", "ep213_quests_julia3_shower", scene="juliahome_bathroomshower", label="juliahome_shower")
    $ add_hook("Kitchen", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen")
    $ add_hook("Kitchen_Item1", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen")
    $ add_hook("Kitchen_Item2", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen")
    $ add_hook("Kitchen_Item3", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen")
    $ add_hook("Kitchen_Item4", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen")
    $ add_hook("Kitchen_Item5", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen")
    $ add_hook("Teleport_Street", "ep213_quests_julia5_exit_street", scene="juliahome_kitchen", label="juliahome_exit")
    $ add_hook("Wardrobe", "ep213_quests_julia6_wardrobe", scene="juliahome_livingroom", label="juliahome_wardrobe")
    $ add_hook("Toilet", "ep213_quests_julia7_toilet", scene="juliahome_bathroom", label="juliahome_toilet")
    $ add_hook("JuliaHome", "ep213_quests_julia9_enter_building", scene="street_juliahome", label="juliahome_enter")
    $ add_hook("Julia", "ep213_quests_julia11_julia", scene="juliahome_livingroom", label="juliahome_julia_regular1")
    $ add_hook("Julia", "ep213_quests_julia11_julia", scene="juliahome_kitchen", label="juliahome_julia_regular1")
    $ add_hook("Julia", "ep213_quests_julia11_julia", scene="juliahome_shower", label="juliahome_julia_regular1")
    $ add_hook("Bed1", "juliahome_bed", scene="juliahome_livingroom", label="juliahome_bed")
    $ add_location("World", caption=("World"), label="world", init_label="world_init", parent="none")

    $ add_hook("exit_scene", "ep213_quests_julia12_exit_livingroom", scene="juliahome_livingroom", label="juliahome_livingroom_exit")
    $ add_hook("before_open", "ep213_quests_julia13_enter_livingroom", scene="juliahome_livingroom", label="juliahome_livingroom_enter")
    $ add_hook("map_teleport", "ep213_quests_julia14_map_teleport", scene="global", label="juliahome_map_teleport", priority=10000)
    $ add_hook("map_teleport_after", "ep213_quests_julia16_exit_house", scene="global", label="juliahome_map_teleport", priority=10000)

    call change_scene("juliahome_livingroom", "Fade_long", False)
    return False


label ep213_quests_julia3_shower: # клик на душ
    if act=="l":
        return
    if monicaLastShowerDay == day and monicaLastShowerDayTime == day_time:
        mt "Я уже принимала душ недавно..."
        return False
    call ep213_dialogues5_julia_15c2()
    $ monicaLastShowerDay = day # Последний день, когда Моника принимала душ
    $ monicaLastShowerDayTime = day_time
    $ juliaHomeBathroomMonicaSuffix = 3
    call change_scene("juliahome_bathroom")

    return False

label ep213_quests_julia4_kitchen: # клик на кухню (еда)
    if act=="l":
        return
    if monicaEatedLastDay != day:
        fadeblack
        imgf 30842
        sound snd_eating
        w
#        pause 1.5
        $ monica_eated()
        call refresh_scene_fade()
    else:
        call ep213_dialogues5_julia_15b()
    return False

label ep213_quests_julia5_exit_street: # Моника выходит на улицу
    $ cloth = monica_juliahome_outside_cloth
    $ cloth_type = monica_juliahome_outside_cloth_type
#    $ juliaHomeLivingRoomJuliaSuffix = 3
    if scene_name == "juliahome_kitchen":
        $ autorun_to_object("ep213_dialogues5_julia_15e", scene="street_juliahome")

    call ep213_quests_julia17_life()
    call change_scene("street_juliahome", "Fade_long", "snd_door_close1")
    return False

label ep213_quests_julia6_wardrobe: # гардероб
    if act=="l":
        call ep213_dialogues5_julia_17()
        return False
    call ep213_dialogues5_julia_18_wardrobe()
    if _return == 0:
        call refresh_scene_fade()
        return False
    $ monica_juliahome_outside_cloth = cloth
    $ monica_juliahome_outside_cloth_type = cloth_type
    call ep213_quests_julia5_exit_street()
    return False

label ep213_quests_julia7_toilet: # Моника писает
    if act=="l":
        return
    if monicaLastPissedDay == day and day_time == monicaLastPissedDayTime:
        mt "Я уже писала недавно. Я пока не хочу."
        return False
    call ep213_dialogues5_julia_15d()
    $ monicaLastPissedDay = day # Последний день, когда Моника писала
    $ monicaLastPissedDayTime = day_time
    call refresh_scene_fade()
    return False

label ep213_quests_julia8_minimap_teleport: # Телепорт по миникарте
    if minimapTeleportButtonName == "JuliaHome_Street":
        if scene_name != "street_juliahome":
            call ep213_quests_julia5_exit_street()
        return
    if scene_name == "street_juliahome":
        call ep213_quests_julia10_check_enter_home()
        fadeblack
        $ monica_juliahome_outside_cloth = cloth
        $ monica_juliahome_outside_cloth_type = cloth_type
        $ cloth = monica_juliahome_cloth
        $ cloth_type = "juliahome"
        sound snd_fabric1
        pause 1.0

    if minimapTeleportButtonName == "JuliaHome_LivingRoom":
        call change_scene("juliahome_livingroom", "Fade", "snd_walk_barefoot")
    if minimapTeleportButtonName == "JuliaHome_Kitchen":
        call change_scene("juliahome_kitchen", "Fade", "snd_walk_barefoot")
    if minimapTeleportButtonName == "JuliaHome_Bathroom":
        call change_scene("JuliaHome_Bathroom", "Fade", "snd_walk_barefoot")

    return

label ep213_quests_julia9_enter_building: # входит с улицы через вход
    if act=="l":
        return
    call ep213_quests_julia10_check_enter_home()
    fadeblack
    $ monica_juliahome_outside_cloth = cloth
    $ monica_juliahome_outside_cloth_type = cloth_type
    $ cloth = monica_juliahome_cloth
    $ cloth_type = "juliahome"
    sound snd_fabric1
    pause 1.0
    call change_scene("juliahome_livingroom", "Fade", "snd_walk_barefoot")
    return False

label ep213_quests_julia10_check_enter_home: # события при входе в дом
    $ juliaHomeLivingRoomMonicaSuffix = 3
    $ juliaHomeLivingRoomJuliaSuffix = 3
    return

label ep213_quests_julia11_julia: # регулярный разговор с Юлией (везде)
    if act=="l":
        return
    call ep213_dialogues5_julia_16a()
    return False

label ep213_quests_julia12_exit_livingroom:
    if juliaHomeLivingRoomMonicaSuffix == 1:
        if day_time == "day":
            $ juliaHomeLivingRoomMonicaSuffix = 2
            $ juliaHomeLivingRoomJuliaSuffix = 2
    return

label ep213_quests_julia13_enter_livingroom:
    if cloth_type != "juliahome":
        $ monica_juliahome_outside_cloth = cloth
        $ monica_juliahome_outside_cloth_type = cloth_type
        $ cloth = monica_juliahome_cloth
        $ cloth_type = "juliahome"

    if juliaHomeLivingRoomJuliaSuffix == 1 or juliaHomeLivingRoomJuliaSuffix == 2:
        $ juliaHomeLivingRoomJuliaSuffix = 2
        $ juliaHomeLivingRoomMonicaSuffix = 2
    if juliaHomeLivingRoomJuliaSuffix != 1 and juliaHomeLivingRoomJuliaSuffix != 2:
        $ set_active("Bed1", True, scene="juliahome_livingroom")

    return

label ep213_quests_julia14_map_teleport: # вызов перед уходом по карте
    # переодеваем Монику назад
    if lastSceneName == "juliahome_livingroom":
        $ cloth = monica_juliahome_outside_cloth
        $ cloth_type = monica_juliahome_outside_cloth_type
    return


label ep213_quests_julia16_exit_house: # Жизнь Юлии при выходе из дома
    if previous_map_scene == "JuliaHome":
        if check_scene_parent(scene_name, "street_juliahome") == True:
            return
        call ep213_quests_julia17_life()
    return

label ep213_quests_julia17_life:
    if week_day != 7 and day_time != "evening":
        $ move_object("Julia", "working_office_cabinet") # Юлия уходит на работу
    return
