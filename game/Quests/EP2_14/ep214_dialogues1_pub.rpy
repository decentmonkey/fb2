default monicaClareBankerPrivate1 = False # Эшли не вешает плакат, если Моника договорится с Клэр о привате
default monicaClareBankerPrivate2 = False # Моника пригласила Клэр в свой офис
default monicaClareBankerPrivate3 = False # Клэр была у Моники в офисе
default monicaClareBankerPrivate4 = False # Моника пошла на 2-й приват с банкиром
default monicaClareBankerPrivate5 = False # Моника разделась перед банкиром
default monicaClareBankerPrivate6 = False # Моника сняла маску перед банкиром



# Моника заходит в паб, стоит возле барной стойки
label ep214_dialogues1_pub_1:
    # на стене справа от барной стойки Джо вешает ее плакат с последней фотосессии
    # Эшли стоит за барной стойкой
    # Джо держит плакат в руках и примеряет его к стене, из-за его спины Монике не видно, что там изображено
    joe "Вот так нормльно?"
    ashley "Нет, правее и выше."
    joe "Сюда?"
    ashley "Теперь немного левее."
    # Моника смотрит на Джо и пока не видит фото на плакате
    mt "Что эта ненормальная семейка извращенцев делает?"
    mt "Решили повесить на стену рекламу дешевого пива для плебеев?"
    m "Эшли, я пришла."
    # Джо поворачивается и показывает Монике плакат с ее фотосессии в красном платье (как на обложке журнала)
    joe "А, это ты!"
    joe "Смотри, что у нас есть!"
    # у Моники шок
    mt "ЧТООО?!"
    mt "О, Боже!"
    mt "Нет, только не это!"
    mt "Они поняли, что я Моника Бакфетт!"
    mt "Теперь все в этой чертовой дыре будут знать, что я не [monica_pub_name]!"
    mt "!!!"
    mt "!!!!!!"
    # Эшли смотрит на Монику
    ashley "Удивлена, [monica_pub_name]?"
    ashley "Я тоже сначала удивилась. Подумала, что это ты."
    ashley "Потом поняла, что такую шлюху, как ты, даже близко не подпустят к фотостудии."
    ashley "Наверняка, там много дорогого оборудования, которое ты захотела бы стащить."
    #
    $ notif(_("Моника воровала чаевые."))
    #
    mt "Это и есть Я!"
    mt "Дура!"
    mt "!!!"
    ashley "Это известная в нашей стране богатая сучка. И ты на нее очень похожа."
    ashley "Я решила воспользоваться этим."
    # Моника с облегчением
    mt "Уф. Как же хорошо, что у этих никчемных барменов нет мозгов..."
    mt "Это же очевидно, что на плакате позирую Я!"
    m "Как воспользоваться?"
    ashley "Мы повесим этот плакат для посетителей."
    ashley "Пусть все знают, что в моем баре работает девочка, похожая на эту супер звезду."
    ashley "Они будут приходить сюда, чтобы поглазеть на тебя, [monica_pub_name]."
    ashley "И будут представлять, что именно эта богатая сучка показывает им свой зад со сцены, а не ты."
    joe "Да! И еще нужно, чтобы ты снимала маску на сцене, [monica_pub_name]."
    joe "Двойник самой Моники Бакфетт танцует стриптиз в Shiny Hole!"
    joe "Ты станешь местной знаменитостью, [monica_pub_name]!"
    # Джо с Эшли довольно смотрят на Монику, Эшли ей подмигивает игриво
    ashley "А в моем баре станет в десятки раз больше клиентов."
    ashley "И все благодаря твоей голой попке, похожей на эту Бакфетт."
    # Моника в шоке
    mt "Нет-нет!"
    mt "Мне нельзя допустить этого!"
    mt "Эти двое настолько тупы, что не узнали меня на плакате..."
    mt "Но это не значит, что никто не поймет этого!"
    mt "!!!"
    menu:
        "Отговаривать Эшли.":
            pass
    m "Эшли, нет!"
    m "Это плохая идея. Я..."
    # Джо стоит их слушает, Эшли удивленно спрашивает у Моники
    ashley "Чего ты паришься?"
    ashley "Да, она намного красивее чем ты..."
    ashley "Но все равно вы очень похожи."
    # Моника упрямо
    m "Я..."
    m "Я не хочу, чтобы этот плакат висел здесь!"
    ashley "Она что, не нравится тебе?"
    ashley "А я потрогала бы ее попку..."
    m "Да, она мне не нравится!"
    m "Поэтому я и не хочу, чтобы ее плакат висел тут!"
    # Эшли говорит, мечтательно глядя на плакат
    ashley "Вам, девочки, далеко до такой звезды..."
    ashley "Ты только посмотри на нее! От нее так и веет роскошью."
    ashley "Джо, чего ты стоишь?! Вешай его на стену!"
    # Джо снова принимается за работу
    menu:
        "Продолжать отговаривать Эшли.":
            pass
    mt "Черт! Черт! Черт!"
    mt "!!!"
    m "Эшли!"
    m "Я не хочу, чтобы это тут висело!"
    # Эшли недовольно
    ashley "Ну не знаю..."
    ashley "Мне нравится, что плакат будет висеть тут."
    ashley "Почему я должна отказывааться от этой идеи?"
    ashley "Дела в баре идут не так хорошо как хотелось бы мне."
    ashley "А это принесет моему бару дополнительную прибыль."
    # Моника продолжает уговаривать ее
    menu:
        "Продолжать отговаривать Эшли.":
            pass
    m "Эшли!"
    m "Я не хочу, чтобы..."
    m "Чтобы меня все сравнивали с этой Моникой Бакфетт!"
    m "Я [monica_pub_name], а не она!!!"
    # Эшли раздраженно
    ashley "[monica_pub_name], хватит уже!"
    ashley "Я бы на твоем месте, наоборот, гордилась бы!"
    ashley "И вообще!"
    ashley "С какой стати я должна прислушиваться к твоим просьбам?"
    ashley "Ты воруешь чаевые! До сих пор не сделала документы!"
    m "Эшли, я..."
    ashley "[monica_pub_name], ты чего ко мне пристала?"
    m "Я не хочу, чтобы этот плакат висел в баре!"
    ashley "..." # сердито
    m "!!!" # упрямо
    # Эшли с хитрецой смотрит на Монику
    ashley "Ну ладно..."
    ashley "Пойдем со мной в гримерку."
    ashley "У меня для тебя есть одно предложение..."
    # смотрит на Джо
    ashley "Джо, подожди пока. Не вешай плакат."
    joe "Но почему?!"
    ashley "Потому что так сказала Я!"
    joe "Вот так всегда... Джо, иди туда... Джо, сделай это..."
    ashley "Джо! Сложи этот чертов плакат и займись работой!"
    # Эшли уходит из-за барной стойки
    mt "Как же хорошо, что мне удалось отговорить ее от этой дурацкой идеи с плакатом!"
    mt "Не хватало еще, что бы моя фотография висела в этой грязной дыре!"
    mt "И все эти никчемные неудачники смотрели бы на нее!"
    mt "Кто-нибудь обязательно догадался бы, что это Я!"
    mt "Кошмар!!!"
    return

# плакат остается лежать свернутый или сложенный на барной стойке где-нибудь сбоку -?
# мысли при клике на плакат (свернутый на барной стойке или возле нее)
label ep214_dialogues1_pub_1a:
    # не рендерить!!
    mt "Мне ни в коем случае нельзя допустить, чтобы эти никчемные бармены повесили плакат со МНОЙ!!!"
    mt "Где они вообще нашли этот гребаный плакат?!"
    mt "!!!"
    return


# гримерка
label ep214_dialogues1_pub_2:
    # по возможности использовать имеющиеся арты
    # Эшли с Моникой стоят в гримерке
    # Моника смотрит подозрительно
    m "Что за предложение?!"
    mt "Очередная извращенская гадость?!"
    # Эшли говорит ей игриво
    ashley "[monica_pub_name], помнишь Мистера Беркельбауха?"
    m "Тот никчемный банкир?"
    ashley "Да, банкир. И не называй его так!"
    ashley "В общем, Мистер Беркельбаух придет к нам на днях..."
    m "И?"
    ashley "И он требует сделать как в прошлый раз."
    ashley "Он хочет снова посмотреть на девочек Shiny Hole."
    ashley "Ну ты понимаешь, о чем я..."
    m "Он хочет посмотреть на задницы шлюх?"
    # Эшли рассержено
    ashley "[monica_pub_name]! Прекрати говорить так о Мистере Беркельбаухе!"
    ashley "Он очень важный человек и помогает моему заведению!"
    ashley "Я даю работу таким шлюхам, как ты!"
    ashley "А ты должна быть благодарна мне за мою доброту!"
    ashley "И за благосклонность Мистера Беркельбауха!"
    # Моника недовольно
    mt "Тоже мне важный человек!"
    mt "Какой-то никчемный банковский клерк! Фи!"
    m "Ты хочешь, чтобы я снова стояла перед ним с голой попой?"
    m "Это и есть твое предложение?"
    ashley "Ты, [monica_pub_name], итак будешь стоять перед ним с голой задницей!"
    ashley "Мне для этого не надо делать тебе предложение!"
    mt "!!!"
    ashley "И вообще! Для меня странно, что ты против этого плаката."
    ashley "Это же отличная реклама для тебя."
    m "Я против, Эшли!"
    ashley "Но раз так, то ты должна будешь кое-что для меня сделать..."
    m "И что же?"
    ashley "Для того, чтобы Мистер Беркельбаух улучшил для меня условия кредитования..."
    ashley "Я договорилась с ним..."
    ashley "В общем, он хочет посмотреть на всех девочек Shiny Hole сразу."
    m "Он что, их не видел? В чем проблема?"
    m "Молли любит вертеть своей задницей перед клиентами. Позови эту шлюху."
    ashley "[monica_pub_name], я же тебе говорю, что всех девочек сразу."
    ashley "И с Молли нет никаких проблем."
    ashley "Проблему может создать Клэр. Она там тоже должна быть."
    m "Клэр на такое не согласится. Без вариантов."
    ashley "В этом все и дело."
    ashley "Она давно здесь работает и у нее не было ни одного приватного танца."
    ashley "Я не могу ее заставить, так как она танцует здесь не ради денег."
    mt "Надеюсь, она не думает, что я пойду уговаривать Клэр?!"
    mt "Что за бред!"
    mt "!!!"
    ashley "И раз ты не хочешь, чтобы тот плакат висел в баре..."
    ashley "С Клэр договариваться будешь ты."
    m "Но Эшли! Клэр на подобное не согласится!"
    m "!!!"
    ashley "[monica_pub_name], ты уговоришь Клэр сделать это вместе со всеми!"
    ashley "Только в этом случае я не стану вешать плакат с богатой сучкой Бакфетт!"
    ashley "Если Клэр не придет на приват к Мистеру Беркельбауху..."
    ashley "То я в этот же вечер прикажу Джо повесить плакат возле барной стойки!"
    ashley "Это все!"
    $ monicaClareBankerPrivate1 = True # Эшли не вешает плакат, если Моника договорится с Клэр о привате

    # Эшли уходит, Моника стоит в гримерке растерянная
    mt "Чертова Эшли!"
    mt "ААААА!"
    mt "И что мне теперь делать?"
    mt "Как мне уговорить Клэр?"
    mt "Мне ни в коем случае нельзя допустить, чтобы эти никчемные бармены повесили плакат со МНОЙ!!!"
    mt "Где они вообще нашли этот гребаный плакат?!"
    mt "!!!"
    return

# гримерка
label ep214_dialogues1_pub_3:
    # по возможности использовать имеющиеся арты
    # Клэр сидит за своим столиком, при клике на нее
    mt "Черт. Мне нужно хотя бы попытаться уговорить Клэр на приват."
    mt "Но как мне это сделать?"
    mt "???"
    mt "Она мне предлагала обращаться к ней за помощью, при необходимости..."
    mt "Думаю, что это как раз тот случай, когда мне нужна ее помощь."
    # Клэр поворачивается к Монике
    clare "Моника, привет."
    m "Привет, Клэр..."
    m "..."
    m "Как у тебя дела?"
    clare "Все отлично."
    clare "Сегодня в очередной раз отказала нескольким поклонникам в привате."
    clare "Они предлагают деньги, я отказываю."
    clare "В следующий раз они предлагают еще большую сумму за приват..."
    clare "А я снова отказываю."
    clare "Им никак не понять, что дело совсем не в деньгах..."
    clare "..."
    clare "А как у тебя дела, Моника?"
    clare "Выглядишь расстроенной. У тебя все в порядке?"
    m "Да. То есть..."
    m "Не совсем..."
    clare "Что случилось?"
    m "Клэр, ты говорила мне, что я могу обратиться к тебе за помощью..."
    m "Надеюсь, твое предложение все еще актуально?"
    clare "Актуально. Тебя Молли опять в чем-то обвиняет?"
    m "Нет. У меня снова проблема с Эшли."
    m "Она поставила условие, которое я не могу не выполнить."
    m "В противном случае, я просто не смогу больше здесь работать."

    # если Моника рассказала Клэр правду о себе
    # if monicaClareStoryAboutLife = True (диалог в лейбле ep210_dialogues4_dance_strip_2)
    #
    $ notif(_("Моника рассказала Клэр правду о себе"))
    #
    m "А мне нельзя терять эту работу из-за моих временных трудностей..."
    m "Я уверена, что совсем скоро я верну себе все, что у меня попытались забрать."
    m "Но мне нужно еще немного времени."
    m "И работа в этом баре нужна. Пока что..."
    m "А из-за каких-то условий Эшли я могу потерять этот источник заработка."
    #

    # если Моника солгала Клэр про спор с подругами
    #
    $ notif(_("Моника сказала Клэр, что работает в баре из-за спора с подругами"))
    #
    m "А я не хочу проиграть этот спор со своими подругами..."
    m "Ведь я уже так долго работаю здесь."
    m "Вернее, делаю вид, что работаю."
    m "Ведь на самом деле мне этот заработок не нужен, у меня итак есть все."
    m "Но мне не хотелось бы, чтобы этот экспиремент провалился из-за каких-то условий Эшли."
    #

    clare "Что за условие поставила тебе Эшли?"
    mt "Черт!"
    mt "Я не хочу рассказывать ей про плакат."
    mt "Она знает мое настоящее имя."
    mt "Если я расскажу про плакат, она подумает, что я не владелица бизнеса..."
    mt "А обычная модель, которая раздевается перед камерой, чтобы заработать больше."
    mt "А это не так!!!"
    mt "!!!"
    m "..."
    m "У Эшли какие-то проблемы с кредитами."
    m "И она договорилась с каким-то никчемным банкиром, что он ей поможет."
    m "Взамен он хочет приват, на который придут все девочки Shiny Hole сразу."
    clare "Все?"
    m "Да."
    clare "То есть и я в том числе?"
    m "Да."
    clare "Дай-ка угадаю."
    clare "Условие, которое тебе поставила Эшли - уговорить меня прийти на этот приват?"
    m "..."
    clare "Моника, я, конечно, очень хочу тебе помочь, но..."
    mt "Она сейчас откажет мне!"
    mt "Что же мне придумать?"
    mt "???"
    mt "Думай, Моника, думай!"
    mt "А что, если..."
    m "..."
    m "Клэр, не торопись давать ответ сейчас."
    clare "???"
    m "Я хочу доказать тебе, что я действительно Моника Бакфетт, а не какая-то [monica_pub_name]."
    m "И что у меня действительно есть все то, о чем я тебе рассказывала."
    m "Ты поймешь, что я тебя не обманывала."
    m "И что для меня работа в этом чертовом баре - необходимость."
    m "Хоть и временная."
    clare "Разве я говорила, что сомневаюсь в твоих словах?"
    m "Я хочу, чтобы ты все увидела своими глазами."
    m "Приходи {c}завтра днем к моему офису{/c} Fashion Business."
    m "Я тебе покажу все, чем я владею."
    clare "Моника, спасибо за приглашение, но я не уверена, что у меня получится."
    m "..."
    # Клэр улыбается
    clare "Хотя, это довольно интересное предложение."
    m "Приходи завтра. Я буду ждать тебя."
    clare "Хорошо, Моника. Я постараюсь."
    $ monicaClareBankerPrivate2 = True # Моника пригласила Клэр в свой офис

    # Моника отходит к гардеробу, Клэр возвращается за свой столик
    mt "Я проведу Клэр по своему офису и тогда она мне поверит."
    mt "Она же не сможет отказать в просьбе самой Монике Бакфетт!"
    mt "Даже если она согласится взамен на что-то..."
    mt "Когда я верну себе свое законное место Большого Босса, я смогу сделать ВСЕ!"
    mt "!!!"
    mt "А пока мне нужно переодеваться и идти на сцену."
    mt "Чертова сцена! Ненавижу!"
    $ log1 = _("Я пригласила Клэр в свой офис, чтобы она убедилась, что я не какая-то [monica_pub_name]. Она же не сможет отказать в просьбе самой Монике Бакфетт!") # квест-лог
    return

# гримерка
# повторный клик на Клэр после того, как Моника пригласила ее в свой офис
label ep214_dialogues1_pub_4:
    # использовать имеющиеся арты
    m "Клэр, приходи {c}завтра днем к моему офису{/c}."
    m "Я тебе покажу все, чем я владею."
    clare "Хорошо, Моника. Я постараюсь."
    m "Приходи. Я буду ждать тебя."
    return

# если Моника пригласила Клэр к себе в офис
# Моника стоит перед офисом на улице, мысли
label ep214_dialogues1_pub_5:
    mt "Я надеюсь, что Клэр не проигнорирует мое предложение."
    mt "Она убедится в том, что я - Моника Бакфетт..."
    mt "И не захочет отказывать МНЕ."
    mt "Мы проведем этот гребаный приват перед никчемным банкиришкой."
    mt "И Эшли, наконец, откажется от дурацкой идеи с плакатом!"
    return

# если Моника пригласила Клэр к себе в офис
# на следующий день Моника приходит на работу в офис
label ep214_dialogues1_pub_6:
    # Клэр в приличной одежде, стоит в холле возле лифта, в холл заходит Моника
    # Клэр поворачивается к ней
    clare "Моника, привет."
    m "Клэр, привет. Я рада, что ты пришла."
    clare "Я не смогла отказаться от такого предложения."
    clare "Не каждый день меня приглашает в офис самого крупного журнала сама Миссис Бакфетт."
    m "С сегодняшнего дня ты можешь приходить сюда, чтобы встретиться со мной."
    m "Только помни, что здесь никто не знает о баре. И не должен узнать."
    clare "Да, конечно."
    m "Пойдем? Я покажу тебе свой кабинет."
    return

# отдел отчетов
label ep214_dialogues1_pub_7:
    # Клэр и Моника заходят в отдел отчетов
    m "Это отдел отчетов моего журнала."
    clare "Эти все сотрудники являются твоими подчиненными?" # удивленно
    m "Да." # гордо
    m "Мой рабочий кабинет временно находится именно в этом отделе."
    m "Так как в настоящее время я провожу оптимизацию процесса работы здесь."
    # подбегает подхалим, как всегда лебезит перед Моникой
    w5 "Миссис Бакфетт, добрый день!"
    w5 "Вы, как всегда, великолепно выглядите!"
    mt "Опять он!"
    mt "Ну почему он всегда и везде лезет?!"
    mt "Снова будет предлагать кофе?!"
    mt "?!"
    m "Здравствуй, Джон."
    # Джон заинтересованно смотрит на Клэр
    w5 "Добрый день, Мисс..."
    w5 "?"
    mt "Вот черт. Я не спросила у Клэр, как мне ее представлять."
    mt "???"
    clare "Добрый день. Я Клэр."
    w5 "Мисс Клэр, приятно с вами познакомиться."
    clare "Взаимно."
    w5 "Добро пожаловать в наш скромный офис, Мисс Клэр!"
    w5 "Не откажете мне в удовольствии угостить вас ароматным кофе?"
    m "Чай, Джон."
    m "И принеси его в мой кабинет."
    w5 "Да, конечно, Миссис Бакфетт. С удовольствием!"
    # подхалим убегает, а айтишник в это время пристально смотрит на Клэр
    # Моника наклоняется к Клэр
    m "Клэр, я не спросила у тебя, как тебя представлять своим подчиненным?"
    # айтишник узнает ее и с радостным удивлением вскакивает со своего стула
    w2 "Мисс Мэнсфилд?!"
    # Моника и Клэр смотрят на него, Моника удивлена
    w2 "Здравствуйте!"
    w2 "Помните меня? Я у Вас учился!"
    w2 "Мой младший брат Эрик сейчас учится у Вас!"
    mt "???"
    # Клэр спокойно ему улыбается
    clare "Конечно, помню. Здравствуй."
    mt "?!?!?!"
    # Клэр поворачивается к Монике
    clare "Моника, покажешь мне свой кабинет?"
    m "Да, конечно. Пойдем."
    m "Джон сейчас уже принесет нам чай."
    # они немного отходят в сторону кабинета
    # Моника удивленно спрашивает Клэр
    m "Так ты Мисс Мэнсфилд?!"
    m "Почему он сказал, что он учился у тебя?!"
    # Клэр спокойно отвечает
    clare "Не Мисс Мэнсфилд. Я просто Клэр."
    clare "Мальчик просто ошибся."
    # Моника смотрит на нее с подозрением
    mt "Мне кажется, я уже слышала где-то эту фамилию."
    mt "Вот только где?"
    mt "..."
    mt "Получается, что фамилия Клэр - Мэнсфилд?"
    mt "Или программист действительно ее с кем-то перепутал?"
    mt "???"
    return

# отдел отчетов
label ep214_dialogues1_pub_8:
    # Клэр и Моника заходят в рабочий кабинет Моники
    m "Проходи, Клэр."
    m "Это мой рабочий кабинет."
    # Клэр спокойно отвечает
    clare "Ого! Мне здесь нравится."
    clare "А это твое кресло?"
    m "Да. Временное."
    # Моника поворачивается и указывает на Юлию
    m "А это моя личная помощница Юлия."
    m "Юлия, это Мисс Клэр. Она моя коллега."
    julia "Добрый день, Миссис Бакфетт, Мисс Клэр."
    julia "Приятно с вами познакомиться."
    clare "Мне тоже очень приятно, Юлия."
    # заходит Джон, несет чашки с чаем (как в сцене с Викторией)
    w5 "Миссис Бакфетт, Мисс Клэр, ваш чай готов."
    m "Хорошо, Джон. Поставь его на столик и можешь идти."
    w5 "Да, Миссис Бакфетт, как скажете."
    w5 "Приятного чаепития."
    # Моника указывает рукой в сторону комнаты отдыха
    m "Клэр, пойдем сюда."

    # смена кадра
    # Моника и Клэр сидят на диванчике и пьют чай, Юлия за своим столом, косится на них и подслушивает
    m "Это и есть мой офис, Клэр."
    m "Конечно, я показала тебе лишь малую его часть..."
    clare "Это все - лишь малая часть?!"
    m "Да, всего один небольшой отдел."
    m "Возможно, как-нибудь я тебе покажу свой офис полностью."

    # смена кадра, айтишник
    # показываем айтишника за его рабочим столом
    # следом показываем монитор айтишника
    # на его компе вид из-под стола Моники с комнаты отдыха
    # он через камеру подсматривает за ними, вертя камеру из стороны в стороны
    w2_t "Что моя бывшая училка здесь делает?"
    # звук бзззз - камера передвигается и показывает то Монику, то Клэр

    # смена кадра, комната отдыха
    # если Моника рассказала Клэр правду о себе
    # if monicaClareStoryAboutLife = True (диалог в лейбле ep210_dialogues4_dance_strip_2)
    #
    $ notif(_("Моника рассказывала Клэр правду о себе"))
    #
    clare "Теперь я понимаю, почему ты готова пойти на многое, чтобы вернуть все это."
    clare "Мне нравится твоя целеустремленность, Моника."
    #

    # если Моника солгала Клэр про спор с подругами
    #
    $ notif(_("Моника говорила Клэр, что работает в баре из-за спора с подругами"))
    #
    clare "Хммм..."
    clare "Теперь я понимаю, почему ты решила поспорить со своими подружками, Моника."
    #

    m "Я рада, что ты меня понимаешь."
    clare "Понимаю и поддерживаю, Миссис Бакфетт."

    # смена кадра, айтишник
    # звук бзззз - камера передвигается и показывает то Монику, то Клэр
    w2_t "Жаль, что я не слышу, о чем они разговаривают."
    w2_t "Надо будет установить звук."

    # смена кадра, комната отдыха
    # Клэр улыбается Монике, ставит чашечку на столик
    clare "Моника, спасибо за чай."
    clare "Я с удовольствием погостила бы еще немного, но..."
    clare "К сожалению, у меня мало времени и мне нужно идти."
    # обе встают, Клэр направляется к выходу
    m "Я тебя провожу, Клэр."
    # Моника поворачивается в сторону Юлии
    m "Юлия, убери со стола чашки."
    m "Пожалуйста."
    julia "Хорошо, Миссис Бакфетт."
    # Юлия вскакивает со своего рабочего места и подходит к столу

    # если Моника состоит в отношениях с Юлией
    # то Юлия подходит к столику и быстро чмокает Монику в щечку
    #
    $ notif(_("Моника состоит в отношениях с Юлией"))
    #
    m "Юлия, милая."
    m "Нас могут увидеть."
    julia "Просто я соскучилась, Миссис Бакфетт."
    julia "А почему Вы сказали, что Мисс Клэр Ваша коллега?"
    julia "Разве она работает в Вашем журнале?"
    mt "Черт!"
    m "Нет, она..."
    m "Она, как и мы, работает в сфере искусства."
    # Моника наклоняется и чмокает Юлию в щечку, Юлия довольно улыбается
    # Моника выходит вслед за Клэр
    # Юлия подходит к столику и наклоняется за чашками

    # смена кадра, айтишник
    # звук бзззз - камера передвигается и показывает то Монику, то Клэр
    w2_t "Хмм... Мне кажется или Юлия теперь ходит без трусиков?"
    w2_t "Как и Миссис Бакфет..."
    # звук каблуков
    w2_t "Черт!"
    # затемнение
    return

# холл возле лифта
label ep214_dialogues1_pub_9:
    # Клэр и Моника заходят и встречают там Бифа
    biff "А, цыпочка."
    # смотрит на Клэр
    biff "А это кто? Новая модель?"
    biff "Почему я не видел ее на кастинге?"
    mt "Чертов Биф!"
    m "Нет, это не модель..."
    # Биф недовольно смотрит на Монику, Клэр с пренебрежением смотрит на Бифа
    biff "Так, кукла! У меня к тебе вопрос: что у нас с инвесторами?!"
    m "Биф, я..."
    biff "Можешь не отвечать."
    biff "Ты ничего не делаешь для того, чтобы очередной денежный мешок вложился в мой журнал!"
    biff "За что я плачу тебе такую зарплату, если ты ничего не делаешь?!"
    biff "Думаешь, если ты похожа на сучку Бакфетт, то я тебе просто так должен деньги давать?"
    m "!!!"
    m "!!!!!!"
    biff "Нет, кукла. Этот номер со мной не пройдет!"
    biff "Не будешь работать - вышвырну с офиса на улицу!"
    biff "Пойдешь сосать члены за 20 баксов, как ты привыкла это делать."
    # затемнение, звук лифта, Биф уходит
    # Клэр и Моника стоят в холле, Клэр смотрит на нее молча
    clare "..."
    mt "Боже!"
    mt "Я сейчас сгорю со стыда!"
    # Клэр делает вид, что ничего не произошло
    clare "Моника, спасибо тебе еще раз за приглашение."
    clare "Мне очень понравилось у тебя на работе."
    clare "Но мне и правда нужно идти."
    clare "Увидимся в баре, как обычно."
    m "Пока, Клэр. До встречи."
    # Клэр уходит, Моника стоит одна в холле
    mt "Биф! Скотина!"
    mt "Как он посмел так со мной разговаривать при Клэр!!!"
    mt "!!!"
    mt "Что она теперь обо мне подумает?!"
    mt "Этот тупой идиот прямо при ней сказал, что я просто похожа на Монику Бакфетт!"
    mt "Клэр теперь не поверит мне!"
    mt "Я НЕНАВИЖУ МЕРЗАВЦА БИФА!"
    mt "НЕНАВИЖУ!"
    mt "!!!"
    $ monicaClareBankerPrivate3 = True # Клэр была у Моники в офисе
    $ log1 = _("Мерзавец Биф! Он при Клэр сказал, что я работаю заменой Моники Бакфетт! Теперь единственный адекватный человек будет считать меня лгуньей!") # квест-лог
    return

# паб, гримерка
# работает Клэр
label ep214_dialogues1_pub_10:
    # Моника заходит в гримерку, Клэр сидит за своим столиком
    mt "Дьявол!"
    mt "Что мне теперь сделать, чтобы она поверила в то, что я - это Я?!"
    # Клэр поворачивается в сторону Моники
    clare "Моника, привет."
    m "Привет, Клэр..."
    m "Я..."
    clare "Моника, кто это разговаривал с тобой в офисе возле лифта? Твой менеджер?"
    m "Да, это..."
    m "Это мой подчиненный."
    m "Иногда ему нравится строить из себя большого босса..."
    m "Хотя на самом деле он там никто."
    clare "Моника..."
    clare "Для меня не важно, являешься ли ты Моникой Бакфетт на самом деле..."
    clare "Или работаешь в том офисе ее заменой."
    m "..."
    clare "Для меня важны совсем другие качества, которые мне нравятся в тебе."
    clare "И мне хочется поддержать тебя не ради какой-то цели."
    clare "А просто потому, что ты хороший человек."
    m "..."
    clare "И я всегда рада буду помочь тебе."
    clare "Только..."
    clare "В случае с приватом для банкира..."
    clare "Пока я не готова дать тебе точный ответ. Мне нужно подумать."
    clare "Пока иди на сцену, тебя там уже ждут."
    # Моника отходит к гардеробу, она удивлена словам Клэр
    mt "Я так и думала..."
    mt "Клэр не придет сегодня на приват с банкиром."
    mt "Ей просто неудобно мне отказать, поэтому она сказала, что подумает."
    mt "..."
    mt "Еще она сказала, что..."
    mt "Для нее не важно, настоящая я Моника Бакфетт или нет."
    mt "Она действительно это сказала? Или мне послышалось?"
    mt "???"
    return

# повторный клик на Клэр после этого диалога
label ep214_dialogues1_pub_11:
    # не рендерить!!
    mt "Мне нужно сейчас идти на сцену."
    mt "После выступления будет приват перед никчемным банкиром."
    return

# после выступления Моника заходит в гримерку
label ep214_dialogues1_pub_12:
    # приходит Эшли
    ashley "[monica_pub_name]!"
    ashley "Мистер Беркельбаух уже ждет нас всех в подсобке!"
    ashley "Давай, поторапливайся!"
    # Эшли уходит
    mt "Ненавижу эту Эшли!"
    mt "И этого никчемного банкира ненавижу!"
    menu:
        "Пойти в подсобку барменов.":
            $ monicaClareBankerPrivate4 = True # Моника пошла на 2-й приват с банкиром
            pass
        "Я не пойду на приват! (увольнение с Shiny Hole)":
            # Моника злая
            mt "Нет!!!"
            mt "Я Моника Бакфетт! Я не буду унижаться перед каким-то неудачником!"
            mt "С меня хватит!"
            mt "Пошло оно все к черту!"
            mt "Я сюда больше не вернусь!"
            mt "!!!"
            # уходит
            return
    mt "Черт! Если я сейчас не пойду на этот приват, то..."
    mt "Тогда Эшли повесит этот гребаный плакат!"
    mt "Я не могу допустить этого!"
    mt "Никто в этой грязной дыре не должен знать, что я Моника Бакфетт!"
    mt "!!!"
    return

# если не пошла в приват, то выходит из паба, ни с кем не разговаривая
# при клике на кого-либо (н-р, барменов)
# мысли - лейбл ep213_dialogues3_pub_14a из версии 13

# если не пошла в приват и вышла на улицу
# + эти же мысли, если хочет зайти обратно в бар после увольнения
# мысли - лейбл ep213_dialogues3_pub_14b

# перед приватом Эшли и Джо у барной стойки
label ep214_dialogues1_pub_13:
    # Эшли стоит руки в боки
    ashley "Джо! Ты совсем не помогаешь мне по работе!"
    ashley "Я с утра до поздней ночи работаю каждый день!"
    ashley "И у меня нет даже нескольких минут на отдых!"
    joe "Как не помогаю?!"
    joe "Я все здесь делаю!"
    ashley "У тебя только одно дело, Джо!"
    ashley "Ты смотришь на голые сиськи шлюх и пускаешь на них слюни!"
    ashley "А я работаю за двоих!!!"
    joe "Это не так, Эшли!"
    joe "Я ни на каких шлюх не смотрю!"
    ashley "Все, Джо! Хватит разговоров!"
    ashley "Займись, наконец, делом!"
    # указывает на бар с бутылками
    ashley "Посмотри на бар! У тебя все бутылки в пыли!"
    ashley "Я тебе даю ровно час!"
    ashley "Если я вернусь и найду хоть одну пылинку..."
    ashley "Я вышвырну тебя из бара! Понял?!"
    joe "Да понял я все, понял. Хватит орать!"
    ashley "Давай, приступай!"
    # Эшли уходит
    return

# приват, подсобка барменов
label ep214_dialogues1_pub_14:
    # банкир, Моника, Молли и Эшли, Клэр нет
    # банкир на диване, Эшли в сторонке у стены
    # Молли и Моника стоят перед столиком, они в масках
    mt "Клэр все-таки отказалась..."
    mt "Я до последнего момента надеялась, что она передумает."
    mt "..."
    mt "Эта извращенка Эшли теперь повесит плакат и слушать ничего не станет."
    mt "Мне нужно будет как-то отговорить ее."
    banker "Эй, крошки."
    banker "Вы чего там застыли?"
    banker "Лезьте на стол и показывайте мне свои попки."
    banker "Не заставляйте меня долго ждать, я этого не люблю."
    mt "Какой же он мерзкий тип!"
    mt "!!!"
    menu:
        "Залезть на стол и снять трусики.":
            $ monicaClareBankerPrivate5 = True # Моника разделась перед банкиром
            pass
        "Не делать этого! (увольнение из паба)":
            m "Я не собираюсь раздеваться перед ним!"
            m "Достаточно было прошлого раза!"
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            return
    # Моника встает на стол, Молли остается стоять на месте
    ashley "Молли, встань рядом с [monica_pub_name]."
    # Молли недовольно смотрит на Монику
    molly "Почему я должна стоять рядом с этой шлюхой?!"
    molly "Пусть она слезет со стола, тогда я туда встану!"
    molly "Я не хочу даже приближаться к ней!"
    # Моника возмущенно смотрит на нее
    mt "Вот сучка!"
    mt "!!!"
    m "Да пошла ты!"
    m "Из нас двоих есть только одна шлюха. Я ее вижу сейчас перед собой!"
    ashley "[monica_pub_name]!"
    ashley "Ты сама сейчас провоцируешь Молли!"
    ashley "Стой и помалкивай!"
    ashley "Не надо мне тут устраивать вашу битву сучек!"
    # Молли самодовольно ухмыляется и смотрит на Монику
    mt "!!!"
    molly "Ну так уж и быть, я постою с тобой рядом..."
    molly "Потерплю тебя..."
    # Молли игриво смотрит на банкира
    molly "Но только ради Мистера Беркельбауха."
    banker "Да, крошка. Сделай это для меня."
    mt "Вот проститутка!"
    mt "Лицемерная дрянь!"
    mt "Ненавижу ее!"
    # Молли встает рядом с Моникой, обе снимают трусики
    banker "Отлично..."
    banker "Какие аппетитные девочки, какие попки."
    banker "Ммм..."
    banker "Будет еще лучше, если вы, крошки, снимете свои маски."
    banker "Так сказать, для более объективной и встесторонней оценки."
    # Молли снимает свою маску, а Моника не торопится и зло смотрит на Эшли
    mt "!!!"
    ashley "[monica_pub_name], чего ты ждешь?"
    ashley "Делай, как говорит Мистер Беркельбаух!"
    mt "!!!"
    menu:
        "Снять маску":
            $ monicaClareBankerPrivate6 = True # Моника сняла маску перед банкиром
            pass
        "Не делать этого! (увольнение из паба)":
            m "Я не собираюсь снимать маску!"
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            return
    mt "Этот неудачник уже видел меня без маски."
    # Моника снимает маску, банкир рассматривает ее и Молли
    banker "Так, хорошо..."
    banker "..."
    banker "Эшли..."
    ashley "Да, Мистер Беркельбаух?"
    banker "Ты помнишь условие нашей сегодняшней встречи?"
    ashley "Конечно, Мистер Беркельбаух."
    banker "И какое же это условие?"
    # Эшли нервничает
    ashley "Условие такое, что здесь будут присутствовать все девочки бара..."
    banker "Ты не выполнила это условие, Эшли..."
    banker "Я не вижу здесь третьей девочки."
    banker "Где она?"
    # Эшли начинет оправдываться
    ashley "Мистер Беркельбаух, дело в том, что..."
    ashley "В общем, с Клэр очень сложно договориться."
    ashley "Она не ходит на приватные танцы с клиентами и..."
    # банкир ее перебивет
    banker "Эшли, ты разговариваешь со мной с неправильной позиции..."
    ashley "Я? С неправильной чего?"
    banker "С неправильно позиции, Эшли."
    banker "Ты стоишь там, а должна стоять здесь." # указывает на стол рядом с девочками
    ashley "Но, Мистер Беркельбаух..."
    banker "Эшли, займи правильную позицию и объясни мне, почему нет третьей девочки."
    # Эшли лезет к Монике и Молли на стол и одновременно с этим продолжает оправдываться перед банкиром
    ashley "Я пыталась поговорить с Клэр, объяснить ей ситуцию..."
    ashley "Что у нас сегодня обязательное условие..."
    ashley "Но она все равно отказалась..."
    ashley "Бесполезно ее уговаривать, Мистер Беркельбаух..."
    # Эшли уже стоит на столе рядом с Молли и Моникой
    ashley "Я правда пыталась сделать это. Я вас не обманываю."
    banker "Эшли, ты знаешь, что будет с твоим заведением..."
    banker "Если ты не выполнишь нашу договоренность."
    ashley "Мистер Беркельбаух, я уверена, что мы с вами сможем договориться!"
    banker "Нет, Эшли. Я не готов подписывать документы для заведения..."
    banker "Которое не может предоставить мне полную прозрачность своей деятельности."
    banker "Почему ты до сих пор не сняла свои трусики, Эшли."
    banker "Я хочу увидеть и твою попку."
    # Эшли продолжает его уговаривать, стягивая трусики
    ashley "Но Мистер Беркельбаух, здесь итак уже полная прозрачность!"
    banker "Нет, Эшли."
    banker "Я должен оценить деятельность твоего заведения встесторонне."
    banker "А ты препятствуешь этому."
    banker "Боюсь, у нас с тобой не получится достигнуть договоренности..."
    ashley "Но Мистер Беркельбаух..."
    # Эшли прерывается на полуслове из-за звука открывающейся двери
    # испуганно оглядывается
    # в дверях стоит недовольная Клэр, в руках ее хлыст для извращенцев
    # Эшли радостно
    ashley "Клэр!"
    mt "Она пришла!"
    mt "Она сделала это!"
    mt "!!!"
    # Клэр подходит к банкиру, тыкает ему в грудь хлыстом
    clare "Этот извращенец захотел всех девочек Shiny Hole сразу?"
    # банкир смотрит на хлыст, похотливо улыбается и молчит
    banker "..."
    # Клэр хлыстом приподнимает его лицо за подбородок (как делала с Эдвардсом)
    clare "И этот мелкий банковский клерк смеет командовать здесь?"
    banker "..."
    # поворачивает лицо хлыстом сначала в одну сторону
    clare "Да... Деньги для такого как ты - единственный способ получить женское внимание."
    banker "..."
    # потом в другую сторону
    clare "Мне тебя даже жалко, клерк."
    clare "Поэтому, так уж и быть..."
    banker "..."
    # Клэр встает на стол к остальным, снимает трусики
    # смотрит на Монику
    clare "..."
    m "..."
    # снимает маску
    # Эшли стоит с голой попой вмесе с остальными, довольная, что Клэр пришла
    # банкир самодовольно смотрит на четыре голые попы перед ними
    # затемнение, смена кадра - банкир уже расстегнул штаны и достал свой стояк
    banker "Ну вот."
    banker "Совсем другое дело."
    banker "Теперь ничто не препятствует встесторонней и объективной оценке работы твоего заведения, Эшли."
    ashley "Да, Мистер Беркельбаух."
    ashley "Я же вам говорила, что готова предоставить все необходимое для этого."
    # начинает дрочить
    banker "Да..."
    banker "Все девочки Shiny Hole собрались для меня..."
    banker "А это значит, что ты мне предоставила полную прозрачность своей деятельности, Эшли."
    ashley "Да, Мистер Беркельбаух."
    banker "И наша с тобой договоренность в силе."
    banker "Ты выполнила свое условие, значит, я выполню свою часть договора."
    ashley "Я рада, Мистер Беркельбаух, что мы с вами смогли договориться."
    banker "Ммммм...."
    banker "Да, Эшли... Мммм..."
    banker "Ааааа..."
    banker "Какие попки..."
    banker "Даааа..."
    banker "Ааааа..."
    banker "ААААА!!!"
    # банкир кончает, глядя на попы
    banker "Я только что утвердил нашу договоренность, Эшли."
    ashley "Спасибо, Мистер Беркельбаух."
    ashley "Вы так добры ко мне."
    # банкир довольно улыбается
    # затемнение
    # смена кадра
    # все стоят одетые
    # банкир шлепает по попе Клэр
    banker "Отличная попка!"
    # она хлыстом хлопает его по руке, он похотливо на нее смотрит
    clare "!!!"
    # убирает руку, обращается к Эшли
    banker "Эшли, жду тебя завтра у себя в офисе."
    banker "Не опаздывай."
    banker "Время - деньги."
    # Моника смотрит ему вслед
    mt "Отвратительный мерзкий неудачник!"
    mt "Никчемный банкиришка!"
    mt "!!!"
    # уходит
    # девочки с Эшли в подсобке
    # Эшли встает руки в боки, включает начальницу
    ashley "Так!"
    ashley "Никто не должне ни слова говорить о произошедшем ни одной живой душе!"
    ashley "О моих договоренностях с этим банкиром никто не должен знать!"
    ashley "Особенно Джо!!"
    ashley "Всем ясно?!"
    # Молли говорит
    molly "Да, Эшли. Без проблем."
    molly "На сегодня все?"
    ashley "Да. Все свободны."
    # Молли с Клэр уходят
    mt "Надо спросить у этой чертовой Эшли про плакат."
    m "Эшли, я выполнила твое условие."
    m "Ты обещала, что не будешь вешать плакат у барной стойки."
    ashley "Да, [monica_pub_name], я помню."
    ashley "Может, ты передумаешь?"
    ashley "Это хорошая реклама дя твоей попки."
    ashley "Сможешь зарабатывать намного больше чаевых." # подмигивает
    m "Я не хочу, чтобы этот плакат висел в баре!!!"
    m "!!!"
    ashley "Ну ладно, ладно..."
    ashley "Но если вдруг передумаешь..."
    m "Нет!"
    m "!!!"
    ashley "Хорошо, хорошо."
    ashley "Все, иди!"
    ashley "Ты на сегодня свободна!"
    mt "Ненавижу ее и этот гребаный бар!"
    mt "!!!"
    return

# если Моника отказалась от каких-либо действий на привате, то будет увольнение с паба
# лейблы при этом фитятся те же, которые используются и при отказе вообще идти в приват
# ep213_dialogues3_pub_14a (клик на кого-л. в баре) и ep213_dialogues3_pub_14b (на улице, а также попытка зайти в бар)


# гримерка после привата с банкиром
label ep214_dialogues1_pub_15:
    # Клэр с Моникой вдвоем
    # Клэр поворачивается в сторону Моники
    mt "Клэр пришла на приват."
    mt "Пошла вразрез со своими принципами..."
    mt "Потому что я ее попросила."
    mt "..."
    m "Клэр, я хотела сказать тебе спасибо..."
    clare "Моника, без проблем. Всегда рада помочь тебе."
    clare "Знаешь что?"
    clare "Сказать, что удивлена этим приватом - это ничего не сказать."
    clare "Это нормально, что Эшли показывает свой голый зад какому-то банковскому клерку?"
    # Моника улыбается
    m "И это уже не в первый раз."
    clare "О, серьезно?!"
    m "Да!"
    clare "Теперь кредитные договора именно так заключаются?"
    m "Видимо, да. Вряд ли у Джо получилось бы договориться с этим мерзким банкиром!"
    clare "Аха-ха!"
    m "Аха-ха!"
    $ log1 = _("Клэр ко мне хорошо относится и готова мне помочь при необходимости. Она говорит, что ей без разницы, настоящая ли я Моника Бакфетт или нет.") # квест-лог
    return

# гримерка после привата, Моника одна в гримерке
label ep214_dialogues1_pub_16:
    # не рендерить!!
    mt "Это был отвратительный приват!"
    mt "Мне пришлось стоять голой, да еще и без маски!"
    mt "И все для какого-то жалкого неудачника!"
    mt "Ненавижу его и эту чертову извращенку Эшли!!!"
    mt "!!!"
    return
