#Фред активируется на следующий день после того как Моника была на работе

label monica_fred_about_dick_dialogue1:
    #Фред зовет Монику на разговор. Уйти никуда нельзя. Только если одето Whore.
    fred "Моника!"
    "Можно Вас на минутку?"
    return

label monica_fred_about_dick_dialogue2:
    #Моника подошла ко Фреду (день и если одета одежда whore)
    #render
    $ store_music()
    music Groove2_85
    img 6163
    with fade
    m "Что тебе надо, Фред?!" #зло
    img 6164
    fred "Миссис Бакфетт! Мне сообщили что {b}Мистер Дик просил Вас зайти к нему{/b}!"
    img 6165
    m "Он что, звонил тебе?!"
    img 6166
    fred "Нет, Миссис Бакфетт! Со мной связалась его секретарь..."
    img 6167
    m "А почему она позвонила тебе???"
    img 6168
    fred "Я не знаю, Миссис Бакфетт! Наверное у нее не было другого способа связаться с Вами!"
    "Ведь у Вас нет телефона, правда?!"
    img 6169
    "Или есть?!"
    img 6170
    m "Пока нет, но это ненадолго, поверь!"
    img 6171
    fred "Миссис Бакфетт! Если Вам потребуется помощь, только скажите!"
    "Я к Вашим услугам!"
    img 6172
    m "Спасибо! ТВОЕЙ помощи мне уж точно не надо!"
    "Я скоро вновь верну этот дом и ты получишь по заслугам!"
    img 6173
    with fade
    mt "Дик просил меня зайти... Что-ж, может и пришло время попытаться еще раз..."
    $ restore_music()
    return

label monica_dick_office_dialogue1:
    #Моника подошла к офису Дика до того как ее вызвали через Фреда
    mt "Я обязательно зайду и поговорю с Диком, но чуть позже..."
    return

label monica_dick_office_dialogue1a:
    if get_active_objects("DickTheLawyer", scene="dick_office_cabinet") != False:
        return True
    # Моника заходит в office_dick_entrance, когда Дика нет
    sound highheels_short_walk
    img 3045
    w
    img 3046
    reception_secretary "Мэм, вы куда?"
    img 3047
    m "Я к Дику Адвокату!"
    img 3056
    reception_secretary "Мэм, его сегодня нет..."
    if day_time == "day":
        #
        reception_secretary "Он куда-то уехал с самого утра."
    else:
        #
        reception_secretary "Он и Мисс Виктория куда-то уехали."

    $ autorun_to_object("monica_dick_office_dialogue1b")
    call refresh_scene_fade()
    return False

label monica_dick_office_dialogue1b:
    mt "Вот черт! Дика нет!"
    "Надо зайти в другой день..."
    return
label monica_dick_secretary_dialogue1:
    #Моника заходит в офис к Дику, общается с секретаршей (даже если идет мимо нее, диалог срабатывает)
    #render
    $ store_music()
    music Groove2_85

    img 6174
    with fade
    w
    img 6175
    with Dissolve(0.5)
    w
    img 6176
    w
    img 6177
    w
    img 6178
    w
    img 6179
    #звук хи-хи
    sound snd_woman_laugh
    pause(3)
    sound snd_woman_laugh2
    w
    img 6180
    with Dissolve(0.5)
    dick_secretary "Миссис Бакфетт!"
    "Вы также прекрасны как и в прошлый раз!"
    "Время на Вас совсем не влияет!"
    img 6181
    m "!!!"
    img 6182
    dick_secretary "Это комплимент..." #с ехидной улыбкой
    "Я просто хочу подружиться с Вами..."
    $ restore_music()
    return

label monica_dick_secretary_dialogue1a:

    img 6183
    with fade
    m "Мне не нужны такие друзья!"
    dick_secretary "..." #ехидно улыбается
    return


label monica_dick_dialogue1a:
    show screen sprites_hover_dummy_screen()
    pause 1
    hide screen sprites_hover_dummy_screen
    img 6184
    with fade
    mt "Вот и тюфяк... Надеюсь в этот раз получится лучше..."
    call refresh_scene_fade()
    return
label monica_dick_dialogue1:
    #Моника говорит с Диком в кабинете
    #render
    $ store_music()
    music Hidden_Agenda
    img 6185
    with fade
    m "Дик! Привет!"
    "Я рада что ты обо мне вспомнил!"
    img 6186
    "Ты позвал меня чтобы сказать что передумал?"
    img 6187
    w
    sound highheels_short_walk
    img 6188
    with fade
    "Ты поможешь мне?"
    img 6189
    with Dissolve(0.5)
    "Милый..." #кокетливо смотрит
    img 6190
    w
    img 6191
    w
    img 6192
    music Master_Disorder
    w
    img 6193
#    music Pyro_Flow
    w
    img 6194
    dick "Моника, я позвал тебя чтобы напомнить о себе..."
    img 6195
    w
    music Hidden_Agenda
    img 6196
    with Dissolve(0.5)
    m "Дорогой!"
    sound snd_heavy_papers_drop
    #звук падения бумаги
    img 6197
    with fade
    w
    img 6198
    with Dissolve(0.5)
    w
    img 6199
    with Dissolve(0.5)
    m "Дорогой!"
    img 6200
    with fade
    "Я помню о тебе все время и я..."
    music stop
    sound plastinka2
    pause(0.5)
    music Master_Disorder
    img 6201
    dick "Моника, ты решила разбить его?!"
    "Разбить мое сердце?!"
    img 6200
    m "..."
    img 6201
    dick "???"

    img 6202
    with Dissolve(0.5)
    music Hidden_Agenda
    m "Нет, дорогой! Что ты!!!"
    img 6203
    with Dissolve(0.5)
    w
    img 6204
    with Dissolve(0.5)
    w
    img 6205
    with Dissolve(0.5)
    "Твое сердце - это самое важное что есть для меня..."
    img 6206
    with Dissolve(0.5)
    w
    music stop
    sound plastinka2
    pause(0.5)
    music Master_Disorder
    img 6207
    with fade
    dick "Тогда где та мелочь, о которой я попросил тебя?"
    img 6208
    w
    m "here"
    label .local1:
        menu:
            "Приставать к Дику. (low corruption, required [monicaTryToDickBlowjobRequiredCorruption]) (disabled)" if corruption < monicaTryToDickBlowjobRequiredCorruption:
                call low_corruption(monicaTryToDickBlowjobRequiredCorruption)
                jump local1
            "Приставать к Дику. (corruption)" if corruption >= monicaTryToDickBlowjobRequiredCorruption:
                #corruption check!!!
                $ monicaTryToDickBlowjob = True
                music Loved_up
                img 6213
                with Dissolve(0.5)
                m "Дик..."
                img 6214
                with Dissolve(0.5)
                w
                img 6215
                with Dissolve(0.5)
                w
                img 6216
                with Dissolve(0.5)
                "Дик... Милый..."
                img 6217
                with fade
                w
                img 6218
                with Dissolve(0.5)
                w
                img 6219
                with Dissolve(0.5)
                "Дик..."
                img 6220
                with Dissolve(0.5)
                "Я пока не нашла деньги на..."
                img 6221
                with Dissolve(0.5)
                "Я пока не нашла деньги на твой галстук..."
                img 6222
                with Dissolve(0.5)
                "Но ведь тебе нужен не галстук, милый?"
                img 6223
                with Dissolve(0.5)
                w
                img 6224
                with Dissolve(0.5)
                "Дик! Иди ко мне!"
                img 6225
                with Dissolve(0.5)
                w

                music Power_Bots_Loop
                img 6226
                with fade
                dick "Моника, я знаю что ты лжешь."
                "Для тебя не составит труда найти эти деньги."
                img 6227
                "Ты просто не хочешь уделить мне знак внимания."

                "..."
                img 6228
                "В общем Моника. Я позвал тебя чтобы сообщить..."
                "Я не хочу больше заниматься твоим делом."
                img 6229
                w

            "Я пока не нашла деньги...":
                music Gloove2_85
                img 6209
                with fade
                m "Дик... Я...."
                "Я пока не нашла деньги на..."

                img 6210
                dick "Моника, я знаю что ты лжешь."
                "Для тебя не составит труда найти эти деньги."
                "Ты просто не хочешь уделить мне знак внимания."

                img 6211
                "..."
                music Power_Bots_Loop
                img 6212
                "В общем Моника. Я позвал тебя чтобы сообщить..."
                "Я не хочу больше заниматься твоим делом."

    img 6230
    with fade
    m "КАК?!?!"

    dick "У тебя есть другие друзья. Тот же Маркус."
    "Общайся с ними. А у меня есть свои друзья, которые думают обо мне!"
    img 6231
    "В отличии от тебя, Моника..."

    img 6232
    m "ДИК?!"
    "МАРКУС МНЕ НЕ ДРУГ!!!"
    "ОН..."

    img 6233
    dick "Моника, мне не важно кто он!"
    "Это твои связи и твои проблемы."
    "Причем тут я?!"

    img 6234
    with fade
    mt "О БОЖЕ!!! КАК ЖЕ ТАК!?!?"
    "Я НЕ ОЖИДАЛА ТАКОГО ПОВОРОТА!!!"
    "МНЕ НАДО КАК-ТО ПЕРЕУБЕДИТЬ ЕГО!!!"
    "ИНАЧЕ КОНЕЦ!!!"

    music Hidden_Agenda
    img 6235
    with fade
    m "ДИК! ПОЖАЛУЙСТА!"
    "Я могу тоже быть твоим другом!"
    "ДИК!"
    "МИЛЫЙ!"

    img 6236
    dick "У меня уже есть друг..."

    img 6237
    m "Я... могу дружить и с твоим другом тоже..."
    "Дик!"
    "Я могу быть вместе с Вами!"

    img 6238
    dick "Ты хочешь сказать что можешь поладить с Викторией?"

    img 6239
    m "Я?? С ней??"
    img 6240
    with fade
    "Конечно, Дик!"
    "Конечно! Я с радостью полажу с ней!"

    img 6241
    dick "Хм..."
    "Моника... Я не знаю..."
    "Я сомневаюсь..."

    img 6242
    m "Дорогой! Пожалуйста, не сомневайся во мне!"
    "Пожалуйста, дай мне шанс! Я не разочарую тебя!"

    img 6243
    dick "Твое дело занимает слишком много сил, а ты..."

    img 6244
    m "Цвет?"

    img 6245
    dick "Что, Моника?"

    m "Какой цвет галстука ты хочешь, милый?"

    img 6246
    dick "Хм... Я не думал..."
    "Такой чтобы понравился Виктории..."
    img 6247
    "Моника! А почему бы Вам вместе с ней не купить мне галстук?"
    "Вы хотите подружиться! Это будет прекрасный повод!"

    img 6248
    m "Да, дорогой..."
    "Я буду очень рада..."
    "Только пожалуйста, не бросай мое дело, Дик..."
    dick "Хм... Возможно Виктория еще не успела отослать факс об отмене дела..."

    music Power_Bots_Loop
    img 6249
    dick "В общем Моника, я жду того что Вы {b}подружитесь с Викторией до конца недели{/b}."
    dick "Я даю тебе шанс, Моника."
    if week_day != 5:
        "{b}В пятницу вечером галстук должен быть на мне!{/b}"
    else:
        "{b}В следующую пятницу вечером галстук должен быть на мне!{/b}"
    img 6250
    m "Да, дорогой! Я тебя не подведу!"
    img 6251
    dick "До свидания, Моника!"
    m "До свидания, Дик!"

    $ restore_music()
    return

label monica_dick_secretary_dialogue2a:
    #Моника пытается выйти из локации до того как поговороила с секретаршей Дика
    mt "Я думаю мне надо проконтролировать эту сучку, вдруг она отправила факс?"
    return False
label monica_dick_secretary_dialogue2:
    #render
    #Моника говорит с секретаршей Дика после разговора с Диком
    img 6252
    with fade
    m "Виктория..."
    img 6253
    with Dissolve(0.5)
    dick_secretary "Мисс Виктория..."
    img 6254
    m "Мисс Виктория... Скажите..."
    "Вы ведь не отправили факс, о котором говорил мистер Дик?"
    img 6255
    dick_secretary "Я отправила все факсы, которые он мне поручал!"
    "Я хорошо делаю свою работу, Миссис Бакфетт!"
    music Power_Bots_Loop
    img 6256
    m "О НЕТ!"
    img 6257
    with Dissolve(0.5)
    dick_secretary "Мистер Дик сообщил о том что один факс посылать не надо."
    "Этот факс касается Вашего дела, Миссис Бакфетт!"
    music Hidden_Agenda
    img 6258
    m "ДА! О ДА!"
    "Нет, его не надо посылать..."
    img 6259
    dick_secretary "Я не буду его далеко убирать."
    img 6260
    "Мистер Дик сказал чтобы {b}я послала его в субботу утром, если Вы себя будете плохо вести{/b}."
    img 6261
    m "..."
    img 6262
    dick_secretary "Есть еще какие-то вопросы, Миссис Бакфетт?"
    img 6263
    m "Мисс Виктория... Я..."
    "Я бы хотела подружиться с Вами..."
    "И я бы хотела попросить Вас составить компанию мне..."
    "Чтобы купить галстук для Мистера Дика..."
    img 6264
    mt "Дьявол! Не могу поверить что я говорю это!!!"
    if monicaBitch == True:
        "Говорю этой сучке!"
    img 6265
    dick_secretary "Вы бы хотели?"
    "Хи-хи!"
    "Да, Вам стоило бы купить галстук вместе со мной!"
    "Иначе, я очень боюсь, что его цвет может не понравиться любимой девушке Мистера Дика!"
    img 6266
    mt "СССУЧКА!!!"
    img 6267
    dick_secretary "Но у меня нет времени на походы по магазинам."
    img 6268
    "Знаете, мне надо хорошо выглядеть, а это занимает много времени..."
    img 6269
    "Вы плохо умеете уговаривать, Миссис Бакфетт!"
    "У Вас мало практики в этом! Вам надо больше практиковаться!"


    music Power_Bots_Loop
    img 6270
    with fade
    mt "Она издевается! Эта сучка издевается!"
    "Я уже заранее знаю что ей не понравится цвет!"
    "И если она не пойдет со мной, то Дик обвинит меня в том что мы не поладили!"
    "Этот тюфяк полностью у нее под каблуком!"

    menu:
        "Попросить Викторию вежливо...":
            pass

    music Hidden_Agenda
    img 6271
    with fade
    m "Мисс Виктория... Пожалуйста, составьте мне компанию..."
    img 6272
    dick_secretary "Нет, не думаю..."

    menu:
        "Попросить Викторию еще вежливее...":
            pass
    img 6273
    m "Мисс Виктория... Пожалуйста, я очень прошу Вас составить мне компанию..."
    with fade

    img 6274
    dick_secretary "Ну кто так уговаривает?"
    "Скажите что я одеваюсь лучше чем Вы и что у меня лучше вкус, на который Вы бы хотели положиться..."
    music Power_Bots_Loop
    img 6275
    with fade
    mt "СУЧКА!!!"
    "ОНА ИЗДЕВАЕТСЯ НАДО МНОЙ!!!"
    "Я НЕНАВИЖУ ЕЕ!!!"

    menu:
        "Сделать Виктории комплимент...":
            pass

    music Loved_up
    img 6276
    with fadelong
    m "..."
    img 6277
    dick_secretary "..." #хитро улыбается
    img 6278
    m "Мисс Виктория..."
    img 6279
    dick_secretary "..."
    img 6280
    m "..."
    img 6281
    dick_secretary "..."
    img 6282
    with fade
    m "Мисс Виктория..."
    img 6283
    "Вы очень хорошо одеваетесь, гораздо лучше чем Я..."
    img 6284
    sound snd_woman_laugh2
    dick_secretary "Хи-хи!"
    img 6285
    m "..."
    img 6286
    m "Я вижу что у Вас очень хороший вкус и я бы очень попросила Вас составить компанию мне..."
    "В покупке галстука для Мистера Дика."
    "Я боюсь что мне может не хватить вкуса и я бы хотела положиться на Ваш вкус и опыт в этом деле..."
    img 6287
    dick_secretary "Ну вот! Другое дело!"
    sound snd_woman_laugh2
    "Хи-хи!"
    music Groove2_85
    img 6288
    if week_day != 5:
        dick_secretary "Хорошо, {b}в пятницу вечером приходите сюда{/b}."
    else:
        dick_secretary "Хорошо, {b}в следующую пятницу вечером приходите сюда{/b}."
    "Я знаю хороший галстук за {b}$ 5.000{/b}."
    "Так что {b}приготовьте деньги{/b}."
    "{b}Если у Вас не будет нужной суммы, то, пожалуйста, не беспокойте меня{/b}."

    img 6289
    with fade
    m "Да, я поняла."
    "Мисс Виктория, я могу идти?"
    img 6290
    dick_secretary "Вы можете идти, Миссис Бакфетт."
    "До пятницы, до свидания."
    img 6291
    m "До свидания, Миссис Виктория..."

    if monicaBitch == True:
        $ notif_monica()
        mt "Сучка!"

    return

label monica_dick_secretary_dialogue3:
    #render
    #Моника подходит к секретарше повторно
    img 6293
    with fade
    m "Виктория..."
    img 6294
    dick_secretary "Мисс Виктория!"
    img 6295
    with fade
    m "Мисс Виктория..."
    img 6294
    dick_secretary "Вы что-то хотели?"
    img 6296
    m "Тот факс... Он все еще у Вас?"
    img 6297
    dick_secretary "Да, я его отправлю в субботу утром."
    if week_day != 5:
        "Либо не отправлю, если мы проведем хорошо время в {b}пятницу{/b}."
    else:
        "Либо не отправлю, если мы проведем хорошо время в следующую {b}пятницу{/b}."
    "Хи-хи!"
    m "Да, Мисс Виктория, конечно..."
    "До свидания..."
    mt "Эта сучка заплатит за все!"
    return

label monica_dick_secretary_dialogue4a:
    if act == "l":
        return
    if dickDoorBlockedDay == day:
        mt "(хмык)"
    else:
        call monica_dick_secretary_dialogue4()
    return False

label monica_dick_secretary_dialogue4:
    # Моника пытается зайти к Дику в кабинет, когда Дика нет
    dick_secretary "Миссис Бакфетт!"
    "Мистера Дика сейчас нет."
    "И Вам не следует отвлекать его."
    "Для этого есть секретарь."
    return

label monica_dick_office_refuse_dialogue1:
    if act=="l":
        return
    mt "Без денег мне там нечего делать."
    return False

label monica_dick_office_dialogue2:
    #Моника выходит из офиса Дика после разговора о галстуке
    mt "ЧЕРТ!"
    "Я еле уломала Дика!"
    "Я была на волоске от гибели или чего еще похуже!"
    "Эта Виктория!"
    "Она полностью овладела Диком!"
    "Мне надо будет что-то придумать с этим!"
    "Это ее идея с галстуком, я уверена!"
    "И мне не получилось выкрутиться и не покупать этот галстук!"
    "Я больше не допущу такого, но сейчас мне {b}надо найти где-то $ 5.000{/b}!"
    "Иначе конец! Я видела это по Дику!"
    "Он не блефовал!"
    "Моя судьба сейчас действительно зависит от этих денег!"
    "..."
    "Но где мне найти такую сумму?!"

    if monicaKnowAboutKebabWork == True:
        $ notif(_("Монике пришлось зарабатывать на еду разноской флаеров"))
        #если Моника разносила флаеры
        "Мне понадобится разносить флаеры несколько лет, чтобы заработать такие деньги!"
        "Это не вариант!"
        #

    "Я - Моника Бакфетт!"
    "Для того чтобы заработать эту сумму мне надо лишь пошевелить пальцем!"
    "Так было всегда!"
    "..."
    "Но что сейчас?"

    "Может быть попробовать снова поговорить с этим {b}ублюдком в моем офисе{/b}?"
    "Из нашего разговора мне показалось что у него есть какое-то предложение ко мне!"
    "Стоит попробовать!"
    "Я чувствую что могу об этом пожалеть, но у меня нет выбора..."

    return
