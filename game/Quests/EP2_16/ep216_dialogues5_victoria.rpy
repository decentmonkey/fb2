default melanieVictoriaMonicaTable1 = False  # Моника осудила Мелани в гостях у Виктории, воткнула в нее розу
default melanieVictoriaMonicaTable2 = False  # Моника попыталась оправдать Мелани перед Викторией



# при условии, что Мелани с Моникой уже были у Дика с телефоном Виктории
# офис, кабинет Моники
label ep216_dialogues5_victoria_1:
    # Моника заходит в свой кабинет, садится за стол
    # к ней подходит Юлия
    img 30586
    julia "Миссис Бакфетт..."
    # если у Моники отношения с Юлией
    #
    $ notif(_("Моника состоит с Юлией в отношениях."))
    #
    img 30587
    mt "Нет, только не это!"
    mt "Снова этой дурочке от меня что-то нужно!"
    mt "Сколько уже можно?!"
    mt "!!!"
    img 30588
    mt "Так, Моника, спокойно."
    mt "Помни о том, что ты с помощью этой никчемной Юлии обретешь свободу!"
    mt "И с каждым днем твоя цель все ближе!"
    img 30585
    m "Да, милая. Ты что-то хотела?"
    #
    # если у Моники нет отношений с Юлией
    img 20369
    mt "Чего она опять ко мне лезет?!"
    mt "Хочет пожаловаться, что у нее много работы?"
    mt "Никчемной, бесполезной и никому не нужной работы."
    mt "Какая же эта бывшая гувернантка жалкая!"
    img 30585
    m "Что?"
    #
    img 30627
    julia "Звонила Мисс Виктория..."
    julia "Просила передать Вам, что ждет Вас у себя."
    img 40265
    m "!!!"
    img 40266
    julia "И еще попросила сказать Вам, что Мелани уже у нее..."
    # у Моники шок
    img 40267
    m "!!!!!"
    mt "Твою мать!!!"
    # Юлия продолжает стоять рядом со столом Моники и умиляться Виктории
    img 40268
    julia "Ой, вам так повезло, Миссис Бакфетт, что Мисс Виктория Ваша подружка!"
    julia "Я когда-нибудь тоже хочу пойти в гости к ней!"
    julia "Она мне так нравится!"
    julia "Такая добрая и милая девушка!"
    # Моника зло смотрит на Юлию
    img 40269
    mt "Нашла добрую и милую девушку!"
    mt "Дура!!!"
    mt "!!!"
    # если у Моники отношения с Юлией
    #
    $ notif(_("Моника состоит с Юлией в отношениях."))
    #
    # притворно улыбается
    img 40270
    m "Да, милая. Виктория очень..."
    m "Кхм..."
    m "Очень милая девушка."
    m "Я рада, что ты с ней подружилась..."
    # Юлия игриво
    img 40271
    julia "А Вы возьмете меня с собой в гости к ней, Миссис Бакфетт?"
    m "Сейчас?"
    julia "Да! Ну пожалуйста, Миссис Бакфетт!"
    img 30634
    m "Нет, милая. Не сегодня. Как-нибудь в следующий раз..."
    # Юлия радостно
    img 40272
    julia "Правда?!"
    julia "Обещаете?!"
    # Моника сквозь зубы
    img 40273
    m "Конечно, милая."
    # Юлия довольно чмокает Монику в губы и уходит на свое рабочее место
    img 40274
    w
    img 40275
    w
    img 40276
    mt "ААААА!!!"
    mt "БЕСИТ!!!"
    mt "!!!"
    #
    # если у Моники нет отношений с Юлией
    # Моника рявкает на нее раздраженно
    img 40277
    m "Я сейчас поеду к Мисс Виктории."
    m "А ты иди работай!"
    m "Хватит болтать о всяких глупостях!"
    # Юлия испуганно
    img 40278
    julia "Д-да, Миссис Бакфетт..."
    img 22338
    # Юлия уходит на свое рабочее место
    #

    # Моника в панике
    img 40279
    mt "Эта белобрысая стерва будет мстить за наш разговор с Диком!"
    mt "!!!"
    mt "Что она задумала на этот раз?!"
    mt "?!?!?!"
    img 30587
    mt "Может, просто не ехать к ней?"
    mt "Скажу, что дурочка Юлия ничего мне не передавала..."
    mt "..."
    img 40280
    mt "Но ведь Мелани уже там!"
    mt "Если я не приеду, сучка Виктория разозлится еще больше!"
    mt "И тогда я даже боюсь представить, какие будут последствия!"
    mt "Дьявол!"
    $ log1 = _("Поехать к Виктории.")
    return

# Моника возле дома Виктории, глазик
label ep216_dialogues5_victoria_2:
    # не рендерить!!
    mt "Я даже думать боюсь о том, какой девичник приготовила эта белобрысая дрянь!"
    mt "Настанет тот день, Моника, когда ты избавишься от сучки Виктории!"
    mt "Это будет один из самых счастливых дней!"
    mt "Не могу дождаться этого момента!"
    mt "А пока я вынуждена терпеть ее присутствие в своей жизни..."
    mt "Иначе меня ждет кое-что похуже... О чем я боюсь даже думать..."
    return

# Моника в квартире Виктории, мысли, когда осматривается
#label ep216_dialogues5_victoria_3:
#    # не рендерить!!
#    mt "Это что, и есть логово белобрысой дьяволицы?!"
#    mt "Это что, шутка?!"
#    mt "Мягкие игрушки... Детские рисунки... Дик поэтому считает ее невинным ангелом?"
#    mt "Прямо сама невинность!"
#    mt "Меня тошнит от изобилия розового!"
#    mt "Фи! Какая безвкусица!"
#    return

# Моника заходит в квартиру Виктории
label ep216_dialogues5_victoria_4:
    # Виктория встречает Монику в холле, мило улыбается ей
    img 40514
    victoria "Ой, подружка Моника пришла!"
    victoria "Я так рада тебя видеть, подружка!"
    img 40515
    victoria "Я знаю, тебе очень хотелось попасть ко мне в апартаменты."
    victoria "И ты очень рада, что я тебя, наконец-то, пригласила."
    # Моника сквозь зубы
    img 40516
    m "Да... очень..."
    img 40517
    victoria "Что подружка делает, чтобы показать, как рада она меня видеть?"
    # Виктория показывает на свою щечку, Моника недовольно на нее смотрит
    m "..."
    menu:
        "Поцеловать Викторию.":
            pass
    # Моника наклоняется и чмокает Викторию в щеку, Виктория довольно хихикает
    img 40518
    w
    img 40519
    victoria "Ой, подружка, какая же ты милая!"
    victoria "Тебе нравится целовать меня, признайся. Хи-хи!"
    # Моника подозрительно смотрит на Викторию
    img 40520
    mt "Лучше не спорить с этой сучкой..."
    mt "Еще не время..."
    mt "И вообще, какая-то она слишком довольная..."
    mt "А где Мелани?"
    mt "???"
    img 40521
    m "Да... Мне нравится тебя целовать... Подружка..."
    img 40522
    victoria "Я знаю, подружка Моника."
    victoria "Ты ведь хорошая подружка, ты меня не расстраиваешь своим поведением."
    m "..."
    victoria "Ну что же ты стоишь возле двери? Проходи в гостиную!"
    # затемнение, звук каблуков
    # проходят через кухню
    img 40523
    victoria "Проходи, подружка Моника."
    img 40524
    mt "Неплохо устроилась эта белобрысая сикалявка!"
    mt "Наверное это Дик за все платит!"
    # смена кадра на гостиную
    # Моника заходит в гостиную, не сразу обращает внимание на стол
    img 40525
    victoria "Присаживайся за стол, подружка."
    victoria "Я хочу выпить с тобой вина..."
    # Виктория садится за стол, внутри которого голая Мелани
    # Моника обращает внимание на стол, она в шоке
    img 40526
    mt "!!!"
    mt "!!!!!"
    img 40527
    mt "О БОГИ!!!"
    mt "Мелани!!!"
    img 40528
    mt "Что?! Что этот дьявол в юбке с тобой сделал?!"
    mt "Что происходит?!"
    mt "?!?!?!"
    # Виктория самодовольно смотрит на реакцию Моники
    img 40529
    victoria "Ах да, подружка Моника, я совсем забыла сказать тебе..."
    victoria "Подружка Мелани пришла немного раньше тебя..."
    victoria "И мы с ней поиграли немного без тебя..."
    img 40530
    victoria "Надеюсь что ты не расстроишься из-за того, что не смогла поучавствовать?"
    victoria "Я ведь знаю ты так любишь наши маленькие дружеские игры!"
    # Моника в ступоре продолжает смотреть на Мелани
    img 40531
    mt "Если она так с Мелани..."
    mt "Что?.. Что эта дрянь приготовила для меня?!"
    mt "!!!"
    img 40532
    m "Н-немного?"
    victoria "Да, совсем чуть-чуть. Ты ведь не против?"
    victoria "Подружка Моника, так ты не будешь на меня обижаться, что я не подождала тебя?"
    # Виктория снова смотрит на Монику и протягивает ей бокал с вином
    # Моника берет его в руки
    img 40533
    w
    img 40534
    m "..."
    img 40535
    mt "Я не хочу ничего пробовать из рук этой твари..."
    mt "Нужно просто сделать вид, что я пью..."
    img 40536
    victoria "Я не слышу ответа, подружка..."
    victoria "Скажи мне, я хочу услышать."
    # Моника переводит взгляд на Викторию
    m "..."
    menu:
        "Я не против.":
            pass
    # Моника смотрит на Викторию с отвращением
    img 40538
    mt "Я хочу, чтобы она отстала от меня!"
    mt "Я хочу уйти отсюда! Поскорее!"
    img 40537
    mt "Мерзкая лицемерная тварь!"
    mt "Извращенка, которая прикидывается невинной девочкой!"
    mt "!!!"
    img 40539
    m "Я не обижаюсь... подружка..."
    m "Я не против, что вы... поиграли без меня..."
    # Виктория довольно хихикает, потом указывает на стол
    img 40540
    victoria "Подружка Моника хорошая."
    victoria "Присаживайся."
    # Моника садится на стул возле столика
    # Виктория садится на диван, смотрит вниз на Мелани, раздвигает ноги
    # Мелани сама, без приказа, начинает ей лизать
    img 40541
    w
    img 40542
    victoria "Смотри, теперь я разрешаю подружке Мелани ласкать меня, не спрашивая разрешения об этом..."
    w
    img 40543
    victoria "Она призналась мне, что ей это очень нравится."
    victoria "Хи-хи-хи!"
    img 40544
    w
    img 40545
    # Моника в шоке смотрит на Мелани
    img 40546
    mt "Боже! Какой кошмар!"
    mt "Что она с ней делала до моего прихода?!"
    mt "!!!"
    # Моника приближает бокал к губам, но не пьет его, потом просто держит в руке
    img 40547
    victoria "Как тебе мои апартаменты, подружка Моника?"
    img 40548
    mt "Отвратительно! Безвкусица!"
    mt "!!!"
    img 40549
    m "Здесь очень красиво... Подружка..."
    m "Я бы сказала, уютно..."
    img 40550
    victoria "Тебе правда нравится?"
    m "Да..."
    victoria "Ты хотела бы жить здесь?"
    m "Да..."
    img 40551
    victoria "Вместо меня?" # Виктория подозрительно
    img 40552
    m "Нннннет..."
    img 40553
    victoria "Хи-хи-хи!"
    victoria "Если знать, как правильно вести себя с Мистером Диком..."
    victoria "То он становится очень внимательным и щедрым."
    victoria "Подружка Моника, ты расстроена, что у тебя с Мистером Диком ничего не получилось?"
    img 40554
    m "..."
    img 40555
    victoria "Можешь не отвечать. Я знаю, что ты мне по-дружески завидуешь. Хи-хи-хи!"
    victoria "Кстати, о дружбе и о Мистере Дике..."
    img 40556
    mt "Черт!"
    mt "!!!"
    img 40557
    victoria "Я считаю, что подружка Мелани поступила не совсем по-дружески..."
    victoria "Когда попыталась показать Мистеру Дику то видео на моем телефоне..."
    victoria "Но я все-же считаю, что подружка Мелани - хорошая подружка."
    victoria "Она просто ошиблась."
    victoria "Ты согласна со мной, подружка Моника, что Мелани ошиблась?"
    # Моника растерянно молчит
    img 40558
    m "..."
    # Виктория наигранно
    img 40559
    victoria "Ой, подружка Моника, это так невежливо с моей стороны!"
    victoria "Я забыла тебя спросить, не хочешь ли ты присоединиться к подружке Мелани?"
    img 40560
    m "Присо... Что?!"
    # кадр на Мелани
    img 40561
    m "!!!"
    m "О, нет-нет!"
    m "Спасибо, мне тут удобно!"
    # Виктория ехидно улыбается и выжидательно смотрит на Монику
    img 40562
    victoria "Ну так что ты скажешь, подружка Моника?"
    victoria "Мелани совершила ошибку? Или ты считаешь иначе?"
    # Моника испуганно смотрит на Мелани
    img 40563
    m "..."
    menu:
        "Сказать, что Мелани совершила ошибку.":
            pass
    img 40564
    mt "Дьявол!"
    mt "Ведь я была вместе с Мелани!"
    mt "Какой кошмар!"
    img 40565
    mt "Что же теперь ожидает меня?!"
    mt "!!!"
    mt "Лучше будет, если я не буду злить эту мерзкую дрянь Викторию!"
    img 40566
    m "Я считаю..."
    m "Я считаю, что Мелани ошиблась..."
    # Виктория самодовольно улыбается, поднимает бокал и протягивает его Монике, чтобы чокнуться
    # Моника тоже тянет бокал
    img 40567
    victoria "За женскую дружбу, подружка Моника!"
    # чокаются
    victoria "Я уверена, что подружка Мелани осознает свою ошибку..."
    victoria "И больше она не будет огорчать меня..."
    img 40566
    m "Д-да..."
    # Виктория опускает взгляд на Мелани, та все продолжает лизать
    img 40569
    victoria "Жаль, что она не может к нам присоединиться..."
    img 40570
    m "..."
    img 40571
    victoria "Кстати, подружка Мелани настолько хочет снова стать хорошей..."
    victoria "Что попросила у меня разрешения..."
    victoria "Быть допущенной не только до моей киски, но и до моей попы."
    #
    $ notif(_("Виктория говорила, что Мелани допущена только до ее киски, а Моника допущена только до ее попы."))
    #
    img 40572
    victoria "Но ведь моя попа только для тебя, подружка Моника..."
    victoria "И я думаю, что же мне делать."
    victoria "Если я допущу подружку Мелани не только до моей киски, но и до попы..."
    img 40573
    victoria "То тебе, подружка Моника, ничего не останется..."
    victoria "А ты так любишь мою попу..."
    victoria "Ведь это так, подружка?"
    img 40574
    m "..."
    menu:
        "Да, это так.":
            pass
    img 40575
    m "Да..."
    victoria "Что 'да'? Скажи мне. Я хочу это услышать от тебя."
    img 40576
    mt "Гребаная сучка!"
    mt "Ненавижу!!!"
    mt "!!!"
    img 40577
    m "Я... Мне нравится твоя... Твоя попа..."
    # Виктория хихикает довольно
    img 40578
    victoria "Хи-хи!"
    victoria "Да, я знаю, подружка..."
    victoria "Ты очень любишь мою попу."
    victoria "И ты специально опаздываешь с сертификатами, чтобы почаще вылизывать прощение у меня."
    img 40579
    victoria "Но, если я допущу подружку Мелани до моей попы..."
    victoria "Тогда ты не сможешь больше быть моей подружкой."
    victoria "Тебе ничего не останется, чем подтверждать нашу дружбу."
    # Моника с непониманием смотрит на нее
    img 40580
    mt "Что она хочет этим сказать?!"
    mt "Чего эта дрянь добивается?!"
    img 40581
    victoria "Скажи мне, подружка, допустить ли мне подружку Мелани к моей попе?"
    victoria "Или она не настолько хорошая подружка, чтобы заслуживать такую привилегию?"
    # Моника смотрит на нее пристально
    img 40582
    mt "Вот черт!"
    mt "Эта белобрысая тварь пытается настроить Мелани против меня!"
    mt "Она хочет сделать так, чтобы мы больше не действовали сообща!"
    mt "Мерзкая, грязная извращенка!"
    mt "!!!"
    img 40583
    victoria "Ну, что скажешь, подружка Моника?"
    victoria "Я жду твоего ответа."
    # Моника в растерянности
    img 40584
    m "..."
    menu:
        "Сказать, что Мелани не настолько хорошая подружка.":
            pass
    img 40585
    mt "Если я ей скажу, чтобы она допустила Мелани до своего мерзкого тощего зада..."
    mt "То я рискую стать плохой подружкой."
    mt "А это значит... Дьявол! Не хочу даже представлять последствия!"
    mt "!!!"
    img 40586
    mt "Твою мать! Моника, эта мелкая сучка вынуждает сказать это!"
    mt "Думаю, Мелани поймет меня..."
    mt "Нужно будет обязательно поговорить с ней об этом. Позже."
    
    m "Я думаю, что..."
    m "Что подружка Мелани не настолько хорошая."
    m "И что она не может быть допущена до твоей попы... Подружка..."
    # Виктория довольно хихикает и смотрит на Мелани
    victoria "Хорошо, подружка Моника, я прислушаюсь к твоему совету."
    victoria "Хи-хи-хи!"
    victoria "Кстати, забыла спросить тебя..."
    victoria "Тебе нравится, как я украсила стол к твоему приходу?"
    victoria "Я старалась для своей хорошей подружки Моники."
    victoria "Эта роза... Мне настолько понравился ее запах, что я даже решила украсить ею стол. Хи-хи!"
    # Моника смотрит на торчащую попу Мелани с цветком
    victoria "Тебе нравится, подружка Моника?"
    m "Д-да..."
    victoria "Я вижу, что ты тоже хочешь понюхать эту розу."
    victoria "Я разрешаю хорошей подружке Монике взять ее в руку и понюхать."
    m "Ч-что?.."
    victoria "Возьми розу и понюхай ее, подружка. Ты можешь не стесняться и делать то что хочешь."
    # Моника медлит, в недоумении смотрит на розу
    m "..."
    menu:
        "Взять розу из попы Мелани.":
            pass
    mt "Я что, должна вытащить розу оттуда?!"
    mt "Это... Это просто отвратительно!"
    mt "!!!"
    mt "Что у нее в голове творится?!"
    mt "Как вообще можно додуматься до ТАКОГО?!"
    mt "И Я вынуждена слушать эту гребаную больную извращенку!!!"
    mt "ААА!!!"
    # Моника протягивает руку и вытаскивает розу, подносит ее к своему лицу
    victoria "Тебе нравится ее аромат, подружка Моника?"
    m "Нравится..."
    victoria "Скажи подружка, ты осуждаешь Мелани за ее ошибку?"
    victoria "Ты считаешь, что такая хорошая подружка, как ты, никогда бы не совершила подобное?"
    m "Я..."
    mt "Дьявол! Меня слышит Мелани!"
    mt "Мы были там вместе!"
    mt "Что же мне сказать?"
    mt "???"
    victoria "Если подружка осуждает Мелани, то она может вернуть розу на место..."
    victoria "Чтобы снова украсить ею стол..."
    m "!???!?"
    menu:
        "Осудить Мелани и воткнуть розу обратно.": # пункт доступен при высокой бичности
            mt "Да, мы были там вместе с Мелани, но это была ее идея."
            mt "Это ее провал и я не хочу отвечать за него!"
            mt "!!!"
            m "Я считаю, что Мелани поступила неправильно."
            m "И осуждаю ее."
            # чпок, вставляет розу назад (показать Мелани лицо)
            melanie "!!!"
            # Виктория довольно
            victoria "Хорошая подружка!"
            victoria "Наш девичник закончен и мои подружки могут идти."
            victoria "Только..."
            victoria "Подружка Моника, тебе не кажется, что стол будет выглядеть..."
            victoria "Не очень красиво без такой чудесной вазы под цветок?"
            m "Да, кажется..."
            victoria "Ты разрешишь мне оставить подружку Мелани еще немного?"
            m "..."
            menu:
                "Разрешить Виктории оставить Мелани у себя.":
                    pass
            # Моника смотрит на Мелани
            mt "Черт! Черт! Черт!"
            mt "Мне потом нужно будет обязательно поговорить с Мелани!"
            mt "Она должна понять меня!"
            mt "Я ведь просто стараюсь не злить сучку Викторию!"
            mt "Я это делаю не только ради себя..."
            mt "Но и ради нее!"
            m "Разрешаю..."
            victoria "Хи-хи-хи!"
            # затемнение
            # смена кадра, холл, Виктория провожает Монику
            # Виктория ехидно смотрит на нее
            victoria "Я рада, что моей хорошей подружке Монике понравился мой девичник."
            victoria "И что она не обижается на то, что я немного поиграла с подружкой Мелани без нее."
            victoria "Но ты не расстраивайся, подружка Моника..."
            victoria "Мы с тобой еще поиграем..."
            victoria "Не сегодня, но уже совсем скоро, подружка."
            m "!!!"
            # Виктория ехидно улыбается, Моника испугано смотрит на нее
            # затемнение
            $ melanieVictoriaMonicaTable1 = True # Моника осудила Мелани в гостях у Виктории, воткнула в нее розу
            # дается bitchiness

        "Аккуратно положить розу рядом.":
            mt "Мелани все слышит."
            mt "Мы были там вместе и я не могу осудить ее, когда она в таком положении!"
            m "Я считаю, что Мелани хорошая подружка."
            m "Думаю, ей можно простить небольшую ошибку..."
            m "..."
            m "Эта роза стояла неровно, вот так она выглядит гораздо эстетичнее..."
            # Моника кладет розу рядом с Мелани на стол
            victoria "Я тоже решила дать подружке Мелани еще один шанс..."
            # подозрительно
            victoria "Хорошо, подружка Моника..."
            m "..."
            victoria "Наш девичник закончен и мои подружки могут идти."
            # затемнение
            # смена кадра, холл, Виктория провожает Мелани и Монику
            # Мелани подавлена, молчит
            victoria "Я рада, что моим подружкам понравился мой девичник."
            # смотрит на Мелани
            victoria "Ведь это так, подружка Мелани?"
            # Мелани отвечает безразлично
            melanie "Да, подружка."
            victoria "Хи-хи-хи!"
            # смотрит на Монику
            victoria "Также я рада, что подружка Моника не обижается на то..."
            victoria "Что я немного поиграла с подружкой Мелани без нее."
            victoria "Но ты не расстраивайся, подружка Моника..."
            victoria "Мы с тобой еще поиграем..."
            victoria "Не сегодня, но уже совсем скоро, подружка."
            m "!!!"
            # Виктория ехидно улыбается, Моника испугано смотрит на нее
            # затемнение
            $ melanieVictoriaMonicaTable2 = True # Моника попыталась оправдать Мелани перед Викторией
    # Виктория продолжает ехидничать с Моникой
    victoria "Кстати, подружка Моника..."
    victoria "Я забыла тебе сказать, что мне нравится твое платье."
    # Моника смотрит на нее удивленно
    m "???"
    victoria "Я бы хотела дальше подружку Монику видеть в нем в моих апартаментах."
    victoria "Так как здесь приличный район. Хи-хи!"
    victoria "Но в офис Мистера Дика приходи в той забавной одежде."
    victoria "Я бы не хотела, чтобы Мистер Дик видел тебя какой-то другой."
    # Моника злобно на нее смотрит
    m "Хорошо... Подружка..."
    m "!!!"
    return

# Моника вышла от Виктории, на улице, глазик
# если она осудила Мелани, стоит на улице одна
label ep216_dialogues5_victoria_5:
    # не рендерить!!
    mt "О Боже!"
    mt "Так неудобно получилось с Мелани, но неизвестно, чем бы это закончилось..."
    mt "В конце концов, это ее ошибка!"
    mt "Эта сучка Виктория настоящая извращенка!"
    mt "Притом больная на всю голову!"
    mt "!!!"
    mt "Она заставила меня сказать, что Мелани совершила ошибку..."
    mt "И что она не хорошая подружка!"
    mt "Но ведь я была у Дика вместе с Мелани!!!"
    mt "Я почти уверена, что эта сикалявка просто так мне это не простит!"
    mt "Чего мне теперь ожидать от нее?!"
    mt "Я не хочу, чтобы она втыкала розу в мою... Мою попу!"
    mt "Это! Это мерзко!"
    mt "Отвратительно!!!"
    mt "Унизительно!!!"
    mt "!!!"
    return

# Моника вышла от Виктории, на улице
# если она попыталась оправдать Мелани, они стоят на улице вдвоем
label ep216_dialogues5_victoria_6:
    # не рендерить!!
    m "Мелани, что эта сучка Виктория сделала с тобой?!"
    m "Она настоящая извращенка!"
    m "Притом больная на всю голову!"
    m "!!!"
    melanie "Миссис Бакфетт, давайте обсудим все позже..."
    melanie "Я сейчас не хочу говорить об этом."
    melanie "Мне... Мне нужно скорее идти..."
    return

# при клике на Мелани после сцены у Виктории дома
label ep216_dialogues5_victoria_7:
    # не рендерить!!
    melanie "Миссис Бакфетт, давайте обсудим все позже..."
    melanie "Сейчас я хочу побыть одна..."
    return

# Моника пытается войти в офис Дика НЕ в одежде шлюхи
label ep216_dialogues5_victoria_8:
    # не рендерить!!
    mt "Я не могу пойти к сучке Виктории в таком виде."
    mt "Она мне сказала, чтобы я приходила сюда только в той кошмарной одежде шлюхи!"
    return
