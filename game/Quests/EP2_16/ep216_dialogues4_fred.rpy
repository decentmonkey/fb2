default monicaJuliaFredVisit1 = False # Фред застукал Монику и Юлию у них в квартире
default monicaJuliaFredVisit2 = False # Моника делала ассликинг Юлии в комнате отдыха


# сразу после сцены утреннего куни Юлии у нее в квартире (ep213_dialogues5_julia_8, при выборе пунктов меню "Продолжить ласкать Юлию")
label ep216_dialogues4_fred_1:
    # Юлия лежит, распластавшись на кровати, прибалдевшая
    # Моника валяется расслабленно раздвинув ноги или как-то
    julia "Ох, Миссис Бакфетт, это было восхитительно!"
    julia "Мммм... Какое хорошее начало дня!"
    mt "Еще бы!"
    mt "Какой-то бывшей никчемной гувернантке ее хозяйка и ее Босс делает ТАКОЕ!"
    mt "Неужели она не понимает, что мне противны все эти извращенства?!"
    mt "Как можно быть такой дурой?!"
    mt "!!!"
    mt "Нужно будет снова поговорить с ней об этом ее родственнике..."
    mt "И об отъезде из страны..."
    mt "Моя свобода уже так близко!"
    mt "Моника, осталось потерпеть эту влюбленную дурочку совсем немного!"
    mt "Потом ты сможешь послать ее ко всем чертям!"
    mt "И начать жизнь с чистого листа!"
    # ее мысли прерывает звук открывающейся двери
    # Моника испуганно накрывается одеялом, Юлия тоже, смотрят в сторону входной двери
    # звук мужских шагов
    m "!!!"
    m "Это кто?!"
    m "У кого-то есть ключи от твоей квартиры?!"
    julia "Н-нет..."
    # Моника с кровати
    # звук пластинка
    m "ФРЕД?!"
    m "!!!"
    m "!!!!!"
    julia "Ой..."
    fred "Миссис Бакфетт?"
    fred "Отлично выглядите!" # со своей улыбочкой

    # Моника вскакивает, прикрывается и орет
    m "Какого черта ты тут делаешь, Фред?!"
    m "!!!"
    fred "У меня к Вам, Миссис Бакфетт, тот же вопрос."
    fred "Что Вы тут делаете? Я весьма удивлен!"
    m "Это не твое дело, что Я тут делаю!"
    # Моника смотрит на Юлию
    m "Почему этот никчемный водитель заходит к тебе в квартиру, как к себе домой?!"
    m "Как это понимать?!"
    # Юлия испуганно молчит
    fred "Миссис Бакфетт, хочу Вам напомнить, что я профессионал."
    fred "И посчитал своим профессиональным долгом проверить..."
    fred "Все ли хорошо у моей подруги Юлии."
    fred "Кстати, дверь была открыта..."
    # Моника снова смотрит на Юлию в бешенстве
    m "Тебя в твоей провинции не учили закрывать двери на ночь?!"
    m "?!?!?!"
    mt "ДУРА!!!"
    mt "!!!"
    julia "Я... Я не знаю как так получилось..."
    julia "Я забыла..."
    fred "Не волнуйтесь, Миссис Бакфетт."
    fred "Я же профессионал."
    fred "Поэтому умею хранить чужие секреты."
    fred "Я никому не скажу о Вашей тайной связи с Вашей помощницей..."
    fred "И Вашей бывшей гувернанткой."
    # Монику бомбит
    m "НЕТ НИКАКОЙ СВЯЗИ!!!"
    m "И ВООБЩЕ!!!"
    m "ТЕБЯ ЭТО НЕ КАСАЕТСЯ!!!"
    m "ТВОЕ ДЕЛО СЛЕДИТЬ ЗА МАШИНОЙ!!!"
    m "А НЕ СОВАТЬ СВОЙ МЕРЗКИЙ НОС НЕ В СВОИ ДЕЛА!!!"
    m "НИКЧЕМНЫЙ ВОДИТЕЛЬ!!!"
    m "!!!"
    m "НЕ СМОТРИ НА МЕНЯ!!!"
    m "ОТВЕРНИСЬ БЫСТРО!!!"
    # Фред, ехидно улыбаясь, отворачивается
    # затемнение, звук надевания одежды, бег на каблуках, хлопает входная дверь
    $ monicaJuliaFredVisit1 = True # Фред застукал Монику и Юлию у них в квартире
    return

# Моника стоит на улице возле дома Юлии, мысли
label ep216_dialogues4_fred_2:
    # не рендерить!!
    mt "Как ты могла допустить ТАКОЕ, Моника?!"
    mt "Этот гребаный мерзавец Фред теперь все знает!!!"
    mt "!!!"
    mt "А что, если он всем расскажет?!"
    mt "Боже! Какой кошмар!!!"
    mt "У него теперь новый повод для того, чтобы шантажировать МЕНЯ!!!"
    mt "Юлия идиотка!!!"
    mt "Бесполезная, глупая идиотка!!!"
    mt "Никчемная!!!"
    mt "Это все из-за ее тупости!!!"
    mt "ААААА!!!"
    mt "НЕНАВИЖУ!!!"
    mt "!!!"
    return

# тем временем, в квартире Юлии
# Юлия также сидит на кровати, Фред стоит посреди комнаты
label ep216_dialogues4_fred_3:
    # Юлия растерянно смотрит на него
    julia "Мистер Фред..."
    julia "Вы... Вы что-то хотели?"
    # Фред отвечает с улыбочкой
    fred "Я просто хотел проверить, как у тебя дела, Юлия..."
    fred "Не обижает ли тебя Миссис Бакфетт..."
    fred "Но теперь я удостоверился, что у тебя все в порядке."
    julia "Д-да..."
    julia "Все хорошо..."
    # Фред подходит к кровати и берет в руку одеяло, которым прикрывается Юлия
    fred "Юлия..."
    fred "Я также считаю своим профессиональным долгом предложить тебе..."
    # тянет одеяло с Юлии, но та его удерживает
    fred "Свою поддержку, если вдруг у тебя возникнут проблемы с Миссис Бакфетт."
    fred "А такая ситуация весьма вероятна, Юлия..."
    fred "Ты даже не представляешь, на что способна эта женщина ради своей выгоды."
    julia "Неправда!"
    julia "Она любит меня!"
    julia "У нас с ней серьезные отношения!" # сердито выдергивает одеяло из руки Фреда
    # Фред смеется на это
    fred "Просто помни о моем предложении..."
    fred "Ты всегда можешь обратиться ко мне за помощью, Юлия."
    julia "..."
    # Фред смотрит на нее с улыбочкой, разворачивается и уходит
    # Юлия в растерянности смотрит ему вслед
    return

# Моника стоит на улице возле дома Юлии, хочет зайти обратно в квартиру, мысли
label ep216_dialogues4_fred_4:
    # не рендерить!!
    mt "Я не пойду туда!"
    mt "Не хочу видеть этого мерзавца Фреда!"
    return

# офис Моники
# при клике на Юлию после визита Фреда
label ep216_dialogues4_fred_5:
    # использовать имеющиеся диалоговые арты!
    mt "Чертова дура Юлия!"
    mt "Я надеюсь, она не рассказала Фреду о нашей связи!"
    mt "Мне нужно будет спросить у нее..."
    # подходит к Юлии
    m "Юлия..."
    julia "Миссис Бакфетт, Вы не сердитесь на меня?"
    julia "Я не знаю, как я могла забыть закрыть дверь..."
    m "Конечно, я не сержусь, милая..."
    # Юлия лезет к ней обниматься
    julia "О, Миссис Бакфетт!"
    julia "Я так переживала, что Вы расстроитесь из-за того..."
    julia "Что Мистер Фред все о нас узнал..."
    # Моника отстраняется
    m "В смысле?!"
    m "Ты ему рассказала о наших отношениях?!"
    m "?!?!?!"
    julia "Да, я ему по-дружески все рассказала."
    julia "Он обещал никому не говорить о нашей маленькой тайне."
    julia "Не переживайте, Миссис Бакфетт."
    julia "Мистеру Фреду можно доверять."
    mt "Черт!"
    mt "Нашла кому доверять!"
    mt "ДУРА!!!"
    mt "!!!"
    julia "Миссис Бакфетт, поцелуйте меня. Я так соскучилась!"
    # Моника зло
    m "Мне некогда, Юлия!"
    m "У меня много важных дел!"
    # Юлия обиженно клянчит
    julia "Я так и знала, что Вы не любите меня, Миссис Бакфетт..."
    julia "Если бы Вы меня любили, то любили бы и целовать меня..."
    julia "И постоянно этого хотели бы..."
    mt "О Боже!!!"
    mt "Когда же прекратится весь этот цирк?!"
    mt "Так, Моника, помни о том, что ты ее просто используешь."
    mt "Тебе даже на руку, что она такая глупая."
    mt "И не замечает, насколько она тебе противна."
    # Моника обнимает Юлию
    m "Ну что ты, милая..."
    m "Конечно, я люблю тебя..."
    m "И поцелую тебя... С удовольствием..."
    # поцелуй
    julia "Ммммм..."
    julia "Я обожаю целоваться с Вами, Миссис Бакфетт..."
    julia "И не только целоваться..." # игриво
    mt "Начинается!"
    mt "!!!"
    m "Я тоже, милая..."
    m "А теперь мне пора."
    m "Мы продолжим позже."
    julia "Буду ждать с нетерпением, Миссис Бакфетт."
    # Моника отходит от нее
    mt "Дьявол!"
    mt "Зачем эта дура все рассказала Фреду?!"
    mt "У нее что, совсем мозгов нет?!"
    mt "Как же она меня БЕСИТ!"
    mt "!!!"
    mt "Что же теперь делать?!"
    mt "Чего ожидать от этого никчемного профессионала?!"
    mt "В любом случае, нужно быть аккуратнее с мерзавцем Фредом!"
    mt "Он обязательно захочет воспользоваться этой информацией против меня!"
    mt "Я должна быть на шаг впереди него!"
    mt "Ведь я не только самая красивая и богатая женщина в этом городе..."
    mt "Я еще и самая умная!"
    mt "Что бы там этом мерзавец не задумал..."
    mt "У него не хватит мозгов обыграть МЕНЯ, саму Миссис Монику Бакфетт!"
    return

# Моника при клике на Фреда после его визита к Юлии в квартиру, мысли
label ep216_dialogues4_fred_6:
    # не рендерить!!
    mt "Гребаный мерзавец Фред!"
    mt "Ничтожный жалкий человечишко!"
    mt "Не хочу с ним разговаривать!!!"
    return

# при условии, что у Моники отношения с Юлией и у Юлии максимальный уровень (т.е. с ней пройдены все сцены в квартире)
# h-сцена с Юлией в офисе
# рабочий кабинет Моники, день
label ep216_dialogues4_fred_7:
    # Моника на рабочем месте, Юлия за своим столом
    # Моника устало
    mt "Что-то у меня разболелась голова."
    mt "..."
    mt "Моника, ты совсем себя не жалеешь..."
    mt "Постоянно в заботах и в работе..."
    mt "Совсем не бережешь свои нервы."
    mt "Как же непросто быть боссом."
    mt "Я единственный умный человек в этом никчемном отделе."
    mt "Вся работа держится на мне одной!"
    mt "И эти все глупые и бесполезные людишки меня утомляют."
    mt "..."
    mt "Мне нужно прилечь и отдохнуть немного..."
    # Моника встает и идет в комнату отдыха
    # ложится на диван и прикрывает глаза
    mt "Я полежу несколько минут..."
    mt "Отдохну..."
    mt "Как же хорошо..."
    mt "Никого не видеть и ни о чем не думать..."
    mt "Расслабься немного, Моника..."
    mt "Ты это заслужила..."
    # некоторое время спустя
    # Моника открывает глаза - перед ней голая попа Юлии
    # у Моники шок
    mt "!!!"
    mt "!!!!!"
    mt "Какого черта?!"
    mt "?!?!?!"
    # Юлия смотрит на Монику из-за плеча
    julia "Миссис Бакфетт, вы такая соблазнительная..."
    julia "Я не смогла удержаться!"
    julia "И тоже решила немного расслабиться вместе с Вами."
    julia "Тем более..."
    julia "Вам ведь так понравилось в прошлый раз целовать мою попу..."
    #
    $ notif(_("Моника лизала попу Юлии в душе."))
    #
    m "Мне?!"
    m "!!!"
    julia "Да..."
    julia "Миссис Бакфетт, а почему Вы так смотрите на меня?"
    # Юлия расстроенно, убирает свою попу в сторону и начинает канючить
    julia "Разве это неправда?"
    julia "Вам не нравится целовать мою попу?"
    mt "Твою мать!"
    mt "Опять она за свое!!!"
    mt "!!!"
    julia "Если это так, то и меня Вам не нравится целовать."
    julia "Значит, я все это время заблуждалась и наши чувства не искренние..."
    mt "АААААА!"
    mt "!!!"
    mt "Так, спокойно!"
    mt "Моника, думай про свою цель: получить свободу и закончить этот кошмар."
    mt "Ты не должна дать ей повод усомниться в своих чувствах."
    m "..."
    m "Конечно, мне понравилось целовать твою попу, милая."
    m "Как может быть иначе? Ведь ты мне очень нравишься..."
    m "И не просто нравишься. Я испытываю к тебе глубокие чувства."
    mt "Глубокое чувство отвращения!"
    julia "Правда, Миссис Бакфетт?!"
    m "Конечно, милая..."
    # Юлия радостная, снова нависает своей голой попой над лицом Моники
    # Моника смотрит на попу Юлии
    mt "Она хочет, чтобы я..."
    mt "О, Боже!"
    mt "Как же это омерзительно! Фу!"
    mt "!!!"
    menu:
        "Отказать Юлии!":
            mt "Нет!"
            mt "Я не собираюсь заниматься этими извращениями!"
            mt "С чего это она решила, что я должна выполнять ее прихоти?!"
            m "Юлия! Не сейчас!"
            m "У меня очень много дел!"
            m "И еще..."
            m "Еще у меня жутко болит голова!"
            m "Давай, мы с тобой позже вернемся к этому вопросу!"
            # Юлия обижена, встает и поправляет свое платье
            julia "Да, Миссис Бакфетт..."
            julia "Как скажете."
            # Моника садится на диван
            mt "Никчемная глупая Юлия!!!"
            mt "!!!"
            return False
        "Целовать попу Юлии.":
            $ monicaJuliaFredVisit2 = True # Моника делала ассликинг Юлии в комнате отдыха
            pass
    # Юлия смотрит на Монику и улыбается
    # Моника смотрит на ее попу с отвращением
    mt "Черт!"
    mt "Почему Я, ее Босс, должна выполнять ее прихоти?!"
    mt "Прямо здесь! В своем кабинете?!"
    mt "Не могу поверить, что я собираюсь делать ЭТО!"
    mt "Какое грязное извращенство!!! Фууу!!!"
    mt "!!!"
    m "Юлия, а если кто-то из сотрудников зайдет?"
    julia "Мы же в комнате отдыха, Миссис Бакфетт..."
    julia "Я успею встать и поправить платье."
    julia "Никто ничего не успеет увидеть..."
    mt "!!!"
    # Моника приближает лицо к ее попе и начинает лизать
    julia "Ооооо!!!"
    julia "Как хорошо!!!"
    m "Милая... Нас могут услышать."
    m "Постарайся потише."
    julia "Да-да..."
    julia "Я постараюсь."
    # Моника снова принимается за ее попу
    julia "Мммммм..."
    # звук открывающей двери, шаги
    # Моника резко отстраняется от Юлии
    m "Дьявол!"
    m "!!!"
    m "!!!!!"
    # Юлия вскакивает с дивана и поправляет платье
    # Моника садится на диван и в этот момент заходит серая мышка в очках
    w1 "Ой, М-миссис Бакфетт..."
    w1 "Я Вам не помешала?"
    if monicaBitch == True:
        # Моника орет на нее
        m "ПОМЕШАЛА!!!"
        m "!!!"
        m "И вообще!"
    m "Тебя что, не учили стучаться?!"
    m "!!!"
    w1 "Я... Просто... Я..." # испуганно
    w1 "Хотела показать Вам свои отчеты..."
    m "Позже! Мне некогда сейчас!"
    w1 "Д-да конечно..."
    m "ИДИ ОТСЮДА!!!"
    # серая мышка испуганно выбегает
    # Моника злая
    m "Юлия!"
    m "Еще немного и она увидела бы нас!"
    julia "Ну чего Вы так расстраиваетесь, Миссис Бакфетт?"
    julia "Она ведь ничего не увидела!"
    mt "Я даже не хочу думать о том, какие сплетни поползли бы по отделу!!!"
    mt "А потом и по всему городу!"
    mt "И в заголовках газет!"
    mt "Моника Бакфетт и ее помощница состоят в интимной связи!"
    mt "Моника Бакфетт лижет зад своей подчиненной прямо на рабочем месте!"
    mt "Успешная бизнес леди и девушка с трущоб. Их история любви!"
    mt "Ужас!!!"
    mt "!!!"
    # Юлия тем временем уже задрала платье и села на диван на колени, игриво зовет Монику
    julia "Миссис Бакфетт, моя попа уже ждет Вашего внимания..."
    julia "Ей так нравится Ваш язычок!#it"
    mt "!!!"
    menu:
        "Целовать попу Юлии.":
            pass
    mt "Твою мать!!! Достала!!!"
    mt "!!!"
    mt "Просто нужно быстрее закончить с этим!"
    mt "И тогда она, наконец, отстанет от меня!"
    mt "Как же она меня бесит!!!"
    mt "!!!"
    # Моника натягивает улыбку
    m "Да, милая, конечно..."
    # Моника наклоняется к попе Юлии и целует ее
    # начинает лизать
    julia "Ааааа..."
    julia "Еще!!"
    julia "Ооо, даааа!!!"
    julia "Еще чуть-чуть, Миссиииис Бакфеееетт!!!"
    julia "Я сейчас коооончуууу!!!"
    # Юлия прижимает ладонь к губам
    julia "МММ!"
    julia "МММММ!!!"
    julia "ММММММММ!!!!"
    julia "!!!"
    # кончает
    # затемнение
    # Моника отстраняется и пока Юлия сидит балдеет, вытирает губы недовольно
    julia "О, Миссис Бакфетт!"
    julia "У Вас с каждым разом получается все лучше и лучше!"
    mt "Потрясающе!"
    mt "Поздравляю, Моника."
    mt "Тебе стали делать подобные комплименты!"
    m "Милая, я рада, что тебе понравилось."
    # затемнение, звук каблуков
    # Юлия возвращается на свое рабочее место
    # Моника злая сидит на диване
    mt "Не могу поверить в это!"
    mt "Эта бывшая гувернантка манипулирует МНОЮ, своим БОССОМ!!!"
    mt "Она делает все для того, чтобы я выполняла ее прихоти!!!"
    mt "!!!"
    mt "Я больше не должна допускать подобных глупостей!"
    mt "Все-таки Я здесь начальник!"
    mt "И командую здесь только Я!"
    mt "!!!"
    return
