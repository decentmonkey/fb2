default monicaFredPhoto1 = False  # Моника попросила Фреда дождаться ее ответа и не показывать фото никому
default monicaFredPhoto2 = False  # Моника сказала Юлии, что хочет попробовать ее киску
default monicaFredPhoto3 = False  # Моника решила вступить в отношения с Юлией
# коммит


# после второго свидания Моники и Юлии
# офис Моники
# Моника сталкивается с Фредом.
label ep212_dialogues5_julia_1:
    img_20870
    m "!!!"
    m "Фред?!"
    img_30300
    mt "Опять этот мерзавец здесь!"
    # Фред со своей улыбочкой
    img_30301
    fred "Миссис Бакфетт, рад Вас видеть."
    fred "Я бы с удовольствием пообщался с Вами, но у меня дела."
    # Моника подозрительно
    img_30302
    m "Какие дела могут быть у никчемного водителя в МОЕМ офисе?"
    m "Что ты тут делаешь?!"
    m "???"
    img_30303
    fred "Мне нужно показать кое-что Вашим подчиненным, Миссис Бакфетт..."
    m "О чем это ты?"
    fred "У меня есть очень интересная фотография."
    img_30304
    m "Какая?"
    fred "О, не беспокойтесь Миссис Бакфетт. Ничего особенного..."
    img_30305
    # Моника смотрит на него с подозрением, он показывает фото на своем телефоне (Моника чистит ковер, на ней нет трусиков)
    img_30306
    m "ЧТООООО?!"
    m "?!?!?!"
    m "ФРЕД!"
    img_20871
    fred "Это одна из моих любимых фотографий, Миссис Бакфетт..."
    fred "Уверен, Вашим сотрудникам она тоже понравится."
    img_20872
    m "Ты!"
    m "!!!!"
    m "Когда ты сделал это фото?!"
    img_20873
    fred "В прошлый раз Вы были так заняты чисткой ковра, Миссис Бакфетт..."
    fred "Что даже не заметили, как я Вас сфотографировал."
    img_30307
    m "Не смей это никому показывать!!!"
    m "!!!"
    img_30308
    fred "Но как же, Миссис Бакфетт? У нас с Вами была договоренность..."
    fred "Но Вы, Миссис Бакфетт, недостаточно серьезно отнеслись к моей небольшой просьбе..."
    fred "Это непрофессионально с Вашей стороны."
    fred "Я решил, что итак дал Вам слишком много времени..."
    img_30309
    fred "Более не вижу смысла ждать ответа от Вас."
    fred "Думаю, на этом мы с Вами закончим нашу небольшую игру."
    fred "До свидания, Миссис Бакфетт."
    # Фред делает шаг в сторону столов сотрудников
    img_30310
    m "СТОП!"
    # Фред останавливается и с улыбочкой смотрит на Монику
    # Моника бесится
    img_30311
    mt "Сволочь!!!"
    mt "А если бы я сейчас не оказалась здесь?!"
    mt "Он... Он показал бы ЭТО всем?!"
    mt "?!?!?!"
    mt "ААААААА!!!!"
    mt "Я убью этого мерзавца!"
    menu:
        "Выгнать этого мерзавца! (прерывание квеста)":
            # Моника орет на Фреда
            img_30312
            m "ФРЕД!!!"
            m "Как ты смеешь вести себя подобным образом?!"
            m "Кто ТЫ и кто Я!!!"
            m "!!!"
            img_30313
            m "Я - Моника Бакфетт!!!"
            m "И мне плевать на то, что ты кому-то покажешь это фото!"
            m "Ты просто какой-то никчемный водитель!!! Тебе никто не поверит!"
            m "Я всем скажу, что ты шантажируешь меня, подделав фото!"
            img_30314
            fred "Миссис Бакфетт, я..."
            img_30315
            m "Молчать!"
            m "Пошел вон отсюда!!!"
            m "Еще раз здесь тебя увижу - вызову охрану!!!"
            m "Жалкий водитель!"
            img_30316
            fred "..." # Фред уходит
            return
        "Попытаться договориться с Фредом.":
            $ monicaFredPhoto1 = True # Моника попросила Фреда дождаться ее ответа и не показывать фото никому
            pass
    img_30317
    mt "Я не могу допустить, чтобы эту фотографию кто-либо увидел!"
    mt "Никто не должен знать о моих временных трудностях..."
    img_30318
    m "Фред..."
    fred "Да, Миссис Бакфетт?"
    m "Я не забыла о твоей просьбе..."
    img_30319
    fred "Если это было так, Миссис Бакфетт, то я давно получил бы ответ на свой вопрос."
    m "Фред, это не так просто, как может показаться."
    m "Я и так выгляжу как какая-то лесбиянка, а все из-за твоего глупого задания!"
    img_30320
    fred "Нет, Миссис Бакфетт. Это не глупое задание."
    m "..." # недовольно
    img_30321
    fred "Хорошо, Миссис Бакфетт."
    fred "Я готов пойти Вам навстречу, но только потому, что хорошо к Вам отношусь."
    fred "Более того, чем требует мой профессионализм."
    img_30313
    mt "Мерзавец!"
    img_30322
    fred "Я дам Вам последний шанс."
    fred "Я жду ответ в ближайшее время."
    fred "Если Вы поступите непрофессионально. Не дадите ответ или попытаетесь обмануть меня..."
    img_30323
    fred "В таком случае, я более не считаю своим профессиональным долгом скрывать это фото..."
    fred "Желаю удачи, Миссис Бакфетт."
    # Фред уходит, Монику бомбит
    img_30324
    mt "Как он посмел!"
    mt "Ни в коем случае нельзя допустить, чтобы мою фотографию кто-то увидел!"
    mt "Пора прекращать весь этот цирк с никчемной Юлией и мерзавцем Фредом!"
    mt "!!!"
    img_30325
    mt "Когда закончатся мои временные трудности..."
    mt "Я убью этого никчемного корнишона!"
    mt "Сначала оторву ему яйца, а потом убью!"
    mt "!!!"
    return

# Кабинет Моники
# частично взять из имеющихся артов
label ep212_dialogues5_julia_2:
    # Моника у себя в кабинете, сидит за столом
    img_20886
    mt "Как меня достала вся эта глупая ситуация с трусиками никчемной Юлии!"
    mt "Мне нужно прекращать этот цирк как можно скорее!"
    mt "И слать ко всем чертям эту дурочку Юлию и мерзавца корнишона!"
    mt "!!!"
    img_20362
    mt "Я вижу только один вариант..."
    mt "Мне нужно сегодня попасть домой к Юлии..."
    mt "И, наконец, узнать чертов цвет ее чертовых трусиков!"
    # Моника выдавливает из себя улыбку и подходит к Юлии
    img_16496
    w
    img_16497
    m "Милая, я так соскучилась по тебе..."
    img_16499
    julia "Миссис Бакфетт..."
    julia "И я по Вам соскучилась... Очень..."
    # обнимашки-целовашки, Юлия довольная
    img_16498
    w
    img_16486
    m "Мне так хочется побыть с тобой наедине, милая."
    m "А тебе?"
    img_16487
    julia "И мне, Миссис Бакфетт."
    julia "Только... Где мы сможем уединиться?" # смущенно
    julia "Не в моей же квартире..."
    julia "Думаю, Вам не захочется возвращаться туда снова..."
    menu:
        "Конечно, у тебя ужасная квартира, но я готова потерпеть.":
            pass
    img_16482
    m "Милая, ты же понимаешь, что такой женщине, как Я, не может понравится у тебя в гостях..."
    m "Я не привыкла бывать в подобных местах и..."
    m "Я вообще не понимаю, как можно там жить."
    julia "..."
    img_16483
    m "Но я готова все это потерпеть ради тебя..."
    m "Милая..."
    img_16484
    julia "М-Миссис Бакфетт, я не хочу, чтобы Вы испытывали неудобства."
    julia "Будет лучше, если мы будем проводить время не в моей квартире."
    julia "Может быть, Вы пригласите меня к себе?"
    img_16485
    mt "Черт!"
    mt "!!!"
    menu:
        "Знаешь, у тебя очень уютно в квартире.":
            pass
    img_16488
    m "Знаешь, что? Несмотря на все, твоя квартира мне показалась очень уютной."
    julia "Правда?"
    m "Да, милая."
    img_30326
    julia "Но... Вы же сказали, что Вам не понравилось у меня в гостях..."
    m "Мне... Мне просто немного непривычно, но не более того."
    julia "..."
    img_30327
    mt "И? Чего эта дурочка молчит?"
    mt "Я ее еще и должна уговаривать?"
    img_30328
    m "..." # целует ее
    img_30329
    m "Я могла бы прийти к тебе в гости сегодня после работы..."
    julia "Я..."
    julia "..."
    m "Ты не хочешь, чтобы я к тебе приходила, милая?"
    img_30330
    julia "Хочу, конечно!"
    img_30331
    julia "Миссис Бакфетт, просто мне так неудобно..."
    julia "Моя квартира не сравнится с Вашим прекрасным домом."
    img_30332
    m "Все в порядке, милая. Не переживай."
    m "Я приду вечером и мы устроим с тобой романтическую встречу."
    # Юлия смотрит на нее радостно
    img_30333
    julia "Да, хорошо, Миссис Бакфетт."
    m "Будешь меня ждать?"
    julia "Конечно, Миссис Бакфетт."
    # снова поцелуй
    img_30334
    w
    img_16489
    mt "На этот раз ты от меня не отвертишься, никчемная Юлия."
    $ log1 = _("Пойти к Юлии домой после работы.")
    return

# при клике на Юлию после назначения встречи
label ep212_dialogues5_julia_2_1:
    julia "Миссис Бакфетт, я не могу дождаться вечера!"
    julia "Так хочется побыть с Вами наедине!"
    return

# Кабинет Моники
label ep212_dialogues5_julia_2_2:
    # не рендерить!!
    # вечер, конец рабочего дня, Юлии нет на месте
    
    mt "Сейчас мне нужно идти к Юлии домой."
    mt "Если я сегодня не узнаю цвет ее никчемных трусиков, то Фред покажет всем мое фото..."
    mt "Я даже боюсь думать о последствиях!"
    return

# Квартира Юлии
label ep212_dialogues5_julia_3:
    # Моника заходит в квартиру Юлии
    # Юлия довольная
    img_30337
    julia "Миссис Бакфетт, я так рада, что Вы ко мне пришли!"
    julia "Я переживала, что Вы передумаете и не придете."
    img_30338
    m "Ну что ты, милая. Как ты могла об этом подумать?"
    m "Ты же знаешь о моих чувствах к тебе."
    m "Мне приятно проводить с тобой время... Обнимать тебя... Целовать..."
    img_30339
    julia "О, Миссис Бакфетт!"
    julia "!!!"
    img_30340
    mt "Как же меня достало притворяться влюбленной дурой и нести эту чушь!"
    mt "Надеюсь, это последний вечер, когда я вынуждена притворяться..."
    mt "Перед своей бывшей гувернанткой..."
    # Моника подходит к ней, обнимает и целуя, опускает свою руку ей на попу и далее все ниже и ниже, приподнимая платье
    img_30341
    w
    img_30342
    w
    img_23585
    w
    img_23586
    w
    img_23587
    m "Юлия... Милая..."
    # Юлия снова отстраняется
    img_23588
    w
    img_30343
    julia "Миссис Бакфетт, Вы..."
    julia "Вы снова хотите потрогать мои трусики?"
    img_30344
    mt "Ну начинается..."
    # Моника выдавливает из себя улыбку
    img_30345
    m "Да, милая. Мне очень приятно прикасаться к тебе и..."
    m "Я хотела бы большего..."
    # Юлия растеряна
    img_30346
    julia "Б-большего?"
    julia "Миссис Бакфетт, Вы уверены?"
    julia "Вы - леди из высшего общества, а я простая девушка..."
    julia "Которая работает у Вас в подчинении."
    img_30347
    m "Да, милая, я уверена в своих чувствах к тебе."
    julia "Вы поэтому постоянно хотите посмотреть на мои трусики?"
    img_30348
    julia "Это просто предлог, чтобы попробовать мою... мою киску?"
    # Моника притворно улыбается
    img_30349
    mt "О Боже! Какая гадость!"
    mt "Моника, неужели тебе придется смотреть на киску этой никчемной Юлии?!"
    mt "Еще и делать вид, что тебе это приятно?"
    mt "..."
    menu:
        "Продолжать притворяться.":
            $ monicaFredPhoto2 = True # Моника сказала Юлии, что хочет попробовать ее киску
            pass
        "Нет! Я не хочу этого! (завершение сюжета с Юлией)":
            img_30350
            w
            img_30351
            mt "Нет!!!" # сердито
            mt "Мне надоело заниматься этими глупостями!"
            img_23598
            m "Знаешь, Юлия, у меня сегодня еще много дел."
            m "Так что, я пойду."
            img_30352
            julia "Но... Миссис Бакфетт!"
            julia "Это из-за того, что я..."
            julia "Постоянно Вам отказываю?"
            img_23600
            m "Это уже не имеет значения!"
            m "Забудь все, что было!"
            m "Увидимся на работе."
            img_23606
            julia "..."
            # Моника уходит, Юлия расстроена
            return
    img_30353
    m "Милая, я очень давно этого хочу..."
    # Юлия все еще не верит, с сомнением
    img_30354
    julia "Давно? А с какого времени? С того, как я у Вас работала гувернанткой?"
    m "Да, еще с того времени."

    # если заставляла оттирать ковер
    $ notif(_("Моника заставляла Юлию оттирать пятно на ковре"))
    img_30355
    m "Я не понимала тогда своих чувств..."
    m "Поэтому иногда злилась на тебя."
    m "Я просто была растеряна и не знала, что мне делать."

    # если НЕ заставляла оттирать ковер
    $ notif(_("Моника не заставляла Юлию оттирать пятно на ковре"))
    img_30355
    m "Именно поэтому я простила тебе тогда за то пятно на ковре."
    m "И не стала тебя наказывать."
    img_30356
    julia "Правда?"
    m "Да, милая..."
    m "Я просто уже не могу дождаться этого момента."
    # Юлия смотрит на Монику влюбленным взглядом
    img_30357
    m "Ты мне веришь, Юлия? Веришь, что ты мне и правда нравишься?"
    # Юлия думает и сомневается
    img_30358
    julia "Я..."
    julia "Я даже не знаю..."
    julia "..."
    m "..."
    img_30359
    julia "Миссис Бакфетт, я даже и мечтать не могла о таком..."
    julia "Неужели, мне это не снится?"
    img_30360
    m "Это не сон, милая."
    julia "Миссис Бакфетт..."
    julia "Я правда, правда начинаю Вам доверять намного больше..."
    # Моника про себя торжествует
    img_30361
    mt "Неужели?! Наконец-то!!!"
    mt "Этот цирк сегодня закончится!!!"
    # Пытается ее обнять и поднять юбку
    img_30362
    w
    img_30363
    w
    img_30364
    m "Юлия, иди ко мне..."
    # Юлия смущенно, отстраняясь
    img_30365
    w
    img_30366
    julia "Миссис Бакфетт, мне надо отлучиться на минутку..."
    julia "Я сейчас вернусь."
    # Юлия выходит из комнаты, Моника садится на ее кровать и ждет
    img_30367
    mt "Все что мне надо - это цвет ее гребаных трусиков."
    mt "Как только увижу, какого они цвета..."
    img_30368
    mt "Укажу своей никчемной бывшей гувернантке на ее место!"
    mt "Возомнила из себя героиню романа! Наивная дурочка!"
    img_30369
    mt "Да кто она такая, чтобы сама Моника Бакфетт говорила с ней о каких-то чувствах! Фи!"
    return

# Квартира Юлии
label ep212_dialogues5_julia_4:
    # Моника сидит у Юлии в комнате на кровати и ждет ее
    # проходит несколько минут
    # Юлия выходит смущенная из душа в полотенце, руки за спиной
    # Моника протягивает ей руку
    img_30370
    w
    img_30371
    w
    img_30372
    w
    img_30373
    m "Иди сюда, милая. Не стесняйся."
    m "Я так давно ждала этого момента..."
    # Юлия смущаясь протягивает ей свою руку и Моника притягивает ее к себе
    # поцелуй
    # Юлия садится на кровать, а Моника опускается на колени перед ней
    # кладет ладони на бедра Юлии и медленно поднимает их все выше и выше
    img_30374
    w
    img_30375
    w
    img_30376
    w
    img_30377
    w
    img_30378
    mt "Этот момент сейчас настанет!"
    mt "Еще немного и корнишон вместе с Юлией пойдут ко все чертям!!!"
    # вот она уже прикоснулась к полотенцу и продолжает движение ладонями, приподнимая полотенце
    # Юлия сидит смущается, но не сопротивляется
    # ладони Моники поднимаются еще выше, она задирает полотенце и видит перед собой голую киску Юлии
    # Моника в ступоре
    img_30379
    w
    img_30380
    w
    img_30381
    w
    img_30382
    mt "Какого черта?!"
    mt "?!?!?!"
    img_30383
    mt "Твою мать!!!!"
    mt "!!!"
    img_30384
    mt "Так, Моника, спокойно!"
    mt "Нельзя, чтобы она поняла, что кроме ее гребанных трусиков тебе больше ничего от нее не нужно!"
    img_30385
    julia "Миссис Бакфетт, Вам нравится моя киска?"
    julia "Я так мечтаю, чтобы Вы прикоснулись к ней своими губами..."
    julia "Я так этого хочу..."
    # Моника смотрит в шоке на киску Юлии, потом поднимает глаза на нее, лицо напряжено "эм. подозрительность"
    img_30386
    m "..."
    julia "У Вас такой вид..."
    julia "Вы же не передумали, Миссис Бакфетт?"
    menu:
        "Черт! Нет, я не передумала!":
            pass
    img_30387
    m "Конечно, не передумала..."
    m "Милая, а где твои трусики? Я хочу на них посмотреть..."
    # Юлия удивленно
    img_30388
    julia "Миссис Бакфетт, я же только что вышла из душа..."
    # Моника перебивает ее, смотрит в сторону ванной, камера издалека
    img_30389
    m "Значит, твои трусики в ванной?"
    img_30390
    julia "Нет, Миссис Бакфетт..."
    julia "Моя киска перед Вами..."
    julia "Зачем Вам мои трусики?"
    # Моника снова смотрит на ее киску
    img_30391
    m "..."
    img_30392
    mt "Дъявол!"
    mt "И что мне теперь делать?"
    mt "Как бы отсюда быстрее свалить!"
    mt "Я не хочу приближаться к ее... киске."
    mt "Какая гадость! Фу!"
    img_30393
    julia "Миссис Бакфетт, я помню, Вы носили мои белые трусики..."
    $ notif(_("Моника показывала Юлии, что она носит ее трусики."))
    img_30393
    julia "С этими Вы хотите сделать то же самое?"
    menu:
        "Отличная идея! Да, я хочу носить твои трусики!":
            pass

    m "Да! Я хочу носить их!"
    m "Мне..."
    m "Мне нравится твой вкус на нижнее белье."
    julia "Хорошо, я покажу Вам свои трусики..."
    m "!!!"
    # Юлия поднимает вверх руку, которая была у нее за спиной, в руке держит черные трусики
    julia "Вот они."
    julia "Вам они нравятся, Миссис Бакфетт?"
    # Моника смотрит на них, не веря в произошедшее
    mt "Черные?!"
    mt "..."
    mt "Просто черные трусики!"
    mt "И почему я не догадалась назвать Фреду черный цвет?!"
    mt "!!!"
    # пока Моника в ступоре смотрит на трусики, Юлия продолжает
    julia "Миссис Бакфетт, Вы останетесь сегодня у меня на ночь?"
    julia "Я так мечтаю подольше побыть с Вами..."
    julia "Я бы убежала с Вами вдвоем подальше отсюда..."
    julia "Только Вы и я!"
    julia "Мы жили бы вместе где-нибудь, где о нас никто не знает..."
    # Моника переводит взгляд с ее трусиков на нее
    m "Убежать и жить вместе?" # удивленно
    mt "Может, она еще и о женитьбе со мной мечтает?"
    mt "Что за бред она несет?!"
    # Юлия мечтательно
    julia "Да, жить вместе. Например, на моей родине..."
    julia "Если бы это было возможно..."
    # Моника смотрит на нее как на дуру
    mt "Моника, пришло время поставить эту наивную дурочку на место!"
    menu:
        "Юлия, это невозможно!":
            pass
    m "Юлия, ты же знаешь, что это невозможно."
    m "Я слишком знаменита, чтобы остаться незамеченной."
    m "Если пресса узнает о том, что я хочу сбежать из страны..."
    m "Об этом напишут все издания. И все об этом узнают."
    m "Мне не нужны подобные скандалы вокруг моей персоны!"
    julia "Конечно, я это понимаю, Миссис Бакфетт."
    julia "Но если обратиться к моему дяде..."
    julia "Он может сделать Вам поддельный паспорт."
    mt "..."
    # Моника продолжает сидеть между Юлиных ног, и снова смотрит в упор на ее киску
    mt "Дядя..."
    mt "Поддельный паспорт..."
    mt "Убежать из страны..."
    mt "..."
    # поворачивает голову от киски и смотрит в камеру -?
    mt "Убежать из страны!"
    mt "!!!"
    mt "!!!!!!"

    # у Моники выбор послать ее, т.к. узнала цвет или вступить в отношения из-за дяди
    # если послать, то Моника говорит, что поняла, что ошибалась в своих чувствах и чтоб Юлия забыла обо всем, что было и уходит

    # Моника напряженно смотрит на Юлию, Юлия на Монику романтично
    menu:
        "Вступить в отношения с Юлией и сбежать с ней по поддельным документам":
            $ monicaFredPhoto3 = True # Моника решила вступить в отношения с Юлией
            pass
        "Нет! Я не хочу этого! Что за бред! (завершение сюжета с Юлией)":
            mt "Нет!!!" # сердито
            mt "Мне надоело заниматься этими глупостями!"
            m "Знаешь, Юлия, у меня сегодня еще много дел." # высокомерно
            m "А мое время стоит слишком дорого, чтобы я тратила его на какие-то глупые отношения!"
            m "Я Моника Бакфетт. Я - твой Босс."
            m "С чего ты взяла, что такая как ТЫ может привлекать такую леди, как Я?!"
            julia "Но... Миссис Бакфетт!"
            m "Никаких 'но', Юлия!"
            m "Не хочу больше ничего слышать! Мне это все надоело."
            m "Межу нами не было никаких отношений и никога не будет!"
            julia "..." # расстроена
            m "Твое место здесь, в трущобах."
            m "Твоя работа - исполнять мои поручения."
            m "Больше мне от тебя ничего не нужно!"
            julia "М-Миссис..."
            m "Будешь пытаться завести со мной разговор об отношениях..."
            m "Скажешь хоть слово об этом - уволю к черту!!!"
            m "!!!"
            m "Ты поняла меня?!"
            julia "Д-да, М-Миссис Бакфетт..."
            julia "..."
            # Моника уходит, Юлия расстроена
            return
    mt "Дядя Юлии - это шанс полностью изменить мою жизнь."
    mt "Решить все мои проблемы."
    mt "Это же элементарно. Мне просто нужно и дальше притворяться влюбленной дурой перед Юлией."
    mt "В другой стране меня не найдет Маркус и остальные извращенцы."
    mt "Мне не нужно будет постоянно переживать из-за этой чертовой Фермы 218."
    mt "..."
    mt "Моника, это твой шанс!"
    mt "Просто продолжай притворяться..."
    # Моника смотрит на Юлию, улыбается ей
    m "Я тоже мечтаю быть с тобой вдвоем, милая."
    m "Только ты и я."
    julia "О, Миссис Бакфетт! Это правда?!"
    julia "Я боялась, что Вы скажете, что это мои глупые мечты..."
    julia "Я так рада, Миссис Бакфетт!"
    julia "!!!"
    m "..."
    julia "..." # Смотря на Монику и на свою киску
    m "!!!"
    julia "Миссис Бакфетт, так Вы останетесь сегодня у меня?.."
    m "..."
    m "Да, Юлия... Я останусь у тебя сегодня..."
    # Моника снова смотрит на киску Юлии, наклоняется к ней и прикасается губами
    # Моника делает Юлии куни
    mt "Боже! Я не верю, что целую киску своей бывшей гувернантки..."
    mt "Фи! Какая гадость!"
    mt "!!!"
    mt "Но если я не стану делать этого, то эта Юлия не поверит мне и мой план не сработает..."
    mt "А мне нужен этот шанс! Шанс решить свои проблемы..."
    julia "О, Миссис Бакфетт! Еще!"
    julia "О Боже, как же хорошо!"
    julia "Миссис... мммммм... Бакфетт..."
    julia "Аааа..."
    julia "Еще немного..."
    julia "Я... Ооооо... Скоро кончу..."
    julia "Да... О, да!"
    julia "Ааааа..."
    julia "ДАААААААА!!!!" # кончает
    # Юлия лежит практически в отключке, балдеет
    # Моника вытирает рот, недовольно смотрит на нее
    mt "Фу!"
    mt "Надеюсь, мне нечасто придется делать это!"
    # Моника ложится рядом с Юлией
    julia "Миссис Бакфетт, это было великолепно!"
    julia "Я... У меня нет слов, чтобы передать, насколько я счастлива!"
    julia "Вы же останетесь у меня, Миссис Бакфетт?"
    m "Да, Юлия... Я останусь..."
    julia "А Вам понравилось ласкать мою киску, Миссис Бакфетт?"
    m "Да, милая..."
    m "Очень..."
    mt "Поздравляю тебя, Моника. Теперь ты вынуждена притворяться какой-то лесбиянкой."
    mt "И делать вид, что тебе нравится киска твоей подчиненной."
    mt "..."
    # они целуются
    # Моника остается на ночь
    $ log1 = _("У меня появилась возможность сбежать из страны. Для этого мне всего лишь нужно притворяться влюбленной дурочкой перед никчемной Юлией.") # квест-лог
    return

# Квартира Юлии
label ep212_dialogues5_julia_5:
    # утро
    # Моника и Юлия лежат в постели в обнимку
    m "Юлия, милая, мне так понравилось спать с тобой."
    m "Может, мы сможем делать это чаще?"
    julia "Правда, Миссис Бакфетт?"
    julia "Мне тоже очень понравилось!"
    julia "Я хочу каждое утро просыпаться в Ваших объятиях."
    m "..."
    m "Милая, ты вчера говорила про то, что хочешь сбежать отсюда..."
    julia "Миссис Бакфетт, я понимаю, что Вы не захотите менять свою роскошную жизнь..."
    julia "Оставлять здесь свой бизнес..."
    julia "Свой дом, всех своих друзей..."
    julia "Только ради того, чтобы быть со мной."
    julia "Это просто мои глупые мечты..."
    mt "Хммм..."
    mt "Как бы мне уломать ее?"
    mt "Нужно, чтобы она поверила в искренность моих чувств..."
    mt "Может, предложить ей жить вместе?"
    # Обе встают, обнаженные
    m "..."
    m "Почему ты говоришь, что это глупости?"
    m "Я хочу быть с тобой и готова ради тебя все бросить."
    m "И я докажу тебе это, милая."
    return

# Моника вышла на улицу
label ep212_dialogues5_julia_5_1:
    # не рендерить!!
    mt "Мне надо придумать как убедить Юлию поверить, что я якобы действительно люблю ее."
    return

# мысли Моники, проснулась у Юлии
label ep212_dialogues5_julia_5_2:
    # не рендерить!!
    mt "Мне пришлось уговаривать никчемную Юлию, чтобы я жила вместе с ней."
    mt "Эта наивная дурочка верит в то, что Я, Моника Бакфетт, влюбилась в нее."
    mt "..."
    mt "Теперь мне нужно как-то уговорить ее, чтобы она связалась со своим дядей..."
    mt "Мне нужны документы..."
    return


# клик на Монику (глазик)
label ep212_dialogues5_julia_5_3:
    # не рендерить!!
    mt "Поздравляю тебя, Моника. Теперь ты вынуждена притворяться какой-то лесбиянкой..."
    mt "Моника Бакфетт и ее бывшая гувернантка Юлия - влюбленная парочка. Фи!"
    mt "!!!"
    mt "Но я готова поиграть перед этой дурочкой Юлией."
    mt "Это стоит того, чтобы забыть Маркуса и его Ферму как страшный сон."
    return

# Офис Моники
label ep212_dialogues5_julia_6:
    # на след. день Моника приходит в офис и снова встреча с Фредом (на том же месте)
    # Моника разговаривает с ним высокомерно
    img_30301
    m "Фред!"
    fred "Миссис Бакфетт, рад Вас видеть."
    img_30335
    m "А я не рада тебя видеть, Фред!"
    m "У меня есть ответ на твою глупую просьбу."
    m "Юлия носит черные трусики."
    # Фред со своей улыбочкой
    img_30336
    fred "Миссис Бакфетт, ну вот видите, как все просто."
    fred "Достаточно было профессионально подойти к этому делу."
    fred "И результат не заставил себя ждать."
    img_30304
    m "..."
    m "Что насчет того, чтобы удалить ту фотографию?"
    img_30303
    fred "Миссис Бакфетт, я не буду ее удалять."
    fred "Могу лишь пообещать Вам, что..."
    fred "Пожертвую своими профессиональными принципами и не покажу Вашу фотографию никому..."
    fred "Пока что..."
    img_30312
    m "!!!"
    m "Что значит 'пока что'?!"
    img_30308
    fred "Как только у меня появится новая просьба..."
    fred "Вы должны будете ее выполнить..."
    fred "Всего хорошего, Миссис Бакфетт."
    # уходит
    img_30324
    mt "Мерзкий корнишон!"
    mt "Пусть даже не мечтает об этом!"
    mt "Сволочь!"
    mt "!!!"
    return
