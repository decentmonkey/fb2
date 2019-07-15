default worker1Option1Cnt = 0
default worker1Option2Cnt = 0

# серая мышка
label worker1_look:
    img 20298
    with fade
    w
    img 20299
    with diss
    mt "Какая-то серая мышь."
    mt "В каждом офисе есть такая."
    return


label worker1_dialogue_workplace:
    music Groove2_85
    img 20300
    with fade
    m "Послушай..."
    w1 "Ой... Я..."
    img 20301
    m "Ты что, язык проглотила?"
    w1 "Нет... Я..."
    img 20300
    with diss
    m "А похоже, что проглотила."
    m "Когда закончишь работать с бумагами, не забудь принести их мне в офис."
    w1 "Да, мэм!"
    return

label worker1_dialogue_office:
    music Sneaky_Snitch
    img 20330
    with fadelong
    w1 "Миссис Бакфетт... Можно?"
    w1 "Я принесла отчет."
    menu:
        "Да, проходи.":
            $ worker1Option1Cnt += 1
            call bitch(-1, "worker1_dialogue_office")
            m "Да, проходи."
            img 20332
            with diss
            m "Напомни, как тебя зовут?"
            w1 "Я...Я Марта."
            music Groove2_85
            img 20333
            with fade
            m "Марта... Ты же понимаешь, что твоя работа очень важна и я на тебя надеюсь?"
            w1 "Да... Мэм..."
            m "Отлично. А теперь положи бумаги на стол и можешь идти."
            img 20334
            with diss
            w1 "Да, хорошо..."
            sound snd_folder_drop
            img 20335
            with diss
            mt "Серая мышь..."
            return
        "Я занята!":
            $ worker1Option2Cnt = 0
            call bitch(1, "worker1_dialogue_office")
            music Pyro_Flow
            img 20331
            with fade
            m "Ты что, не видишь, я занята!"
            w1 "Простите..."
            m "Положи отчет на стол и выметайся!"
            img 20334
            with diss
            w1 "Хорошо..."
            sound snd_folder_drop
            img 20335
            with fade
            mt "Кучка никчемных идиотов..."
            return
