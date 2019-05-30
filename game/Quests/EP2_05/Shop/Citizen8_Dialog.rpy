#Girl5
label cit8_dialog_1:
    $ store_music()
    music Hidden_Agenda
    img 10955
    with fade
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 10956
    with diss
    cit8 "Я занята, в другой раз!"
    $ restore_music()
    return True

label cit8_dialog_2:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10957
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 10958
    with fade
    cit8 "Что тебе надо от меня?"
    # corruption +1 req 80

    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit8_dialog_2")

    img 10959
    with fade
    m "Я... Я работаю здесь манекеном."
    m "И я хотела бы предложить Вам это платье..."
    music Loved_Up
    img 10960
    with fade
    cit8 "О! Какой очаровательный манекен!"
    cit8 "Могу я приобрести это платье вместе с манекеном?"
    img 10961
    with diss
    m "Нет... Мэм..."
    m "Манекен... Собственность магазина и он не продается..."
    music Groove2_85
    img 10962
    with fade
    cit8 "Очень жаль!"
    m "А платье? Купите платье, Мэм!"
    # исчезает
    return True

label cit8_dialog_3:
    img 10963
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    img 10964
    cit8 "О! Кто это у нас?"
    cit8 "Это тот очаровательный манекенчик, который не продается?"
    m "Мэм, я по поводу платья."
    img 10965
    cit8 "Я бы хотел снять это платье с манекена."
    # corruption +2 req 90
    menu:
        "Это возможно только в случае примерки платья...":
            pass
        "Это невозможно, Мэм.":
            img 10966
            m "Это невозможно, Мэм."
            $ monicaSellingDressRefuseLastDay = day
            return False
    img 10967
    m "Мэм, простите."
    m "Это возможно только в случае примерки платья..."
    cit8 "Хорошо, пойдем. Я хочу примерить его!"

    # примерочная
    img 10968
    w
    img 10969
    with diss
    w
    img 10970
    w
    img 10971
    cit8 "Снимай его скорее!"

    sound snd_fabric1
    img 10972
    with fadelong
    w
    # жадно смотрит на Монику
    # посетительница надела платье
    img 10973
    cit8 "Помоги мне, манекенчик!"
    img 10974
    m "Да, Мэм. Вам что-то мешает?"
    cit8 "Да, мне мешает, вот здесь снизу." #Показывает в ноги
    img 10975
    m "Где, Мэм?"
    cit8 "Еще ниже, вон там."
    img 10976
    with diss
    w
    img 10977
    m "Где, Мэм?"
    cit8 "Встань на коленки, тебе отсюда не видно."
    # corruption +3 req 100
    menu:
        "Встать на колени.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    #Моника встает на колени
    img 10978
    with fade
    w
    img 10979
    w
    img 10980
    w
    img 10981
    m "Где, Мэм?"
    sound snd_fabric1
    img 10982
    with diss
    w
    img 10983
    w
    img 10984
    cit8 "Чуть повыше!"
    img 10985
    m "Где?"
    # Посетительница притягивает голову Моники между ног :)
    # Звук чавкания
    img 10986
    with diss
    w
    img 10987
    cit8 "Вот здесь! Здесь, манекенчик!"
    img 10988
    m "ММмммммм!!!"
    img 10989
    cit8 "Лижи! Лижи вот здесь!"
    img 10990
    w
    img 10991
    m "МММммпфффф!!!"
    img 10992
    cit8 "Не вырывайся, манекенчик. Я держу тебя крепко."
    img 10993
    cit8 "Аххххххх!!!"
    img 10994
    m "ММмммммм!!!"
    img 10995
    m "ФУ! КАКАЯ МЕРЗОСТЬ!!!"

    #уходит
    img 10996
    with fade
    w
    img 10997
    with fade
    mt "Эта сучка и не собиралась покупать платье!"
    return True
