label cit10_dialog_1:
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    cit10 "Да, Мэм."
    cit10 "Что Вы хотели?"
    m "Я бы хотела предложить Вам купить это платье."
    cit10 "Какое платье?"
    m "Вот это, которое на мне..."
    cit10 "Это что, подержанное платье?"
    m "Нет, Мэм. Это новое платье..."
    cit10 "А почему оно надето на тебе?"
    # corruption +1 req 80
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            return False

    m "Я... Я работаю здесь манекеном."
    cit10 "Я уже тороплюсь, может быть в следующий раз..."
    return True

label cit10_dialog_2:
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    cit10 "Прогуляйся."
    m "В смысле?"
    cit10 "Пройдись, я хочу посмотреть на это платье."
    m "Хорошо..."
    # Моника прогуливается
    cit10 "Хорошо, я еще подумаю."
    return True

label cit10_dialog_3:
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    cit10 "По поводу платья?"
    m "Да."
    cit10 "Хорошо, пойдем примерим его."
    #примерочная
    cit10 "Снимай его, я примерю."
    m "..."
    cit10 "Ну?"
    #Моника раздевается, покупатель одевает платье
    cit10 "А туфли?"
    m "Мэм, туфли продаются отдельно."
    cit10 "Одень мне туфли, я хочу примерить платье в них."
    m "Да, Мэм, конечно."
    # Ставит туфли
    cit10 "Я сказала одеть туфли мне на ноги."
    m "Мэм, Вы не можете сделать этого сами?"
    cit10 "Это сделаешь ты..."
    m "Дьявол! Ненавижу!!!"
    # corruption +2 req 100
    menu:
        "Одеть туфли покупательнице.":
            pass
        "Уйти.":
            return False
    # Моника одевает туфли
    cit10 "Нет, это не мой стиль!"
    #исчезает
    return True

















#
