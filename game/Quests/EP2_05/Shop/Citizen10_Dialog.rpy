label cit10_dialog_1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11028
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 11029
    with diss
    cit10 "Да, Мэм."
    cit10 "Что Вы хотели?"
    m "Я бы хотела предложить Вам купить это платье."
    cit10 "Какое платье?"
    img 11030
    with fade
    m "Вот это, которое на мне..."
    img 11031
    with fade
    cit10 "Это что, подержанное платье?"
    m "Нет, Мэм. Это новое платье..."
    cit10 "А почему оно надето на тебе?"
    # corruption +1 req 80
    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False

    $ add_corruption(1, "cit10_dialog_1")
    img 11032
    with fade
    m "Я... Я работаю здесь манекеном."
    img 11033
    with diss
    cit10 "Я уже тороплюсь, может быть в следующий раз..."
    return True

label cit10_dialog_2:
    img 11034
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    img 11035
    cit10 "Прогуляйся."
    m "В смысле?"
    img 11036
    cit10 "Пройдись, я хочу посмотреть на это платье."
    img 11037
    m "Хорошо..."
    # Моника прогуливается
    img 11038
    w
    img 11039
    w
    img 11040
    w
    img 11041
    w
    img 11042
    cit10 "Хорошо, я еще подумаю."
    img 11043
    mt "!!!"
    return True

label cit10_dialog_3:
    img 11044
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    img 11045
    cit10 "По поводу платья?"
    m "Да."
    img 11046
    cit10 "Хорошо, пойдем примерим его."
    #примерочная
    img 11047
    cit10 "Снимай его, я примерю."
    img 11048
    m "..."
    img 11049
    cit10 "Ну?"
    menu:
        "Раздеться и отдать платье.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    #Моника раздевается, покупатель одевает платье
#    cit10 "А туфли?"
#    m "Мэм, туфли продаются отдельно."
    sound snd_fabric1
    img 11050
    with fadelong
    w
    img 11051
    cit10 "Одень мне туфли, я хочу примерить платье в них."
    img 11052
    m "Да, Мэм, конечно."
    img 11053
    # Ставит туфли
    w
    img 11054
    cit10 "Я сказала одеть туфли мне на ноги."
    img 11055
    m "Мэм, Вы не можете сделать этого сами?"
    cit10 "Это сделаешь ты..."
    img 11056
    m "Дьявол! Ненавижу!!!"
    # corruption +2 req 100
    menu:
        "Одеть туфли покупательнице.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    # Моника одевает туфли
    img 11057
    w
    img 11058
    w
    img 11059
    with fade
    w
    img 11060
    cit10 "Вторую..."
    img 11061
    w
    img 11062
    w
    img 11063
    w
    img 11064
    w
    img 11065
    w
    img 11066
    w
    img 11067
    cit10 "Нет, это не мой стиль!"
    #исчезает
    return True

















#
