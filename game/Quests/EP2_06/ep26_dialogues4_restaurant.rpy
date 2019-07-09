# Моника входит в Le Grand

# voucher or gift coupon

# На нее смотрит рецепшин
# Моника не хочет к ней подходить
# Моника может пойти в ресторан
label ep26_dialogues4_restaurant1:

# Если Моника занималась миньетом в туалете, то:
# При входе в ресторан, ее перехватывает рецепшионист.
# Спрашивает, Мэм, какая цель Вашего визита сюда?
# Моника отвечает что это не ее дело!
# Та отвечает что это ее дело, потому как у нее есть подозрение на незаконное занятие проституцией.
# Это запрещено в нашем отеле.
    img 20391
    w
    img 20392
    w
    img 20393
    w
    img 20394
    reception "Женщина, постойте-ка!"
    img 20395
    m "Что Вам надо?!"
    img 20396
    reception "Мэм, какая цель Вашего визита сюда?"
    img 20397
    m "Это не Ваше дело!"
    m "Я посещаю любые места когда захочу."
    m "И не собираюсь отчитываться ни перед кем!"
    img 20398
    reception "Мэм, это мое дело, как сотрудника отеля."
    reception "У нас есть подозрение на незаконное занятие проституцией."
    img 20399
    reception "Это запрещено в нашем отеле!"
# Моника отвечает да как она смеет?!
# Моника приличная леди!
# И идет просто отведать ланч в ресторане!
# Рецепшионист заявляет, чтобы Моника предъявила доказательства этого, иначе она сейчас вызовет охрану.
# выбор Моники: показать тикет на ланч, либо уйти (если тикета нет, то он серый), либо устроить скандал (если Моника сучка)
    img 20400
    m "ЧТО?!"
    img 20401
    m "Да как ты смеешь, никчемный работник!?"
    m "Я приличная Леди!"
    m "И иду отведать ланч в Вашем ресторане!"
    m "По приглашению!"
    img 20402
    reception "Мэм, пожалуйста, предъявите доказательства того, что Вы собираетесь посетить ресторан."
    reception "И Ваше приглашение."
    img 20403
    reception "Иначе я вынуждена буду вызвать охрану."
    img 20404
    menu:
        "Показать сертификат.":
# Либо Моника показывает тикет и рецепшионист заявляет что Моника может проходить, но она будет следить за ней.
# Моника зло и надменно смотрит и проходит.
            img 20405
            m "Абсолютно не понимаю необходимость этого ненужного действия."
            m "Но вот, пожалуйста!"
            img 20406
            m "Если уж Вам так надо!"
            reception "..."
            return True
        "Показать сертификат. (disabled)":
            pass
        "Устроить скандал и войти":
# Моника устраивает скандал:
# Моника говорит рецепшионистке что у нее достаточно с собой денег на то, чтобы скупить весь этот отель!
# И если рецепшионистка желает, то может ходить за ней и следить.
# Однако, если она это делает с целью получить на чай от такой леди как Моника, то она выбрала неверный путь!
# А сейчас пусть уйдет с дороги, пока Моника по настоящему на разозлилась!
            img 20407
            m "Доказательства?!"
            m "У меня достаточно денег, чтобы скупить весь этот дурацкий отель!"
            reception "..."
            img 20408
            m "Поверь, я уже все всем доказала в этой жизни!"
            m "И, если тебе кажется, что в этом есть необходимость, то можешь ходить за мной и следить."
            m "Однако, если твоя цель преследования меня получить чаевые от такой леди как Я, то ты выбрала неверный путь!"
            img 20409
            m "А сейчас, уйди с дороги, пока я по настоящему не разозлилась!"
            img 20410
            reception "..."
            return True
        "Уйти.":
            # Если Моника уходит, то говорит что еще вернется и устроит неприятности такому нерадивому и никчемному сотруднику как она!
            img 20411
            m "Я не собираюсь предъявлять каких-то дурацких доказательств!"
            img 20412
            m "Я ухожу!"
            m "Но я еще вернусь!"
            m "И устрою неприятности такому нерадивому и никчемному сотруднику, как Вы!"
            img 20413
            reception "..."
            return False




label ep26_dialogues4_restaurant2:
# Если Моника НЕ занималась миньетом в туалете, то:
# Рецепшионист перехватывает Монику
# Мэм. Пожалуйста, назовите цель Вашего визита.
# Я иду в ресторан!
# Хорошо, Мэм.
    img 20414
    reception "Мэм! Пожалуйста, назовите цель Вашего визита."
    img 20415
    m "Я иду в ресторан!"
    img 20416
    reception "Хорошо, Мэм."
    img 20417
    w
    return

label ep26_dialogues4_restaurant3:
# Моника входит в ресторан:

# Если Моника обещала уволить официантку:
# waitress: Здравствуйте, Мэм! Это... Это ВЫ?!
# Моника отвечает: Да, это я!
# Удивительно что ты все еще работаешь здесь!
# waitress: Мэм... Что Вам будет угодно?! (злое лицо)
    img 20418
    waitress "Здравствуйте, Мэм!"
    img 20419
    waitress "Это... Это ВЫ?!"
    img 20420
    m "Да, это Я!"
    m "Удивительно, что ты все еще работаешь здесь!"
    img 20421
    waitress "Мэм... Что Вам будет угодно?!"
# Моника говорит что их ресторан не дотягивает до ее требований, но она, так уж и быть,
# соблаговолит откушать здесь
# waitress: Да, Мэм... Присаживайтесь, пожалуйста, за свободный столик (злое лицо)
    img 20422
    m "Этот ресторан не дотягивает до моих требований."
    m "Но я, так уж и быть, соблаговолю откушать здесь."
    img 20423
    waitress "Да, Мэм..."
    waitress "Присаживайтесь, пожалуйста, за свободный столик."
# Моника садится
# waitress: Мэм, Что Вам будет угодно?
    img 20424
    waitress "Мэм, Что Вам будет угодно?"
# меню выбора блюд (если нет тикета, то указаны цены, большие):
# блюдо1
# блюдо2
# блодо3
    menu:
        "Стейк из форели, греческий салат и шампанское."
            img 20425
            m "Стейк из форели, греческий салат и шампанское."
        "Морепродукты и коктейль.":
            img 20425
            m "Морепродукты и коктейль."
        "Лазанья с кофе."
            img 20425
            m "Лазанья с кофе."
        "Суши и сок.":
            img 20425
            m "Суши и сок."
        "Уйти.":
            # Моника уходит
            img 20426
            m "В этом дурацком ресторане нет нормальной еды для такой леди как Я!"
            m "Я ухожу!"
            img 20427
            waitress "!!!"
            return False
# Моника говорит какие блюда выбрала
# Если есть тикет, то она добавляет что оплатит тикетом.
    img 20428
    m "Я оплачу этим сертификатом"

# waitress: Да, Мэм. Несколько минут и все будет готово.
# Моника надменно говорит чтобы официантка поторопилась, если не хочет вылететь с работы прямо сейчас.
# waitress морщится в злобе
    img 20429
    waitress "Да, Мэм. Несколько минут и все будет готово."
    img 20430
    m "Я советую тебе поторопиться, деточка."
    m "Если ты не хочешь вылететь с работы прямо сейчас!"
    img 20431
    waitress "!!!"

# waitress: Пожалуйста, Мэм.
# Моника кушает и говорит как же вкусно.
# Она отвыкла от такой вкусной пищи, а зря!
# Надо скорее возвращать назад ее прежнюю жизнь.
    #Стейк из форели, греческий салат и шампанское.
    img 20432
    img 20433
    img 20434
    img 20435
    #Морепродукты и коктейль.
    img 20436
    img 20437
    img 20438
    img 20435
    #Лазанья с кофе.
    img 20439
    img 20440
    img 20441
    img 20435
    #Суши и сок.
    img 20442
    img 20443
    img 20444
    img 20435

    #1
    waitress "Пожалуйста, Мэм."

    #2
    m "Ммммм... Как вкусно..."
    #3
    m "Я уже отвылка от такой вкусной пищи."
    #4
    m "А зря!"
    m "Надо скорее возвращать назад мою прежнюю жизнь!"

    # смотрят

    mt "Интересно, почему та девушка так смотрит на меня?"


# Моника говорит официантке. Я закончила. Было невкусно!
# waitress: Мэм, прошу прощения, в следующий раз мы постараемся угодить Вам... (злое лицо)
    m "Я закончила."
    m "Было невкусно!"
    waitress "Мэм, прошу прощения."
    waitress "В следующий раз мы постараемся угодить Вам..." # (злое лицо)
    return True

label ep26_dialogues4_restaurant4:
# Моника входит в ресторан:
# Если Моника помогла официантке:

# waitress: Здравствуйте, Мэм! Это... Это ВЫ?!
# Моника отвечает: Да, это Я!
# waitress: Мэм... Я очень рада видеть Вас и тепло приветствую Вас от имени заведения!
# Моника говорит что хотела бы поесть у них
# waitress: Да, Мэм... Присаживайтесь, пожалуйста, за свободный столик (доброе лицо)
    waitress "Здравствуйте, Мэм!"
    waitress "Это... Это ВЫ?!"
    m "Да, это Я!"
    waitress "Мэм... Я очень рада видеть Вас!"
    waitress "И тепло приветствую Вас от имени заведения!"
    m "Спасибо."
    m "Я бы хотела у Вас что-нибудь поесть."
    waitress "Да, Мэм."
    waitress "Присаживайтесь, пожалуйста, за свободный столик." # (доброе лицо)

# Моника садится
# waitress: Мэм, Что Вам будет угодно?
# waitress: Специально для Вас у нас скидка 50% на все меню.
    waitress "Мэм, что Вам будет угодно?"
    waitress "Специально для Вас у нас скидка 50 процентов на все меню."
# меню выбора блюд (если нет тикета, то указаны цены, со скидкой):
# блюдо1
# блюдо2
# блодо3
    menu:
        "Уйти.":
            m "Спасибо, я передумала. Зайду попозже."
            waitress "Мэм, мы всегда ждем Вас!"
            return False

# Моника говорит какие блюдо выбрала
# Если есть тикет, то она добавляет что оплатит тикетом.
    waitress "Я оплачу сертификатом."

# waitress: Да, Мэм. Несколько минут и все будет готово.
    waitress "Да, Мэм."
    waitress "Несколько минут и все будет готово."

# waitress: Пожалуйста, Мэм.
    waitress "Пожалуйста, Мэм."
# Моника кушает и говорит как же вкусно.
# Она отвыкла от такой вкусной пищи, а зря!
# Надо скорее возвращать назад ее прежнюю жизнь.
    m "Ммммм... Как вкусно..."
    m "Я уже отвылка от такой вкусной пищи."
    m "А зря!"
    m "Надо скорее возвращать назад мою прежнюю жизнь!"

# Моника говорит официантке. Я закончила. Было очень вкусно, спасибо!
# waitress: Мэм, добро пожаловать к нам снова!
    m "Я закончила."
    m "Было очень вкусно. Спасибо!"
    waitress "Мэм, добро пожаловать к нам снова!"
    return True

label ep26_dialogues4_restaurant5:
    mt "Я уже посещала ресторан сегодня."
    mt "Больше мне пока нечего там делать."
    return
