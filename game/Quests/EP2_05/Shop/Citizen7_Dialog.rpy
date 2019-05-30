# Girl4
label cit7_dialog_1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10935
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 10936
    with diss
    cit7 "Что тебе надо, девочка?"
    cit7 "Ты не похожа на продащицу."
    # corruption +1 req 80

    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit7_dialog_1")

    img 10937
    with fade
    m "Я... Я работаю здесь манекеном."
    img 10938
    with diss
    cit7 "Манекеном?! Фи!"
    #Исчезает
    return False
label cit7_dialog_2:
    img 10939
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    img 10940
    cit7 "Это кто? Снова девочка-манекен?"
    # corruption +1 req 80
    menu:
        "Да, Мэм.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    img 10941
    m "Да, Мэм."
    m "Пожалуйста, рассмотрите приобретение этого замечательного платья."
    img 10942
    cit7 "Этого?"
    cit7 "Хм... Оно вполне ничего..."
    img 10943
    if monicaBitch == True:
        mt "Еще бы вполне ничего, сучка! Это самое дорогое платье в этой дыре!"
    else:
        mt "Еще бы вполне ничего! Это самое дорогое платье в этой дыре!"
    img 10944
    cit7 "Сегодня я уже потратила деньги."
    cit7 "Манекен, продемонстрируй мне это платье в следующий раз."
    m "Да, Мэм..."
    #исчезает
    return True
label cit7_dialog_3:
    img 10945
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    img 10946
    cit7 "Это кто? Снова девочка-манекен?"
    m "Да, Мэм.":
    img 10947
    cit7 "Я помню это платье."
    cit7 "Пойдем я его померю."
    #уходят в примерочную
    img 10948
    m "..."

    img 10949
    cit7 "Ну? Что стоишь?"
    img 10950
    cit7 "Снимай его!"
    # corruption +2 req 90

    menu:
        "Снять платье...":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    # Моника снимает платье, покупатель одевает
    # Моника стоит обнаженная, закрывается
    img 10951
    cit7 "Ну как?"
    img 10952
    cit7 "Как я тебе в этом платье?"
    m "Мэм. Вы выглядите в нем великолепно."
    img 10953
    cit7 "Хорошо, я куплю это платье со скидкой 50 процентов!"
    m "Мэм, простите. На это платье не действует скидка..."
    img 10954
    cit7 "Тогда УВЫ!"
    #исчезает
    return True
