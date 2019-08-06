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
            call bitch(-1, "worker1_dialogue_office") from _call_bitch_191
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
            call bitch(1, "worker1_dialogue_office") from _call_bitch_192
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

label takeReportsFlashCard_Worker1:
    m "Привет. Мне нужны отчеты, которые ты сделала."
    w1 "Но... Миссис Бакфетт, простите, я еще не доделала. И мне нужно будет их проверить..."
    menu:
        "Ничего страшного.":
            m "Ничего страшного. Конечно, не следует такого допускать."
            m "Ты же постараешься следать так, чтобы такой ситуации не повторилось?"
            w1 "Я...Да, конечно..."
            pass
        "И почему же они еще не готовы?":
            m "И почему же они еще не готовы?"
            w1 "..."
            m "А?"
            w1 "Миссис Бакфетт, я... У меня..."
            m "Ты же знаешь, какую важную работу все мы здесь делаем!"
            w1 "Обещаю Вам, я их доделаю! Сегодня же!"
            pass
    m "Отлично, а пока скопируй мне все, что у тебя есть на данный момент."
    w1 "Хорошо..."
    w1 "Я все скопировала."
    m "Хорошо."
    m "И не забывай, твой вклад в работу компании очень высок."
    w1 "Да, миссис Бакфетт."
    return
