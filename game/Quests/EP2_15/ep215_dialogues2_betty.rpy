default monicaBettyNeighbor1 = False # клик на соседа, квест с Бетти активирован
default monicaBettyNeighbor2 = False # Бетти решила отнести утюг соседу
default monicaBettyNeighbor3 = False # Бетти решила помочь Лиаму и показать, как пользоваться утюгом
default monicaBettyNeighbor4 = False # Бетти согласилась потрогать член Лиама
default monicaBettyNeighbor5 = False # у Бетти с соседом был секс



# при условии, что Моника уже спит с Ральфом
# в один из дней, когда Моника возвращается домой вечером
label ep215_dialogues2_betty_1:
    # во дворе дома Фред стоит возле машины рядом с ним стоит негр-сосед
    # они разговаривают о чем-то, смеются (вид со стороны)
    # Монику не показываем (вид из ее глаз)
    # Моника подозрительно
    img 19226
    mt "А этот неудачник что тут делает?!"
    mt "Я думала, что он уже не живет здесь!"
    mt "!!!"
    mt "Зачем он пришел?!"
    mt "Какие у него могут быть общие темы для разговора с Фредом?!"
    mt "..."
    mt "Я тогда хотела обратиться к своему адвокату (чертов Дик!!) и закатить ему иск..."
    #
    $ notif(_("Моника хотела закатить соседу иск на $ 100 000."))
    #
    img 19227
    mt "Вот черт!"
    mt "Что если он сейчас увидит меня! В такой одежде!"
    mt "Что он подумает обо мне?!"
    mt "?!?!?!"
    mt "Мне нужно незаметно пробежать мимо..."
    mt "Но если я узнаю, что мерзавец Фред что-нибудь рассказал этому никчемному соседу обо мне!"
    mt "Я ему оторву его корнишончик! Клянусь!"
    mt "!!!"
    # Моника быстро проходит в дом, отвернув лицо от Фреда с соседом
    # сосед стоит спиной к ней и не смотрит на нее
    # а Фред видит, как Моника пытается быть незаметной, и мерзко улыбается
    # Моника заходит дом
    img 19234
    # а Фред тем временем прощается с соседом
    img 19228
    liam "Эй, Фред, мне пора по делам!"
    liam "Загляну еще к тебе поболтать."
    img 19229
    fred "До встречи, Лиам."
    # сосед Лиам уходит
    # Фред смотрит на крыльцо, куда забежала Моника и мерзко улыбается
    $ monicaBettyNeighbor1 = True # клик на соседа, квест с Бетти активирован
    return

# после этого (на след. день-?) Моника заходит в любую локацию
# возникает надпись "Тем временем"
label ep215_dialogues2_betty_2:
    # показываем двор дома, сосед отходит от Фреда и идет к крыльцу
    # затемнение, звонок в дверь, звук шагов и звук открываемой двери
    # на крыльце стоит Бетти
    # сосед неуверенно
    img 19230
    w
    img 19231
    liam "Мэм... Добрый день!"
    # Бетти держится с ним высокомерно, как и полагается хозяйке богатого дома и порядочной жене
    img 19232
    betty "Вы кто?"
    liam "Я Лиам, живу в доме по-соседству..."
    betty "Здравствуйте, Лиам... Вы что-то хотели?"
    # Лиам чешет затылок и осматривает Бетти с головы до ног
    img 19233
    liam "Да, Мэм... Дело в том, что..."
    # Бетти вопросительно на него смотрит
    img 19235
    betty "Что?"
    img 19236
    liam "Понимаете, Мэм, у меня сгорел утюг..."
    liam "А мне надо ехать в банк... По поводу рассрочки по кредиту за мой дом..."
    liam "Мне надо произвести на менеджера должное впечатление..."
    img 19237
    liam "И я не могу поехать на встречу в мятых брюках..."
    liam "А у меня совсем не осталось времени на то, чтобы покупать другой утюг."
    img 19238
    betty "Вы хотите взять мой утюг?"
    img 19239
    liam "Да, Мэм... Всего на несколько минут..."
    betty "Лиам, я хозяйка богатого дома и такими вопросами занимается моя гувернантка."
    betty "Я помогла бы вам, но моей гувернантки сейчас нет дома."
    betty "Сожалею, но ничем не могу вам сейчас помочь."
    # затемнение, звук закрываемой двери
    # сосед стоит на крыльце один, расстроенно смотрит и уходит
    return

# показываем Бетти в доме
label ep215_dialogues2_betty_3:
    # Бетти стоит, как всегда, у зеркала и смотрит на себя
    img 14655
    betty_t "Этот Лиам думает, что всю работу по дому делаю я сама?"
    betty_t "У хозяйки такого роскошного дома всегда есть гувернантка!"
    betty_t "И ему совсем не обязательно знать, что Я все делаю по дому, а не эта нерадивая гувернантка!"
    betty_t "Все потому, что я порядочная жена и хорошая хозяйка!"
    menu:
        "Помочь соседу.":
            img 19246
            betty_t "Хммм..."
            betty_t "Теперь сосед будет думать, что я плохая хозяйка..."
            betty_t "Раз я не знаю, где в моем собственном доме находится утюг."
            betty_t "А это не так! Я хорошая хозяйка!"
            img 14656
            betty_t "Черт! Мне надо найти утюг и отнести ему!"
            betty_t "Там где я выросла, соседи приыкли поддерживать хорошие отношения и помогать друг другу."
            $ monicaBettyNeighbor2 = True # Бетти решила отнести утюг соседу
            pass
        "Это не мои проблемы! (прерывание квеста)":
            img 19246
            betty_t "И вообще, у меня есть другие важные дела!"
            betty_t "Почему я должна тратить свое время на него?!"
            return
    # Бетти выходит из комнаты
    # затемнение
    return

# Бетти с утюгом выходит во двор дома
label ep215_dialogues2_betty_4:
    # Фред стоит возле машины, Бетти подходит к нему
    img 19240
    betty "Фред, ты не знаешь, в каком доме живет наш сосед?"
    img 19241
    fred "Какой сосед, Миссис Робертс?"
    img 19242
    betty "Который сейчас приходил. По-моему, его зовут Лиам..."
    img 19243
    fred "Его дом сразу за забором, слева."
    img 19244
    betty "Спасибо, Фред."
    img 19245
    # она отходит от него и он, мерзко улыбаясь, смотрит ей вслед
    return

# надпись Несколько минут спустя...
# Бетти идет по двору дома соседа к крыльцу
# он стоит на крыльце, расстроенный, в трусах
label ep215_dialogues2_betty_5:
    # Бетти подходит к нему, в руках утюг
    # сосед удивленно
    liam "Мэм?!"
    betty "Лиам... Я все-таки решила помочь вам и нашла утюг. Берите."
    # он обрадованно
    liam "О, спасибо! Мэм, вы так выручили меня!"
    # а сам смотрит на утюг и хмурится
    betty "Что-то не так?"
    liam "Эээ..."
    liam "Здесь так много кнопок..."
    liam "Мэм, сможете показать мне, как его включить?"
    liam "Пожалуйста..."
    menu:
        "Помочь Лиаму.":
            $ monicaBettyNeighbor3 = True # Бетти решила помочь Лиаму и показать, как пользоваться утюгом
            pass
        "Сам разберется! (прерывание квеста)":
            betty "Там нет ничего сложного, поэтому вы сами сможете разобраться!"
            liam "Спасибо, Мэм..."
            # Бетти разворачивается и уходит, а он смотрит ей вслед
            return
    # Бетти задумчиво
    betty_t "Если я сейчас откажу ему, он подумает, что я сама не знаю, как пользоваться утюгом..."
    betty_t "А это не так! Я же хорошая хозяйка..."
    betty "Да, Лиам, я помогу вам."
    liam "Тогда проходите в дом, Мэм. Мы сразу включим утюг."
    # затемнение, звук двери, шаги
    # Бетти и Лиам стоят в его гостиной
    img 19247
    betty "Куда я могу включить утюг?"
    # Лиам рукой указывает в сторону
    # сам смотрит не на утюг, а на грудь Бетти
    img 19248
    liam "Вон там есть розетка, Мэм."
    img 19249
    # Бетти идет в сторону стены с розеткой, наклоняется, чтобы включить утюг (провода и включение не показываем)
    # сосед подходит к ней
    # Бетти стоит спиной к нему и объясняет как пользоваться утюгом
    # сосед стоит сразу сзади нее, прижимаясь
    img 19250
    w
    img 19251
    w
    img 19252
    betty "Смотрите, достаточно включить утюг..."
    betty "Потом эту кнопку повернуть сюда..."
    betty "А потом нажать вот сюда и гладить."
    img 19253
    liam "Это так сложно, Мэм..."
    liam "Я привык к старым железным утюгам, где была одна кнопка... Большая."
    # Бетти продолжает держаться с ним немного высокомерно, общается, как бы делая ему одолжение
    img 19254
    betty "Это современная тонкая техника."
    betty "В моих умелых руках она работает безотказно."
    # сосед смотрит на нее уже похотливо
    img 19255
    liam "Мэм, а я предпочитаю одну кнопку, зато большую."
    # сосед прижимается к ней сзади и она чувствует его стояк
    # на лице Бетти удивлениеи растерянность
    img 19256
    liam "Уверен, она тоже сработала бы безотказно и выполнила бы все нужные функции..."
    liam "Особенно, в таких умелых руках, как ваши, Мэм..."
    # Бетти поворачивается к нему, опускает взгляд и видит, что у него встал
    img 19257
    betty "..."
    menu:
        "Отказать ему!":
            pass
    # Бетти возмущена
    img 19258
    betty_t "Он что, пристает ко мне?!"
    betty_t "Да как он смеет?!"
    betty_t "Я порядочная женщина и верная жена!!!"
    # Бетти поспешно ставит утюг и идет к двери
    img 19259
    betty "Мне срочно нужно идти!"
    liam "Мэээм! Я принесу вам утюг завтра!"
    liam "Спасибо, Мэм!"
    # Бетти с возмущенным видом уходит
    return

# после этого игра переключается на события с Моникой

# на след. день, когда Моника кликает на любую локацию и хочет выйти из дома
# возникает надпись "Тем временем"
# Бетти стучится в дверь соседского дома
label ep215_dialogues2_betty_6:
    # затемнение, звук двери, шаги
    # Бетти и Лиам стоят в гостиной его дома
    # Лиам удивлен ее визиту
    img 19260
    liam "Мэм? Рад вас видеть."
    # Бетти общается высокомерно
    betty "Добрый день."
    betty "Я... Я пришла за утюгом..."
    img 19261
    liam "Не стоило утруждаться, Мэм."
    liam "Я сам собирался принести вам утюг."
    # Бетти мнется
    img 19262
    betty "Я сделала это, потому что у меня..."
    betty "У меня сегодня запланировано много дел..."
    betty "Мне нужно успеть много чего перегладить для своего мужа Ральфа."
    betty "Вы принесли бы мне утюг, а я была бы уже не успела этого сделать..."
    # сосед улыбается
    img 19263
    liam "Мэм очень милая и заботливая!"
    liam "Я завидую вашему мужу, Мэм."
    liam "У него такая красивая и такая порядочная жена!"
    liam "К тому же еще и хорошая хозяйка!"
    # Бетти нравятся его комплименты, она горделиво улыбается
    img 19264
    betty "Да, я очень порядочная женщина и хорошая хозяйка!"
    betty "А вы смогли разобраться с кнопками, Лиам?"
    img 19265
    liam "Да, Мэм... Как вы и говорили, ничего сложного."
    liam "Я нажал на все кнопки и утюг стал нагреваться."
    liam "Так что принцип действия такой же, как и с одной большой кнопкой, Мэм..."
    # он кладет руку себе на пояс, а Бетти смотрит ему в область паха, потом снова на него
    img 19266
    w
    img 19267
    betty "..."
    img 19268
    liam "Вы вчера так выручили меня, Мэм..."
    liam "Ваши умелые ручки так ловко управляются с кнопочками..."
    liam "Не хотите помочь мне еще с одной проблемой, Мэм? По-соседски?"

    # с этого момента можно начать повторную сцену, если Бетти отказалась сначала
    img 19269
    betty "Помочь? С чем помочь, Лиам?"
    betty "У вас какие-то проблемы?"
    # сосед неуверенно
    img 19270
    liam "Да, Мэм. У меня имеется одна достаточно большая проблема..."
    liam "Я могу обратиться с этой просьбой только к хорошему человеку..."
    liam "А точнее, к хорошей соседке... Такой как вы, Мэм."
    # Бетти озабоченно
    img 19271
    betty "Лиам, расскажете мне о своей проблеме?"
    liam "Да, Мэм. Эта проблема меня давно терзает..."
    liam "Мне когда-то давно одна женщина сказала об этом..."
    liam "Я даже ходил к врачам, но они сказали, что не могут мне помочь."
    img 19272
    liam "Еще врачи сказали, что для решения этой проблемы надо, чтобы..."
    liam "Чтобы кто-то другой опроверг мнение той женщины."
    liam "По этому поводу у меня сильные душевные расстройства."
    liam "Я даже не сплю по ночам, Мэм..."
    img 19273
    betty "Все настолько серьезно?"
    liam "Да, Мэм..."
    betty "А что это за проблема, Лиам?"
    # сосед мнется, потом смущенно говорит
    img 19274
    liam "Кхм..."
    liam "Мне так неудобно говорить об этом..."
    liam "Я так переживаю, что вы не сможете опровергнуть слова той женщины..."
    liam "Мне... У меня..."
    img 19275
    betty "Говорите смелее, не переживайте."
    liam "Мне кажется, что он у меня недостаточно твердый..."
    # сосед приспускает штаны и достает свой большой член
    
    liam "Вот. Посмотрите, Мэм."
    # Бетти удивленно смотрит на его член
    betty "И? С какой стати вы думаете, что я могу помочь?"
    liam "Вы же не оставите в беде своего соседа, Мэм..."
    # Бетти не отводит глаз от его члена
    betty "Ну..."
    betty "На вид он достаточно упругий."
    # Лиам расстроенно
    liam "Мэм, я вижу, что вы говорите это, чтобы просто меня утешить..."
    liam "На самом деле вы так не считаете, Мэм."
    liam "А это значит, что теперь уже две женщины считают, что это так!"
    liam "Теперь я совсем потеряю сон!"
    # Бетти продолжает смотреть на его член
    betty "Лиам, я говорю то, что вижу."
    betty "Ваш член выглядит вполне упругим."
    # Лиам все также расстроен
    liam "Я уверен, Мэм, вы так не стали бы говорить, если потрогали бы его..."
    betty "Я? Что?"
    betty "Потрогать?"
    menu:
        "Я просто потрогаю и все.":
            $ monicaBettyNeighbor4 = True # Бетти согласилась потрогать член Лиам
            pass
        "Нет! Я не буду этого делать! (прерывание квеста)":
            # Бетти встает руки в боки, возмущенно
            betty "Как вы можете мне предлагать подобные вещи?!"
            betty "Я верная жена и порядочная женщина!"
            betty "Вы придумали сами себе какую-то нелепую проблему!"
            betty "Вот сами с этим и разбирайтесь!"
            betty "Где мой утюг?!"
            # сосед отходит к столу и возвращается с утюгом
            liam "Вот он, Мэм. Спасибо вам, Мэм..."
            # Бетти разворачивается и уходит возмущенно, а он смотрит ей вслед
            return
    # Бетти не в силах отвести взгляд от члена соседа, но продолжает ломаться
    liam "Да, Мэм. Только потрогать."
    # Бетти возмущается
    betty "Я не собираюсь прикасаться к вам ТАМ!"
    betty "Вообще-то, у меня есть муж!"
    liam "Мэм, если вы прикоснетесь к нему своими умелыми ручками..."
    liam "И скажете, что он упругий, то я поверю вам, Мэм."
    liam "И тогда, возможно, моя проблема перестанет терзать меня..."
    liam "При всем уважении к вашему мужу, это не касается отношений между людьми."
    liam "Вы сейчас мой врач, а я ваш пациент!"
    # Бетти смотрит на него пристально
    betty_y "Я - врач? Никогда не была в такой роли..."
    betty_t "Если я просто к нему прикоснусь, это ведь не измена мужу."
    betty_t "Я ведь порядочная женщина и верная жена!"
    betty_t "Это же не секс, а просто прикосновение... Это не считается..."
    betty_t "Тем более, я помогаю больному человеку! Тем более, соседу!"
    batty_t "Как врач."
    # Бетти неотрывно смотрит на член соседа и тянет руку к его члену
    betty "Учтите, Лиам! Я его потрогаю, но совсем чуть-чуть!"
    # проводит пальцами по члену
    betty "Не более того!"
    # снова проводит
    betty "И я не собираюсь больше ничего с ним делать!"
    # обхватывает его рукой
    liam "Конечно, Мэм..."
    liam "Как скажете, Мэм."
    # Бетти проводит рукой по члену вверх-вниз
    betty "Он у вас очень упругий и вам не о чем переживать, Лиам."
    betty "Я уже достаточно его потрогала!"
    betty "И больше не собираюсь прикасаться к нему!"
    # а сама продолжает водить рукой по нему
    liam "Мммэм... Я так рад это слышать от вас..."
    liam "Вы такая замечательная соседка, Мэм..."
    # Бетти продолжает наяривать ему рукой
    betty "И помогаю вам только по-соседски!"
    liam "Да, Мэм... Вы такая заботливая!"
    betty "Больше подобных просьб я не желаю слышать, Лиам!"
    betty "У меня есть муж! Я ему никогда и ни с кем не изменяла!"
    betty "И не собираюсь этого делать!"
    # продолжает дрочить
    liam "Даааа... Мээээм..."
    liam "Хотите попробовать, какой он на вкус?"
    menu:
        "Конечно, нет!":
            pass
    # Бетти возмущенно, продолжая работать рукой
    betty "Конечно, нет!!!"
    betty "Что за глупости?!"
    # сама наклоняетя к его члену
    betty "Почему я должна хотеть этого?!"
    # а сама уже облизывает его
    betty "Ммммм... Мне совершенно это не интересно!"
    liam "Оооо! Мээээм!!!"
    # Бетти делает несколько движений головой, сосед кайфует
    liam "Мэээм, как вы думаете, мой член достаточно твердый..."
    liam "Чтобы войти в вас? Ооооо!!!"
    # Бетти отрывается от него
    betty "Войти в меня?!"
    betty "Это же измена!"
    betty "А я верная жена своего мужа!"
    liam "Мэм, я ведь только попробую, войдет или нет."
    liam "И сразу уберу его! Обещаю, Мэм!"
    menu:
        "Я верная жена!":
            $ monicaBettyNeighbor5 = True # у Бетти с соседом был секс
            pass
        "Нет! Я не буду этого делать! (прерывание квеста)":
            # Бетти встает руки в боки, возмущенно
            betty "Как вы можете мне предлагать подобные вещи?!"
            betty "Я верная жена и порядочная женщина!"
            betty "Вы придумали сами себе какую-то нелепую проблему!"
            betty "Вот сами с этим и разбирайтесь!"
            betty "Где мой утюг?!"
            # сосед отходит к столу и возвращается с утюгом
            liam "Вот он, Мэм. Спасибо вам, Мэм..."
            # Бетти разворачивается и уходит возмущенно, а он смотрит ей вслед
            return
    # Бетти смотрит на его член
    betty_t "Я же помогаю человеку, который долгое время терзался своей проблемой."
    betty_t "Он ведь просто попробует и сразу уберет свой член..."
    betty_t "Это же не измена. Это помощь соседу."
    betty "Лиам, я верная жена и не собираюсь изменять своему мужу!"
    betty "Так что ты быстро попробуешь и сразу же уберешь его, ясно?"
    liam "Я так и сделаю, Мэм!"
    betty "Хорошо, но только быстро!"
    betty "Меня ждет мой муж! Я должна приготовить ему обед!"
    liam "Конечно, Мэм!"
    liam "Ложитесь на диван, Мэм."
    liam "Так мне будет намного удобнее."
    # Бетти ложится на диван и задирает платье
    # Лиам смотрит на ее голую киску

    # если Барди заставляет ходить без трусиков
    liam "Вы не носите трусики, Мэм?"
    betty "Я делаю это для своего мужа! Ему так нравится!"
    #
    $ notif(_("Бетти не носит трусики по приказу Барди."))
    #
    #

    liam "Ваш муж счастливчик, Мэм!"
    liam "Хотел бы я быть на его месте!"
    liam "О такой жене, как вы, можно только мечтать!"
    betty "Да, это так!"
    liam "Раздвиньте ваши ножки пошире, Мэм..."
    # Бетти раздвигает, сама неотрывно смотрит на член соседа
    liam "У вас такая киска... Мммм..."
    liam "Так и хочется скорее почувствовать себя внутри ее!"
    # нацеливает член на киску Бетти
    betty "Помнишь, что ты только пробуешь?!"
    betty "Один раз!"
    betty "Потом сразу уберешь свой член!"
    betty "Я не собираюсь изменять своему мужу с каким-то соседом!"
    liam "Да, конечно помню, Мэм!"
    # вводит головку в киску
    betty "Ооооох..."
    liam "Еще немного, Мэм..."
    liam "Я еще не распробовал..."
    # входит в нее полностью
    liam "Даааа! О, даааа!"
    liam "Мээээммммм..."
    betty "Оооо!!! Оооодин раз!"
    # он выходит из нее, но не полностью
    # Бетти требовательно
    betty "Я сказала только один раз, ты помнишь?!"

#    betty "Еще один раз попробуй, чтобы уж точно удостовериться!"
    liam "Да, Мэм!!!"
    liam "Но ведь я не вынул его!"
    liam "Мне надо его хорошенько ввести и подобрать удобное положение."
    liam "После этого я сразу выну его и это будет как раз один раз, который вы мне разрешили, Мэм!"
    betty "Давай быстрее подбирай свое удобное положение и вытаскивай его!"
    betty "Я верная жена и не собираюсь изменять своему мужу, я уже говрила тебе!"

    # снова вводит член
    betty "Аааааах!!!"
    liam "Дааааа, как же хорошо у вас внутри, Мэм!"
    betty "Мммммм!!! Даааа..."
    liam "Нет, так тоже неудобно, надо сдвинуть левее..."
    # продолжает жарить

    # Бетти поплыла, секс
    betty "Дааа! Еще!!!"
    liam "ООООО!!!"
    liam "Вот так удобнее, Мэм!"
    betty "Еще-еще!!!"
    betty "Быстрее!!!"
    liam "Я почти подобрал удобное положение, Мэм!"
    betty "Аааааах!!!"
    liam "О, Мээээм! Кончайте, Мэм!"
    # Бетти кончает
    betty "Ооооох!!!"
    betty "ОООООО!!!"
    menu:
        "Кончить внутрь Бетти.":
            liam "Я тоже сейчааааас!!!"
            liam "Кончаааааююююю!!!"
            betty "Не вздумай кончать в меня!"
            liam "ААА!"
            liam "АААААА!!"
            liam "ААААААААА!!!"
            betty "Черт! Сказала же, не в меня!!!"
            pass
        "Кончить на киску Бетти.":
            liam "Я тоже сейчааааас!!!"
            liam "Кончаааааююююю!!!"
            betty "Не вздумай кончать в меня!"
            liam "ААА!"
            liam "АААААА!!"
            liam "ААААААААА!!!"
            betty "Черт! Сказала же, не в меня!!!"
            pass
    # затемнение
    # Бетти лежит прибалдевшая на диване, сосед стоит рядом
    # стук в дверь, голос из-за двери
    fred "Миссис Робертс!"
    # Бетти подрывается с дивана
    betty "ЧЕРТ!"
    fred "Миссис Робертс, вас ищет ваш муж!"
    fred "Вы тут, Миссис Робертс?!"
    betty "Мне надо бежать!"
    betty "Чтобы никому ни слова о моей помощи!"
    # Бетти убегает, он смотрит ей вслед
    # забытый утюг остается стоять на столе у соседа
    # отдельно показать это
    return

# сразу после секса с соседом
# гостиная дома
label ep215_dialogues2_betty_7:
    # Ральф стоит посреди гостиной
    ralph "Бетти, дорогая, ты где была?"
    ralph "Я тебя везде искал."
    betty "Ральф, у меня были дела."
    menu:
        "Поцеловать Ральфа в губы.":
            # Бетти приближает свои губы к губам Ральфа
            # целует его
            pass
        "Не целовать.":
            betty "Ты же знаешь, что я занятая женщина, Ральф!"
            betty "Не могу же я весь день сидеть возле тебя!"
            ralph "Да, дорогая, конечно."
            pass
    # кадр на ноги Бетти - по бедру стекает сперма соседа
    betty "Сейчас я приготовлю тебе обед."
    betty "Подожди немного."
    ralph "Хорошо, дорогая."
    return
