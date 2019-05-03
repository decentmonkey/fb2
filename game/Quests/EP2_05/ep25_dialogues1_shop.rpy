label ep25_dialogues1_shop1:

# Моника пытается зайти к Стиву в офис.
# Если Моника не ходила к Виктории, то она говорит что сначала надо проверить перевел-ли Стив деньги.
    mt "Мне надо сначала узнать, перевел-ли Стив деньги Виктории..."
    return

# Если не куплена новая одежда, то она говорит что не пойдет туда в таком виде.
# Что она леди и Босс и ей надо выглядеть подобающе. Говорит что надо наведаться в магазин одежды
    mt "Я не могу идти туда в таком виде."
    mt "Вообще-то я Леди!"
    mt "И Босс!"
    mt "И мне надо выглядеть подобающе."
    mt "Возможно, стоит наведаться в тот магазин одежды, куда меня водил Дик?"
    mt "Это еще та дыра, но, может быть, я смогу найти там что-то подходящее."
    mt "Из того что я могу себе позволить в данный момент..."
    mt "!!!"
    mt "Когда же кончится этот кошмар!"
    return

label ep25_dialogues1_shop2:
    # Если не whore outfit, то магазин закрыт!

# Моника приходит в магазин одежды.
# Там, в зависимости от ее предыдущего поведения, ее встречает продавец.
# Моника спрашивает есть-ли что-то приличное из деловой одежды.
# Продавец показывает самое приличное что есть. Бизнес костюм.
# Моника говорит что это дешевая подделка и есть-ли что-то получше.
# Продавец отвечает что получше ничего нет.
# Костюм стоит $1000.
    cashier "Здравствуйте, Мэм!"
    cashier "Чем могу быть Вам полезна?"
    m "Мне нужно подобрать что-то приличное."
    m "Что-то, что смотрится по деловому, но, в тот же момент, очень стильное."
    m "Что-нибудь что подойдет для такой бизнес-леди..."
    # смущенно смотрит на себя. продавщица тоже
    m "Как Я..."
    cashier "..."
    m "..."
    cashier "Мэм, пройдемте, я покажу Вам самое лучшее платье, которое имеется в продаже."
    # Показывает платье Моники
    mt "О БОЖЕ! Это же мое платье!"
    mt "То платье, которое я вернула."
    mt "Оно мне сейчас кажется таким красивым!"
    m "Простите, Мэм..."
    m "Я бы предпочла сейчас что-нибудь подешевле..."
    cashier "Хорошо, вот еще неплохое платье, оно подойдет Вам."
    # Моника смотрит на еще одно платье
    m "Сколько стоит это платье?"
    cashier "Это платье стоит $ 500, Мэм."
    m "Я разбираюсь в моде и вижу что это подделка под более дорогой бренд."
    cashier "Мэм, это прекрасное платье. По очень доступной цене."
label ep25_dialogues1_shop2_loop1:
    menu:
        "Попросить скидку.":
            if clothShopCashierOffended2 == False and clothShopCashierOffended3ReturnDress == False and clothShopCashierFirstNightOffended == False:
                $ notif(_("Моника была добра к продавцу."))
                m "Скажите, можно-ли сделать какую-то скидку?"
                cashier "Мэм, вообще-то это платье не продается по скидке..."
                m "Я очень прошу Вас. Вы ведь узнаете меня? Я очень лояльный клиент."
                cashier "..."
                cashier "Да, я узнала Вас. Хотя Вы и одеты сегодня немного странно."
                cashier "Хорошо, я сделаю скидку в 50 процентов, только ради Вас!"
                menu:
                    "Купить платье за $ 250." if money>=250:
                        m "Давайте я померю его."
                        cashier "Проходите в примерочную..."
                        # примерочная
                        m "Мне нравится."
                        m "Я беру его."
                        cashier "Мэм, пройдемте на кассу."
                        return True
                    "Купить платье за $ 250. (не хватает денег) (disabled)" if money < 250:
                        pass
                    "Уйти."
                        m "Хорошо, я подумаю."
                        m "Возможно вернусь позже."
                        cashier "Да, Мэм. Возвращайтесь! Мы всегда рады Вам."
                        return False
            else:
                $ notif(_("Моника была недостаточно добра к продавцу."))
                m "Скажите, можно-ли сделать какую-то скидку?"
                cashier "Мэм, вообще-то это платье не продается по скидке..."
                m "Я очень прошу Вас. Вы ведь узнаете меня? Я очень лояльный клиент."
                cashier "..."
                cashier "Я узнала Вас! И я не могу сказать что Вы лояльный клиент нашего магазина."
                cashier "Для Вас цена составляет $ 500!"
                if monicaBitch == True:
                    mt "Сучка!"
                else:
                    mt "!!!"
                jump ep25_dialogues1_shop2_loop1

        "Купить платье за $ 500.":
            m "Давайте я померю его."
            cashier "Проходите в примерочную..."
            # примерочная
            m "Мне нравится."
            m "Я беру его."
            cashier "Мэм, пройдемте на кассу."
            return True

        "Уйти.":
            m "Хорошо, я подумаю."
            m "Возможно вернусь позже."
            cashier "Да, Мэм. Возвращайтесь! Мы всегда рады Вам."
            return False

label ep25_dialogues1_shop3:
    # Моника пытается зайти в магазин после покупки платья за деньги
    mt "Мне нечего делать там сейчас..."
    return

label ep25_dialogues1_shop4:
# Моника замечает что в этот раз в магазине мало народа и она может украсть его.
    mt "А в этом магазине сегодня на удивление никого нет..."
    mt "Может быть мне попробовать... украсть это платье?"
    return

label ep25_dialogues1_shop5:
    # Моника заходит в магазин снова
    menu:
        "Обратиться к продавцу.":
            return False
        "Украсть платье.":
            return True
    return

label ep25_dialogues1_shop6:
    # Моника пытается украсть платье
# Если пытается украсть, то ее ловит продавец.
# Происходит перепалка и продавец хочет вызвать полицию.
# Моника просит не делать этого.
# В зависимости от того как Моника вела себя, продавец затаскивает ее в примерочную, где делает femdom.
# Диалоги отличаются в зависимости от поведения Моники.
# Если Моника вела себя хорошо и она скромная, то можно сказать что ей сейчас трудно и она отдаст деньги после.
# Продавец тогда соглашается. Моника затем не входит в магазин, т.к. ей пока не до отдачи долгов.
# Затаскивание в примерочную:
# Продавец говорит что помнит Монику. Что она- та сучка, которая ругалась на нее и вернула платье.
# Моника просит, пожалуйста, не надо вызывать полицию.
# Моника может ударить продавщицу и убежать
# Либо Продавщица говорит Монике одеть то платье, которое она возвращала.
# Моника спрашивает: но зачем?
# Продавщица говорит делать что сказано, иначе через 5 минут она будет в полцейском участке.

    cashier "Ну что, сучка, далеко собралась?!"
    cashier "Думаешь из этого магазина можно что-то украсть?"
    m "Что Вы от меня хотите?!"
    m "Не трогайте меня!"
    m "Дайте мне пройти!"
    cashier "Тебе некуда идти, я закрыла магазин, чтобы ты не убежала."
    cashier "Я вызываю полицию!"
    m "Что?! Да как ты смеешь! Я респектабельный клиент!"
    if clothShopCashierFirstNightOffended == True:
        cashier "Я узнала тебя! В прошлый раз тебе удалось отвертеться, но в этот раз полиция схватит тебя!"

    cashier "Я видела, ты пыталась украсть это платье!"
    cashier "Я закрываю магазин, ты отсюда не уйдешь!"
    m "Что?! Полиция?!"
    m "Мне не нельзя в полицию!!!"
    cashier "Это уже твои проблемы!"
    cashier "Алло! Полиция?"
    cashier "У меня в магазине вор, я прошу Вас приехать скорее."
    mt "О БОЖЕ!!! ЧТО МНЕ ДЕЛАТЬ?!"
    menu:
        "Ударить продавца и убежать!" if monicaBitch == True:
            m "Ты не могла успеть закрыть дверь!"
            m "Ты все врешь!"
            m "Получай, На!"
            cashier "Аххх!"
            # Моника убегая
            m "Это мое платье! Я заслужила его!"
            return False
        "Ударить продавца и убежать! (Моника слишком приличная) (disabled)" if monicaBitch == False:
            pass
        "Умолять не вызывать полицию...":
            return True

label ep25_dialogues1_shop7:
    # Умоляет не вызывать полицию

    m "Пожалуйста, не надо!"
    m "Я готова на ВСЕ!!!"
    m "ВЫ СЛЫШИТЕ?! Я ГОТОВА НА ВСЕ!!!"
    m "Только не вызывайте полицию! Пожалуйста!"
    cashier "На все говоришь?"
    policeman "Пожалуйста, назовите адрес..."
    m "Да, НА ВСЕ!!!"
    m "ПОЖАЛУЙСТА, ПОЛОЖИТЕ ТРУБКУ!"
    cashier "У меня есть идея."
    cashier "Вас плохо слышно, я перезвоню."
    # кладет трубку

    cashier "Идем за мной."
    # Приводит в примерочную
    cashier "Жди здесь."
    # Берет манекен с красивым платьем
    cashier "Вот, одевай!"

    m "Мое платье?! Но зачем?"
    cashier "Оно не твое! Ты вернула его, забыла?"
    cashier "Быстро одевай!"
    # Моника одевает платье
    cashier "А теперь ложись!"
    m "Зачем?"
    cashier "Еще одно зачем и я вызываю полицию!"
    m "Хорошо, я ложусь..."
    m "Эй, что Вы делаете?!"

    # Продавец садится на Монику
    cashier "Я Вас обслуживала ранее и теперь хотела бы получить фидбек."
    cashier "Вам понравилось обслуживание?"
    m "Мммпфххх...."
    cashier "Только попробуй сказать нет..."
    cashier "Вам понравилось обслуживание?"
    m "Мммм... Да..."
    cashier "Оцените обслуживание по десятибальной шкале!"
    cashier "Вы ведь оцениваете обслуживание на десять баллов, правда?"
    m "Мммпфхх..."
    cashier "Отвечай, сучка. Иначе отправишься в полицию прямо сейчас."
    m "Мммпфхх... Да..."
    cashier "Посоветуете-ли Вы этот магазин своим друзьям и знакомым?"
    m "Мммпфхх... Да..."

    cashier "А теперь я хочу попробовать твою розовую киску. Мммм..."
    cashier "Ммммм... Какая прелесть..."
    cashier "Ммммм... Такая вкусная киска мне еще не попадалась..."
    cashier "Ммммм..."

    # встает
    cashier "А теперь быстро переодевайся назад!"
    # Моника переодевается

# Дает платье.
# Моника в шоке: мое! мое платье! оно такое красивое!
# Продавщица говорит Монике скорее одеть его. Продавщица говорит идти в примерочную.
# Моника одевает платье.
# Продавщица заходит и говорит Монике ложиться на пол!
# Моника не понимает зачем?
# Продавщица зло смотрит.
# Моника ложится.
# Продавщица говорит что она обслуживала ее и теперь хочет получить фидбек.
# Продавщица садится Монике на лицо (femdom)
# По ходу сцену, Продавщица говорит диалоги о том как Вам понравилось обслуживание?
# Монике приходится отвечать что ей очень понравилось.

# В конце продавщица кончает и говорит Монике что у нее есть предложение.
# Что она может отдать ей ту одежду что Моника хотела украсть в случае, если Моника поможет продать
# это гребаное платье.
# Моника спрашивает, а можно ей отдать это платье?
# Продавщица говорит что нет. Это самое дорогое платье в этом магазине.
# Здесь нет ни у кого денег, чтобы купить такую дорогую тряпку.
# И поставщик отказывается принимать это платье назад.
# Так что, это платье надо продать, чтобы не потерять премиальные за квартал.
# На манекене оно смотрится хуже, чем на тебе, сучка.
# Потому у тебя есть шансы продать его.

    cashier "Ты можешь идти, но не вздумай даже смотреть на то платье, которое собиралась украсть."
    cashier "Хотя..."
    cashier "У меня есть предложение для тебя..."
    m "Кккккакое предложение?"
    cashier "Я могу тебе подарить то платье, что ты хотела украсть."
    cashier "Но только в случае, если ты сможешь продать другое."
    m "Какое другое?"
    cashier "То платье, которое ты вернула некоторое время назад."
    cashier "То, в котором ты сейчас была на полу."
    m "А можно... Просто подарить мне его."
    cashier "Нет! Это самое дорогое платье в этом магазине."
    cashier "В этом районе ни у кого нет денег, чтобы купить такую дорогую тряпку."
    cashier "И поставщик отказывается принимать это платье назад."
    cashier "Мне надо продать это платье, иначе я рискую потерять премиальные за квартал."
    cashier "На манекене оно смотрится хуже, чем на тебе, сучка."
    cashier "Потому у тебя гораздо большие шансы продать его."

# Моника спрашивает что от нее требуется?
# Продавщица говорит что ей надо будет одеть это платье и показывать его покупателям.
# Ей не важно что Моника будет делать, но если продаст его, то получит взамен ту одежду.
# И пусть даже не думает о том, чтобы убежать в этом дорогом платье!
# Продавщица фотографирует Монику в платье.
# Говорит этот снимок сразу отправится в полицию, если она попробует убежать.
# Выбор:
# Согласиться продавать платье.
# Отказаться.
    m "Что он меня требуется?"
    m "Как я буду его продавать? Я буду работать продавцом?"
    mt "О БОЖЕ! Кажется я нашла нормальную работу!"
    cashier "Здесь уже есть продавец!"
    cashier "Тебе надо будет работать манекеном!"
    cashier "Ты оденешь это платье и будет показывать его покупателям."
    cashier "И мне не важно как будешь уговаривать покупателей его купить."
    cashier "Но, если ты продашь его, то получишь в награду взамен ту одежду, что хотела украсть."
    m "Но, разве можно продать одежду, которая надета на продавце?"
    cashier "Не на продаце, а на манекене!"
    cashier "И если этот манекен умеет убеждать купить одежду, то так даже лучше!"
    cashier "В любом случае, я уже испробовала все другие варианты продать его!"
    mt "РАБОТАТЬ... МАНЕКЕНОМ!!!"
    cashier "Да, кстати."
    # щелкает ее на телефон
    cashier "И только попробуй что-нибудь украсть."
    cashier "Этот снимок сразу отправится в полицию!"
    m "!!!"
    cashier "Ну так что, ты согласна?"
    menu:
        "Согласиться работать манекеном.":
            m "Я... Я согласна..."
            cashier "Приходи завтра днем!"
            cashier "Сегодня посетителей уже не будет!"
            return True
        "Отказаться.":
            m "Я... пока не готова..."
            cashier "Если надумаешь, приходи!"
            return False


label ep25_dialogues1_shop8:
    # Моника рассуждает на улице
    mt "Работать манекеном?"
    mt "Какой ужас!"
    mt "..."
    mt "С другой стороны, у меня может появиться нормальная одежда."
    mt "НОРМАЛЬНАЯ!!!"
    mt "А не эти тряпки!!!"
    return

label ep25_dialogues1_shop9:
    # Моника приходит в магазин работать манекеном
    menu:
        "Работать манекеном...":
            m "Я... Я пришла работать манекеном..."
            if day_time != "day"
                cashier "Приходи днем! Вечером мало посетителей!"
                return False
            cashier "Хорошо. Переодевайся и выходи работать!"
            return True
        "Уйти.":
            return False

label ep25_dialogues1_shop10:
    return

    if clothShopCashierOffended2 == False and clothShopCashierOffended3ReturnDress == False and clothShopCashierFirstNightOffended == False:

# Если отказаться, то затем можно вернуться и сказать снова.

# Продавщица говорит, чтобы Моника приходила завтра днем.
# Моника приходит, выбор:
# Работать манекеном.
# Уйти

# В магазине народ

# Моника подходит к людям и предлагает платье

# Платье продается в несколько этапов.
# Этап 1
# Моника стоит в платье.
# Подходят люди и спрашивают сколько оно стоит.
# Моника может отвечать цену, либо промолчать
# Также Моника может говорить что это платье из хорошего материала и будет смотреться отлично на любой девушке.
# Говорят что слишком дорого

# Этап 2
# Моника стоит в платье.
# Подходят люди и спрашивают сколько оно стоит.
# Говорят что слишком дорого
# Подходит покупатель и спрашивает про цену
# Моника отвечает.
# Покупатель просит повернуться спиной
# Моника поворачивается и продолжает говорить что это хорошая покупка
#














#
