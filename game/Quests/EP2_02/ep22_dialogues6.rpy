# Если Моника уже заработала 5000, то Бифа нет

# Если Биф есть, то Моника спрашивает еще о работе
# Биф говорит нет проблем, иди в студию, но сначала ты пройдешь кастинг.
# И если Моника не проходила его в прошлый раз, то Биф говорит что ты увиливаешь от кастинга, но тебе придется его пройти, иначе не будет карьерного роста.
# Моника идет к Алексу, одевается в выбранную одежду (еще 2 варианта одежды)
# Затем появляется идти к Бифу на кастинг или не идти (если не идти, то прогресс у Бифа не растет)
# Кастинг пока - грудь, по паре-тройке поз. Биф говорит прими какую-нибудь позу с голой грудью, покажи папочке как ты привлекательна.
# Если Моника не заставляла мартышек раздеваться, то прогресс у Бифа растет без кастинга

# Моника делает фотосессию в выбранной одежде. В конце каждой фотосессии развратные позы.
# После каждой фотосессии растет прогресс у Алекса. На lvl.2 он встает

# Моника возвращается к Бифу и спрашивает про деньги.
# (Если Моника обещала вести себя как хорошая цыпочка, то Биф не хочет давать деньги), но Моника упрашивает его говоря
# что она хорошая цыпочка и заслужила денежку.
# Первый раз Биф говорит что наличных у него в этот раз для нее нет. Моника дает бумажку и просит купить этот сертификат на этот адрес.
# Биф отвечает окей.
# В следующие разы Биф спрашивает что купить такой же сертификат как тогда?
# Моника отвечает что да, Биф шутит что куда она девает все те аксессуары, которые покупает?
# Ей, видимо нравится ходить в таком виде. Моника злится.

# Моника встречает секретаршу, та говорит что все хорошо, мистер Биф заботится о нас.
# Мы должны делать что он говорит. Моника спрашивает что с тобой сделали???
# В этот момент идет вызов и Биф называет секретаршу сиськой и говорит чтобы она подошла в кабинет
# Та отвечает да, мистер Биф, уже беги и идет
# У нее рендер в штанах с голой задницей с трусами

label ep22_dialogue6_1:
    #Диалог секретарши с Моникой, когда Моника пытается зайти к Бифу
    img 8268
    m "Дорогуша, как у тебя дела?"
    img 8269
    secretary "..." #Сидит как истукан
    img 8270
    m "Я знаю что на тебя сильно давит новый Босс."
    "Но, поверь, я скоро разберусь со всем этим!"
    img 8271
    secretary "Мистер Биф лучше нас знает что нам необходимо."
    secretary "Мистер Биф заботится о нас..."
    img 8272
    m "Что?"
    "Что ты такое говоришь, дорогуша???"
    img 8271
    secretary "Мы должна благодарить Мистера Бифа что работаем у него..."
    img 8273
    m "Что они с тобой сделали???"

    img 8274
    #звук коммутатора
    biff "Эй! Сиська!"
    "Быстро зайди ко мне в кабинет!"
    "И захвати еще виски!!!"
    secretary "Да, Мистер Биф! Одну секунду!"

    img 8275
    "Где же?!"
    "Где же виски???"
    img 8276
    "Здесь нет!"
    "Он все выпил..."
    img 8277
    w
    img 8278
    "Ах, я же спрятала еще бутылку здесь, чтобы он сразу не нашел..."
    img 8279
    "Вот оно!"
    #Секретарша уходит, Моника смотрит на ее зад
    img 8280
    w
    img 8281
    mt "О БОЖЕ!!!"
    "Бедняжка! Что они с тобой сделали?!?!"

    #пауза спустя 5 минут
    #Секретарша возвращается
    return

label ep22_dialogue6_2:
    #render
    #Моника разговаривает с секретаршей повторно
    if act == "l":
        return

    $ store_music()
    music Stealth_Groover
    img 8282
    secretary "Мистер Биф лучше нас знает что нам необходимо."
    secretary "Мистер Биф заботится о нас..."

    #если Моника сегодня не просила деньги, то появляется меню выбора
    img 8283
    menu:
        "Попросить деньги в долг.":
            "Дорогая..."
            secretary "Да, Миссис Бакфетт?"
            m "Скажи, у тебя не будет немного денег?"
            img 8284
            secretary "Миссис Бакфетт! Я пока не видела зарплаты здесь, после Вашего ухода..."
            #если у Моники меньше 5 долларов, то дает, иначе нет
            if money > 2:
                secretary "Поэтому у меня нет никаких денег сейчас, Миссис Бакфетт!"
                "Простите!"
                m "А как же Биф? Он что, не дает тебе деньги?"
                img 8285
                secretary "Мистер Биф лучше нас знает что нам необходимо."
            else:
                #
                secretary "У меня есть только кредитная карточка, но мне надо платить за ипотечный кредит."
                "У меня есть $ 5 наличными и все..."
                m "Дорогуша, дай мне, пожалуйста, эти $ 5..."
                img 8286
                secretary "Да, Миссис Бакфетт!"
                "Держите..."
                $ add_money(5)
                #дает 5 баксов


        "Уйти.":
            m "Не переживай, дорогуша!"
            "Я скоро вернусь!"

    $ restore_music()
    return

label ep22_dialogue6_3:
    #render
    #Моника заходит регулярно к Бифу по работе
    menu:
        "Спросить о работе":
            pass
        "Уйти.":
            return False
    img 8287
    m "Биф..."
    "Я хотела узнать у тебя..."
    "Есть-ли еще работа?"
    img 8288
    "Мне нужны деньги..."

    if biffWeeklyPhotoShootEnabled == False:
        #Если не прошла неделя
        img 8289
        biff "Нет, цыпочка!"
        "Сейчас очередь других цыпочек!"
        "Ты пока еще не настолько полюбилась папочке!"
        img 8290
        mt "УРОД!!!"
        menu:
            "Уйти...":
                return False
            "А если я пройду дополнительный кастинг?...":
                img 8291
                m "А если я пройду дополнительный кастинг?..."
                img 8292
                biff "Эта цыпочка пока слишком скучная для дополнительного кастинга!"
                "Я держу эту куклу только из-за того что она похожа на сучку Бакфетт!"
                "Иди и не отвлекай папочку! Ему нужно заботить о других цыпочках!"
                img 8290
                mt "Я НЕНАВИЖУ ЭТОГО УРОДА!!!"
                "КОГДА Я ВЕРНУ СВОЕ МЕСТО НАЗАД?!?!"
                return False

    img 8293
    biff "Да, цыпочка!"
    "Работа есть!"
    "Иди в студию!"

    if biffMonicaCastingsEnabled == True:
        #если надо пройти кастинг
        img 8294
        with fade
        biff "Только цыпочка! Тебе надо пройти кастинг!"
        img 8295
        mt "О БОЖЕ!!!"
        "Только не это!!!"

        if biffMonicaLastCastingSkipped == True:
            #если Моника увиливала от кастинга в прошлый раз
            img 8296
            with fade
            biff "Я знаю ты увиливаешь от кастинга, но тебе придется его пройти!"
            "Иначе не будет карьерного роста!"
            "Ты понимаешь?"
            img 8297
            m "Да, я понимаю, Биф..."
            img 8290
            mt "Сволочь!!!"

    #блокировать выход на monica_office_secretary_dialogue6
    return

label ep22_dialogue6_4:
    #render
    #Моника пришла к Алексу, фотосессии еще нет
    img 6352
    with fade
    alex_photograph "Миссис Бакфетт!"
    "Здравствуйте!"
    img 6353
    m "Здравствуй, Алекс..."
    img 6354
    alex_photograph "Вы хотите сделать еще одну фотосессию?"
    menu:
        "Пока нет...":
            pass
    m "Пока нет..."
    alex_photograph "Миссис Бакфетт! Приходите в любой момент!"
    img 6358
    "Я всегда рад фотографировать Вас!"
    img 6353
    mt "!!!"
    return

label ep22_dialogue6_5:
    #render
    #Моника пришла к Алексу, фотосессия начинается
    img 6352
    with fade
    alex_photograph "Миссис Бакфетт!"
    "Здравствуйте!"
    img 6353
    m "Здравствуй, Алекс..."
    img 6354
    alex_photograph "Вы хотите сделать еще одну фотосессию?"
    menu:
        "Да... (черт!)":
            pass
        "Пока нет...":
            return False
    m "Да, Алекс..."
    "Еще одну..."
    img 8314
    mt "Дьявол! Не знаю куда эти грязные фотосессии меня заведут!"
    "Надо кончать с этим скорее!"

    img 6354
    alex_photograph "Миссис Бакфетт!"
    "Вы уже знаете кем в каком наряде Вы будете сниматься в этот раз?"

    img 6353
    m "Еще не знаю..."
    "Что там Биф придумал на этот раз?"
    return True

label ep22_dialogue6_5a:
    #выбор наряда завершен
    img 6357
    with fade
    alex_photograph "Отлично, Миссис Бакфетт!"
    "Можете переодеваться здесь! Я не буду смотреть!"
    img 6356
    m "Я переоденусь в гримерке!"
    "Надеюсь Мелани не закрыла ее в этот раз?"
    img 8315
    alex_photograph "Нет, Миссис Бакфетт, она открыта..." #грустно
    img 8316
    m "Я скоро вернусь!"
    return

    # СТАРЫЙ КОНТЕНТ
    call ep22_photoshoot1()
    "Выберите наряд для фотосессии сегодня!"

    m "Я выбираю это..."
    #Если кастинг у Бифа
    menu:
        "Идти на кастинг к Бифу.":
            call ep22_dialogue6_6()
        "Не идти к Бифу.":
            pass
    #fade

    #начинается фотосессия
    music Molten_Alloy
    alex_photograph "Начинайте, позировать!"
    "Мотор!"
    img black_screen
    with Dissolve(1.0)
    #фотосессия Моники обычная
#    $ add_char_progress("AlexPhotograph", photoshot2AlexProgressAmount, "photoshot_day_" + str(day))

#    call photoshop_flash() from _call_photoshop_flash

    alex_photograph "Миссис Бакфетт! Примите, пожалуйста, эту позу!"
    m "Алекс, снова ты за свое!"
    alex_photograph "Мэм! Это теперь моя работа!"
    menu:
        "Смириться с неизбежностью откровенных поз...":
            pass
        "Предложить Алексу другой вариант... (Alex, low progress) (disabled)":
            pass
    #развратные позы
    menu:
        "Продолжить делать кадры. (corruption)" if corruption >= monicaBiffWorkPhotoShot1PervertCorruptionRequired:
            $ add_char_progress("AlexPhotograph", photoshot1AlexProgressPervertAmount, "photoshot1_corruption")
            $ add_corruption(monicaBiffWorkPhotoShot1PervertCorruptionAdding, "monicaBiffWorkPhotoShot1PervertCorruptionAdding")

            alex_photograph "Мы закончили, Мэм!"
            "Хотите переодеться назад?"
        "Продолжить делать кадры. (low corruption, required [monicaBiffWorkPhotoShot1PervertCorruptionRequired]) (disabled)" if corruption < monicaBiffWorkPhotoShot1PervertCorruptionRequired:
            pass
        "Прекратить это.":
            music Stealth_Groover
            m "Я не буду так сниматься!"
            m "Мы сделали достаточно кадров!"
            alex_photograph "Хотите переодеться назад?"


    #Если кастинг у Бифа не необходим
    #Рост прогресса у Бифа
    return

label ep22_dialogue6_6:
    #render
    #Кастинг у Бифа
    #Моника в зависимости от одетой одежды

    # если Моника обещала вести себя как цыпочка
    biff "О! Цыпочка! Ты пришла?"
    "Что надо сказать?"
    "Помнишь, что ты обещала?"
    m "Цыпочка пришла на кастинг к папочке..."
    mt "Ненавижу!!!"
    biff "Молодец цыпочка!"
    # иначе
    biff "О! Цыпочка! Ты пришла?"
    m "Да, Биф! Я пришла, потому что ты заставил!"
    #

    biff "Итак, цыпочка пришла на кастинг..."
    "Чем цыпочка готова удивить папочку в этот раз?"


    mt "Мерзавец!"
    #рост прогресса у Бифа
    return

label ep22_dialogue6_7a:
    mt "Я сделала фотосессию!"
    mt "Мне надо получить деньги от Бифа!"
    return False
label ep22_dialogue6_7:
    #render
    # Моника возвращается к Бифу и спрашивает про деньги.
    img 8298
    with fade
    m "Биф! Я сделала фотосессию!"
    "Где мои деньги?"

    if monicaSaidBiffSheIsWillBeAGoodChick == True:
        #Если Моника хорошая цыпочка
        biff "Только хорошие цыпочки получают деньги от папочки!"
        "Моника хорошая цыпочка?"
        menu:
            "Моника хорошая цыпочка...":
                pass
            "Уйти без денег...":
                img 8290
                mt "Я лучше уйду без денег, чем скажу это снова!!!"
                return

        img 8299
        m "Моника хорошая цыпочка."
        "Моника заслужила денежку..."
        mt "!!!"
        #иначе

    if monicaAskBiffGiftCertificateFirstTime == True:
        $ monicaAskBiffGiftCertificateFirstTime = False
        #Если первый раз
        img 8300
        biff "Цыпочка! У меня нет наличных!"
        img 8301
        m "Можно купить сертификат и послать его на этот адрес..." #дает бумажку
        biff "Окей, цыпочка! Нет проблем!"
    else:
        #иначе
        img 8302
        biff "Цыпочке купить такой же сертификат как обычно?"
        m "Да..."

    #fade
    img 8303
    with fade
    $ monicaEarnedWeeklyMoney = True
    $ notif(_("Подарочный сертификат на $ 5000 отправлен Виктории"))
    biff "Все готово!"
    img 8304
    menu:
        "Ты что-то говорил по поводу работы в офисе?":
            img 8305
            m "Ты что-то говорил по поводу работы в офисе?"
            biff "Да, когда ты станешь очень хорошей цыпочкой, я возьму тебя сюда в офис!"
            "Ты полезная кукла, я смогу продавать тебя здесь!"
            img 8306
            m "Что значит продавать меня???"
            img 8307
            biff "Торговать твоим личиком!"
            "Ты ведь похожа на Монику Бакфетт!"
            "Ты наверное уже забыла!"
            "Ха-Ха-Ха!"
            img 8290
            mt "!!!"
            img 8308
            biff "Но, может быть и не только личиком!"
            "Думаю многие партнеры готовы будут неплохо заплатить, чтобы запустить свои пальчики..."
            "В киску Моники Бакфетт!"
            "И не только пальчики!"
            "Ха-Ха-Ха!"
            "И все будут думать что ты настоящая!"
            img 8309
            mt "!!!"
            img 8308
            "Тебе это очень понравится!"
            "Ты будешь заниматься тем же самым чем занимаешься на улице сейчас..."
            "Только будешь значительно больше получать за это!"
            img 8310
            m "Нет, Биф!"
            "Давай пока ограничимся личиком!"
            img 8311
            biff "Без проблем, крошка!"
            "Все-равно тебе еще надо заработать это доверие!"
            "А это значит быть хорошей цыпочкой!"
            img 8312
            biff "К тому же, тебе придется значительно чаще развлекать меня."
            "Проводить кастинги."
            "И придумывай что-нибудь новое почаще!"
            "Папочке может наскучить однообразная цыпочка!"
            img 8313
            mt "!!!"
            m "Я могу идти?"
            biff "Да, цыпочка! Иди!"
            return
        "Уйти.":
            pass
    m "Я могу идти?"
    biff "Да, цыпочка! Иди!"
    return
