# толстуха
label worker6_look:
    mt "Как можно быть такой толстой коровой?"
    mt "Фи!"
    return

label worker6_dialogue_workplace:
#    m "Послушай..."
    w6 "Как же достали эти амбициозные новички и карьеристы!"
    w6 "Ничего не делают, только сидят в своем интернете."
    w6 "А как надо сделать какой-то сложный отчет дак Грета, сделай пожалуйста..."
#    mt "Пожалуй, пойду к себе в кабинет..."
    return

label worker6_dialogue_office:
    w6 "Миссис Бакфет, можно?"
    menu:
        "Да, заходи.":
            m "Да, заходи."
            w6 "Миссис Бакфетт, Я бы хотела поговорить о ситуации в нашем отделе."
            w6 "Вы же наверняка знаете на ком все держится..."
            w6 "А этот карьерист Джон... Как он меня достал!"
            w6 "Думаю, с Вашими менеджерскими талантами Вы понимаете, кто достоин стать главой отдела."
            m "Уж будь в этом уверена."
            m "Придет время и ты все узнаешь."
            mt "Глава отдела? Как же вы мне надоели..."
            m "Я тебя услышала. Ты свободна."
            w6 "Да, спасибо миссис Бакфет. Вот кстати отчет, который я сегодня сделала."
            m "Спасибо, можешь положить на стол."
            return
        "Я занята.":
            m "Я занята, приходи завтра."
            w6 "Но как же..."
            m "Я сказала завтра, я сейчас занята!"
            return
