default monicaBiffInvestorsLeGrand1 = False # Моника согласилась с требованием Бифа провести презентацию
default monicaBiffInvestorsLeGrand2 = False # Моника согласилась провести презентацию в отеле
default monicaBiffInvestorsLeGrand3 = False # Моника провела презентацию и позировала для инвесторов в Ле Гранд


# при условии, что было свидание с Олафом и он уже стал инвестором
# через неделю после свидания с ним
# Моника приходит в кабинет Бифа
label ep217_dialogues6_office_1:
    # использовать имеющиеся арты
    # при выборе пункта меню "Спросить о работе"
    m "Биф..."
    m "Я хотела узнать у тебя..."
    m "Есть-ли еще работа?"
    m "Мне нужны деньги..."
    biff "Для хорошей цыпочки у папочки всегда найдется работа."
    m "Тогда я в фотостудию..."
    # разворачивается, чтобы выйти из кабинета
    biff "Эй, кукла! Стой!"
    biff "Папочка тебя еще не отпускал!"
    mt "Что этому придурку еще нужно от меня?!"
    # Моника возвращается
    m "..."
    biff "Ты с чего взяла, что у тебя фотосессия?"
    biff "Или ты тут вместо меня распределяешь работу?"
    biff "Кто из нас Босс? Ты или Я?"
    mt "Я!!! Я здесь БОСС!!!"
    mt "!!!"
    biff "Вот и правильно делаешь что молчишь."
    biff "Умнее выглядишь, когда у тебя закрыт рот."
    biff "Я смотрю ты настолько вжилась в роль сучки Бакфетт..."
    biff "Что начала строить тут из себя главного."
    biff "Босс тут один! И это Я!"
    biff "Я Босс!"
    biff "Вау! Я - БОСС!!!"
    # Моника смотрит на него с презрением
    m "..."
    m "Это все, что ты хотел мне сказать, Биф?"
    biff "Нет, цыпочка."
    biff "Ты хотела работу? Работа для тебя есть."
    biff "Но это не фотосессия."
    biff "Я для наших многоуважаемых господ, которые уже инвестировали в мой журнал..."
    mt "МОЙ ЖУРНАЛ!"
    mt "Кретин!!!"
    biff "А также для будущих инвесторов..."
    biff "Приготовил приватную презентацию."
    m "Какую презентацию?!"
    m "?!?!?!"
    m "Что это значит, Биф?"
    biff "Это значит, что ты проведешь презентацию для них."
    biff "Расскажешь о том, как хорошо дела у тех, кто уже инвестировал..."
    biff "Чтобы остальные денежные мешки тоже захотели раскошелиться."
    biff "А чтобы придать им больший интерес с моему журналу..."
    biff "Презентацию для них проведет сучка Бакфетт..."
    biff "В приватной интимной обстановке."
    biff "Что максимально подчеркнет то, с каким почтением мы к ним относимся..."
    m "Приватная и интимная обстановка, Биф?"
    m "???"
    mt "Что за чушь несет этот идиот?!"
    mt "Что еще за приватная презентация?!"
    mt "Если этот мерзавец хочет нарядить меня в какой-нибудь глупый наряд..."
    mt "То пусть надевает его сам!"
    mt "И сам проводит эту чертову презентацию!"
    mt "Жалкий бездельник!"
    mt "Сволочь!"
    biff "Именно, цыпочка!"
    biff "Приватная и интимная!"
    biff "Многоуважаемым господам инвесторам это понравится!"
    biff "Папочка знает, как нужно вести бизнес!"
    biff "И как развести их на вложение в мой журнал!"
    m "Ты ни черта не понимаешь, как нужно вести бизнес, Биф!"
    m "Деловые переговоры не проводят в интимной обстановке!"
    m "Это официальные переговоры!"
    biff "Это кто тут учит Босса как управлять бизнесом?!"
    biff "Двадцатидолларовая безмозглая кукла?!"
    # если Моника переспала с Олафом или была месть Линде
    #
    $ notif(_("Моника после ужина с Олафом поехала в отель."))
    #
    biff "Ты забыла, как успешно ты провела переговоры с денежным мешком Олафом, а?!"
    biff "Хочешь сказать, это были официальные переговоры в официальной обстановке?!"
    m "!!!"
    #
    biff "Если Я тебе сказал, что ты проведешь эту презентацию, ты это сделаешь!"
    biff "Если, конечно, хочешь сохранить свое рабочее место!"
    biff "Ты же помнишь, кукла безмозглая, что на твое место уже есть претенденты?!"
    #
    $ notif(_("Биф устраивает кастинг в поисках новой куклы."))
    #
    biff "Или у тебя настолько нет мозгов, что ты забыла про это?!"
    m "Перестань так со мной разговаривать, Биф!"
    m "Я не безмозглая кукла!"
    biff "Ты тупая безмозглая двадцатиолларовая шлюха!"
    biff "Твое место в какой-нибудь подворотне в трущобах!"
    biff "И ты отправишься туда, когда я тебя вышвырну с МОЕГО офиса!"
    biff "Если и дальше будешь со мной спорить!"
    biff "Тебе все понятно?!"
    m "..."
    biff "Я НЕ СЛЫШУ ОТВЕТА!!!"
    m "..."
    menu:
        "Да, понятно.": #corruption
            $ monicaBiffInvestorsLeGrand1 = True # Моника согласилась с требованием Бифа провести презентацию
            pass
        "НЕТ!":
            m "Я не тебе не кукла!"
            m "И я не буду кривляться перед инвесторами!!!"
            m "!!!"
            biff "Ты не получишь никакую другую работу!"
            biff "Пока не сделаешь то, что Я тебе говорю!"
            mt "Да пошел ты!"
            mt "Я найду другой способ зарабатывать деньги!"
            # Моника уходит. В след. визит к Бифу разговор возобновляется (Биф не дает ей фотосессии)
            return -1
    # Моника зло
    mt "НЕНАВИЖУ!!!"
    mt "Оторву ему яйца!"
    mt "Заставлю вымаливать прощения у моих ног!"
    mt "Сволочь!!!"
    mt "!!!"
    m "Да, понятно!"
    m "!!!"
    biff "Другое дело!"
    biff "Значит так, кукла!"
    biff "Презентация запланирована на завтра."
    biff "Я уже пригласил наших мнгоуважаемых господ инвесторов."
    biff "Они приедут в отель Ле Гранд [завтра вечером]."
    m "КУДА?!"
    m "ЛЕ ГРАНД?!"
    m "!!!"
    m "!!!!!"
    m "!!!!!!!"
    biff "Да. И нечего так орать!"
    biff "Я снял там отличный номер, где ты проведешь приватную презентацию."
    m "Я тебе не шлюха какая-то, чтобы ездить с толпой инвесторов в номер отеля!!!"
    m "!!!"
    biff "Все, тихо!"
    biff "Мне надоели твои вечные споры и недовольства!"
    biff "Пошла вон отсюда!"
    m "Биф!.."
    biff "Вон отсюда, я сказал!!!"
    m "!!!"
    menu:
        "Согласиться провести презентацию в отеле Ле Гранд.": #corruption
            $ monicaBiffInvestorsLeGrand2 = True # Моника согласилась провести презентацию в отеле
            pass
        "Да пошел он!":
            m "Я не тебе не кукла!"
            m "И я не буду кривляться перед инвесторами!!!"
            m "!!!"
            biff "Ты не получишь никакую другую работу!"
            biff "Пока не сделаешь то, что Я тебе говорю!"
            mt "Да пошел ты!"
            mt "Я найду другой способ зарабатывать деньги!"
            # Моника уходит. В след. визит к Бифу разговор возобновляется (Биф не дает ей фотосессии)
            return -1
    # Моника в растерянности
    mt "Вот дьявол!!!"
    mt "Что же мне теперь делать?!"
    mt "?!?!?!"
    mt "Эта сволочь заставляет меня провести презентацию в Ле Гранд!"
    # если Моника работает или раньше работала в эскорте
    #
    $ notif(_("Моника работает в ВИП-эскорте."))
    #
    mt "Если я приду туда, меня увидит эта сучка администраторша!"
    mt "И подумает, что я пытаюсь работать в обход администрации эскорта!"
    mt "А потом еще и оштрафует меня за это!"
    mt "!!!"
    mt "А если она даст понять при Бифе или инвесторах, что я там работаю?!"
    mt "Что тогда будет?!"
    mt "!!!!"
    mt "Я должна как-то выкрутиться из этой ситуации!"
    mt "Если я сейчас откажу Бифу, то он меня уволит."
    mt "А я должна иметь доступ в СВОЙ офис!"
    mt "Я должна быть в курсе того, что творит здесь этот придурок Биф!"
    mt "И это намного важнее какого-то гребаного эскорта!"
    mt "Да! Плевать, что подумает сучка администраторша!"
    mt "МОЙ офис для меня намного важнее!"
    mt "Я что-нибудь придумаю!"
    mt "Ты и не из таких сложных ситуаций находила выход, Моника!"
    mt "Ты умная и сильная!"
    mt "И пусть эти убогие человечешки пока недооценивают твою силу!"
    mt "Придет время - они все поймут!!!"
    mt "!!!"
    # Моника зло смотрит на Бифа
    m "Я проведу эту презентацию!"
    m "Я приду завтра вечером в отель!"
    m "!!!"
    biff "Ну вот видишь, цыпочка, как все просто!"
    biff "Зачем нужно было делать столько нервов папочке и спорить с ним?"
    biff "Тогда [завтра вечером жду тебя в отеле Ле Гранд]."
    biff "И не опаздывай, цыпочка!"
    biff "Нельзя заставлять наших многоуважаемых господ инвесторов ждать."
    mt "Мерзавец!"
    mt "Ненавижу его!!!"
    mt "!!!"
    m "..."
    m "Я приду, Биф."
    biff "Так-то лучше."
    biff "И вообще, цыпочка! Ты испортила папочке настроение!"
    biff "Как ты собираешься это исправлять, а?"
    # Моника сквозь зубы
    mt "Безмоглый кретин!"
    mt "!!!"
    # меню кастинга, кастинг.
    # после кастинга
    biff "Я жду тебя завтра в отеле, цыпочка."
    m "..."
    $ log1 = _("Идти в отель Ле Гранд для проведения приватной презентации.") # появляется на след. день после этого разговора
    return

# мысли Моники, если отказалась и стоит на улице возле офиса
label ep217_dialogues6_office_2:
    # не рендерить!!
    mt "Моника Бакфетт не позволит поставить себя в такую унизительную ситуацию!"
    mt "Пусть сам кривляется перед своими никчемными инвесторами!"
    mt "Пошел он к черту!"
    mt "Мерзавец!"
    mt "Ненавижу его!!!"
    mt "!!!"
    return

# мысли Моники, если отказалась и стоит на улице возле офиса, хочет снова зайти к Бифу, чтобы согласиться
label ep217_dialogues6_office_2a:
    # не рендерить!!
    mt "Я должна иметь доступ в СВОЙ офис!"
    mt "Я должна быть в курсе того, что творит здесь этот придурок Биф!"
    mt "И это важнее, чем какая-то гребаная приватная презентация!"
    mt "МОЙ офис для меня намного важнее!"
    mt "Я что-нибудь придумаю!"
    mt "Мне нужно идти к Бифу и согласиться эту чертову презентацию!"
    return

# если Моника отказалась и оказалась на улице (return -1), но снова пришла к Бифу
# офис, кабинет Бифа
label ep217_dialogues6_office_3:
    # использовать имеющиеся арты
    m "Биф..."
    m "Мне нужна работа."
    biff "Я дам тебе работу, если ты согласишься на приватную презентацию..."
    m "..."
    biff "Ты согласна?"
    mt "!!!"
    menu:
        "Согласиться провести презентацию в отеле Ле Гранд.": #corruption
            $ monicaBiffInvestorsLeGrand2 = True # Моника согласилась провести презентацию в отеле
            pass
        "Да пошел он!":
            m "Я не тебе не кукла!"
            m "И я не буду кривляться перед инвесторами!!!"
            m "!!!"
            biff "Ты не получишь никакую другую работу!"
            biff "Пока не сделаешь то, что Я тебе говорю!"
            mt "Да пошел ты!"
            mt "Я найду другой способ зарабатывать деньги!"
            # Моника уходит. В след. визит к Бифу разговор возобновляется (Биф не дает ей фотосессии)
            return -1
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "Где я смогу заработать деньги для сучки Виктории?"
    m "Я..."
    m "Я проведу эту презентацию..."
    biff "Ну вот, цыпочка."
    biff "Совсем другое дело!"
    biff "Тогда [завтра вечером жду тебя в отеле Ле Гранд]."
    biff "И не опаздывай, цыпочка!"
    biff "Нельзя заставлять наших многоуважаемых господ инвесторов ждать."
    mt "Мерзавец!"
    mt "!!!"
    $ log1 = _("Идти в отель Ле Гранд для проведения приватной презентации.") # появляется на след. день после этого разговора
    return

# на следующий день, мысли если согласилась на презентацию в отеле
label ep217_dialogues6_office_4:
    # не рендерить!!
    mt "Мне нужно идти в Ле Гранд и провести эту чертову презентацию!"
    return

# Ле Гранд, ресепшн
# Моника пришла на презентацию
label ep217_dialogues6_office_5:
    # заходит в отель, на ресепшн
    # администраторша как всегда стоит у стойки ресепшна
    # Биф стоит в фойе
    # если Моника работает в эскорте
    #
    $ notif(_("Моника работает в ВИП-эскорте."))
    #
    mt "Гребаная сучка администраторша!"
    mt "Надеюсь, она ничего не скажет при Бифе!"
    mt "Нельзя допустить того, чтобы этот кретин узнал..."
    mt "Что эскорт - мой источник дохода!"
    mt "Даже не хочу думать о последствиях!"
    mt "!!!"
    # если Моника раньше работала в эскорте и уволилась
    #
    $ notif(_("Моника уволилась из ВИП-эскорта."))
    #
    mt "Гребаная сучка администраторша!"
    mt "Надеюсь, она ничего не скажет при Бифе!"
    mt "Нельзя допустить того, чтобы этот кретин узнал..."
    mt "Что эскорт - был моим источником дохода!"
    mt "Даже не хочу думать о последствиях!"
    mt "!!!"
    # если Моника не работала в эскорте
    mt "Ненавижу эту мерзкую сучку!"
    mt "Она всегда так смотрит на меня..."
    mt "Как-будто я ей чего-то должна!"
    mt "!!!"
    # Биф, увидев Монику, подходит к ней
    biff "А, привет цыпочка!"
    biff "Иди в номер, который я арендовал для презентации."
    biff "И быстро переодевайся!"
    biff "Наши многоуважаемые господа прибудут с минуты на минуту!"
    biff "Я их тут встречу у входа в отель, а ты жди нас в номере!"
    biff "Давай иди! Быстро!"
    # Биф выходит
    # Моника идет мимо стойки ресепшна
    # если Моника работает или раньше работала в эскорте
    reception "[monica_hotel_name], кто этот Мистер?"
    reception "Это твой клиент сегодня?"
    mt "Черт!"
    m "Нет, он не клиент. Просто знакомый."
    reception "Ты ведь помнишь, [monica_hotel_name], что нельзя работать в обход администрации отеля?"

    # если Моника уволилась из эскорта
    m "Я помню. А ты помнишь, что я больше здесь не работаю! Вообще-то!"
    # else
    m "Помню. Но я сегодня не работаю..."
    #
    reception "А придется проработать, раз ты сюда пришла."
    reception "Сейчас приедут важные господа и будет большой заказ."
    reception "Твое присутствие обязательно, [monica_hotel_name]!"
    mt "Нет! Только не это!"

    # если Моника уволилась из эскорта
    m "Я больше не работаю в ВИП-эскорте! С какой стати мое присутствие обязательно?!"
    m "Я пришла сюда по важным делам!"
    # else
    m "Я... Я не смогу! Я не планировала выходить сегодня а работу!"
    m "У меня важные дела!"
    #
    reception "Какие важные дела могут быть у тебя здесь, в отеле?!"
    reception "Или ты задумала снова обмануть меня?"
    reception "Решила привести клиента в номер и не заплатить положенный отелю процент?!"
    m "Я..."
    reception "Молчи! Я не собираюсь выслушивать твое вранье!"
    reception "Когда господа будут готовы к выбору девочек, я позову тебя!"
    reception "И ни слова больше!"
    mt "Твою мать!"
    mt "Моника!"
    mt "Нужно что-то придумать!"
    mt "Я убегу сразу после презентации!"
    mt "Точно! Я быстро убегу и администраторша меня не увидит!"
    mt "Пошла она к черту со своими гребаными правилами ВИП-эскорта!"

    # если Моника не работала в эскорте
    mt "Какого черта она всегда на меня так пялиться?!"
    mt "Какой непрофессионализм! Ужас!"
    mt "!!!"
    # затемнение, звук лифта, каблуки
    return

# локация видео-рум
# Моника заходит в номер, там никого нет
label ep217_dialogues6_office_6:
    # Моника осматривается
    # на экране демонстрируется график роста schedule3
    mt "Какое-то странное помещение..."
    mt "Это какой-то кинозал?!"
    mt "И зачем этот кретин Биф поставил здесь алкоголь?"
    mt "Он собрался проводить презентацию или развлекать этих никчемных инвесторов?"
    # если была сцена унижения Линды перед Олафом
    mt "Интересно, этот жалкий тюфяк Олаф придет сюда?"
    mt "В прошлый раз я ему запретила приближатся к этому отелю."
    mt "Хмм... Посмотрим, насколько уважительно он относится к словам Миссис Моники Бакфетт..."
    # Моника оглядывается
    mt "Никчемный Биф сказал, что мне нужно переодеться..."
    mt "И где этот наряд, который он мне приготовил?"
    # взгляд на пуф, где стоит алкоголь, на нем валяется красная одежда
    # Моника подходит и наклоняется, протянув руку
    mt "..."
    menu:
        "Переодеться.":
            pass
    # затемнение, шуршание одежды
    # после затемнения показываем Монику в красном аутфите
    # она в шоке смотрит на свою одежду
    mt "ЧТО!"
    mt "ЭТО!"
    mt "ТАКОЕ?!"
    mt "Я убью этого мерзавца!!!"
    mt "Я ни за что не буду проводить..."
    # ее грозные мысли прерывает звук открываемой двери, мужские шаги
    mt "О НЕТ!!!"
    mt "!!!"
    mt "Черт! Черт! Черт!"
    mt "Они сейчас увидят меня в ЭТОМ!!!"
    # заходят инвесторы, все кроме Олафа, с ними довольный Биф
    mt "!!!"
    mt "!!!!!"
    biff "Уважаемые господа, прошу вас! Проходите, располагайтесь!"
    biff "А вот и Миссис Бакфетт!"
    biff "Прекрасно выглядите, Миссис Бакфетт..." # Биф ехидно улыбается
    mt "Мразь!!!"
    mt "!!!"
    mt "Он специально все это подстроил!" # смотрит на Бифа злобно
    mt "Я теперь даже уйти не смогу отсюда!!!"
    mt "У меня в этой юбке вся попа видна!!!"
    mt "Так, Моника, упокойся..."
    mt "Ты и не из таких сложных ситуаций находила выход."
    mt "Сейчас ты проведешь эту гребаную презентацию..."
    mt "Тебе просто не нужно поворачиваться к инвесторам спиной."
    mt "..."
    # Стив подходит и здоровается с ней, хитро улыбаясь
    steve "Миссис Бакфетт, добрый день!"
    steve "Рад Вас видеть!"
    mt "Стив. Мешок с дерьмом!"
    mt "Какого черта он сюда пришел?!"
    # сама протягивает ему руку, приподнимая уголок губ в подобии улыбки
    # следом за ним подходит и тянет руку Филипп
    # она протягивает ему руку, Филипп наклоняется, целует ей руку, сам смотрит ей в глаза и ухмыляется
    philip "Мэм... Рад нашей встрече..."

    # если Моника работает у него субботней шлюхой № 2
    mt "Ненавижу мерзавца Филиппа!"
    mt "Отвратительный самодовольный жадный извращенец! Как и все они!"
    mt "!!!"
    # если не работает субботней шлюхой у Филиппа
    #
    $ notif(_("Филипп предлагал Монике деньги за секс в ресторане Ле Гранд."))
    #
    mt "Это тот мерзкий тип, который постоянно пытается предложить мне какую-нибудь извращенскую гадость!"
    mt "Какой же он отвратительный!"

    # остальные тоже подходят, здороваются, она слегка им улыбается
    mt "Сборище никчемных неудачников..."
    mt "Считают, что они такие влиятельные и уважаемые личности..."
    mt "А на деле - все о одного пустое место!"
    mt "Им не сравниться с такой леди, как Я!"
    mt "!!!"
    biff "Господа, присаживайтесь."
    # мужчины рассаживаются на креслах, лицом к экрану
    # инвестор, который был в номере отеля, когда Моника работала реквизитом, внимательно смотрит на нее
    investor3 "..."
    mt "..."
    # если Моника работала реквизитом Линды в номере отеля
    #
    $ notif(_("Моника работала реквизитом Линды в номере отеля Ле Гранд."))
    #
    mt "Я надеюсь, что этот придурок не узнает меня!"
    mt "!!!"
    # если Моника ударила инвестора в номере отеля
    #
    $ notif(_("Моника ударила инвестора и убежала из номера."))
    #
    mt "Надо было ударить его не только по яйцам, но и по голове!"
    mt "Чтобы у него отшибло память!"
    mt "!!!"
    # пока остальные рассаживаются, этот инвестор подходит к Бифу и шепчет ему, наклонившись
    investor3 "Мистер Биф..."
    investor3 "Вы проявляете себя как отличный личный ассистент Миссис Бакфетт..."
    investor3 "И наверняка знаете все ее предпочтения..."
    biff "Да, конечно!"
    biff "Вы хотели что-то узнать про Миссис Бакфетт?"
    investor3 "Дело в том, что Миссис Бакфетт очень меня привлекает..."
    investor3 "Но я понимаю, что инвестирование в ее журнал - это не повод, чтобы она обратила на меня внимание..."
    investor3 "Я хотел бы спросить у вас, Мистер Биф..."
    investor3 "Возможно, вы сможете мне подсказать, что я могу сделать..."
    investor3 "Чтобы бы трахнуть Миссис Бакфетт."
    biff "О, не переживайте!"
    biff "Я постараюсь что-нибудь придумать, чтобы помочь вам..."
    biff "Это, конечно, будет не так просто."
    biff "Вы ведь понимаете, насколько Миссис Бакфетт влиятельная персона."
    investor3 "Да-да... Поэтому я к вам и обратился."
    investor3 "Я готов вознаградить вас лично за вашу помощь, Мистер Биф."
    biff "Я подумаю, чем я могу помочь вам..."
    investor3 "Договорились."
    # инвестор отходит и садится на свободное кресло
    # Филипп смотрит на Монику с мерзкой ухмылочкой
    campbell "Да, Миссис Бакфетт."
    campbell "Мы с нетерпением ждем Вашей презентации."
    # Биф самодовольно улыбается и подходит к Монике
    # шепчет ей
    biff "Так, кукла, сейчас ты не двадцатидолларовая шлюха, а сучка Бакфетт."
    biff "Сучка Бакфетт сделает все, чтобы угодить инвесторам."
    biff "Для этого ей чаще надо поворачиваться к ним спиной и демонстировать свой зад."
    m "Что?! Я не буду делать этого!"
    m "Я... Миссис Бакфетт никогда не стала бы проводить стречу в таком виде!"
    m "Что это еще за вульгарный костюм?!"
    m "Как ты мог подобрать ТАКОЕ?!"
    biff "Рот закрой и делай так, как тебе говорю Я!"
    biff "Или ты сейчас же поворачиваешься к инвесторам спиной..."
    biff "И начинаешь говорить о плюсах сотрудничества с моим журналом!"
    biff "Или я сейчас же звоню охране моего офиса и отдаю распоряжение, чтобы тебя туда не пускали больше!"
    biff "Все поняла, кукла безмозглая?!"
    # Моника зло на него смотрит
    mt "СКОТИНА!"
    mt "!!!"
    mt "Черт!"
    mt "Мне нельзя допустить того, чтобы этот мерзавец выгнал меня с моего же офиса!"
    mt "Мне придется повернуться к ним спиной!"
    mt "И они все увидят мою попу!!!"
    mt "Какой кошмар, Моника!"
    mt "Не могу поверить, что ты оказалась в такой унизительной ситуации!"
    mt "Шестеро неудачников и ты в таком наряде!"
    mt "В отеле!!!"
    # Биф отходит от Моники и садится на кресло сбоку от остальных инвесторов
    biff "Можете начинать, Миссис Бакфетт."
    # Моника смотрит на экран
    mt "Черт!"
    mt "Мне снова нужно нести какую-нибудь чушь перед этими гребаными графиками!"
    mt "При том демонстрируя свой вид сзади!"
    mt "Мало этому мерзавцу было той ужасной фотосессии!"
    #
    $ notif(_("Моника проводила фотосессию перед инвесторами."))
    #
    mt "Я была перед инвесторами почти обнаженная!"
    mt "!!!"
    mt "Ненавижу скотину Бифа!!!"
    mt "!!!"
    # на экране график schedule3
    m "Добрый вечер, господа."
    m "Я рада привествовать вас на нашей презентации."
    m "Я хотела бы продемонтировать вам... Промежуточные отчеты..."
    m "Предоставленные нашим аналитическим отделом."
    # Моника косится на Бифа
    # тот улыбается и показывает пальцем на экран, говоря жестом, чтобы она поворачивалась
    mt "Боже!"
    mt "Я не верю, что мне сейчас придется сделать ЭТО!"
    mt "!!!"
    mt "Так, Моника, успокойся!"
    mt "Это сборище жалких неудачников уже имело честь..."
    mt "Лицезреть твою восхитительную красоту на прошлой фотосессии..."
    mt "Сейчас ты по крайней мере в трусиках..."
    mt "Черт!"
    # Моника поворачивается спиной к инвесторам
    # все взгляды устремлены на попу Моники
    m "Взгляните на этот график, господа..."
    investor3 "Вау!"
    investor4 "Впечатляет!"
    steve "Какой отличный график, Миссис Бакфетт!"
    mt "Боже, я сейчас сгорю от стыда!!!"
    # если Стив видел попу Моники на первой презентации
    mt "Этот гадкий слизняк Стив в прошлый раз видел, что..."
    mt "Я проводила презентацию с голой попой!"
    mt "Теперь он будет издеваться надо мной, сволочь!"
    mt "Я снова с почти голой попой!!!"
    mt "!!!"
    # если Филипп видел попу Моники на первой презентации
    mt "Этот мерзкий Филипп в прошлый раз видел, что..."
    mt "Я проводила презентацию с голой попой!"
    mt "Что он теперь подумает бо мне?!"
    mt "Я снова с почти голой попой!!!"
    mt "!!!"
    #
    mt "Я чувствую их мерзкие, липкие взгляды на моей... на моей спине!!"
    m "На этом графике вы можете наглядно увидеть..."
    m "Кхм..."
    # Моника поворачивается лицом к инвесторам
    philip "Рост биткоина, полагаю, Миссис Бакфетт?"
    m "Да, верно..."
    m "Как в прошлый раз мы с вами могли заметить, рост криптовалюты..."
    m "Зависит от роста продаж тиража моего журнала."
    m "И сейчас, глядя на этот график, мы можем увидеть..."
    m "Что рост идет вверх."
    campbell "Кхм..." # у Кэмбелла испанский стыд
    # слайд меняется на график schedule1
    # Моника косится на Бифа, тот снова жестом ей показывает, что надо повернуться
    m "!!!"
    # Моника поворачивается спиной
    m "На этом графике..."
    m "Помимо кривой роста моего журнала, отображается..."
    mt "Черт! Что здесь отображается?!"
    mt "?!?!?!"
    m "Здесь показано развитие наших конкурентов."
    m "Эта линия - продажи журнала Миссис Уайт..." # показывает на одну из линий внутри кривой, внизу графика
    m "А это - еще один журнал о моде..." # на другую линию внизу графика
    # она снова поворачивается лицом к ним
    m "Как видите, конкурентами назвать их сложно."
    m "Поскольку мы ушли далеко вперед и продолжаем расти и развиваться."
    m "Во многом наш рост обусловлен сменой курса журнала..."
    m "А также поддержкой наших инвесторов, которые поверили в мой журнал..."
    m "И дали ему дополнителную возможность для... для развития..."
    mt "Моника, какую же чушь ты несешь!"
    mt "Если бы ты была на месте инвесторов, то уже давно покинула бы это помещение!"
    mt "!!!"
    # слад меняется на schedule2
    # Моника снова вынуждена повернуться к экрану
    m "Еще один график и на нем отмечен пик роста..."
    m "Который произошел сразу же после нашей колоборации с Мистером Кэмпбеллом."
    campbell "Да, все верно, Миссис Бакфетт."
    campbell "Я рискнул и это оказалось действительно выгодным вложеним..."
    m "Мистер Кэмпбелл стал нашим первым инвестором..."
    m "Потом к нему присоединилиь Мистер Уильямс и Мистер Олаф..." # Мистер Уильямс - негр, кадр на него
    campbell "Кстати, а почему Олафа сегодня нет с нами?"
    # если Моника запрещала Олафу приближаться к отелю
    #
    $ notif(_("Моника запрещала Олафу приближаться к отелю."))
    #
    mt "Потому что этот жалкий тюфяк боится гнева Миссис Моники Бакфетт!"
    mt "Жалкий подкаблучник!"
    #
    m "..."
    biff "Мистер Олаф сегодня не смог приехать, о чем очень сожалеет..."
    biff "У него важная командировка и он не смог ее перенести."
    m "Да..."
    m "Итого, уже трое инвесторов сделали выгодное вложение..."
    m "И мы надеемся на положительное решение остальных господ..."
    # кадр на экране меняется на фоследний кадр с фотосессии, когда Моника отодвигала трусики для негра-инвестора
    # Моника этого не видит, так как стоит спиной к экрану
    # Биф мерзко улыбается
    investor3 "Прекрасная презентация, Миссис Бакфетт!"
    investor4 "О, да!"
    biff "Господа, Миссис Бакфетт решила сделать вам небольшой презент..."
    biff "Мы выпустили специальный ограниченный тираж номера..."
    biff "С самыми смелыми фотографиями Миссис Бакфетт."
    # Моника в шоке смотрит на него
    mt "ЧТО?!"
    biff "В общий тираж эти фотографии не вошли..."
    biff "И предназначены специально для вас, господа."
    biff "Номер разослан вам сегодня, чтобы вы после презентации смогли оценить эти великолепные кадры!"
    biff "Кстати, вот одни из них..." # показывает рукой на экран
    # Моника резко поворачивается
    m "БИФ!!!"
    m "!!!"
    # Биф смотрит на экран, потом на инвесторов
    biff "Господа, Миссис Бакфетт хотела, чтобы этот прекрасный кадр был сюрпризом для вас..."
    biff "При просмотре нашего журнала с ограниченным тиражом."
    biff "Но это всего лишь один из множества великолепных кадров..."
    biff "Так что, уверен, вы не будете разочарованы!"
    mt "Кретин!!!"
    mt "Убью!!!"
    mt "!!!"
    # Стив смотрит на Монику похотливым взглядом
    steve "Миссис Бакфетт, это прекрасный презент."
    steve "Скажите, а когда будет Ваша следующая фотосессия?"
    steve "Мы с удовольствием поприсутствуем на ней."
    investor3 "Да, я тоже хотел бы посмотреть, как вы проводите фотосессию, Миссис Бакфетт..."
    # Моника зло
    m "Я..."
    # Биф перебивает
    biff "Фотосессия запланирована на ближайшее будущее."
    biff "Но в качестве компенсации Миссис Бакфетт может вам, господа..."
    biff "Продемонстрировать свой профессионализм..."
    biff "И свою готовность следовать намеченному курсу журнала..."
    biff "Показав вам несколько поз, которые она подобрала для будущей фотосессии!"
    biff "Это будет очень оригинальная фотосессия! И смелая!"
    biff "Уверен, вы будете в восторге!"
    # смотрит на Монику
    biff "Миссис Бакфетт, вы можете начинать демонстрацию, которую вы хотели провести."
    m "Биф, я..."
    biff "Ну что вы, Миссис Бакфетт! Вам совершенно нечего стесняться!"
    biff "Здесь собрались серьезные люди!"
    biff "Они будут оценивать исключительно ваш профессионализм!"
    # Моника в растерянности
    mt "Боже! Какой-то кошмарный сон!"
    mt "Я должна позировать для этого стада баранов?!"
    mt "?!?!?!"
    mt "Как это все омерзительно!!!"
    mt "Я хочу поскорее завершить этот цирк и уйти отсюда!!!"
    mt "!!!"
    # Биф подходит к пуфу
    biff "Если вам удобно, Миссис Бакфетт, можете использовать это."
    # затемнение, звук посуды, каблуки
    # Моника стоит возле пуфа, бутылка и стаканы убраны с него
    philip "Миссис Бакфетт... Мы с нетерпением ждем демонстрации..."
    investor3 "Да, Миссис Бакфетт..."
    investor3 "Всегда приятно наблюдать за тем, как работает настоящий профессионал!"
    investor4 "Соглашусь."
    campbell "Можете приступать, Миссис Бакфетт."
    steve "Да, мы все заинтригованы!"
    # Моника зло на них смотрит
    menu:
        "Сесть на пуф и принимать различные позы.":
            $ monicaBiffInvestorsLeGrand3 = True # Моника провела презентацию и позировала для инвесторов в Ле Гранд
            pass
    # Моника медлит, смотрит на пуф
    mt "Биф! Ублюдок!"
    mt "И как я должна это делать?!"
    mt "!!!"
    mt "С другой стороны, если после этого я смогу уйти отсюда..."
    mt "То нужно сделать это скорее!"
    mt "Надеюсь, придурок Биф больше ничего не придумал!"
    mt "!!!"
    # Моника начинает позировать
    # инвестора пяляться на нее, Биф стоит довольный
    # Моника принимает несколько разных поз
    biff "Да, Миссис Бакфетт, это отличная поза!"
    biff "Она хорошо подойдет для запланированной фотосессии!"
    steve "Особенно с этого ракурса..."
    steve "Взгляните, господа!"
    investor3 "О, вы правы..."
    investor4 "Отличный ракурс!"
    steve "А если немного отставить ножку в сторону, Миссис Бакфетт?"
    # Моника отодвигает ногу
    mt "Этот жалкий мешок с дерьмом вздумал командовать мною?!"
    steve "Шикарно!"
    investor3 "А если немного нагнуться, то будет просто потрясающе смотреться!"
    mt "!!!"
    # Моника наклоняется
    campbell "Миссис Бакфетт, а теперь повернитесь к нам спиной..."
    campbell "Мне очень нравится Ваш сегодняшний наряд."
    campbell "Он меня вдохновил на создание новой коллекции..."
    # Моника поворачивается к ним попой
    investor3 "Миссис Бакфетт, Вы восхитительны."
    investor3 "Уверен, фотографу работать с Вами - одно удовольствие..."
    investor3 "Я мечтал бы оказаться на его месте..."
    mt "Да пошел ты, кретин!"
    mt "!!!"
    # Биф подходит к Монике
    biff "Господа, поблагодарим Миссис Бакфетт за блистательную демонстрацию!"
    biff "Спасибо, Миссис Бакфетт!"
    # мужчины аплодируют, Моника зла
    investor3 "Это было восхитительно, Миссис Бакфетт!"
    steve "Великолепно!"
    mt "Сборище жалких неудачников!"
    mt "Ненавижу всех до единого!"
    mt "Мерзкие извращенцы!"
    mt "!!!"
    # Биф с самодовольным лицом обращается к инвесторам
    biff "Господа..."
    biff "Мы с вами хорошо поработали сегодня."
    biff "Теперь пришло время немного расслабиться..."
    # Моника смотрит на него подозрительно
    mt "Что это значит?!"
    mt "Что этот клоун еще придумал?!"
    biff "Сейчас сюда придут девочки, которые работают в ВИП-эскорте этого прекрасного отеля..."
    biff "Они хотят нас немного нас развлечь."
    biff "За все уже оплачено, господа!"
    biff "Вам остается только расслабиться и насладиться обществом прекрасных дам."
    steve "Да, расслабиться не помешало бы... Ха-ха!"
    mt "!!!"
    mt "!!!!"
    mt "!!!!!"
    mt "Девочки из ВИП-эскорта?!"
    mt "?!?!?!"
    # если Моника раньше работала в эскорте и уволилась
    mt "АААА!!!"
    mt "НЕТ!!!"
    mt "Сучка администраторша говорила про важный заказ!"
    mt "Получается, что я должна быть здесь в качестве эскортнцы?!"
    mt "Моника! Пока тебя не увидели эти шлюхи из эскорта и администраторша!"
    mt "Беги, отсюда! Быстро!!!"
    mt "!!!"
    # если Моника не работала в эскорте
    mt "Этот идиот Биф совсем охренел?!"
    mt "Я не собираюсь принимать участия в этом!!!"
    mt "!!!"
    #
    menu:
        "Убежать!!!":
            pass
    # Моника быстро направляется к входной двери
    m "Господа, приятно было поработать с вами."
    m "Мне пора, у меня еще назначена встреча."
    m "По развитию журнала!"
    # Биф ей вслед
    biff "Миссис Бакфетт, не желаете остаться с нами?"
    m "Нет-нет! Спасибо!"
    m "Я..."
    m "Я уже опаздываю!"
    # звук открывающейся двери
    # Моника не успела убежать, в номер заходят админ и девочки-эскортницы
    reception "Добрый вечер, господа!"
    biff "здравствуйте, дамы!"
    biff "Проходите, мы вас уже ждем!"
    # они заходят, все бросают подозрительные взгляды на Монику
    reception "Наши лучшие девочки сегодня скрасят ваш вечер."
    # девочки встают в ряд перед экраном, Моника невольно оказывается в одном ряду с ними
    mt "Боже!"
    mt "Что же делать?!"
    mt "Я не могу остаться здесь!!!"
    reception "Можете выбрать себе любую понравившуюся вам девочку."
    reception "Или можете оставить всех пятерых..." # взляд на Монику
    mt "!!!"
    mt "Что мне теперь делать?!"
    mt "Это провал!!!"
    # Филипп поднимается со своего кресла и спрашивает у администратора
    philip "Мисс, можно вас на пару слов?"
    reception "Да, Мистер. Конечно."
    # они отходят в сторону
    # Филипп говорит, указывая на Монику
    philip "Я выбираю вот эту шлюху."
    philip "Я хотел бы остаться с ней наедине."
    philip "Поэтому забираю ее к себе."
    reception "Как пожелаете, Мистер."
    reception "Вы знаете, что по правилам нашего ВИП-эскорта выезд к клиенту опачивается по повышенному тарифу?"
    philip "Знаю. Деньги для меня не проблема."
    philip "Я готов заплатить за выезд."
    # Филипп подзывает кивком головы Монику, админша отходит
    # Моника подходит, она в растерянности
    philip "Я решил, что нам нужно кое-что обсудить."
    philip "Поэтому забираю вас отсюда..."
    # затемнение, лифт, мотор
    return

# Моника приходит на работу в эскорт после презентации
# ресепшн
label ep217_dialogues6_office_7:
    reception "[monica_hotel_name], ты в прошлый раз снова хотела меня обмануть?!"
    m "В смысле?"
    reception "Ты говорила мне, что не работала в тот вечер..."
    reception "А сама прибежала раньше всех девочек в номер к важным клиентам!"
    reception "Думала, что осилишь шестерых клиентов одна?!"
    reception "Ты переоцениваешь свои силы, [monica_hotel_name]!"
    reception "Ты шлюха с улицы, а девочки уже опытные и знают, как себя вести с такими важными господами!"
    reception "В следующий раз я накажу тебя за подобную самонадеянность!"
    m "Я не..."
    reception "И вообще! Где тот костюм, в котором ты была тогда?!"
    reception "Я жду, что ты его принесешь и отдашь для работы девочкам!"
    reception "Я тебе уже говорила, что реквизит ВИП-эскорта должны пополнять все девочки!"
    reception "Ты не исключение!"
    mt "Черт!"
    mt "!!!"
    m "Я принесу в следующий раз..."
    reception "Все, хватит болтать!"
    reception "Иди работай!"
    mt "Сучка!!!"
    mt "Ненавижу ее!!!"
    mt "!!!"
    return

# разговор с Бифом после презентации
label ep217_dialogues6_office_8:
    biff "А, цыпочка!"
    biff "Папочка доволен, как ты провела презентацию для денежных мешков!"
    biff "У тебя хорошо получилось притворяться сучкой Бакфетт!"
    biff "Еще немного, и все инвесторы будут у меня в кармане!"
    m "Ты заставил меня стоять перед ними в ужасно вульгарном костюме, Биф!"
    m "Так не ведутся дела в бизнесе!"
    biff "Главное, что наши многоуважаемые господа остались довольны!"
    m "И что еще за журнал с ограниченным тиражом?!"
    m "Почему я узнала об этом только на перезнтации?!"
    m "?!?!?!"
    biff "Так, я не понял!!!!"
    biff "Ты, кукла безмозглая, собралась учить своего Босса, как нажо вести дела?!"
    biff "Рот закрой и покажи, чем ты готова порадовать сегодня папочку!!!"
    mt "Мерзавец!"
    mt "Убью его!"
    mt "Сначала оторву ему яйца, а потом убью!!!"
    mt "!!!"
    # меню кастинга, кастинг.
    return
