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
    music Groove2_85
    img 8268
    with fade
    m "Дорогуша, как у тебя дела?"
    img 8269
    secretary "..." #Сидит как истукан
    img 8270
    with fade
    m "Я знаю что на тебя сильно давит новый Босс."
    "Но, поверь, я скоро разберусь со всем этим!"
    img 8271
    secretary "Мистер Биф лучше нас знает что нам необходимо."
    secretary "Мистер Биф заботится о нас..."
    img 8272
    m "Что?"
    "Что ты такое говоришь, дорогуша???"
    img 8271
    with fade
    secretary "Мы должна благодарить Мистера Бифа что работаем у него..."
    img 8273
    m "Что они с тобой сделали???"

    sound beep1
    img 8274
    with fade
    #звук коммутатора
    pause 1.0
    biff "Эй! Сиська!"
    "Быстро зайди ко мне в кабинет!"
    "И захвати еще виски!!!"
    secretary "Да, Мистер Биф! Одну секунду!"

    music Funk_loop8
    img 8275
    with fade
    "Где же?!"
    "Где же виски???"
    img 8276
    with Dissolve(0.5)
    "Здесь нет!"
    "Он все выпил..."
    img 8277
    w
    sound highheels_short_walk
    img 8278
    with fade
    "Ах, я же спрятала еще бутылку здесь, чтобы он сразу не нашел..."
    sound highheels_run1
    img 8279
    with fade
    "Вот оно!"
    #Секретарша уходит, Моника смотрит на ее зад
    img 8280
    w
    img 8281
    with fade
    mt "О БОЖЕ!!!"
    "Бедняжка! Что они с тобой сделали?!?!"
    #пауза спустя 5 минут
    #Секретарша возвращается
    img black_screen
    with Dissolve(1.0)
    sound highheels_run1
    pause 2.0
    return

label ep22_dialogue6_2a:
    mt "Бедняжка! Что они с тобой сделали?!?!"
    return

label ep22_dialogue6_2:
    #render
    #Моника разговаривает с секретаршей повторно
    if act == "l":
        return

    $ store_music()
    music Stealth_Groover
    img 8282
    with fade
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
            with fade
            secretary "Миссис Бакфетт! Я пока не видела зарплаты здесь, после Вашего ухода..."
            #если у Моники меньше 5 долларов, то дает, иначе нет
            if money > 2:
                secretary "Поэтому у меня нет никаких денег сейчас, Миссис Бакфетт!"
                "Простите!"
                m "А как же Биф? Он что, не дает тебе деньги?"
                img 8285
                with fade
                secretary "Мистер Биф лучше нас знает что нам необходимо."
            else:
                #
                secretary "У меня есть только кредитная карточка, но мне надо платить за ипотечный кредит."
                "У меня есть $ 5 наличными и все..."
                m "Дорогуша, дай мне, пожалуйста, эти $ 5..."
                img 8286
                with fade
                secretary "Да, Миссис Бакфетт!"
                "Держите..."
                $ add_money(5)
                #дает 5 баксов

        "Дорогуша, ты не видела Мелани?" if melanieDisappeared == True:
            call ep23_dialogue9_5b() from _call_ep23_dialogue9_5b

        "Уйти.":
            m "Не переживай, дорогуша!"
            "Я скоро вернусь!"

    $ restore_music()
    return

label ep22_dialogue6_2b:
    if get_active_objects("Biff", scene="monica_office_cabinet") == False:
        if day_time == "day":
            if cloth == "Whore":
                #render
                img 8284
                secretary "Миссис Бакфетт!"
                "Мистера Бифа сейчас нет на месте!"
                img 8283
                m "Когда он будет?"
                img 8285
                secretary "Он сказал что будет вечером!"
                img 8284
                m "Хорошо, дорогая, спасибо."
            else:
                secretary "Миссис Бакфетт!"
                "Мистера Бифа сейчас нет на месте!"
                m "Когда он будет?"
                secretary "Он сказал что будет вечером!"
                "Но Вы знаете, он говорит что хочет и совершенно не обладает дисциплиной!"
                m "Хорошо, дорогая, спасибо."
            return False
        if day_time == "evening":
            if cloth == "Whore":
                #render
                img 8284
                secretary "Миссис Бакфетт!"
                "Мистера Бифа сейчас нет на месте!"
                img 8283
                m "Когда он будет?"
                img 8285
                secretary "Он сказал что будет завтра!"
                "Но Вы знаете, он говорит что хочет и совершенно не обладает дисциплиной!"
                img 8284
                m "Хорошо, дорогая, спасибо."
            else:
                secretary "Миссис Бакфетт!"
                "Мистера Бифа сейчас нет на месте!"
                m "Когда он будет?"
                secretary "Он сказал что будет завтра!"
                "Но Вы знаете, он говорит что хочет и совершенно не обладает дисциплиной!"
                m "Хорошо, дорогая, спасибо."
            return False
    return

label ep22_dialogue6_3:
    #render
    #Моника заходит регулярно к Бифу по работе
    menu:
        "Спросить о работе":
            pass
        "Биф, ты не видел Мелани?" if melanieDisappeared == True:
            call ep23_dialogue9_5c() from _call_ep23_dialogue9_5c
            return False
        "Уйти.":
            return False
    music Groove2_85
    img 8287
    with fade
    m "Биф..."
    "Я хотела узнать у тебя..."
    "Есть-ли еще работа?"
    img 8288
    "Мне нужны деньги..."

    call process_hooks("photoshoots_work_available_check", "global") from _call_process_hooks_31
    if biffWeeklyPhotoShootEnabled == False or _return == False:
        #Если не прошла неделя
        img 8289
        with fade
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
                with fade
                m "А если я пройду дополнительный кастинг?..."
                img 8292
                biff "Эта цыпочка пока слишком скучная для дополнительного кастинга!"
                "Я держу эту куклу только из-за того что она похожа на сучку Бакфетт!"
                "Иди и не отвлекай папочку! Ему нужно заботить о других цыпочках!"
                img 8290
                with fade
                mt "Я НЕНАВИЖУ ЭТОГО УРОДА!!!"
                "КОГДА Я ВЕРНУ СВОЕ МЕСТО НАЗАД?!?!"
                return False

    img 8293
    with fade
    biff "Да, цыпочка!"
    "Работа есть!"
    "Иди в студию!"

    if biffMonicaCastingsEnabled == True:
        $ notif(_("Моника заставляла моделей проходить обнаженный кастинг"))
        #если надо пройти кастинг
        img 8294
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
    if act=="l":
        return
    $ store_music()
    music Stealth_Groover
    img 6352
    with fade
    alex_photograph "Миссис Бакфетт!"
    "Здравствуйте!"
    img 6353
    m "Здравствуй, Алекс..."
    img 6354
    alex_photograph "Вы хотите сделать еще одну фотосессию?"
    menu:
        "Алекс... А где Мелани?" if monicaNeedToAskMelanieForHelp == True and day_time == "evening":
            call ep23_dialogues5_1() from _call_ep23_dialogues5_1
            return False
        "Алекс... А где Мелани?" if get_active_objects("Melanie", scene="monica_office_makeup_room") != False:
            call ep23_dialogues8_1() from _call_ep23_dialogues8_1
            return False
        "Алекс... А где Мелани?" if melanieDisappeared == True:
            call ep23_dialogue9_5a() from _call_ep23_dialogue9_5a
            return False
        "Пока нет...":
            pass
    m "Пока нет..."
    alex_photograph "Миссис Бакфетт! Приходите в любой момент!"
    img 6358
    "Я всегда рад фотографировать Вас!"
    img 6353
    mt "!!!"
    $ restore_music()
    return

label ep22_dialogue6_5:
    #render
    #Моника пришла к Алексу, фотосессия начинается
    if act=="l":
        return
    music Stealth_Groover
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
        "Алекс... А где Мелани?" if monicaNeedToAskMelanieForHelp == True and day_time == "evening":
            call ep23_dialogues5_1() from _call_ep23_dialogues5_1_1
            return False
        "Алекс... А где Мелани?" if get_active_objects("Melanie", scene="monica_office_makeup_room") != False:
            call ep23_dialogues8_1() from _call_ep23_dialogues8_1_1
            return False
        "Алекс... А где Мелани?" if melanieDisappeared == True:
            call ep23_dialogue9_5a() from _call_ep23_dialogue9_5a_1
            return False

        "Пока нет...":
            return False
    m "Да, Алекс..."
    "Еще одну..."
    img 8314
    mt "Дьявол! Не знаю куда эти грязные фотосессии меня заведут!"
    "Надо кончать с этим скорее!"

    img 6354
    with fade
    alex_photograph "Миссис Бакфетт!"
    "Вы уже знаете кем в каком наряде Вы будете сниматься в этот раз?"

    img 6353
    m "Еще не знаю..."
    "Что там Биф придумал на этот раз?"

    img 6527
    w
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
    with fade
    m "Я скоро вернусь!"

    img black_screen
    with Dissolve(1.0)
    sound snd_fabric1
    pause 2.0
    return

    # СТАРЫЙ КОНТЕНТ
    call ep22_photoshoot1() from _call_ep22_photoshoot1
    "Выберите наряд для фотосессии сегодня!"

    m "Я выбираю это..."
    #Если кастинг у Бифа
    menu:
        "Идти на кастинг к Бифу.":
            call ep22_dialogue6_6() from _call_ep22_dialogue6_6
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
    music Groove2_85
    img 8298
    with fade
    m "Биф! Я сделала фотосессию!"
    "Где мои деньги?"

    if monicaSaidBiffSheIsWillBeAGoodChick == True:
        #Если Моника хорошая цыпочка
        $ notif(_("Моника обещала быть хорошей цыпочкой."))
        biff "Только хорошие цыпочки получают деньги от папочки!"
        "Моника хорошая цыпочка?"
        menu:
            "Моника хорошая цыпочка...":
                pass
            "Уйти без денег...":
                music Power_Bots_Loop
                img 8290
                with fade
                mt "Я лучше уйду без денег, чем скажу это снова!!!"
                return False

        img 8299
        with fade
        m "Моника хорошая цыпочка."
        "Моника заслужила денежку..."
        mt "!!!"
        #иначе

    if monicaAskBiffGiftCertificateFirstTime == True:
        $ monicaAskBiffGiftCertificateFirstTime = False
        #Если первый раз
        img 8300
        with fade
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
    with fade

    #
    if photoShootDisabledNextWeek == True:
        img 8293
        with fade
        biff "Да, цыпочка!"
        biff "На следующей неделе я не нуждаюсь в твоих услугах!"
        biff "Приходи позднее!"
        img 8306
        music Power_Bots_Loop
        m "КАК?!!"
        m "Биф, но ты говорил что это регулярная работа!"
        img 8293
        with fade
        biff "Это регулярная работа, цыпочка. Но на следующей неделе ты мне не нужна."
        img 8295
        with fade
        mt "Дьявол! Где же я достану деньги для Виктории!"
        music Groove2_85
        img 8305
        with fade
        m "Биф, хорошо, но мне все-равно нужны деньги..."
        img 8294
        biff "Цыпочка! Ты начинаешь утомлять папочку!"
        biff "Тебя что-то не устраивает? Ты хочешь разорвать наше соглашение?"
        img 8287
        with fade
        m "Нет... Биф..."
        img 8288
        m "В этом нет... необходимости"

label ep22_dialogue6_7b:
    menu:
        "Ты что-то говорил по поводу работы в офисе?":
            img 8305
            with fade
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
            with fade
            biff "Но, может быть и не только личиком!"
            "Думаю многие партнеры готовы будут неплохо заплатить, чтобы запустить свои пальчики..."
            "В киску Моники Бакфетт!"
            "И не только пальчики!"
            "Ха-Ха-Ха!"
            "И все будут думать что ты настоящая!"
            img 8309
            mt "!!!"
            img 8308
            biff "Тебе это очень понравится!"
            "Ты будешь заниматься тем же самым чем занимаешься на улице сейчас..."
            "Только будешь значительно больше получать за это!"
            img 8310
            with fade
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
            with fade
            mt "!!!"
            m "Я могу идти?"
            biff "Да, цыпочка! Иди!"
            return True

        "Биф... Мог бы ты дать еще немного денег?":
            call ep23_dialogues1() from _call_ep23_dialogues1
            jump ep22_dialogue6_7b

        "Уйти.":
            pass
    img 8288
    m "Я могу идти?"
    biff "Да, цыпочка! Иди!"
    return True
