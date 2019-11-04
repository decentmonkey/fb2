# Меню "Отношения с Юлией"
label ep29_dialogues1_julia_1:
    menu:
        "Выяснить, какого цвета трусики на Юлии сегодня":
            menu:
                "Заставить Юлию включить неработающий компьютер.":
                    return 1
                "Заставить Юлию принести горячий кофе.":
                    return 2
                "Есть же подчиненные. Поручить им выполнить просьбу Фреда.":
                    return 3

    # При нажатии на 3, когда сцены в процессе
    mt "Мои сотрудники уже занимаются этим."
    mt "Надо пдодождать новостей от них..."


# Кабинет Моники.
label ep29_dialogues1_julia_2:
    # Моника стоит у себя в кабинете, Юлия работает за своим столом
    img 22287
    mt "Как мне узнать цвет трусиков Юлии?"
    mt "Я уже не знаю, что придумать..."
    mt "..."
    img 22288
    # садится за свой рабочий стол, смотрит на свой неработающий комп
    mt "Хм..." #с улыбочкой
    img 22289
    m "Юлия! Подойди ко мне!"
    # Юлия смотрит на Монику с подозрением
    img 22290
    julia "???"
    # Юлия подходит и встает перед столом Моники
    img 22291
    julia "Да, Миссис Бакфетт..."
    # Моника тоном босса
    img 22292
    m "Юлия! У меня не работает компьютер!"
    m "Посмотри, что с ним не так!"
    # Юлия удивленно смотрит на Монику
    img 22293
    julia "Миссис Бакфетт, но я совсем не разбираюсь в компьютерах."
    julia "У нас есть программист. Я могу позвать его. Он поможет Вам."
    # Моника смотрит на Юлию строго
    img 22294
    mt "!!!"
    mt "Черт! Я совсем забыла про него..."
    img 22295
    m "Юлия!" # тоном Я ТУТ БОСС
    m "..."
    julia "Да, Миссис Бакфетт..."
    img 22296
    m "Хм..."
    m "Юлия! Ты забываешь, что работаешь в серьезной компании!"
    m "О работе в такой организации мечтают сотни девушек!"
    m "И мне не составит труда найти тебе замену, Юлия!"
    img 22297
    julia "!!!" # Юлия осознает, что ничего хорошего этот разговор не предвещает
    # Моника продолжает вещать тоном БОССА
    img 22298
    m "Поэтому ты, как и любой другой сотрудник здесь, должна..."
    m "..."
    m "Должна выполнять не только свои прямые обязанности!"
    m "Ты должна справляться с любыми поставленными задачами, если это потребуется!"
    m "Ты понимаешь, о чем я говорю, Юлия?!"
    julia "Да, Миссис Бакфетт..." # испуганно
    img 22299
    m "Тогда почему я дважды должна повторять, что ты должна посмотреть, что с моим компьютером?!" # переходит на крик
    #sound Юлия бежит к компьютеру
    img 22300
    julia "Д-д-да, М-м-миссис Бакфетт. Я сейчас посмотрю." # растерянно
    mt "Никчемная помощница!!!"
    img 22301
    m "Я жду!"
    m "И быстрее! У меня много работы!"
    # Юлия подходит справа, смотрит на монитор
    img 22302
    julia "М-м-миссис Бакфетт, Ваш компьютер... Он не работает..." # растерянно
    img 22303
    m "О чем я тебе и говорю!" # смотрит на зад Юлии
    m "!!!"
    m "Заставь его работать!!!"
    img 22304
    julia "..."
    julia "Но как я это сделаю?.."
    img 22305
    m "Откуда я знаю?! Там есть каие-то кнопки..."
    m "Понажимай на них."
    # Юлия нагибается, чтобы нажать кнопки
    img 22306
    w
    img 22307
    #sound Юлия нажимает на кнопки
    w
    img 22308
    m "..."
    menu:
        "Заглянуть Юлии под платье.": #corruption
            pass
        "Не заглядывать.":
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return False
    img 22309
    w
    img 22310
    w
    img 22311
    w
    img 22312
    w
    img 22313
    w
    img 22314
    w
    img 22315
    w
    img 22316
    w
    img 22317
    w
    img 22318
    # Моника тоже нагибается, пытаясь подсмотреть Юлии под платье, но ей ничего не видно
    mt "Черт! Еще немного!"
    # Юлия поворачивает голову и видит, что Моника подглядывает
    img 22319
    julia "Миссис Бакфетт! Что Вы делаете?!"
    # Юлия резко выпрямляется, Моника растерянно
    img 22320
    m "..."
    img 22321
    w
    img 22322
    m "!!!"

    #sound Моника делает рывок, чтобы подсмотреть
    img 22323
    w
    img 22324
    julia "Миссис Бакфетт!!!"
    # потом Моника делает вид, что ничего не произошло
    img 22325
    w
    img 22326
    m "!!!"
    img 22327
    m "Я, как твой начальник, Юлия, должна контролировать, насколько ты хорошо исполняешь свою работу!"
    m "И я не понимаю, чему ты так удивляешься!"
    m "!!!"
    # Юлия смутилась
    img 22328
    w
    img 22329
    m "Ты уже починила мой компьютер, Юлия?!" # строго
    mt "Я снова ничего не успела рассмотреть..."
    img 22330
    julia "Миссис Бакфетт, я нажала на кнопки..."
    julia "Компьютер все равно не работает..." # растерянно
    img 22331
    m "Юлия, ты уверена, что нажала на все кнопки?"
    img 22332
    julia "Да, Миссис Бакфетт..."
    julia "Я не знаю, что еще можно нажать..."
    julia "Я могу спросить у программиста, Миссис Бакфетт..."
    # Моника рассержена
    img 22333
    m "!!!"
    img 22334
    m "У программиста я и сама могу спросить, Юлия!"
    m "А тебе ничего нельзя поручить!"
    img 22335
    m "!!!"
    img 22336
    m "А теперь иди работай! Не отвлекайся!"
    # Юлия расстроенная уходит и садится за свой стол
    img 22337
    #sound Юлия уходит
    w
    img 22338
    mt "Вот черт! У меня снова ничего не получилось!"
    mt "По-моему, она поняла, что я пыталась заглянуть ей под платье!!!"
    img 22339
    mt "!!!"
    mt "Нужно придумать какой-нибудь другой способ подсмотреть, какие у нее трусики."
    img 22340
    mt "Такой способ, чтобы точно сработало."
    img 22341
    mt "Мне надоело уже заниматься этими глупыми играми этого профессионального мерзавца Фреда!"
    mt "Пора заканчивать с этим!"
    return True

# В конце рабочего дня. Гримерка.
# Моника сталкивается с Фредом. Разговор Фреда и Моники.
label ep29_dialogues1_julia_3:
    # Моника раздаженно
    m "Опять ТЫ!"
    m "!!!"
    # Фред ей отвечает спокойно
    fred "Миссис Бакфетт... Я тоже рад Вас видеть снова."
    fred "Вы выяснили то, о чем я вас просил?"
    # Моника зло смотрит на него
    m "!!!"
    m "НЕТ!"
    # Фред с улыбочкой
    fred "Как же так, Миссис Бакфетт? Вы поступаете крайне непрофессионально..."
    mt "Ненавижу этого мерзавца!"
    m "..."
    menu:
        "Отказаться выполнять дурацкие приказы этого мерзавца!": # если отказалась подглядывать
            # Моника орет на Фреда
            m "ФРЕД!!!"
            m "Ты не смеешь мне указывать, что мне делать!"
            m "И мне плевать на то, что ты кому-то расскажешь!"
            m "Ты просто какой-то ничегонезначащий водитель!!! Тебе никто не поверит!"
            m "А я всем скажу, что ты шантажируешь меня, подделав фото!"
            m "Пошел вон отсюда!!!"
            m "Еще раз здесь тебя увижу - вызову охрану!!!"
            m "Жалкий водитель!"
            fred "..." # Фред уходит
            return False
        "Продолжить играть в 'профессиональную' игру Фреда.": # если подглядывала
            pass
    fred "Вы очень долго не можете выполнить мою маленькую просьбу, Миссис Бакфетт."
    fred "И это меня очень расстраивает..."
    fred "Я начинаю задумываться о том, что Вы ничего не предпринимаете для этого..."
    # Моника зло смотрит на него
    m "Я ничего не предпринимаю?!"
    m "!!!"
    m "Я только тем и занимаюсь, что пытаюсь заглянуть под платье своей помощницы, как какая-то лесбиянка!!!"
    m "Помимо этого, я еще должна терпеть эти твои визиты в мою гримерку!!!"
    m "Хватит уже сюда ходить!!!"
    fred "Миссис Бакфетт, мне кажется, Вы забываете о том, что у меня есть информация..."
    fred "Которая будет крайне интересна Вашим подчиненным и Вашему начальству..."
    fred "Я даже подумываю о том, чтобы продать Вашему журналу Ваши же фотографии в костюме гувернантки."
    fred "Уверен, что поклонникам Вашего журнала они очень понравятся!"
    m "Не смей!!!" # орет
    mt "Мерзавец!!! Ненавижу!!!"
    m "Ты не сделаешь этого!!!"
    fred "Миссис Бакфетт, я даю Вам еще немного времени на выполнение моей маленькой просьбы." # с улыбочкой
    fred "Я не сомневаюсь, что у Вас все получится..."
    fred "До скорой встречи, Миссис Бакфетт."
    # Фред уходит
    mt "!!!"
    mt "Этот мерзкий Фред будет первым, кому я отомщу!"
    mt "Когда верну себе все, что у меня отняли!"
    mt "Я его заставлю пожалеть об этих его 'маленьких просьбах'!"
    mt "!!!"
    return

# Кабинет Моники.
label ep29_dialogues1_julia_4:
    # Моника стоит у себя в кабинете, Юлия работает за своим столом
    img 22342
    mt "Итак, рабочий день снова начинается с вопроса: как мне узнать цвет трусиков Юлии?"
    mt "У меня скоро это войдет в привычку..."
    mt "Хотя, мой рабочий день должен начинаться не с этого."
    mt "А с чашечки горячего кофе, например."
    img 22343
    mt "..."
    mt "Горячий кофе..."
    mt "Хм..." #с улыбочкой
    img 22344
    m "Юлия!" # тоном босса
    # Юлия смотрит на Монику с подозрением
    julia "???"
    img 22345
    julia "Да, Миссис Бакфетт?"
    img 22346
    m "Юлия, я хочу выпить кофе! Принеси мне его!"
    # Юлия удивленно
    img 22347
    julia "Кофе?"
    img 22348
    m "Да!"
    img 22349
    julia "Хорошо, Миссис Бакфетт. Но где мне его взять?"
    img 22350
    m "Юлия! Ты в прошлый раз себя проявила как некомпетентный сотрудник!" # строго
    m "Ты не смогла включить мой компьютер!!!"
    m "И это после разговора о том, что на твое место найдется масса желающих?!"
    m "!!!"
    # Юлия смотрит испуганно
    img 22351
    julia "!!!"
    img 22352
    m "Принести мне горячего кофе - это тоже сложная задача для тебя?!" # также строго
    m "Создается впечатление, что ты совсем не дорожишь своей работой, Юлия..."
    img 22353
    julia "М-м-миссис Бакфетт, это не так..." # растерянно
    julia "Я сейчас принесу Вам кофе, Миссис Бакфетт!"
    img 22354
    m "Горячего кофе, Юлия!"
    img 22355
    julia "Да, Миссис Бакфетт, я поняла."
    # Юлия уходит за кофе, Моника с довольной ухмылкой садится на диванчик в зоне отдыха
    img 22356
    mt "И как я раньше не могла додуматься до этого?"
    mt "Это же самый простой способ заставить ее нагнуться: ей нужно будет поставить горячий кофе на стол."
    mt "А я в это время смогу заглянуть ей под платье..."
    img 22357
    mt "И в этот раз она не сможет отпрыгнуть от меня. Ведь у нее в руке будет горячий кофе."
    mt "Главное, не упустить момент..."
    # Моника сидит на диванчике расслабленно, улыбается
    img 22358
    mt "..."
    mt "Наконец-то, я смогу узнать цвет трусиков Юлии."
    mt "Да еще и совместить это с чашечкой ароматного кофе."
    mt "Чувствую, что сегодня меня ожидает просто отличный день!"
    img 22359
    mt "Сегодня закончится эта дурацкая ситуация, когда мне надо узнавать какие-то глупости у никчемных работников..."
    mt "..."
    mt "И больше я не буду слушать Фреда! С меня хватит!"
    # в кабинет заходит Джон-подхалим, следом за ним идет Юлия. У подхалима кофе в руке
    # они подходят к Монике, у нее шок
    # подхалим доволен собой, ставит кофе на столик. Юлия стоит рядом с ним. Моника смотрит на чашку кофе, потом на Юлию, потом на подхалима
    # затемнение
    img 22360
    w
    img 22361
    w
    img 22362
    mt "!!!"
    mt "Какого черта?!"
    img 22363
    w5 "Миссис Бакфетт! Вы сегодня прекрасно выглядите!" # решил выслужиться, как обычно
    img 22364
    mt "..."
    img 22365
    w5 "Я узнал от Вашей помощницы, что Вам нужен кофе, и сразу принес его Вам!"
    img 22366
    mt "..."
    menu:
        "Послушать, что он скажет дальше.":
            img 22367
            w5 "Миссис Бакфет, Вы всегда можете на меня рассчитывать."
            mt "!!!" # начинает сердиться, но молчит
            mt "О, Боже! Когда он уйдет отсюда?!"
            img 22368
            w5 "Ведь я могу не только качественно и быстро выполнять свои прямые обязанности..."
            w5 "Я также могу помогать Вам, ведь Вам приходится очень много работать."
            mt "!!!"
            mt "Какой же он мерзкий тип этот Джон!"
            mt "Какого черта ОН притащил мне этот кофе!!!"
            mt "!!!" # уже очень злая
            img 22369
            w5 "И такой помощник, как Я, будет Вам как раз кстати, Миссис Бакфетт."
            w5 "В отличии от толстухи Греты, Я могу делать любую работу в этом отделе."
            w5 "Даже самую сложную и ответственную..."
            img 22370
            mt "!!!" # очень-очень злая
            mt "Когда этот сукин сын уже замолчит?!"
            img 22371
            w5 "Помимо этого, я всегда внимателен к желаниям начальства..."
            w5 "Я могу приносить Вам горячий кофе каждое утро, Миссис Бакфетт!"
            w5 "Я..."
            img 22372
            m "ТАК, ХВАТИТ!"
            m "!!!"
            m "Ты слишком много разговариваешь! Иди работай!!!"
            # подхалим, ничуть не смутившись
            img 22373
            w5 "Да, конечно, Миссис Бакфетт. Я понимаю, что Вам некогда."
            w5 "Помните, что всегда можете на меня рассчитывать, Миссис Бакфетт."
            img 22374
            w5 "Надеюсь, Вам понравится кофе. Если захотите еще, я с радостью его Вам принесу..."
            img 22375
            m "Вон из моего кабинета!!!"
            mt "!!!"

        "Не слушать его болтовню, прогнать этого подхалима из кабинета.":
            img 22376
            m "Я не знала, что в ваши обязанности входит работать моей помощницей!"
            m "Выйди и закрой за собой дверь!!!"
            img 22377
            w5 "Хорошо, Миссис Бакфетт. Понимаю, Вы очень заняты."
            w5 "Помните, что Вы всегда можете на меня рассчитывать, Миссис Бакфетт." # уходит

    # подхалим уходит, Юлия стоит на том же месте. Моника зло смотрит на нее
    # sound переход, подхалим уходит
    img 22378
    w
    img 22379
    julia "???"
    menu:
        "Отчитать Юлию и выгнать из комнаты отдыха.":
            img 22380
            m "Юлия!!!" # строго
            m "Я в очередной раз убедилась, что самостоятельно ты не можешь справиться с поставленными задачами!!!"
            img 22381
            julia "Но, Миссис Бакфетт..." # растерянно
            img 22382
            m "Никаких 'но'!!! Я не желаю слушать твои жалкие оправдания!"
            m "Иди работай!!!"
            # Юлия расстроенная уходит
            pass
        "Не отчитывать Юлию.":
            img 22383
            m "Юлия, ты можешь заняться своей работой." # сдержанно
            m "Я хочу побыть одна."
            julia "Хорошо, Миссис Бакфетт..."
            img 22384
            #sound Юлия уходит на рабочее место, Моника смотрит вслед
            m "..."
            # Юлия уходит
    # Моника кипит от злости
    img 22385
    mt "!!!"
    mt "Это был просто отличный план, чтобы закончить эту историю с трусиками Юлии!!!"
    mt "Какого черта ОН притащил мне этот долбанный кофе!!!"
    img 22386
    mt "ААААААААРРРГХХХХХ!!!"
    mt "Как меня достал этот мерзкий тип!!!"
    mt "!!!"
    img 22387
    mt "Никчемные сотрудники!!! Все они никчемные!!! Бесполезные!!!"
    mt "Когда верну себе свое место босса, вышвырну отсюда всех этих бездельников!!!"
    mt "!!!"
    img 22388
    mt "Теперь мне снова нужно придумывать какой-нибудь способ заглянуть Юлии под платье!"
    mt "..."
    return True

# Кабинет Моники.
label ep29_dialogues1_julia_5:
    # Моника стоит у себя в кабинете, Юлия работает за своим столом
    mt "Мне сегодня снова предстоит заниматься тем, чтобы исполнить 'маленькую просьбу' мерзавца Фреда..."
    mt "Только у меня совсем кончились идеи, как можно это сделать..."
    mt "..." # задумчиво
    mt "Хотя..."
    mt "Этот мерзкий карьерист, который мне притащил тогда кофе, может мне помочь..."
    mt "Почему бы мне не поручить это задание этому подхалиму и еще кому-нибудь?"
    mt "В конце концов, Я их Босс! Они обязаны исполнять мои распоряжения!"
    mt "А подхалим будет только рад выслужиться передо мной, исполнив это задание!"
    mt "Только как это сделать? Не могу же я им прямо сказать об этом..."
    mt "..."
    mt "Хм..." #с улыбочкой
    m "Юлия!" # тоном босса
    # Юлия смотрит на Монику настороженно
    julia "???"
    julia "Да, Миссис Бакфетт?"
    m "Юлия, сегодня я хочу провести совещание."
    m "На нем должны присутствовать Джон и... И Грета."
    m "Позови их сюда!"
    # Юлия удивленно
    julia "Хорошо, Миссис Бакфетт. Во сколько будет совещание?"
    m "Прямо сейчас, Юлия!"
    m "Давай быстрее!"
    # Юлия уходит, Моника проходит в комнату отдыха, садится в кресло
    mt "Никчемная секретарша!"
    mt "!!!"
    mt "Сегодня я, наконец-то, избавлю себя от необходимости думать, как заглянуть ей под платье."
    mt "Нужно было сразу озадачить этим вопросом своих подчиненных."
    mt "Все равно целыми днями сидят и выполняют никому ненужную работу..."
    mt "Теперь займутся хотя бы полезным делом..."
    mt "Для меня..."
    # в комнату отдыха заходит Юлия, за ней Джон и Грета
    julia "Миссис Бакфетт, Джон и..."
    # подхалим перебивает ее
    w5 "Миссис Бакфетт! Вы сегодня прекрасно выглядите!"
    w5 "Хотите, я принесу Вам горячего кофе, как в прошлый раз?"
    mt "Мерзкий тип..."
    m "Нет! Садитесь на кресла. У меня к вам серьезный разговор!"
    mt "!!!"
    menu:
        "Не разрешать Юлии присутствовать на совещании.":
            m "Юлия, твое присутствие на совещании не обязательно! Можешь возвращаться к своей работе!"
            julia "Хорошо, Миссис Бакфетт."
            pass
        "Заставить Юлию вести протокол совещания.":
            m "Юлия!" # строго
            m "Тебе нужно будет вести протокол совещания. Для отчета..."
            julia "Для отчета? Хорошо, Миссис Бакфетт..."
            m "Иди на свое рабочее место и все подробно записывай!"
            mt "Кому нужен этот протокол совещания?"
            mt "Уж точно не мне..."
            mt "Зато Юлия будет думать, что занимается полезным делом..."
            mt "..."
            mt "Какие же они все жалкие неудачники! Фи!"
            pass
    # Грета с Джоном садятся на диван, Юлия уходит и садится за свой стол
    # Грета услужливо обращается к Монике
    w6 "Миссис Бакфетт, если речь пойдет о повышении качества работы, то у меня есть несколько предложений..."
    # Джон, перебивая Грету
    w5 "У меня также есть предложения. Я думаю, что они значительно повысят скорость работы отдела по составлению отчетов."
    mt "Да кому они нужны эти ваши отчеты... Их никто даже не открывает! "
    m "Речь пойдет не совсем об этом..."
    m "Хм..." # Моника включает БОССА
    m "Как вы оба знаете, я в этом отделе я занимаю должность начальника временно."
    m "Это совершенно не мой уровень и, я надеюсь, Вы понимаете это."
    m "Тем не менее, я вижу своей задачей оптимизацию процесса работы отдела."
    m "Другими словами, здесь необходимо навести порядок..."
    m "..."
    # Джон и Грета внимают
    # если Моника выгнала Юлию с совещания, то Юлия греет уши со своего рабочего места и косится в сторону Моники
    # если Моника заставила записывать ход совещания, то Юлия то смотрит в ее сторону, то печатает протокол
    m "Вы работаете в очень крупной и серьезной компании."
    m "И вы должны понимать, что абсолютно на каждом сотруднике лежит большая ответственность."
    m "То, насколько качественно каждый из нас выполняет свою работу, зависит качество нашего... Хм, моего журнала."
    m "А его читают миллионы людей по всей стране!"
    m "И мы должны сделать все, чтобы становиться только лучше и лучше с каждым номером."
    m "Если каждый из нас будет думать только о себе, то ничего хорошего из этого не выйдет..."
    m "Мы с каждым днем в таком случае будем наблюдать все большую раздробленность в коллективе."
    m "А это недопустимо!"
    m "Одной из главной составляющих налаженной работы я вижу в поднятии корпоративного духа в коллективе."
    m "И мне нужен человек, которому я смогу доверить эту ответственную задачу в будущем."
    # Джон и Грета кивают и слушают внимательно
    m "Вы являетесь лучшими сотрудниками в этом, заинтересовавшем меня отделе."
    m "Поэтому я и пригласила вас сегодня на это совещание..."
    w6 "!!!"
    w5 "!!!"
    m "Фактически, я выполнила свою работу здесь..."
    m "Выявила сильные и слабые стороны в организации работы отдела."
    m "Теперь мне необходимо решить, кого я смогу поставить на должность начальника отдела."
    # оба кандидата переглядываются, потом снова смотрят на Монику
    w6 "!!!"
    w5 "!!!"
    # Джон, преисполненный важности
    w5 "Миссис Бакфетт..."
    m "Я еще не закончила!!!" # раздраженно
    m "Помимо этого, возможно, мне потребуется еще и личный помощник..."
    w6 "!!!"
    w5 "!!!"
    m "Вы должны быть точно уверены в своих силах."
    m "И понимать ту ответственность, которая будет возложена на одного из вас."
    m "Сотрудник, достойный этого места, должен справляться с любыми трудностями..."
    m "И решать любые задачи..."
    m "..."
    # Джон, преисполненный важности
    w5 "Миссис Бакфетт, я сделаю все, чтобы доказать Вам, что именно я достоин занимать эту должность!"
    # Грета также полна решимости
    w6 "Миссис Бакфетт, я готова сделать все, что в моих силах! О каких задачах Вы говорите? "
    m "..."
    m "Хм... Я под этим подразумевала абсолютно любую задачу."
    m "Притом, она может прямо не относиться к вашим профессиональным обязанностям..."
    m "Руководитель высокого уровня никогда не знает, с чем он может столкнуться."
    m "И он должен быть готов к любым вызовам!"
    m "И я бы хотела убедиться, что хотя бы один из вас готов к ним..."
    # Джон и Грета с готовностью
    w6 "Конечно, Миссис Бакфетт! Я готова!"
    w5 "Вы только скажите мне, что нужно сделать! Я Вам докажу свою исполнительность, Миссис Бакфетт!"
    # Моника делает задумчивый вид
    m "..."
    m "Даже не знаю. Можно взять любой пример..."
    # оглядывается, как бы отыскивая, чем можно их озадачить, потом смотрит на Юлию
    m "Точно! Допустим, вам нужно узнать, какого цвета трусики носит моя помощница Юлия!"
    # Юлия в шоке
    julia "!!!"
    julia "М-миссис Бакфетт!"
    # Моника ее игнорит, отворачивается от нее и смотрит вопросительно на Джона и Грету. Те тоже в шоке
    w6 "!!!"
    w5 "!!!"
    # Грета первая приходит в себя, смотрит на Юлию
    w6 "Миссис Бакфетт, судя по стилю Юлии..."
    w6 "..."
    w6 "Я думаю, что она носит черные трусики..."
    m "Меня не интересуют догадки!" # строго
    m "Я поставила вам конкретную задачу и вы должны сделать все, чтобы ее решить!"
    m "Таким образом, я смогу понять..."
    m "Кто из вас является более целеустремленным и ответственным кандидатом на эту должность."
    # оба кандидата переглядываются, потом снова смотрят на Монику
    w6 "!!!"
    w5 "!!!"
    # Моника сидит с надменным лицом
    m "Я жду от вас решения поставленной задачи в кратчайшие сроки!"
    w6 "Да, Миссис Бакфетт..."
    w5 "Конечно, Миссис Бакфетт!"
    m "Совещание окончено. Можете быть свободны!"
    # Джон с Гретой встают, плотоядно смотрят в сторону Юлии и уходят, преисполненные решимости
    # Юлия смотрит на них, офигевая от происходящего, после их ухода смотрит в сторону Моники
    julia "М-миссис Бакфетт, можно спросить Вас?"
    m "..."
    menu:
        "Позволить Юлии задать вопрос.":
            m "Да, Юлия?"
            julia "Миссис Бакфетт, почему Вы дали им именно такое задание?.."
            m "..."
            m "Юлия, ты отвлекаешь меня своими глупыми вопросами!"
            m "Я хочу побыть в тишине. Сиди и занимайся своей работой!!!"
            julia "..."
            pass
        "Не позволять.":
            m "Нет, нельзя!" # сердито
            m "Занимайся своей работой и не отвлекай меня!"
            mt "Эта Юлия задает слишком много вопросов!"
            mt "Меня это раздражает!"
            mt "Как же мне надоело сидеть здесь и общаться со всякими никчемными работничками!"
            mt "Скорей бы вышвырнуть эту сволочь Биффа из моего кабинета!!!"
            mt "Мое место там! Среди моды!"
            mt "А не среди этих безмозглых болванов!"
            pass
    # Моника сидит с покерфейсом, на Юлию не смотрит
    mt "Моя идея с совещанием оказалась просто гениальной!"
    mt "Хотя, по-другому быть и не могло. Монику Бакфетт не могут посещать какие-нибудь глупые идеи!"
    mt "!!!"
    mt "Все оказалось намного проще, чем я могла ожидать..."
    mt "Эти двое сделают все, чтобы выслужиться передо мной!" # довольно ухмыляясь
    mt "И мне, наконец-то, не нужно будет придумывать, как заглянуть под платье этой никчемной секретарши."
    mt "..."
    mt "Еще немного и я смогу послать этого мерзавца Фреда куда подальше с его глупыми 'просьбами'!"
    mt "Не могу дождаться этого момента!!!"
    mt "!!!"
    return

# После совещания. Если Моника подходит к Джону. (спросить про задание)
label ep29_dialogues1_julia_6:
    w5 "Миссис Бакфетт! Вы, как всегда, великолепно выглядите!"
    w5 "Хотите кофе?"
    m "Нет. Я хотела узнать, выполнено ли мое задание?" # строго
    w5 "Миссис Бакфетт, я в процессе его выполнения."
    w5 "В отличии от Греты, у меня есть идеи, которые я в ближайшие дни планирую воплотить."
    m "Мне ведь не придется долго ждать?"
    w5 "Можете мне поверить, задание будет выполнено качественно и в кратчайшие сроки!"
    m "Надеюсь, вы меня не подведете."
    m "Ведь именно ВАШУ кандидатуру на место начальника я рассматриваю в первую очередь..."
    w5 "!!!" # воодушевленно
    w5 "Я не подведу Вас, Миссис Бакфетт!"
    mt "Не сомневаюсь. Тебе ведь так хочется занять мое место в этом бесполезном отделе..."
    mt "..."
    return

# После совещания. Если Моника подходит к Грете. (спросить про задание)
label ep29_dialogues1_julia_7:
    w6 "Миссис Бакфетт..."
    m "Как идет выполнение моего задания?" # строго
    w6 "Миссис Бакфетт, я как раз планирую, как его лучше выполнить."
    w6 "А вот Джон только тем и занимается, что пьет кофе целыми днями."
    w6 "Но я бы никогда не стала так пренебрежительно относиться к поставленной вами задаче, как он!"
    w6 "Я обязательно выполню Ваше задание и сообщу Вам результат."
    w6 "Вы можете не беспокоиться, Миссис Бакфетт."
    m "Я рассчитываю на вас."
    m "Ведь именно ВАШУ кандидатуру на место начальника я рассматриваю в первую очередь..."
    w6 "!!!" # воодушевленно
    w6 "Я не подведу Вас, Миссис Бакфетт!"
    mt "Конечно, не подведешь. Ты же спишь и видишь себя на моем месте."
    mt "Фи!"
    return

# Грета приходит к Юлии, когда в кабинете нет Моники.
label ep29_dialogues1_julia_8:
    w6 "Юлия..." # смущенно, стоит перед ее столом
    julia "Привет, Грета." # настороженно
    julia "Ты что-то хотела спросить?"
    w6 "..."
    w6 "Хм..."
    w6 "Понимаешь, я тут провожу опрос среди наших сотрудников. Психологический опрос."
    julia "Психологический опрос? Зачем?"
    w6 "Мне нужно составить для руководства отчет."
    w6 "В нем мне нужно предоставить психологический портрет каждого сотрудника."
    w6 "Я просто задам тебе несколько вопросов."
    w6 "Этого будет достаточно для того, чтобы дать тебе краткую характеристику."
    w6 "Ты же не против?"
    julia "..." # смотрит на Грету с подозрением
    julia "Если это нужно для отчета, то, конечно, не против..."
    w6 "Тогда приступим..."
    w6 "В конце рабочего дня к тебе подходит коллега и просит помочь ему с работой."
    w6 "Что ты сделаешь? Откажешься или поможешь ему?"
    julia "Помогу."
    w6 "Хорошо." # делает серьезный вид, что-то записывает в блокнот
    w6 "У твоего коллеги сложная ситуация на работе."
    w6 "Допустим, он не успевает в срок выполнить какое-то ответственное задание руководства."
    w6 "..."
    w6 "А ты знаешь, как выполнить это задание."
    w6 "Ты подскажешь коллеге?"
    julia "Подскажу." # подозрительно
    w6 "Отлично." # что-то записывает в блокнот
    w6 "И последний вопрос: какого цвета нижнее белье ты носишь на работу?"
    # Юлия офигевает, подскакивает и возмущенно
    julia "ГРЕТА!!!"
    julia "!!!"
    julia "Я не ожидала от ТЕБЯ такого!!!"
    # Грета, смутившись
    w6 "Нет..."
    w6 "Юлия, ты не так поняла..."
    w6 "..."
    w6 "По любимому цвету можно охарактеризовать любого человека..."
    w6 "..."
    julia "Так, а причем здесь мое нижнее белье?!"
    julia "Ты все это затеяла, чтобы выполнить задание Миссис Бакфетт?!"
    julia "Не могу поверить!.."
    w6 "Юлия..."
    julia "Нет! Я не буду больше отвечать на твои вопросы!" # возмущенно
    julia "Цвет моего нижнего белья - это мое личное дело!"
    julia "И никакого отношения к работе это не имеет!"
    julia "!!!"
    w6 "Юлия, просто скажи мне цвет и все. Это же несложно."
    julia "Нет. У меня много работы, Грета. Извини."
    w6 "!!!"
    # с возмущением начинает работать, давая понять Грете, чтоб та уходила
    # Грета раздосадованная, уходит
    return

# Джон приходит к Юлии, когда в кабинете нет Моники.
label ep29_dialogues1_julia_9:
    julia "Джон?" # с выражением лица 'уже не знаю, чего ожидать от этих придурков'
    w5 "Юлия, ты сегодня прекрасно выглядишь!" # уверенно, с широкой улыбкой
    w5 "Не составишь мне компанию за чашечкой кофе?"
    w5 "Ты работаешь у нас в отделе уже давно, а мы с тобой так и не познакомились поближе."
    julia "Поближе?" # удивленно
    julia "..."
    julia "Нет, Джон. Спасибо, но я откажусь."
    w5 "Как скажешь, Юлия."
    w5 "Слушай, у меня к тебе есть небольшое дело..."
    julia "Какое?" # подозрительно
    w5 "Ко мне сегодня заходил коллега из другого отдела."
    w5 "У них завтра планируется фотосессия."
    w5 "Но там с моделью какие-то проблемы..."
    w5 "В общем, есть вероятность срыва съемки из-за нее."
    julia "А я тут причем?" # подозрительно
    w5 "..."
    w5 "Если бы ты согласилась подменить ее, если она не придет..."
    julia "Но... Я никогда не участвовала в фотосессиях. Я даже не знаю..."
    w5 "Тебе не о чем беспокоиться, Юлия!"
    w5 "Ты очень красивая и фигура у тебя модельная. Ты будешь отлично смотреться в кадре!"
    julia "Ну..." # сомневаясь
    julia "Хорошо. Если им потребуется замена, то я согласна."
    julia "Только я переживаю, что у меня не получится..."
    julia "..."
    w5 "Я рад, что ты согласилась! Не переживай!"
    w5 "Это несложно, Юлия. Фотограф тебе все объяснит."
    w5 "И костюм для съемки тебе выдадут..."
    w5 "..."
    w5 "Кстати, о костюме! Я чуть не забыл!"
    w5 "!!!"
    julia "???"
    w5 "Тебе нужно будет сниматься в костюме красного цвета."
    w5 "Поэтому..."
    w5 "Обязательно надень завтра красные трусики."
    w5 "Не забудь! Это очень важно!"
    w5 "Красные трусики. Завтра."
    # Юлия офигевает, подскакивает и возмущенно
    julia "ЧТО?!"
    julia "Трусики?!"
    julia "!!!"
    julia "Джон!!!"
    w5 "..." # смотрит на нее, ничуть не смутившись
    w5 "А что тут такого? Это обычное для моделей дело!"
    julia "Ты это все придумал, чтобы выполнить задание Миссис Бакфетт!"
    julia "А завтра ты подойдешь ко мне и скажешь, что замена на фотоссесии не нужна?"
    julia "А потом пойдешь к Миссис Бакфетт и скажешь ей, что на мне красные трусики?!"
    julia "Да и я вообще сомневаюсь что у такого как ты есть коллега, который связан со съемками моделей!"
    julia "Джон! Я не собираюсь участвовать в этом!"
    julia "!!!"
    w5 "Хорошо, Юлия. Успокойся."
    w5 "Тогда просто скажи мне цвет и все. Это же несложно."
    julia "Нет!"
    julia "У меня много работы, Джон. Извини."
    w5 "!!!"
    # с возмущением начинает работать
    # Джон уходит
    return

# Джон и Грета стоят возле рабочего стола Джона в их офисе.
label ep29_dialogues1_julia_10:
    # вид у обоих озадаченный
    w5 "Грета, ты пыталась выполнить задание Миссис Бакфетт?"
    w6 "Ага. Безуспешно. Это оказалось не так просто, как я думала сначала."
    w6 "..."
    w6 "А ты? У тебя получилось?"
    w5 "Я придумал просто идеальный план, но тоже ничего не получилось..."
    w5 "..." # оба стоят задумчивые
    w6 "Джон, а ты не задумывался над тем, что Миссис Бакфетт просто пошутила тогда?"
    w5 "..."
    w5 "Мне кажется, что такие шутки не в стиле Миссис Бакфетт, Грета..."
    w6 "Ну или она проверяет, насколько мы глупы."
    w6 "Поймем ли, что на такие глупые задания нельзя тратить свое рабочее время..."
    w6 "Потом еще и накажет нас, что на работе занимаемся всякой ерундой..."
    w5 "..."
    w5 "А мне кажется, что она хочет проверить нашу стрессоустойчивость."
    w5 "И способность работать в режиме многозадачности..."
    w5 "Конечно, задание она нам дала более, чем странное..."
    w5 "..."
    w6 "..."
    w6 "Джон, а с другой стороны, Миссис Бакфетт работает в модном журнале..."
    w6 "..."
    w5 "???"
    w5 "И? Мы тоже здесь работаем."
    w6 "Мы сидим и целыми днями занимаемся отчетами."
    w6 "А она всегда работала с моделями..."
    w6 "Сама участвовала в фотосессиях..."
    w6 "Скорее всего, она и костюмы для фотосессий подбирала."
    w5 "Ты хочешь сказать, что раз она имеет отношение к моде..."
    w5 "..."
    w6 "Да, именно. Мода и стиль - это ее жизнь."
    w6 "Совсем неудивительно, что она придумала задание, связанное с одеждой."
    w6 "Точнее, с нижним бельем..."
    w5 "Думаю, ты права, Грета. А мы с тобой совсем не так ее поняли."
    w5 "..."
    w5 "А помнишь, она сказала еще, что ей нужен личный помощник?"
    w5 "Как ты думаешь, это она серьезно?"
    w6 "Уверена, что Миссис Бакфетт действительно нуждается в личном помощнике."
    w6 "Ведь у нее так много обязанностей в нашей компании."
    w6 "Но ты можешь не мечтать об этой должности!"
    w6 "Ей нужна женщина в качестве личного помощника!"
    w6 "То есть Я!"
    w6 "!!!"
    # Джон крайне удивлен такому заявлению, начинают спорить
    w5 "???"
    w5 "Почему ты так считаешь? Уверен, что она имела ввиду МЕНЯ!"
    w6 "Нет, МЕНЯ!"
    w6 "И вообще, у меня больше шансов выполнить задание с трусиками Юлии!"
    w5 "С чего бы это?!"
    w6 "Потому что Юлия более охотно расскажет, какого цвета ее трусики, мне, а не тебе!"
    w6 "Вот увидишь! Я прямо сейчас пойду и все выясню!"
    w6 "!!!"
    w5 "!!!"
    # разворачивается и идет в сторону кабинета Моники, подхалим бежит за ней, обгоняет ее
    # в итоге, они наперегонки бегут к Юлии
    # Джон и Грета врываются в кабинет Моники. Моники нет, Юлия сидит за своим столом.
    # Юлия подпрыгивает от неожиданности.
    # Джон и Гретта с крайне сосредоточенными лицами подбегают к ней, окружают с двух сторон
    # Юлия напугана, смотрит то на Джона, то на Грету
    julia "!!!"
    julia "Ч-ч-что вы делаете?!"
    w6 "!!!"
    w5 "!!!"
    w5 "Юлия! У меня к тебе серьезный разговор!"
    w6 "Ты должна помочь мне Юлия!"
    w6 "Ты же говорила, что будешь помогать коллегам!"
    w5 "Тебе ничего не надо делать! Просто скажи мне цвет своих трусиков."
    w6 "Нет, ему не надо ничего говорить! Скажи мне!"
    w5 "Нет, МНЕ!!!"
    w6 "МНЕ!!!"
    julia "Хватит!" # Юлия в шоке
    julia "!!!"
    julia "Я не собираюсь никому ничего рассказывать!"
    w5 "Тогда покажи!"
    w6 "Она не будет тебе показывать! А мне покажет! Да, Юлия?"
    julia "Конечно, нет!!!"
    w6 "!!!"
    w5 "!!!"
    # Грета тянется рукой к юбке Юлии, та отстраняется
    julia "!!!"
    julia "Вы совсем ненормальные?!"
    julia "Не трогайте меня!"
    julia "Я сегодня же пожалуюсь Миссис Бакфетт на вас!"
    julia "!!!"
    # Юлия убегает из кабинета, они смотрят ей вслед, потом друг на друга
    w6 "!!!"
    w5 "!!!"
    return



###############

# Юлия приходит к Монике и говорит что не понимает что происходит
# Моника говорит что все просто. Скажи цвет своих трусиков
# Юлия отвечает что это личное и она не может это сказать
# Юлия спросит зачем Монике это надо?
# Моника понимает что ей не сказать про Фреда, иначе правда про нее всплывет
# Юлия спрашивает, что это потому что я нравлюсь Вам?
# Моника может ответить что да, ты мне нравишься
# Думает сейчас подыграю и выясню у нее
# свидание и развитие отношений



# Мелани + Моника + Виктория у Моники дома
