# серая мышка
label worker1_dialogue_workplace:
    m "Послушай..."
    w1 "Ой... Я..."
    m "Ты что, язык проглотила?"
    w1 "Нет... Я..."
    m "А похоже, что проглотила."
    m "Когда закончишь работать с бумагами, не забудь принести их мне в офис."
    w1 "Да, мем!"
    return

label worker1_dialogue_office:
    w1 "Миссис Бакфет... Можно?"
    w1 "Я принесла отчет."
    menu:
        "Да, проходи.":
            m "Да, проходи."
            m "Напомни, как тебя зовут?"
            w1 "Я...Я Марта."
            m "Марта... Ты же понимаешь, что твоя работа очень важна и я на тебя надеюсь?"
            w1 "Ну...Да..."
            m "Отлично. А теперь положи бумаги на стол и можешь идти."
            w1 "Да, хорошо..."
            mt "Надеюсь теперь она станет работать еще лучше."
            return
        "Я занята!"
            m "Ты что, не видишь, я занята!"
            w1 "Простите..."
            m "Положи отчет на стол и выметайся!"
            w1 "Хорошо..."
            mt "Кучка никчемных идиотов..."
            return
