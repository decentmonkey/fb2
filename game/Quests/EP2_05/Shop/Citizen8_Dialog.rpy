#Girl5
label cit8_dialog_1:
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    cit8 "Я занята, в другой раз!"
    return True

label cit8_dialog_2:
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    cit8 "Что тебе надо от меня?"
    # corruption +1 req 80
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            return False

    m "Я... Я работаю здесь манекеном."
    m "И я хотела бы предложить Вам это платье..."
    cit8 "О! Какой очаровательный манекен!"
    cit8 "Могу я приобрести это платье вместе с манекеном?"
    m "Нет... Мэм..."
    m "Манекен... Собственность магазина и он не продается..."
    cit8 "Очень жаль!"
    m "А платье? Купите платье, Мэм!"
    # исчезает
    return True

label cit8_dialog_3:
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    cit8 "О! Кто это у нас?"
    cit8 "Это тот очаровательный манекенчик, который не продается?"
    m "Мэм, я по поводу платья."
    cit8 "Я бы хотел снять это платье с манекена."
    # corruption +2 req 90
    menu:
        "Это возможно только в случае примерки платья...":
            pass
        "Это невозможно, Мэм.":
            m "Это невозможно, Мэм."
            return False
    m "Мэм, простите."
    m "Это возможно только в случае примерки платья..."
    cit8 "Хорошо, пойдем. Я хочу примерить его!"
    # примерочная
    cit8 "Снимай его скорее!"
    # жадно смотрит на Монику
    # посетительница надела платье
    cit8 "Помоги мне, манекенчик!"
    m "Да, Мэм. Вам что-то мешает?"
    cit8 "Да, мне мешает, вот здесь снизу." #Показывает в ноги
    m "Где, Мэм?"
    cit8 "Еще ниже, вон там."
    m "Где, Мэм?"
    cit8 "Встань на коленки, тебе отсюда не видно."
    # corruption +3 req 100
    menu:
        "Встать на колени.":
            pass
        "Уйти.":
            return False
    #Моника встает на колени
    m "Где, Мэм?"
    cit8 "Чуть повыше!"
    m "Где?"
    # Посетительница притягивает голову Моники между ног :)
    cit8 "Вот здесь! Здесь, манекенчик!"
    cit8 "Лижи! Лижи вот здесь!"
    m "ФУ! КАКАЯ МЕРЗОСТЬ!!!"

    mt "Это сучка и не собиралась покупать платье!"
    return True
