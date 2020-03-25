default monicaEscortAngryWife1 = False  # Моника согласилась раздеться и лечь на пуф
default monicaEscortAngryWife2 = False  # Моника согласилась дрочить клиенту


# при выборе пункта меню "Встреча с клиентом (сцена)" (лейбл ep211_escort_scene1_1a), подпункт "Клиент в номере отеля"

# Моника сидит за столиком в ожидании клиента
label ep212_dialogues3_escort_hotel_1:
    # по возможности использовать имеющиеся арты
    mt "Моника, до сих пор не могу поверить, что ты этим занимаешься..."
    mt "Моника Бакфетт, леди из высшего общества..."
    mt "Сидит за столиком в каком-то никчемном ресторане и ждет клиента..."
    mt "Неужели для тебя это теперь в порядке вещей?"
    mt "..."
    mt "С другой стороны, здесь можно неплохо заработать."
    mt "А мне нужны деньги."
    mt "..."
    mt "Это делает не Моника Бакфетт, это делает [monica_hotel_name]."
    mt "Для нее - это норма. А деньги достанутся мне!"
    mt "..."
    mt "Да уж, Моника..."
    mt "Так и до биполярного расстройства недалеко..."
    # подходит официантка
    waitress "Здравствуйте, Мэм! Администратор Вас ждет на ресепшене."

    #
    $ notif(_("У Моники хорошие отношения с официанткой."))
    #
    mt "Черт!"

    # если была сцена с выездом к клиенту Нэду
    mt "Надеюсь, это не выезд к клиенту в какой-нибудь гостевой дом..."
    mt "Где его друзья с женами..."
    m "Я сейчас подойду к ней."

    # официантка уходит

    #
    $ notif(_("У Моники плохие отношения с официанткой."))
    #
    mt "Снова она!"
    m "Что?"
    waitress "Мэм... Вас администратор попросила позвать к себе..."
    waitress "Обычно она так зовет к себе проститу... Кхм... Девочек из эскорта..." # подозрительно
    # Моника перебивает ее
    m "Меня не интересует, что в вашем никчемном ресторане обычно происходит!"
    m "Я не собираюсь выслушивать всякие глупости от какой-то официантки!"
    # официантка уходит
    $ log1 = _("Пойти на ресепшн к администратору.")
    return

# ресепшн
label ep212_dialogues3_escort_hotel_2:
    # Моника приходит на ресепшн
    # там стоит девочка из эскорта (брюнетка, карэ) и администраторша
    # они смотрят на Монику
    reception "[monica_hotel_name], есть работа."
    reception "Иди и надень что-нибудь подходящее из белья."
    reception "И быстро. Там клиентка торопится. И нервничает."
    m "Клиентка?"
    m "???"
    reception "Да. То есть, не совсем."
    reception "Это муж с женой.У них там в номере семейная сцена."
    reception "Никто из девочек не хочет идти туда."
    reception "Поэтому пойдете вы вдвоем."
    reception "И сделаете все, как надо!"
    reception "Клиент должен остаться доволен вашей работой!"
    # брюнетка возмущенно, указывая на Монику
    girl_1 "Пусть эта идет одна!"
    girl_1 "Я не пойду никуда!"
    reception "Так, тихо!"
    reception "Это твой постоянный клиент, поэтому ты пойдешь вместе с [monica_hotel_name]."
    m "Зачем тогда мне идти в этот номер, если это ее клиент?"
    reception "[monica_hotel_name]!"
    reception "Потому что Я сказала тебе идти туда!"
    reception "Сейчас же прекратите спорить и идите переодеваться!"
    reception "Чтобы через 5 минут были в номере!"
    # Моника с брюнеткой недовольно смотрят друг на друга
    m "!!!"
    girl_1 "!!!"
    reception "Поторопитесь!"
    # затемнение, прошло 5 мин, Моника и брюнетка идут из служебного коридора
    # у Моники под платьем видно белье
    # обе недовольно косятся друг на друга
    return

# номер отеля
label ep212_dialogues3_escort_hotel_3:
    # Моника с брюнеткой заходят в номер и стоят возле двери
    # семейная пара стоит посреди номера
    # женщина зло смотрит на вошедших девушек
    # мужчина стоит, скукожившись, видно, что боится ее
    wife "Ага!"
    wife "Вот они!"
    wife "!!!"
    wife "Смотри, сволочь, потаскушки твои пришли!"
    husband "Д-дорогая, п-прошу тебя..."
    wife "МОЛЧАТЬ!!!" # в сторону мужа
    wife "!!!"
    # снова смотрит на девушек
    wife "Смотри-ка, как разрядились!"
    wife "У вас обеих прямо на лбу написано, чем вы зарабатываете!"
    wife "!!!"
    # Моника в шоке смотрит на нее
    mt "Боже!"
    mt "Какая-то провинциальная дура, а строит из себя..."
    mt "Кто она такая, чтобы разговаривать в таком тоне?!"
    mt "Если бы не долбанные правила ВИП-эскорта, я быстро поставила бы ее на место!"
    mt "!!!"
    # жена пристально рассматривает девушек, потом поворачивается к мужу (девушек она не видит при этом)
    wife "Ну?! Чего ты молчишь?!"
    wife "Говори, к кому из них ты постоянно бегаешь, а?!"
    # муж смотрит на брюнетку, потом на Монику
    husband "Я..."
    wife "Говори, сволочь неблагодарная!"
    # Моника спокойна, ведь это не ее постоянный клиент
    # брюнетка заметно нервничает
    mt "Хорошо, что это не мой клиент."
    mt "Сейчас этой сучке из эскорта достанется!"
    mt "А я уйду отсюда."
    mt "И мне не приется иметь дела с этой мерзкой провинциалкой."
    husband "Я... Ходил..."
    # Моника смотрит на брюнетку насмешливо, та поворачивается к Монике
    m "У кого-то из нас сегодня будет проблемный клиент..."
    m "И это уж точно буду не я."
    # брюнетка смотрит на нее зло и отворачивается
    girl_1 "!!!"
    # брюнетка, пока жена на них не смотрит, шепчет угрожающе мужу
    girl_1 "Только попробуй ей сказать правду!"
    girl_1 "!!!"
    girl_1 "Я расскажу ей все твои грязные фантазии!"
    girl_1 "Молчи!"
    girl_1 "!!!"
    # Моника видит это, и продолжает злорадствовать
    mt "Можно подумать, такой жалкий запуганный неудачник сможет соврать этой злобной мегере!"
    mt "!!!"
    husband "Я... Ходил... К..."
    girl_1 "Молчи!"
    girl_1 "!!!"
    # жена дает ему подзатыльник, у него очки немного сползают с носа и сидят криво
    wife "Говори, скотина! Не скажешь ты, я у администратора сама узнаю!"
    wife "!!!"
    husband "Я ходил к... к ней..."
    # указыват пальцем на Монику
    m "ЧТО?!"
    m "Это неправда!!!"
    m "!!!"
    # брюнетка ехидно улыбается
    m "Я его первый раз вижу!"
    m "!!!"
    # жена смотрит на Монику презрительно
    wife "Молчи!"
    wife "Продажная девка!"
    wife "Чтобы я от тебя ни слова не слышала!"
    wife "!!!"
    m "!!!"
    mt "Да как она смеет?!"
    mt "!!!"
    # Моника переводит взгляд на мужа, тот стоит, потупив глаза
    mt "?!?!?!"
    mt "Жалкий никчемный неудачник!"
    mt "!!!"
    # жена встает, руки в боки
    wife "Так!"
    wife "Ты раздеваешься и ложишься сюда!" # отдает Монике приказ и указывает на пуф возле кровати
    mt "!!!"
    wife "А ты стоишь на месте! И ни звука!" # брюнетке
    girl_1 "..."
    # затем смотрит на мужа
    wife "И ты, сволочь, раздевайся! Чего стоишь?!"
    husband "Н-но... Дорогая... З-зачем?"
    wife "Покажешь мне, как ты делал с ней ЭТО!"
    husband "В с-смысле?.." # испуганно
    wife "Я посмотрю, как ты с ней трахаешься, козел!"
    husband "Н-но..."
    wife "Я сказала раздевайся! Быстро!!!"
    wife "А ты чего стоишь?! Не слышала, что тебе сказано делать?!"
    wife "Я деньги за что заплатила, а?!"
    wife "Отрабатывай!"
    # Моника медлит
    mt "..."
    menu:
        "Сказать правду и уйти отсюда!":
            # Моника возмущенно
            mt "Это несправедливо!"
            mt "Пусть эта сучка с эскорта с ними сама разбирается!"
            mt "!!!"
            # указывает на брюнетку
            m "Это ее клиент!"
            m "Твой муж тебе солгал, чтобы ее защитить!"
            m "Я его вообще перый раз в жизни вижу!"
            girl_1 "!!!"
            wife "Так, ну-ка быстро говори мне правду, козел!" # мужу
            wife "!!!"
            husband "П-прости, д-дорогая..."
            husband "Я... П-просто перепутал..."
            mt "Сборище жалких неудачников!!!"
            mt "!!!"
            # Моника уходит
            return
        "Сделать, как требует клиент.":
            $ monicaEscortAngryWife1 = True # Моника согласилась раздеться и лечь на пуф
            pass
    mt "Дъявол!"
    mt "Что же мне делать?"
    mt "Эта сучка с эскорта! Ненавижу ее!!!"
    mt "!!!"
    mt "Но если я попытаюсь сказать правду этой провинциальной дуре, она мне не поверит..."
    mt "..."
    mt "А если я сейчас откажусь, то меня уволят с этой работы..."
    mt "А мне нужны деньги..."
    mt "..."
    # жена рявкает на Монику
    wife "Я долго должна ждать?!"
    wife "Я заплатила за час, уже итак много времени прошло!"
    wife "Давай, пошевеливайся!"
    mt "Черт! Для [monica_hotel_name] это обычные рабочие будни."
    mt "Просто очередной неудачник..."
    mt "..."
    mt "Зато [monica_hotel_name] сегодня сможет заработать."
    # смена кадра, платье Моники лежит на полу, она стоит в одном нижнем белье возле пуфа
    # муж стоит рядом в одном галстуке и ботинках, прикрывая свои причиндалы
    wife "Ну, приступайте!"
    wife "Я вам все рассказывать должна, что делать надо?!"
    mt "..."
    # Моника опирается руками и коленями на пуф
    # муж в ужасе смотрит на нее
    husband "Д-дорогая, д-давай пойдем домой..."
    husband "Т-там и п-поговорим."
    husband "П-пойдем, а?"
    wife "А ну-ка замолчи!"
    wife "Давай, покажи мне, чем ты занимаешься!"
    wife "Когда врешь мне, что ты допоздна на совещании!"
    wife "Сволочь!"
    mt "Скорее бы это закончилось!"
    mt "Кошмар!"
    husband "Д-дорогая..."
    husband "М-можно я не буду этого делать?"
    wife "Нет! Ты сделаешь сейчас это!!!"
    husband "Н-но..."
    husband "У меня не с-стоит..."
    # разводит руки в стороны и показывает свой грустный член
    wife "!!!"
    # жена зло смотрит на него, потом говорит Монике
    wife "Ты, шлюха!"
    wife "Давай, делай свою работу!"
    wife "Поднимай его!"
    mt "..."
    menu:
        "Сказать правду и уйти отсюда!":
            # Моника возмущенно
            mt "С меня хватит!"
            mt "Пусть эта сучка с эскорта с ними сама разбирается!"
            mt "!!!"
            # указывает на брюнетку
            m "Это ее клиент!"
            m "Твой муж тебе солгал, чтобы ее защитить!"
            m "Я его вообще перый раз в жизни вижу!"
            girl_1 "!!!"
            wife "Так, ну-ка быстро говори мне правду, козел!" # мужу
            wife "У тебя поэтому не встает на эту шлюху?"
            husband "П-прости, д-дорогая..."
            husband "Я... П-просто перепутал..."
            mt "Сборище жалких неудачников!!!"
            mt "!!!"
            # Моника уходит
            return
        "Сделать, как требует клиент.":
            $ monicaEscortAngryWife2 = True # Моника согласилась дрочить клиенту
            pass
    mt "Жена - дрянь!"
    mt "Муж - жалкий неудачник!"
    mt "Ненавижу их!"
    mt "!!!"
    # Моника садится на пуф, он стоит рядом, она ему дрочит
    wife "Ну же, шлюха!"
    wife "Через тебя в день десятки членов проходит!"
    wife "Ты что, не можешь справиться с этим?!"
    wife "Или у нормальных мужиков на такую грязную шлюху, как ты, не встает?!"
    wife "Старайся лучше!"
    mt "Никчемная мерзкая дура!!!"
    mt "!!!"
    # Моника продолжает работать рукой и у него приподнимается
    wife "Да неужели!"
    wife "Шлюха встает в позу!"
    wife "А ты, сволочь, быстро засовывай в нее член, пока он не упал снова!"
    # Моника встает снова на пуф, муж пристраивается сзади и пытается засунуть полуэрогированный член в нее
    # у него ничего не получается
    husband "Д-дорогая..."
    husband "У м-меня все равно н-не получается..."
    husband "Д-давай, п-прекратим это?"
    wife "Засунь!"
    wife "В нее!"
    wife "Свой член!!!"
    wife "!!!"
    # он снова пытается войти в нее
    husband "Ч-черт..."
    husband "Ну же..."
    # брюнетка стоит в стороне и усмехается, Моника видит это
    mt "Сучка!"
    mt "!!!"
    # наконец, у него получается и он входит в Монику
    wife "Давай, кобель, покажи как ты это делаешь!"
    wife "!!!"
    wife "Что эта грязная потаскуха делает такого, что ты к ней бегаешь?!"
    wife "И тратишь на это наши деньги!"
    wife "!!!"
    # муж шпилит Монику, брюнетка с женой наблюдают
    husband "Д-дорогая, м-может этого д-достаточно?"
    wife "Нет, сволочь! Продолжай!"
    # жена подходит с другой стороны, так чтобы смотреть на лицо Моники
    wife "Ты - падшая грязная женщина!"
    wife "Тебе не противно от самой себя?!"
    # Моника зло смотрит, но молчит
    mt "!!!"
    wife "Молчишь?"
    wife "Ты хоть помылась после предыдущего клиента, шлюха?"
    # жена смотрит на мужа
    wife "Ну и что, кобель?!"
    wife "Тебе нравится?!"
    # тот продолжает секс
    husband "Н-нет, дорогая..."
    husband "М-мне с-совсем не н-нравится..."
    wife "..."
    wife "Скажи мне, кто лучше?"
    wife "Эта грязная шлюха или я?"
    husband "К-конечно же ты, л-любимая..."
    husband "Т-ты лучше в-всех..."
    wife "С кем тебе больше нравится, сволочь?!"
    husband "М-мне нравится т-только с тобой, д-дорогая..."
    husband "Т-ты самая л-лучшая..."
    husband "М-может, достаточно уже? Д-дорогая..."
    wife "Нет, кобель!"
    wife "!!!"
    wife "Давай, трахай эту дрянь!"
    wife "Я хочу увидеть, насколько она тебе 'не нравится'!"
    # жена снова смотрит на Монику
    wife "Ну что, шлюха?!"
    wife "Тебе нравится?!"
    wife "Отвечай!"
    # Моника зло смотрит на нее
    mt "Черт!"
    mt "И что мне ответить этой дуре?!"
    mt "Чтобы она отвязалась от меня!"
    mt "!!!"
    menu:
        "Да, нравится.":
            mt "Да..."
            mt "Мне нравится..."
            wife "Я и не ожидала другого ответа от такой падшей женщины!"
            wife "!!!"
            wife "Спать с чужими мужьями, да еще и брать за это деньги!"
            wife "И как тебе не стыдно после этого мне в глаза вообще смотреть!"
            wife "Дрянь!"
            wife "!!!"
            mt "Дура!"
            mt "!!!"
            pass
        "Не нравится.":
            mt "Нет..."
            mt "Мне не нравится..."
            wife "Смотри, кобель!"
            wife "Ты ее трахаешь! Даешь ей за это деньги!"
            wife "А ей еще и не нравится!!!"
            wife "Вот к такой грязной и бессовестной шлюхе ты бегал все это время?!"
            wife "!!!"
            mt "Дура!"
            mt "!!!"
            pass
    # Моника зло смотрит на жену, муж делает еще несколько движений и кончает
    menu:
        "Кончить внутрь Моники.":
            husband "Ах..."
            husband "Аааах..."
            pass
        "Кончить на попу Моники.":
            husband "Ах..."
            husband "Аааах..."
            pass
    mt "Наконец-то, это безумие закончилось!"
    mt "Теперь эта провинциальная дура довольна?!"
    mt "Сняла мужу эскортницу, чтобы посмотреть, как он занимается с ней сексом!"
    mt "Идиотка!"
    mt "!!!"
    # муж испуганно смотрит на жену
    wife "Раз ты кончил, сволочь, значит тебе понравилось!"
    husband "Н-нет... Я..."
    wife "Ты мне врал, что она тебе не нравится!"
    husband "Я нечаянно, д-дорогая..."
    husband "П-прости..."
    wife "!!!"
    wife "Быстро оделись! Оба!"
    # затемнение
    return

# ресепшн
label ep212_dialogues3_escort_hotel_4:
    # китаянка стоит за стойкой ресепшена, вся наша компания стоит перед стойкой
    # жена такая же злая, муж зашуганный, брюнетка довольная собой, Моника злая
    wife "Эта ваша проститутка ни на что не годна!"
    wife "Не понятно, за что я должна вообще платить?!"
    wife "Она что, член впервые в жизни видит?!"
    wife "Вы ее как на работу взяли?!"
    reception "Что случилось?"
    wife "У моего мужа не встал на нее!"
    wife "Мало того! Она еще и не смогла ничего сделать с этим!"
    wife "!!!"
    # админ спрашивает у брюнетки, та скажет, что да, не встал у него
    reception "У него и правда ничего не получилось?"
    girl_1 "Да, у него не встал."
    # Моника в шоке
    m "Что?!"
    m "Это..."
    # Моника пытается возразить, но жена на нее рявкает
    wife "Заткнись!!!"
    wife "!!!"
    # Моника испепеляет взглядом брюнетку
    mt "Вот дрянь!"
    mt "!!!"
    # админ недовольно смотрит на Монику, потом снова спрашивает у брюнетки
    reception "[monica_hotel_name] вообще отказалась работать?"
    girl_1 "Она старалась что-то сделать..."
    girl_1 "Но у нее ничего не получилось..."
    girl_1 "Просто зря потратила время клиентов."
    mt "!!!"
    # админ обращается к клиентке
    reception "Я приношу извинения от лица нашей организации."
    reception "Так как услуга не была вам оказана, то я верну вам деньги."
    wife "Хорошо." # недовольно
    wife "А с этой что будете делать?"
    reception "Я приму необходимые меры в отношении [monica_hotel_name]."
    reception "Она будет наказана."
    mt "!!!"
    reception "Я ее оштрафую за ненадлежащее исполнение своих обязанностей."
    m "Оштрафуешь?!"
    m "Но..."
    wife "Молчать!!!"
    mt "!!!"
    wife "Ну что, грязная шлюха?"
    wife "Ты все поняла?!"
    wife "Больше не будешь с ним спать?!"
    # Моника со злостью
    m "Не буду!"
    m "!!!"
    # переводит взгляд на брюнетку, та стоит, подмигивает мужу и ехидно улыбается
    # занавес
    return

# ресепшн
# компания разошлась, Моника одна с админом
label ep212_dialogues3_escort_hotel_5:
    reception "[monica_hotel_name]!"
    reception "Мне пришлось вернуть деньги клиентке!"
    reception "Это недопустимо!!!"
    reception "Какого черта, [monica_hotel_name]?!"
    m "Все было совсем не так!"
    m "Эта..."
    reception "Я не очу слышать никаких глупых оправданий!"
    reception "Ты ни цента не получишь за сегодняшнюю работу!"
    reception "А если подобное повторится, то я оштрафую тебя на 1000 долларов!"
    reception "У нас ВИП Эскорт! Такое отношение к клиентам недопустимо!"
    reception "Ты поняла меня?!?!"
    m "Да..."
    mt "Сучка!"
    mt "Ненавижу!"
    mt "Ненавижу их всех!!!"
    mt "!!!"
    return

# Моника вышла на улицу после диалога на ресепшене
label ep212_dialogues3_escort_hotel_6:
    # не рендерить!!
    mt "Я терпела эту семейку идиотов ради того, чтобы мне ничего не заплатили?!"
    mt "Мерзкая провинциальная дура!"
    mt "Она специально нажаловалась администратору!"
    mt "Меня тошнит от нее!!!"
    mt "!!!"
    mt "А эта сучка из эскорта!"
    mt "АААААА!!!"
    mt "НЕНАВИЖУ!"
    mt "!!!!!"
    return

# Моника вышла на улицу после того, как отказалась работать и ушла
label ep212_dialogues3_escort_hotel_7:
    # не рендерить!!
    mt "Пусть эта сучка из эскорта сама разбирается с этими идиотами!"
    mt "В отличие от нее, я не какая-то там проститутка!"
    mt "Я - Моника Бакфетт! Я леди!"
    mt "И я не позволю какой-то провинциальной дуре оскорблять себя! Фи!"
    return


# при выборе пункта меню "Ждать клиента за столиком." (лейбл ep211_escort_scene1_1a)

# ресторан
# Моника сидит в ожидании клиента
label ep212_dialogues3_escort_hotel_8:
    mt "Надеюсь, сегодня мне удастся заработать хоть что-нибудь."
    mt "Мне нуны деньги..."
    mt "..."
    # к столику Моники подходит служащий отеля
    hotel_staff "Мэм..."
    hotel_staff "Добрый вечер, Мэм..."
    m "?!?!?!"
    m "Ты?!"
    m "Что тебе от меня нужно?!"

    #
    $ notif(_("Моника делала минет служащему отеля в служебном коридоре"))
    #
    mt "Снова хочет предложить пойти с ним в уединенное место?!"
    mt "За 50 долларов!!!"
    mt "!!!"

    hotel_staff "Мэм, я скопил сумму денег, достаточную для того, чтобы..."
    hotel_staff "Кхм..."
    m "Что?"
    hotel_staff "Чтобы уединиться с Вами..."
    m "..."
    menu:
        "Нет! Мне не нужны проблемы с администратором.":
            # Моника высокомерно
            m "!!!"
            m "Нет!"
            m "Во-первых, это запрещено правилами ВИП-эскорта!"
            m "Во-вторых, я не хочу с тобой идти после того..."
            m "Как ты бросил тогда меня с администратором!"
            #
            $ notif(_("Служащий отеля убежал, когда администратор их застукала"))
            #
            hotel_staff "Мэм, этого больше не повторится!"
            hotel_staff "Я Вам обещаю!"
            hotel_staff "Мэм..."
            hotel_staff "Я могу заплатить Вам целых 100 баксов за минет!"
            m "!!!"
            m "Мне не нужны проблемы с администратором из-за тебя!"
            m "Халдей!"
            mt "Никчемный неудачник!"
            # Моника зло на него смотрит, тот смутившись, уходит
            return
        "Сколько денег ты скопил?! (в следующем обновлении)":
            return
    return





    return
