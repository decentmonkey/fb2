# Girl4
label cit7_dialog_1:
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    cit7 "Что тебе надо, девочка?"
    cit7 "Ты не похожа на продащицу."
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            return False

    m "Я... Я работаю здесь манекеном."
    cit7 "Манекеном?! Фи!"
    #Исчезает
    return False
label cit7_dialog_2:
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    cit7 "Это кто? Снова девочка-манекен?"
    menu:
        "Да, Мэм.":
            pass
        "Уйти.":
            return False
    m "Да, Мэм."
    m "Пожалуйста, рассмотрите приобретение этого замечательного платья."
    cit7 "Этого?"
    cit7 "Хм... Оно вполне ничего..."
    mt "Еще бы вполне ничего, сучка! Это самое дорогое платье в этой дыре!"
    cit7 "Сегодня я уже потратила деньги."
    cit7 "Манекен, продемонстрируй мне это платье в следующий раз."
    m "Да, Мэм..."
    #исчезает
    return True
label cit7_dialog_3:
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    cit7 "Это кто? Снова девочка-манекен?"
    m "Да, Мэм.":
    cit7 "Я помню это платье."
    cit7 "Пойдем я его померю."
    #уходят в примерочную
    m "..."
    cit7 "Ну? Что стоишь? Снимай его!"
    menu:
        "Снять платье...":
            pass
        "Уйти.":
            return False
    # Моника снимает платье, покупатель одевает
    # Моника стоит обнаженная, закрывается
    cit7 "Ну как?"
    cit7 "Как я тебе в этом платье?"
    m "Мэм. Вы выглядите в нем великолепно."
    cit7 "Хорошо, я куплю это платье со скидкой 50 процентов!"
    m "Мэм, простите. На это платье не действует скидка..."
    cit7 "Тогда УВЫ!"
    #исчезает
    return True
