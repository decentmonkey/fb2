default monicaShawarmaApartment1 = False  # Моника спросила у продавца шавермы про квартиру
default monicaShawarmaApartment2 = False  # Моника согласилась посмотреть квартиру продавца шавермы
default monicaShawarmaApartment3 = False  # Моника посмотрела квартиру и согласилась ее арендовать
default monicaShawarmaApartment4 = False # Моника внесла первую оплату Джеку за квартиру


# улица Хостела, рядом с пабом, после работы
label ep211_dialogues6_slum_apartment_1:
    # Моника стоит на улице
    mt "Каждый раз, когда прихожу сюда..."
    mt "Боюсь, что встречу ту кошмарную лесбиянку."
    mt "Как вспомню этот ужас в хостеле..."
    mt "Нет! Даже думать об этом не хочу!"
    mt "Тоже мне, дешевый ночлег!"
    mt "!!!"
    mt "Хммм..."
    mt "Кстати, о дешевом ночлеге..."

    # если нет отношений с Юлией и Моника не задумывалась ранее об аренде квартиры
    mt "И почему я раньше об этом не задумывалась?!"
    mt "У меня сейчас есть работа. Заработок у меня стабильный."
    mt "Возможно, мне удастся арендовать какую-нибудь небольшую квартиру?"
    mt "По-моему, это хорошая идея!"
    mt "Я, наконец-то, перестану работать на эту семейку идиотов!"
    mt "И жить независимо ни от кого!!!"
    mt "Только как мне подобрать подходящую по цене квартиру?"
    mt "..."
    #

    # если Моника была в гостях у Юлии и задумывалась об аренде квартиры
    mt "Юлия снимает квартиру в ужасном доме!"
    mt "Но стоит признать, что квартира у нее довольно уютная."
    mt "Конечно, там все старое и убогое..."
    mt "Но все же я была бы не против жить в подобной квартире."
    mt "Представь только, Моника!"
    mt "Никто не будет тебе указывать, что делать и какую одежду носить..."
    mt "Никто не будет ограничивать тебя в еде или в походах в душ..."
    mt "..."
    #

    mt "Кто может знать, где найти дешевое жилье?"
    mt "???"
    mt "В прошлый раз продавец шавермы посоветовал мне хостел..."
    mt "Возможно, стоит спросить у него?"
    $ log1 = _("Спросить у продавца шавермы про аренду квартиры.")
    return

# трущобы, рядом с шавермой
label ep211_dialogues6_slum_apartment_2:
    mt "Уверена, он знает какое-нибудь дешевое жилье."
    mt "Мне эта идея настолько понравилась..."
    mt "И почему я раньше об этом не подумала?"
    return

# разговор с продавцом шавермы, при клике на него
label ep211_dialogues6_slum_apartment_3:
    menu:
        "Спросить про квартиру...": #corruption
            shawarma "О, Мадамэ!"
            shawarma "Мадамэ, Вы пришли за самый вкусный кебаб в округе?"
            m "Нет. Мне не нужен твой кебаб!"
            m "..."
            $ monicaShawarmaApartment1 = True # Моника спросила у продавца шавермы про квартиру
            pass
        "Уйти отсюда.":
            mt "Нет, я пока не готова тратить деньги на квартиру."
            mt "Мне это сейчас не по карману."
            m "Сам ешь свой отвратительный кебаб!"
            # если называла его животным
            mt "Животное!"
            #
            m "!!!"
            return False
    # ехидно смотрит на него
    m "Я хотела кое-что у тебя спросить..."
    shawarma "Все, что Мадамэ захотеть, Джек все сделает!"
    shawarma "Для прекрасной Мадамэ Джеку ничего не жалко!"
    m "Мне..."
    m "..."
    m "Одной моей знакомой нужна квартира."
    m "Она хочет ее арендовать..."
    m "За небольшую плату."
    m "Ты знаешь, где можно что-то подходящее найти?"
    shawarma "О, Мадамэ!"
    shawarma "Вы правильно сделали, что пришли ко мне!"
    shawarma "Джек все здесь знает!"
    shawarma "Для восхитительной Мадамэ у Джека есть квартира!"
    m "Это... Это не для меня квартира..."
    shawarma "Мадамэ может не волноваться."
    shawarma "Джек никому не рассказывать!" # подмигивает ей
    m "!!!"
    m "Так у тебя есть квартира под аренду?" # воодушевленно
    shawarma "Конечно, Мадамэ!!!"
    shawarma "И как раз сейчас она сдается!"
    shawarma "Это шикарный квартира! Мадамэ будет очень рад!"
    # он не знает, что у нее нет документов. говорит, что квартира стоит 50 долларов
    # разговор про документы и про 300 баксов происходит уже в квартире
    shawarma "И всего за 50 долларов в неделю!"
    shawarma "Специальный цена для прекрасной Мадамэ!"
    mt "Боже! Я не верю в эту удачу!"
    mt "Наконец-то!"
    mt "!!!"
    mt "Стоп!"
    m "..."
    m "А почему так дорого?!"
    m "Эта квартира где-то в городе?"
    shawarma "У Джека квартира недалеко отсюда, Мадамэ."
    m "Квартира в трущобах за 300 долларов в неделю?!"
    m "?!?!?!"
    shawarma "Специально для Мадамэ!"
    shawarma "Документы есть - квартира стоит 200 долларов!"
    shawarma "Документов нет - квартира стоит 300 долларов!"
    shawarma "Джек все для Вас готов сделать, Мадамэ!"
    mt "Вот сволочь!"
    mt "!!!"
    mt "300 долларов в неделю..."

    # если работает в эскорте и уже обслуживала клиентов
    mt "В эскорте я за один вечер могу заработать такую сумму."
    mt "Почему бы и нет?"
    #

# если отказалась идти смотреть квартиру, диалог начнется с этого момента
    shawarma "Мадамэ хочет посмотреть свою будущую квартиру?"
    m "..."
    menu:
        "Согласиться.": #corruption
            $ monicaShawarmaApartment2 = True # Моника согласилась посмотреть квартиру продавца шавермы
            pass
        "Нет, это слишком дорого.":
            mt "Я пока не готова тратить деньги на квартиру."
            mt "Мне это сейчас не по карману."
            m "Нет."
            m "Мне нужно еще подумать."
            shawarma "Если Мадамэ надумает, может приходить к Джеку!"
            shawarma "Джек будет рад помочь прекрасной Мадамэ!"
            # если называла его животным
            mt "Животное!"
            #
            m "!!!"
            return False
    m "А там никто больше не будет жить, кроме меня?"
    shawarma "Конечно, нет!"
    shawarma "Мадамэ будет хозяйкой в этот шикарный квартира!"
    mt "Отлично!"
    m "Я хочу ее посмотреть!"
    shawarma "Завтра вечером приходи к дому рядом с кафе (???)" # идут сразу и оказываются в новой локации
    m "Я приду. И только попробуй обмануть меня!"
    shawarma "Джек никогда не обманывать! Он честный!"
    shawarma "Джек будет ждать Мадамэ!"
    $ log1 = _("Вечером прийти к дому рядом с кафе, чтобы арендовать квартиру.")
    return

# Моника возле дома рядом с кафе (глазик)
label ep211_dialogues6_slum_apartment_4:
    mt "Этот дом просто кошмарный!!!"
    return

# след день. дом рядом с кафе
label ep211_dialogues6_slum_apartment_5:
    # стоит возле дома, Джек стоит рядом
    mt "Жуть!!!"
    mt "Он что-то говорил про шикарную квартиру?"
    mt "Шикарная квартира в ТАКОМ доме?!"
    mt "???"
    m "Ты уверен, что квартира хорошая?"
    shawarma "Конечно, Мадамэ!"
    shawarma "Мадамэ идти за мной и сам все посмотреть!"
    m "..."
    return

# квартира Моники
label ep211_dialogues6_slum_apartment_6:
    # Моника стоит посередине квартиры
    m "Куда ты меня привел?!"
    m "Это что?! Квартира?!"
    m "?!?!?!"
    shawarma "Да, Мадамэ!"
    shawarma "Теперь это Ваш шикарный квартир!"
    m "Шикарный?!"
    m "Да ты охренел?!"
    shawarma "Мадамэ без документов."
    shawarma "Она никакой квартир больше не найдет!"
    shawarma "Да и еще и по специальный цена для Мадамэ!"
    mt "!!!"
    mt "!!!!"
    menu:
        "Согласиться.":
            $ monicaShawarmaApartment3 = True # Моника посмотрела квартиру и согласилась ее арендовать
            pass
        "Уйти отсюда!":
            m "Я не буду жить в этой!"
            m "В этой!"
            m "В этом пристанище для бомжей!!!"
            m "!!!"
            shawarma "Если Мадамэ надумает, может приходить к Джеку!"
            shawarma "Джек будет рад помочь прекрасной Мадамэ!"
            # если называла его животным
            mt "Животное!"
            #
            m "!!!"
            # Моника уходит
            return False
    mt "Дьявол!"
    mt "Мне не удастся снять квартиру без документов..."
    mt "Получается, что это пока что единственный вариант."
    mt "..."
    shawarma "Мадамэ жить один и Джек ее не беспокоить совсем."
    shawarma "Только один раз в неделю Джек прихоить за деньгами. {c}В субботу{/c}"
    mt "И что мне делать?"
    mt "???"
    mt "С другой стороны... Это будет МОЯ квартира..."
    mt "О том, где я живу, никто не будет знать..."
    mt "Я буду сама себе хозяйка..."
    mt "И больше никакие никчемные деревенщины мною не будут командовать!"
    # поворачивается к Джеку
    shawarma "Мадамэ согласен?"
    m "Деньги сейчас платить?"
    shawarma "Да. Сейчас."
    shawarma "И Мадамэ может сразу оставаться жить здесь."
    m "Следующая оплата ровно через неделю?"
    shawarma "Джек будет приходить каждая суббота за деньгами."
    shawarma "Суббота вечер."
    shawarma "Мадамэ платить и оставаться здесь жить!"
    m "..."
    menu:
        "Заплатить $ 300 за квартиру.":
            $ monicaShawarmaApartment4 = True # Моника внесла первую оплату Джеку за квартиру
            pass
    # у Моники списываются с баланса деньги
    shawarma "Джек счастлив помочь прекрасной Мадамэ!"
    shawarma "Джек придет за деньгами в следующий суббота."
    shawarma "Вот ключи от Вашей шикарный квартир!"
    # ключи кладет куда-нибудь на стол и уходит
    shawarma "До суббота, прекрасная Мадамэ!"
    m "..." # смотрит на него недовольно
    # Джек уходит
    return






# он приходит раз в неделю и забирает эти деньги
# предлагает ей скидку, 10 процентов - за минет, 20 процентов - за секс с ним
