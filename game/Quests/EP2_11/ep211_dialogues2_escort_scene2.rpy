default monicaEscortNed1 = False  # Моника сразу призналась друзьям клиента Нэда, что работает в эскорте
default monicaEscortNed2 = False  # Моника согласилась пойти с Дэниелем и заняться с ним сексом
default monicaEscortNed3 = False  # Моника смирилась с прейскурантом и занялась сексом с Марти
default monicaEscortNed4 = False  # Моника после секса с Дэниелем и Марти занялась сексом с Нэдом


# Моника сидит за столиком в ожидании клиента
label ep211_escort_scene2_1:
    # подходит официантка
    waitress "Здравствуйте, Мэм! Администратор Вас ждет на ресепшене."

    #
    $ notif(_("У Моники хорошие отношения с официанткой."))
    #
    waitress "Вы? Вы здесь работаете?!" # удивленно
    waitress "Я, даже не думала, что..."
    # Моника немного растеряна
    m "Я..."
    m "Я здесь не работаю... Я жду, когда мне принесут еду."
    waitress "Мэм, но Вы же ничего не заказывали..."
    mt "Вот черт!"
    m "Да?"
    m "..."
    m "А, ну конечно. Не заказывала..." # выдавливает улыбку
    m "Я... Жду здесь человека."
    m "..."
    m "Кто там меня звал? Администратор?"
    waitress "Да, Мэм."
    m "Я сейчас подойду к ней."
    # официантка уходит

    #
    $ notif(_("У Моники плохие отношения с официанткой."))
    #
    waitress "Вы?!" # удивленно
    m "Да, это Я!"
    m "Удивительно, что ты все еще работаешь здесь!"
    waitress "Мэм..."
    waitress "А для меня удивительно, что Вы работаете здесь..."
    m "!!!"
    m "С чего ты взяла, что я здесь работаю?!" # высокомерно
    m "По-твоему, я похожа на работника ресторана?!"
    waitress "Мэм... Вас администратор попросила позвать к себе..." # подозрительно
    waitress "Она сказала, что Вы одна из..."
    # Моника перебивает ее
    m "Это неважно, что она сказала!"
    m "Я не собираюсь выслушивать от тебя всякие глупости!"
    m "Никчемная официантка!"
    # официантка уходит

    $ log1 = _("Пойти на ресепшн к администратору.")
    return

# Моника подходит к ресепшену, администратора там нет
label ep211_escort_scene2_2:
    mt "Странно, что ее здесь нет."
    mt "Возможно, она в служебном коридоре?"
    return

# служебный коридор
label ep211_escort_scene2_3:
    # Там стоит заказчик (Ned) и администраторша
    # они смотрят на Монику
    client "Да, вот эта девушка. Я хочу ее."
    reception "Это [monica_hotel_name]. Вы уверены?"
    reception "У нас есть другие девушки для такого заказа."
    client "Меня интересует именно эта."
    client "Она больше подойдет для меня, чем остальные девушки."
    # администраторша поворачивается к Монике
    reception "У тебя сегодня выезд к клиенту."
    reception "Ты должна будешь сопровождать этого джентельмена на встрече."
    reception "И вести себя, как его девушка."
    reception "..."
    reception "Правда, мне не понятно, почему клиент выбрал именно тебя..."
    # парень в этом время рассматривает Монику, потом поправляет администратора
    client "Не просто вести себя как моя девушка!"
    client "Нужно сделать так, чтобы никто не догадался, что я плачу за это."
    client "Это очень важно!"
    reception "Будьте спокойны. Наши девушки - профессионалы."
    reception "Если что-то будет не так..."
    reception "То Вам будет компенсирована сумма вдвое больше той..."
    reception "Которую Вы заплатите за заказ."
    client "Очень надеюсь на это."
    client "Для меня это принципиально важный момент."
    # Моника
    m "Что мне нужно будет делать?"
    client "Вам надо будет быть моей девушкой. Луизой."
    # Моника удивленно
    m "Почему Луизой?"
    # Администратор цикает на нее
    reception "Помолчи!"
    reception "Это желание клиента и у тебя нет права обсуждать его!"
    # Моника злится
    mt "Никчемная администраторша!"
    # Администратор обращается к клиенту
    reception "Вы уверены, что Вам нужен только эскорт?"
    reception "Не хотите ли воспользоваться опцией секса с этой девушкой?"
    reception "Согласно нашего прейскуранта?"
    client "Нет. Для меня важно, чтобы она вела себя как моя девушка."
    client "Больше меня никакие услуги не интересуют."
    client "Очень важно, чтобы она была похожа на мою девушку!"
    reception "Вы можете воспользоваться любой услугой из прейскуранта..."
    reception "Если передумаете."
    reception "В наших интересах оказать как можно больше услуг для того..."
    reception "Чтобы наш клиент остался максимально доволен."
    # Моника кривится
    mt "Она прямо навязывает ему услуги из прейскуранта."
    mt "Ее, видимо, не устраивает, что мне попался нормальный клиент."
    mt "А не какой-нибудь извращенец."
    mt "Эти сучки теперь будут мне завидывать."
    # Администраторша смотрит на Монику
    reception "Ну что, ты все поняла?"
    reception "Будешь осуществлять эскорт, играя роль его девушки."
    reception "Если будешь делать это плохо, то будешь оштрафована!"
    reception "Тебе понятно, [monica_hotel_name]?!"
    # Моника сквозь зубы
    m "Да, мне все понятно."
    reception "Иди переодевайся."
    reception "Для этого заказа тебе надо кое-что поприличнее."
    return

# перед домом, Моника с клиентом. их встречает хозяин дома - Дэниел
label ep211_escort_scene2_3a:
    img 16514
    w
    img 16515
    mt "Это его друг? Больше похож на его босса..."
    client "Эй, Дэниел! Привет!"
    daniel "Привет, Нэд! Как всегда, опаздываешь!"
    img 16516
    ned "Да, мы с моей девушкой немного задержались..."
    ned "Кстати, познакомься. Это Луиза."
    img 16517
    ned "Луиза, это мой друг и коллега Дэниел."
    ned "Сегодня он устраивает небольшую вечеринку для друзей."
    img 16518
    daniel "Ну, наконец-то, Нэд познакомил меня со своей девушкой!"
    daniel "Луиза, вы очаровательны!"
    img 16519
    m "Приятно познакомиться, Дэниел."
    img 16520
    daniel "Проходите в дом. Там вас давно уже все ждут."
    return

# Смена кадра. Моника с заказчиком подходит к столику, где сидят две пары:
# Daniel, Emma и Marty, ​​Natalie.
# Daniel богаче заказчика (возможно его босс)
label ep211_escort_scene2_4:
    # Заказчик знакомит Монику, представляет ее как свою девушку Луизу.
    img 16521
    w
    img 16522
    w
    img 16523
    ned "Эй, ребята, привет!"
    ned "Хочу представить вам мою девушку. Ее зовут Луиза."
    ned "Луиза, это мои коллеги и друзья."
    # показывает на первую пару, потом на вторую
    img 16524
    ned "Дэниел и его жена Эмма."
    emma "Приятно познакомиться!"
    img 16525
    ned "Марти и его жена Натали."
    marty "Привет!"
    natalie "Присаживайтесь к нам."
    natalie "Наконец-то, Нэд познакомил нас со своей девушкой."
    natalie "Я очень рада познакомиться, Луиза."
    # они садятся за столик
    img 16526
    m "Мне тоже приятно познакомиться."
    img 16527
    mt "Моника, тебе сегодня повезло с клиентом..."
    mt "Вкусный ужин, светские разговоры в компании приличных людей..."
    mt "И никаких извращенцев."
    mt "Все, к чему ты так привыкла... И чего так не хватает теперь."
    img 16528
    ned "Луиза, дорогая, хочешь вина?"
    m "Пожалуй, я не откажусь."
    # Между всеми происходят какие-то диалоги
    
    daniel "Нэд, так вот почему ты стал опаздывать на работу!" # подмигивает
    daniel "Очевидно, что с такой прекрасной девушкой ты не спишь целыми ночами!"
    daniel "Аха-ха!"
    # Эмма его одергивает
    emma "Дэниел, оставь свои пошлые шуточки."
    emma "Ты смущаешь ими Луизу!"
    daniel "Да ладно тебе, детка."
    emma "И перестань называть меня деткой. Ты же знаешь, мне это не нравится!"
    daniel "Хорошо, любимая, как скажешь."
    # в это время Марти сидит, уткнувшись в телефон и что-то там просматривает
    daniel "Эй, Марти! Ты когда-нибудь расстаешься с телефоном?"
    daniel "Натали, он в постель его тоже берет? Аха-ха!"
    natalie "Марти очень много работает."
    natalie "Даже сейчас он просматривает документы по работе."
    natalie "Совсем не отдыхает. Да, дорогой?"
    marty "Угу..."
    # камера сзади Марти, он листает фотки на порно-сайте (его жене не видно, что он там смотрит)
    emma "Луиза, расскажи нам, чем ты занимаешься?"
    emma "Нэд ничего нам не рассказывал про тебя..."
    # Моника с удовольствие ловит свою минуту славы, расправляет плечи и с гордостью говорит
    m "Я являюсь руководителем в одной крупной компании."
    natalie "Ого!"
    m "Да. Помимо основной деятельности, связанной с индустрией моды..."
    m "У меня еще бизнес в сфере недвижимости."
    emma "О, серьезно?!" # удивленно
    m "Да, у меня в подчинении много сотрудников."
    daniel "Твоя деятельность связана с модной индустрией?"
    emma "Расскажи нам. Это очень интересно!" # заинтересованность
    m "По работе мне часто приходится посещать публичные мероприятия..."
    m "Выступать перед публикой, давать интервью."
    m "И, конечно же, я всегда в курсе всех событий в мире моды."
    ned "Да, Луиза очень занятая девушка." # дружелюбно
    ned "Редко такое бывает, что мы можем провести вечер вместе..."
    ned "Я вас давно хотел с ней познакомить, но у нее не бывает свободного времени."
    ned "По вечерам она обычно ведет какие-нибудь переговоры..."
    ned "И важные бизнес-встречи."
    ned "Ведь такие встречи очень важны для развития ее бизнеса."
    ned "Да, дорогая?"
    m "Все верно."
    m "У меня широкий круг знакомых, которые имеют немалый вес в этом городе..."
    m "И даже в стране."
    daniel "И как у тебя хватает времени на что-то, кроме работы?" # удивленно
    # Моника преисполнена важности, ей нравится здесь
    mt "Никчемные людишки..."
    mt "Млеют при виде меня и от мысли том, кто я такая!!!"
    m "Да, это довольно непросто..."
    m "Грамотное планирование своего рабочего времени..."
    m "А также помощь моих личных ассистентов..."
    m "Позволяют мне иногда провести вечер не на работе, а в свое удовольствие."
    # Моника поворачивается к Нэду
    m "Нэд, налей мне еще вина!" # в приказном тоне
    m "..."
    m "Пожалуйста, дорогой." # выдавливает из себя улыбку
    ned "Конечно, любимая."
    # Затемнение, вино не показываем
    emma "Луиза, как тебе наш с Дэниелем дом?"
    emma "Мы его так долго выбирали..."
    emma "Это наш гостевой дом. Мы любим устраивать здесь вечеринки с друзьями."
    emma "У нас есть даже рояль!"
    natalie "Но, к сожалению, никто из нас не умеет играть на нем..."
    emma "Да..."
    m "Эмма, у вас чудесный дом. Он очень изысканный."
    mt "Конечно, не такой изысканный как мой дом..."
    m "А что касается игры на пианино..."
    m "Я из высшего общества, как вы уже поняли..."
    m "Соответственно, у меня очень хорошее образование и воспитание."
    m "В высшем обществе считается дурным тоном для девушки..."
    m "Неумение владеть каким-либо музыкальным инструментом."
    m "И я когда-то посещала занятия в музыкальной школе."
    # девушки смотрят на нее с восхищением
    emma "Правда?! Это замечательно, Луиза!"
    natalie "Сыграй нам что-нибудь, пожалуйста!!!"
    m "Легко! Для меня это не составит никакого труда!"
    emma "Мальчики, Луиза сейчас будет играть на пианино!"
    natalie "Нэд, почему ты раньше не познакомил нас с такой замечательной девушкой?!"
    ned "..."
    # все внимание присутствующих на Монике, она встает и подходит к пианино
    # играет мелодию
    # все сидят на стульях за ней, открыв рты
    # после того, как Моника закончила играть, все хлопают и восхищенно на нее смотрят

    # затемнение, что прошло какое-то время, снова за столом (поменять им позы)
    # Моника сидит расслабленная, вся компания дружелюбно общается
    mt "Похоже, что эта работа не так уж и плоха..."
    mt "Нет, конечно это отвратительно, но..."
    mt "Учитывая другие варианты заработать деньги, эскорт не так уж плох..."
    mt "Я думала, что работа в эскорте будет моим кошмаром."
    mt "Однако, в большинстве своем, это вполне безобидное общение."
    mt "Я, пожалуй, поработаю здесь, пока не решу все свои проблемы."
    mt "В любом случае, никто меня здесь не знает..."
    mt "Даже если будут вопросы, я скажу, что это мой двойник."
    mt "Если будет нужно, я найду где-нибудь в стране девушку, похожую на меня..."
    mt "И предъявлю тем, кто будет что-то подозревать."
    mt "Конечно, она будет всего-лишь похожа на меня..."
    mt "У нее, конечно, не может быть такой красоты, которой обладаю Я!"
    mt "Но, все-же..."
    # Моника смотрит на Нэда, тот общается с Дэниелем
    ned "Если у нас получится заключить с ними контракт..."
    ned "Наши продажи взлетят в несколько раз."
    daniel "Нэд, я не стал бы делать такие оптимистичные прогнозы."
    daniel "С ними не так просто договориться, уж поверь мне..."
    daniel "Но если у тебя это получится сделать..."
    daniel "Я поговорю с директором о твоем повышении."
    # Моника перебивает их
    m "Нэд, подай мне салфетку."
    # Нэд не очень доволен, что она тут командует им, но выполняет ее просьбу
    ned "..."
    ned "Конечно, дорогая."
    m "И налей мне еще вина."
    ned "..."
    # затемнение, не показываем как дается вино
    # в затемнении звук наливаемого вина # sound pour_wine
    # он снова отворачивается к Дэниелу
    natalie "Луиза, наши мужья всегда так себя ведут..."
    natalie "Постоянно только и разговоров, что о работе."
    emma "Это точно."
    emma "Но мы с Натали уже привыкли."
    emma "Так что и ты привыкнешь."
    natalie "Луиза, а какие у вас с Нэдом планы?"
    natalie "Вы уже живете вместе или просто встречаетесь?"
    emma "А может, вы собираетесь пожениться?"
    natalie "Это было бы чудесно! Вы такая красивая пара!"
    emma "Нэд не делал тебе предложение?"
    # Моника
    m "Нэд только и думает, что о работе."
    m "Уверена, ему мысль о женитьбе даже в голову не приходила."
    m "Но когда Нэд все-таки решится..."
    m "Ему придется постараться, чтобы я рассмотрела его предложение..."
    # девушки хихикают и смотрят на своих мужей
    emma "Хи-хи-хи..."
    # те общаются, не обращая на них внимания
    natalie "Девочки, мне нужно выйти на улицу, во двор."
    natalie "Дэниел не разрешает курить в доме."
    natalie "Никто не хочет составить мне компанию?"
    emma "Я с тобой, Натали."
    emma "Луиза, пойдем с нами?"
    m "Да, пойдем."
    # в этот момент Нэд поворачивается к Монике
    ned "Луиза, дорогая, останься со мной, пожалуйста."
    ned "Мы с тобой немного позже прогуляемся."
    # Моника остается с мужчинами, Натали с Эммой выходят из гостиной
    return

# в гостиной только Нэд, Дэниел, Марти и Моника
label ep211_escort_scene2_5:
    # Моника сидит с самоуверенным видом, Нэд смотрит на нее, потом поворачивается к Дэниелу, смеясь
    ned "Ну что, Дэниел! Я выиграл наше пари! Аха-ха!!!"
    ned "Гони мне мои деньги! Я сделал это!"
    ned "У меня получилось! Наконец-то!"
    # Дэниел в шоке, Марти удивленно откладывает свой телефон
    daniel "Что?!"
    marty "???"
    daniel "Ты про что?" # смотрит на Монику
    # ему приходит озарение
    daniel "Ты про... про... Она что, проститутка?!" # с изумлением смотрит на Нэда
    ned "Да!" # торжествующе
    m "Ч-что?" # Моника не верит в происходящее, растеряна
    m "???"
    mt "Мне это послышалось?"
    daniel "Не могу поверить! Нет!"
    daniel "Сколько раз ты пытался нас провести..."
    daniel "Я всегда чую проституток за версту!"
    daniel "Но как?! Нет! Я не верю!"
    # Марти с Дэниелем в шоке смотрят на Монику
    m "..."
    marty "Пусть она сама нам скажет!"
    # Нэд поворачивается к Монике
    ned "Ну? Скажи им, кто ты?"
    # Моника в напряжении как струна
    mt "!!!"
    mt "Я не могу поверить!!!"
    mt "Он это все... Подстроил из-за спора?!"
    mt "?!?!?!"
    m "Я... Я его девушка..."
    # Дэниел смеется
    daniel "Аха-ха!"
    daniel "Ну что я говорил тебе! Я не могу ошибиться!"
    daniel "Ты не смог провести меня в те разы, не сможешь и теперь!"
    # Нэд недоволен, что ему не верят
    ned "Нет! Она проститутка! Ее зовут [monica_hotel_name]."
    ned "Мы заключили пари..."
    ned "Если я приведу проститутку и ты не сможешь ее определить, то пари мое!"
    # Дэниел все еще не верит Нэду и спрашивает у Моники
    daniel "Скажи, кто ты?"
    daniel "Ты ведь Луиза, правда?"
    # Моника пытается сохранить хорошую мину при плохой игре
    m "Да. Я Луиза."
    m "Я девушка Нэда..."
    # Нэд злится на нее
    ned "Ну хватит уже!"
    ned "Говори им, кто ты! Твоя игра закончена, [monica_hotel_name]!"
    m "..."
    ned "Если ты не скажешь, то я сообщу администратору сервиса эскорта..."
    ned "Что ты не выполняешь условия заказа!!!"
    mt "!!!"
    mt "Сволочь! Мерзавец!"
    menu:
        "Сказать, что я его девушка и уйти!":
            # Моника встает
            m "Я БЫЛА твоей девушкой!"
            m "Но, после того как ты посмел устроить такое при своих друзьях!"
            m "Я больше не хочу тебя видеть!"
            ned "!!!"
            # Моника гордо уходит
            daniel "Ну что, Нэд? Ты снова облажался!" # язвительно
            marty "Аха-ха!!!"
            ned "..." # сидит злой, смотрит Монике вслед
            daniel "Я тебе говорил, что за версту вижу шлюх!"
            return False
        "Сказать, что я работаю в эскорте.":
            $ monicaEscortNed1 = True # Моника сразу призналась друзьям клиента Нэда, что работает в эскорте
            pass
    # Моника зло смотрит на Нэда
    m "В условиях заказа было то, что я говорю, что я твоя девушка!"
    m "А не доказываю обратное!!!"
    m "Я соблюдаю условия!"
    # Нэд довольно восклицает
    ned "Ага!"
    ned "Она заговорила про условия!"
    ned "Она призналась! Видишь, Дэниел?!"
    # Дэниел и Марти в шоке, смотрят на Монику
    daniel "Что?!"
    daniel "Так ты действительно работаешь в эскорте?!"
    # Моника отвечает, напряженно
    m "Я... Я действительно здесь не совсем из чувственных побуждений..."
    marty "А из каких?"
    # Моника кидает злой взгляд на Нэда
    ned "Говори!"
    m "..."
    m "Из... Из несколько... Меркантильных..."
    ned "Да она обычная проститутка из ВИП Эскорта!"
    ned "Из отеля Ле Гранд! Я там нашел ее!"
    mt "!!!"
    marty "Я знаю всех, кто там работает..."
    marty "Я не видел ее там!"
    ned "Она там работает совсем недавно, потому я ее и заприметил."
    ned "Я знал, что вы не могли ее там видеть."
    ned "И она держится так статно, что сложно поверить в то..."
    ned "Что она обычная проститутка."
    # Монику сидит злая
    mt "!!!"
    mt "Мерзавец! Никчемный неудачник!"
    mt "НЕНАВИЖУ!!!"
    # Дэниел вопросительно смотрит на Нэда
    daniel "То есть... Погоди... Если она все же проститутка..."
    daniel "То зачем ты притащил ее на эту встречу?!"
    daniel "Ведь здесь же наши жены, Нэд!!!" # возмущенно
    daniel "Ты что, совсем сдурел?! Ты за кого нас держишь, а?!"
    # Нэд самодовольно
    ned "Я знал, что ты не сможешь раскусить ее здесь, при Эмме. Аха-ха!"
    ned "Если бы я привел ее в нашу сауну, как обычно приводил других..."
    ned "То не смог бы выиграть наше пари!"
    # Дэниел недовольно смотрит на него
    daniel "Ладно, твоя взяла."
    daniel "Хотя..." # задумчиво
    daniel "Ты утверждаешь, что она проститутка..."
    daniel "И, если она проститутка, то, получается, я могу ее трахнуть?"
    ned "Конечно, можешь!"
    # Моника вскикивает
    m "ЧТО?!"
    m "Нет!"
    m "Мы так не договаривались!"
    m "Ты меня нанял только сопровождать тебя!!!"
    # Нэд спокойно отвечает
    ned "Твоя администраторша навязывала мне ваш прейскурант."
    ned "Она сказала, что я могу передумать в любой момент!"
    # Монику бомбит
    m "Нет!"
    m "!!!"
    ned "Твое агентство гарантировало мне, что с тобой не будет проблем!"
    ned "Мне позвонить твоему начальству?!"
    # Моника злится
    mt "Сволочь!!!"
    mt "Компания придурков!"
    mt "Жалкие неудачники!"
    mt "!!!"
    # Дэниел и Марти смотрят на Монику и пускают слюни
    # Подмигивает
    daniel "Нэд, скажи, ты уже далал это?"
    daniel "Пробовал ее? Ну и как она?"
    ned "Если честно, то нет."
    ned "Я договорился только сопровождать меня."
    ned "Доплачивать за секс $ 500 - для меня дороговато."
    ned "А вдруг бы ты раскусил ее? Тогда наше пари не покрыло бы мои расходы."
    ned "Так что с нашим пари? Ты признаешь, что я выиграл?"
    daniel "Да, черт возьми!"
    daniel "И если ты ее еще не пробовал, то я буду первым!"
    daniel "Я хочу трахнуть ее прямо сейчас!"
    # Марти удивленно
    marty "А как же Эмма?"
    marty "Она и Натали придут с минуты на минуту!"
    # Дэниел отмахивается
    daniel "К черту! Ребята, соврите что-нибудь!"
    daniel "Скажите, что у меня важный звонок, а у Луизы..."
    daniel "У Луизы закружилась голова и она ушла в уборную!"
    daniel "И попросила ее не беспокоить!"
    # Дэниел обращается к Монике
    daniel "Как там тебя зовут?"
    m "..."
    ned "[monica_hotel_name]."
    daniel "[monica_hotel_name], пойдем за мной!"
    # Моника растеряна
    m "Но..."
    m "Нет... Я не пойду... Я..."
    # Нэд берет в руки телефон, говорит сердито
    ned "Все! Я звоню в ВИП Эскорт!"
    ned "Скажу, что девушка отказывается работать по прейскуранту!"
    mt "Черт! Что же мне делать?!"
    mt "Я просто хотела заработать немного денег..."
    mt "Я не предполагала, что это зайдет так далеко!"
    mt "!!!"
    # Нэд говорит по телефону
    ned "Добрый вечер. Да, я передумал..."
    ned "Я хочу взять некоторые пункты из вашего прейскуранта."
    # ему по телефону отвечает администратор, показывается из рецепшина отеля. Администратор улыбается в трубку
    reception "Да, сэр. Мы рады оказать Вам любые перечисленные в прейскуранте услуги!"
    ned "Видите ли... Эта девушка... Она..." # Нэд смотрит на Монику
    reception "Она что, отказывается что-то делать?!"
    reception "Передайте ей, что она будет оштрафована или уволена!"
    ned "Она..."
    # Нэд отстраняется от телефона и говорит Монике
    ned "Так ты согласна?"
    m "!!!"
    menu:
        "Уйти!":
            # Моника встает
            m "Да пошел ты к черту!"
            m "Вместе со своими друзьями!"
            m "Сборище жалких неудачников!!!"
            ned "Эй... Полегче!"
            ned "А то останешься без денег!"
            m "Засунь их себе в задницу!"
            m "!!!"
            return False
        "Согласиться пойти с Дэниелем.":
            $ monicaEscortNed2 = True # Моника согласилась пойти с Дэниелем и заняться с ним сексом
            pass
    # Моника злится
    mt "!!!"
    mt "Мерзавец!!!"
    mt "Если я сейчас откажусь, меня выгонят из эскорта!"
    mt "Что же делать?!"
    mt "Я не могу потерять эту работу..."
    mt "Я Моника Бакфетт и никогда не соглашусь на что-то подобное!"
    mt "..."
    mt "Мне нужно представить, что я не Моника Бакфетт, а [monica_hotel_name]."
    mt "Для [monica_hotel_name] обслужить клиента - несложное дело."
    mt "Для [monica_hotel_name] важна только сумма заработка за вечер."
    mt "Поэтому [monica_hotel_name] сейчас согласится пойти с Дэниелем..."
    # Моника сквозь зубы
    m "Я все слышала и нет необходимости никого увольнять."
    m "Я согласна."
    # мужчины ехидно улыбаются
    ned "Ну вот. Другое дело."
    daniel "[monica_hotel_name], пошли за мной."
    daniel "Давай, быстрее. У меня не так много времени."
    # Дэниел встает и идет к выходу их гостиной, Моника идет за ним с каменным лицом
    return

# вторая комната в доме
label ep211_escort_scene2_6:
    # Моника с Дэниелем заходят в комнату, он поворачивается к ней и хваает ее за попу, прижимает к себе
    # Монике противно, но она не сопротивляется
    daniel "Я с самого начала вечера захотел трахнуть тебя, [monica_hotel_name]."
    mt "Эмма, видимо, и не подозревает, какой он козел на самом деле."
    mt "Может, рассказать ей?"
    # Дэниел продолжает лапать Монику
    daniel "Даже если ты была бы женой Нэда..."
    daniel "Я непременно сделал бы это в один из дней!"
    daniel "Я весь вечер раздумывал над тем, как осуществить это..."
    daniel "И вовсе не ожидал, что трахнуть такую как Луиза будет так просто!"
    mt "!!!"
    mt "Мерзавец!"
    daniel "Скорее раздевайся!"
    # Моника парится
    m "Дэниел, я... Могу я тебя попросить?"
    daniel "Что такое, [monica_hotel_name]?"
    m "Я не хочу, чтобы о том, что здесь произойдет, кто-то узнал..."
    daniel "Конечно, [monica_hotel_name]!"
    daniel "Я не собираюсь никому рассказывать про такую сладкую детку."
    daniel "Я не хочу делиться тобой с кем-то!"
    daniel "Я буду заказывать тебя и трахать тебя сам!"
    daniel "Снимай с себя это скорее! Мне не терпится!"
    # Моника медлит
    mt "[monica_hotel_name] сейчас снимет с себя платье."
    mt "И будет зарабатывать деньги."
    mt "Это просто работа."
    # Моника раздевается, Дэниел приспускает штаны
    daniel "Ложись на диван и раздвинь ноги."
    # Моника ложится на диван, Дэниел наваливается на нее сверху, лапает грудь, попу, рассматривает ее прелести
    daniel "Ммммм, какая же ты охренительная, детка..."
    daniel "Я никому тебя не отдам."
    daniel "Я буду твоим постоянным клиентом."
    daniel "Ты будешь трахаться только со мной."
    mt "У тебя, неудачник, денег на меня не хватит..."
    # Дэниел входит в киску Моники и начинает двигаться
    daniel "О, ты просто супер, [monica_hotel_name]!"
    daniel "Такая горячая! Такая охренительная!"
    daniel "Дааа! Хочу трахать тебя каждый день!"
    daniel "Мммммм..."
    daniel "О, просто чертовски охренительно!!!"
    daniel "Даааа!"
    daniel "Ааааа!!!"
    # затемнение экрана, надпись "В это время в гостиной..."
    return

# смена кадра. гостиная
label ep211_escort_scene2_7:
    # Показывается как сидит компания, Эмма с Натали уже вернулись и сидят за столом
    # Меняем им позы!
    emma "Нэд, Марти, а где Дэниел?"
    marty "Ему позвонили с работы. Какой-то срочный звонок."
    marty "Он пошел в свой кабинет на второй этаж, чтобы поговорить без посторонних."
    marty "Он не хочет, чтобы ему мешали разговаривать по телефону."
    natalie "А где Луиза?"
    ned "У нее началось небольшое недомогание и она ушла в туалет."
    ned "Попросила нас пока веселиться и не беспокоить ее."
    ned "Она скоро придет."
    ​natalie "Странно..."
    marty "Что странного?"
    natalie "Что парень и девушка одновременно отсутствуют..."
    # Эмма хихикает
    emma "Натали, уж не думаешь ли ты, что такая как Луиза..."
    emma "Станет общаться с моим оболтусом и хамом?"
    marty "..."
    ned "..."
    emma "Да и я его знаю..."
    emma "Дэниел никогда бы не стал поступать так по отношению к Нэду."
    emma "Так что, не говори ерунды. Они скоро придут."
    emma "А пока давайте веселиться!"
    natalie "Да, ты права. Я слишком подозрительна..."
    natalie "Марти, дорогой, налей мне еще вина."
    # кадр меняется на вторую комнату в доме
    return

# вторая комната в доме
label ep211_escort_scene2_8:
    # Снова сцена секса Дэниела и Моники
    daniel "Мммммм..."
    daniel "Какие же у тебя сиськи!"
    daniel "Даааа!"
    daniel "В следующий раз я куплю тебя на всю ночь!"
    daniel "И буду трахать тебя до утра!"
    daniel "Ааааа!!!"
    # в комнату заходит Марти
    # Дэниел испуганно
    daniel "Эй! Что ты делаешь здесь?!"
    daniel "Что-то случилось?!"
    daniel "Эмма что-то заподозрила?!"
    marty "Нет, все в порядке!"
    daniel "Тогда зачем ты приперся сюда?"
    marty "Я сказал, что пойду проверю, все ли у тебя хорошо."
    # Дэниел отворачивается от Марти, смотрит на Монику
    # делает еще несколько движений и кончает
    daniel "Ааааа..."
    daniel "Твою мать! ДА!!!"
    daniel "АААААА!!!"
    # отлепляется от Моники, встает и надевает штаны
    # Моника садится на диване, прикрывается руками и тянется за своим платьем
    daniel "У меня все хорошо, как видишь."
    # Марти ухмыляется
    marty "Вижу..."
    marty "Вообще-то, я спросил у Нэда..."
    marty "И он разрешил мне тоже воспользоваться Луизой или как там ее зовут."
    m "!!!"
    daniel "Аха-ха!"
    daniel "Я уже закончил, так что можешь делать с ней все, что хочешь!"
    # Моника возмущенно
    m "Нет!!!"
    m "Я занималась этим с одним человеком!"
    m "Не было условия, чтобы делать это с кем-то еще!!!"
    marty "Нэд сказал, что дополнительный клиент стоит сверху $ 400."
    marty "Это входит в твой прейскурант."
    m "А почему $ 400?! Разве не должно быть дороже, если клиентов больше?!"
    marty "Администратор сказала Нэду, что у тебя индивидуальный прейскурант."
    marty "Чем больше мужчин, тем дешевле!"
    marty "Аха-ха!"
    daniel "Аха-ха!"
    # Монику бомбит
    mt "Сволочь!"
    mt "Сучка!!!"
    mt "Ненавижу эту тварь!!!"
    mt "Она специально сделала это!"
    mt "Она мстит мне за то, что я обозвала ее никчемной и обещала уволить!"
    mt "Между прочим, вполне заслуженно!"
    mt "Это несправедливо!!!"
    mt "Дьявол!!!"
    # Дэниел уходит, Марти остается и смотрит на Монику вопросительно
    marty "Ну так что? Я могу сделать это?"
    m "!!!"
    menu:
        "Уйти!":
            # Моника встает
            m "Да пошел ты к черту!"
            m "Вместе со своими друзьями!"
            m "Сборище жалких неудачников!!!"
            marty "Эй... Полегче!"
            marty "А то останешься без денег!"
            m "Засунь их себе в задницу!"
            m "!!!"
            return False
        "Смириться с прейскурантом.":
            $ monicaEscortNed3 = True # Моника смирилась с прейскурантом и занялась сексом с Марти
            pass
    # Моника смотрит на него с ненавистью
    mt "!!!"
    mt "Ненавижу их всех!"
    mt "Поотрывала бы им яйца!!!"
    mt "Мерзкие неудачники!"
    marty "Ну? Чего молчишь? Ты согласна?"
    mt "С другой стороны..."
    mt "[monica_hotel_name] за этот вечер неплохо заработает."
    mt "И, так получается, что деньги у меня с ней общие..."
    m "Да... Согласна..."
    # Марти приспускает штаны, указывает Монике на диван или еще куда-нибудь, на окно (подоконник), например
    marty "Вставай раком!"
    # Моника зло на него смотрит и выполняет приказ, Марти подходит к ней сзади
    # затемнение экрана, надпись "В это время в гостиной..."
    return

# гостиная
label ep211_escort_scene2_9:
    # все в сборе, кроме Марти и Моники, Натали смотрит вопросительно на Дэниела
    natalie "Дэниел, куда Марти ушел?"
    # Дэниел спокойно сидит и врет ей
    daniel "Марти нашел меня и спросил, все ли у меня в порядке."
    daniel "Я как раз закончил разговор и собирался возвращаться."
    daniel "Тогда Марти решил зайти в туалет и я проводил его."
    daniel "Нам пришлось идти в другой туалет, потому что основной был занят."
    daniel "Там, видимо, сейчас Луиза."
    daniel "Мы даже слышали какие-то звуки. Похоже, что ее тошнит."
    natalie "Бедняжка!"
    # с сочувствием, Дэниел с Нэдом заговорщицки переглядываются и усмехаются
    natalie "Она, должно быть, выбрала какое-то не то сочетание продуктов."
    natalie "Эмма, может быть, нам стоит сходить к ней?" # обращается к Эмме
    natalie "Проверим, все ли с ней хорошо?"
    # кадр меняется на вторую комнату в доме
    return

# вторая комната в доме
label ep211_escort_scene2_10:
    # Снова сцена секса Марти и Моники, Моника стоит нагнувшись, Марти пристроился сзади и двигается
    marty "Мммм, какая у тебя клевая попка!"
    marty "Такая упругая..."
    # Моника со злым лицом
    mt "Когда же он уже кончит и отстанет от меня?"
    marty "О, дааа!"
    marty "Мммммм..."
    # Марти он кончает
    marty "ААААААХ!!!"
    mt "Ну наконец-то!!!"
    mt "Надо одеваться и скорее уходить из этого чертового дома!!!"
    # затемнение экрана, надпись "В это время в гостиной..."
    return

# гостиная
label ep211_escort_scene2_11:
    # Переключение на компанию
    # Заказчик говорит Натали и Эмме
    ned "Не стоит. Я сейчас сам пойду к Луизе и проверю, как она себя чувствует."
    emma "Да, конечно. Пусть Нэд идет." # обращается к Натали, потом говорит Нэду
    emma "Нэд, тебе стоит заботиться о такой хорошей девушке, как Луиза."
    emma "Иначе ты рискуешь ее потерять."
    emma "Должно быть, у нее действительно к тебе чувства..."
    emma "Раз такая как она согласилась встречаться с тобой."
    # Нэд еле заметно ухмыляется
    ned "Да, Эмма. Луиза моя девушка и я очень горжусь этим!"
    # кадр меняется на вторую комнату в доме
    return

# вторая комната в доме
label ep211_escort_scene2_12:
    # Марти одевает штаны, Моника уже надела платье и поправляет его
    # Забегает Нэд.
    ned "Черт! Пустите меня!"
    ned "Теперь моя очередь! Дайте сюда!"
    ned "Я должен ее трахнуть тоже! Все-таки, это моя девушка!!!"
    # Моника смотрит на него зло и хочет что-то сказать
    m "!!!"
    m "Ты..."
    # Нэд перебивает ее
    ned "$ 200! Следующий клиент стоит $ 200!!!"
    ned "Я специально подождал, чтобы получить скидку!!!"
    ned "Жаль, мы не взяли с собой Джима!"
    ned "Тогда мне бы это обошлось всего в $ 100!"
    mt "Жалкий жадный неудачник!!!"
    mt "Подонок!!!"
    m "!!!"
    menu:
        "Уйти!":
            # Моника встает
            m "Да пошел ты к черту!"
            m "Вместе со своими друзьями!"
            m "Сборище жалких неудачников!!!"
            ned "Эй... Полегче!"
            ned "А то останешься без денег!"
            m "Засунь их себе в задницу!"
            m "!!!"
            return False
        "Смириться, иначе меня ждет штраф или увольнение.":
            $ monicaEscortNed4 = True # Моника после секса с Дэниелем и Марти занялась сексом с Нэдом
            pass
    # Моника смотрит на него с ненавистью
    mt "!!!"
    mt "Это просто работа..."
    # Нэд хватает Монику под попу, прислоняет ее спиной к стене, расстегивает штаны, задирает ее платье и входит в нее
    ned "Даааа!!!"
    # Марти стоит смотрит на них
    marty "Эй, Нэд! Натали ничего не спрашивала про меня?"
    # Нэд, не прекращая трахать Монику
    ned "Нет, но беги скорее, а то тебя начнут искать!"
    # Марти убегает довольный
    ned "Аааа..."
    ned "Аааааа..."
    ned "Аааааааа..."
    ned "АААААА!!!" # кончает
    # затемнение экрана
    return

# гостиная
label ep211_escort_scene2_13:
    # Снова сцена компании, где все сидят за столом, включая Монику
    mt "Я не могу смотреть на этих похотливых козлов!"
    mt "Они только что изменили своим женам!"
    mt "Изменили, сделав... сделав... Даже не хочу об этом думать!"
    mt "А теперь сидят и лгут им! Как ни в чем не бывало!"
    mt "Как же это мерзко!"
    mt "А более мерзко то, что мне после всего..."
    mt "После всей этй грязи..."
    mt "Мне нужно тоже притворяться перед Эммой и Натали!"
    mt "Это какой-то кошмар!"
    # Нэд обращается к Монике
    ned "Луиза, любимая, ты себя уже лучше чувствуешь?"
    m "Да..."
    m "Спасибо за твою заботу, дорогой..."
    mt "Подонок!!!"
    natalie "Луиза, мы с Эммой так переживали за тебя."
    emma "Тебе точно стало лучше? Может, тебе дать какие-нибудь лекарства?"
    mt "Дайте мне яду. Я налью его в бокалы ваших козлов!"
    m "Мне уже лучше, спасибо."
    natalie "Ну и хорошо. Луиза, у меня на завтра запланирован шоппинг."
    natalie "Эмма тоже ко мне присоединиться. Не хочешь составить нам компанию?"
    emma "Да, это отличная идея!"
    emma "Луиза, ты же хорошо разбираешься в моде..."
    emma "Пойдем завтра с нами!"
    emma "Погуляем по магазинам, зайдем в ресторан."
    natalie "Потом можно будет сходить в СПА. Мы отлично проведем время!"
    m "Спасибо за предложение, девочки, но..."
    m "У меня завтра много работы."
    m "У меня каждый день расписан буквально поминутно."
    m "К сожалению, у меня не будет времени."
    mt "Не хватало еще тратить на всякую ерунду деньги, которые я заработала с таким трудом..."
    mt "Тем более, их даже не хватит на новую сумочку..."
    emma "Жаль..."
    natalie "Луиза, у тебя такой плотный рабочий график."
    natalie "Когда вы успеваете встречаться с Нэдом?"
    m "..."
    m "По вечерам... Мы уделяем друг другу время."
    ned "Да, любимая. Мы стараемся встречаться каждый вечер."
    emma "Наверное, это так волнительно - ждать вечера, чтобы встретиться с любимым..."
    m "..."
    natalie "Луиза, а Нэд часто дарит тебе подарки?"
    natalie "Мне вот Марти дарит цветы только по праздникам..."
    marty "Дорогая, ну ты же итак знаешь, что я тебя люблю..."
    natalie "Знаю. Но мне все равно хочется внимания."
    natalie "А ты только и знаешь, что сидишь целыми вечерами в телефоне и работаешь!"
    marty "Ну не обижайся. Я стараюсь ради нас с тобой." # целуются
    emma "А мой Дэниел часто балует меня цветами и всякими приятными сюрпризами."
    daniel "Конечно, любимая. Мне нравится делать тебя счастливой." # тоже целуются
    mt "Боже... Меня сейчас стошнит от этого всего..."
    ned "Луиза, дорогая. Мне кажется, тебе снова нехорошо."
    ned "Может быть, я отвезу тебя домой?"
    m "Да, дорогой. Я буду тебе очень благодарна."
    m "Спасибо за приятный вечер." # говорит с натянутой улыбкой
    m "Я была рада с вами познакомиться."
    # Моника с Нэдом встают, Эмма с Натали подходят к Монике, целуют в щечку или обнимают
    emma "Я надеюсь, вы с Нэдом к нам еще приедете."
    emma "Я буду очень рада тебя видеть, Луиза!"
    natalie "И мы обязательно еще сходим с тобой на шоппинг!"
    m "Хорошо. Обязательно."
    marty "Пока, Луиза. Приятно было познакомиться."
    daniel "И мне тоже было приятно. Пока."
    # Моника выдавливает из себя улыбку
    # затемнение экрана
    return

# служебный коридор ресторана в отеле Ле Гранд
label ep211_escort_scene2_14:
    # разговор администраторши и Моники
    mt "Ненавижу эту никчемную администраторшу!"
    mt "!!!"

    # Если Моника ушла от клиентов, отказавшись обслуживать любого из них, то администратор орет на Монику
    reception "[monica_hotel_name]!!!"
    reception "Мне звонил клент!"
    reception "Он крайне недоволен твоим поведением!"
    reception "Какого черта ты решила, что можешь диктовать свои условия клиенту?!"
    m "Он изменил первоначальные условия..."
    reception "Да!!! И он имел на это право!!!"
    reception "Я тебя прощаю на первый раз и ограничусь только штрафом!"
    reception "В следующий раз ты за подобное поведение вылетишь отсюда!!!"
    reception "У нас ВИП Эскорт! Такое отношение к клиентам недопустимо!"
    reception "Ты поняла меня?!?!"
    m "Да..."
    mt "Сучка!"
    mt "Ненавижу!"
    reception "Клиент за сопровождение заплатил $500."
    reception "Ты оштрафована за невыполнение услуг согласно прейскуранту."
    reception "И с этих денег ты не получаешь ни цента!"
    mt "!!!"
    m "Как?"
    reception "Да, ни цента! И это ты еще легко отделалась!"
    reception "Еще хоть одно малейшее нарушение и тебя ждет увольнение!!!"
    reception "Тебе все понятно, [monica_hotel_name]?!"
    m "Да..."
    mt "Гори в аду, мразь!"

    # Если Моника обслужила клиентов
    reception "Ты хорошо справилась с сегодняшним заказом..."
    reception "Но клиент сказал, что ты вела себя нерешительно."
    reception "[monica_hotel_name] должна сама предлагать услуги из прейскуранта!"
    reception "И не заставлять клиентов уговаривать себя!"
    reception "Если подобное поведение будет встречено еще раз..."
    reception "То ты будешь оштрафована, понятно?!"
    m "Да..."
    mt "!!!"
    reception "Клиент заплатил $500 за сопровождение на вечере..."
    reception "И $1100 за три дополнительные услуги из прейскуранта."
    reception "Твой заработок составляет 50 процентов от суммы."
    reception "То есть $800."
    reception "Вот твои деньги."
    # отдает ей 800 долларов
    reception "Завтра можешь приходить снова."
    reception "На сегодня все. Клиенты не любят использованный товар."
    mt "Вот сучка!"

    mt "!!!"
    # Моника уходит
    return
