default ep224_quests_julia_init_flag = False
default ep224_quests_julia_completed1_day = 0
default ep224_quests_julia_completed2_day = 0

label ep224_quests_julia_init:
    if ep224_quests_julia_init_flag == True:
        return
    $ ep224_quests_julia_init_flag = True
    $ questHelp("julia_57")
    $ add_hook("before_open", "ep224_quests_julia1_start", scene="juliahome_livingroom", label="ep224_quests_julia1_start", priority=1)
    return

label ep224_quests_julia1_start:
    if day_time != "evening" or ep218_quests_julia_completed_last_day == day or get_active_objects("Julia", scene="juliahome_livingroom") == False:
        # если не вечер, было сегодня свидание, либо нет Юлии в комнате
        return
    $ remove_hook()
    call ep22_4_dialogues3_julia_1()
    if _return == False:
        $ cloth = monica_juliahome_outside_cloth
        $ cloth_type = monica_juliahome_outside_cloth_type
        $ juliaQuestRefused = True
        call ep218_quests_abort_julia()
        call bitch(20, "abort_julia")
        call process_change_map_location("House")
        call change_scene("street_house_outside", "Fade_long")
        $ autorun_to_object("ep22_4_dialogues3_julia_2", scene="street_house_outside")

        return False
    $ questHelp("julia_57", True)
    if _return == -1:
        $ autorun_to_object("ep22_4_dialogues3_julia_2", scene="juliahome_livingroom")
    else:
        $ ep224_quests_julia_completed2_day = day
        call change_scene("juliahome_kitchen", "Fade_long")
    $ ep224_quests_julia_completed1_day = day
    call juliahome_livingroom_init2() # добавляем пятно
    $ add_hook("Stain", "ep224_quests_julia2_stain", scene="juliahome_livingroom", label="ep224_quests_julia2_stain")
    return


label ep224_quests_julia2_stain:
    if act=="l":
        call ep22_4_dialogues3_julia_2a()
        return False
    if (juliaHomeLivingRoomJuliaSuffix == 1 or juliaHomeLivingRoomJuliaSuffix == 2) or ep224_quests_julia_completed1_day == day or get_active_objects("Julia", scene="juliahome_livingroom") == False:
        # сегодня уже терли пятно, либо Юлии нет
        call ep22_4_dialogues3_julia_2b()
        return False
    # повтор сцены с пятном
    call ep22_4_dialogues3_julia_1a()
    if _return == -1:
        $ autorun_to_object("ep22_4_dialogues3_julia_2", scene="juliahome_kitchen")
    else:
        $ ep224_quests_julia_completed2_day = day
    call change_scene("juliahome_kitchen", "Fade_long")
    $ ep224_quests_julia_completed1_day = day
    return False






#
