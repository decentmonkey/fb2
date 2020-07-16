default ep214_quests_citizens_stage2 = False

label ep214_quests_citizens_regular:
    call ep214_dialogues2_citizens_23()

label ep214_quests_citizens_regular_loop1:
    call pylonController(1, 1, 1)
    with fade
    menu:
        "Придумать что-нибудь, чтобы заработать деньги." if citizenId == 1 or citizenId == 7:
            if citizenId == 1:
                menu:
                    "Пригласить к себе.":
                        call ep214_quests_citizen1_2a()
                    "Назад.":
                        jump ep214_quests_citizens_regular_loop1
            if citizenId == 7:
                menu:
                    "Искусство живописи.":
                        pass
                    "Назад.":
                        jump ep214_quests_citizens_regular_loop1

        "Придумать что-нибудь, чтобы заработать деньги. (в будущих обновлениях) (disabled)" if citizenId != 1 and citizenId != 7:
            pass
        "Уйти.":
            call pylonController(1, 1, 2)
            with fade
            m "Я... Передумала..."
            if citizenId == 1:
                call pylonController(5, 1, 1)
                citizen1 "Не ожидал я такого тетя. Думаю, ты скоро передумаешь."
            if citizenId == 3:
                call pylonController(5, 1, 1)
                citizen3 "Похоже, я только зря потратил с тобой время..."
            if citizenId == 4:
                call pylonController(5, 1, 1)
                citizen4 "Какое то не продуктивное вышло знакомство. Надеюсь, в другой раз будет лучше."
            if citizenId == 5:
                call pylonController(5, 1, 1)
                citizen5 "Мистер разочарован, он ничего не посмотрел."
            if citizenId == 6:
                call pylonController(5, 1, 1)
                citizen6 "Похоже, я зря потратил свое время, пойду найду другую шлюху."
            if citizenId == 7:
                call pylonController(5, 1, 1)
                citizen7 "Ты не дала мне ни капли вдохновения!"
            if citizenId == 8:
                call pylonController(5, 1, 1)
                citizen8 "Сделки нет, ты не выполнила свою часть."
            if citizenId == 9:
                call pylonController(5, 1, 1)
                citizen9 "Дамочка, ни цента! Ничего не получишь!"
            if citizenId == 13:
                call pylonController(5, 1, 1)
                citizen13 "Подруга, в следующий раз не халтурь."
            if citizenId == 15:
                call pylonController(5, 1, 1)
                citizen15 "Сходи поищи себе кого-нибудь еще."
            call falling_path_store_customer()
            $ autorun_to_object("ep214_dialogues2_citizens_24", scene="hostel_edge_1_a")
            call refresh_scene_fade()
            return False
    call falling_path_store_customer()
    call refresh_scene_fade()
    return False


label ep214_quests_citizen1_2a: # пригласить к себе (панки)
    call ep214_dialogues2_citizens_16()
    if _return == False:
        $ autorun_to_object("ep214_dialogues2_citizens_17b", scene="hostel_edge_1_a")
        return
    call change_scene("street_monicahome", "Fade_long")
    call ep214_dialogues2_citizens_17() # апартаменты Моники в трущобах
    if _return == False:
        call bitch(5, "ep214_quests_citizen1_2a")
        $ autorun_to_object("ep214_dialogues2_citizens_17b", scene="hostel_edge_1_a")
        return
    return
