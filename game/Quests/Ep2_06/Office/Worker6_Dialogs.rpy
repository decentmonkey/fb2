default worker6Option1Cnt = 0
default worker6Option2Cnt = 0

# толстуха
label worker6_look:
    img 20313
    with fade
    mt "Как можно быть такой толстой коровой?"
    mt "Фи!"
    return

label worker6_dialogue_workplace:
#    m "Послушай..."
    music Groove2_85
    img 20314
    with fade
    w6 "Как же достали эти амбициозные новички и карьеристы!"
    w6 "Ничего не делают, только сидят в своем интернете."
    img 20315
    with diss
    w6 "А как надо сделать какой-то сложный отчет дак Грета, сделай пожалуйста..."
    mt "Боже! Какое занудство!"
#    mt "Пожалуй, пойду к себе в кабинет..."
    return

label worker6_dialogue_office:
    music Sneaky_Snitch
    img 20364
    with fadelong
    w6 "Миссис Бакфетт, можно?"
    menu:
        "Да, заходи.":
            $ worker6Option1Cnt +=1
            m "Да, заходи."
            img 20365
            w6 "Миссис Бакфетт, Я бы хотела поговорить о ситуации в нашем отделе."
            img 20366
            with diss
            w6 "Вы же наверняка знаете на ком все держится..."
            img 20367
            with diss
            w6 "А этот карьерист Джон... Как он меня достал!"
            w6 "Думаю, с Вашими менеджерскими талантами Вы понимаете, кто достоин стать главой отдела."
            music Groove2_85
            img 20368
            with fade
            m "Уж будь в этом уверена."
            call bitch(-1, "worker6_dialogue_office") from _call_bitch_195
            m "Придет время и ты все узнаешь."
            img 20369
            with diss
            mt "Глава отдела? Как же вы мне надоели..."
            img 20370
            with fade
            m "Я тебя услышала. Ты свободна."
#            w6 "Да, спасибо миссис Бакфет. Вот кстати отчет, который я сегодня сделала."
#            m "Спасибо, можешь положить на стол."
            return
        "Я занята.":
            call bitch(2, "worker6_dialogue_office") from _call_bitch_196
            $ worker6Option2Cnt += 1
            m "Я занята, приходи завтра."
            music Pyro_Flow
            img 20370
            with fade
            w6 "Но как же..."
            m "Я сказала завтра, я сейчас занята!"
            return
