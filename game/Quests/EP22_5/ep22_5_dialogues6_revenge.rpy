label ep22_5_dialogues_revenge_quest1:
    # трущобы. моника стоит и смотрит на мамочку, проститутку и на бывшую модель
    img 60201
    w
    img 60202
    mt "Итак... Вот это место..."
    mt "Я уверена, что что-то случилось здесь в тот день..."
    mt "Что это место скрывает от меня?"

    # проститутка показывает на Монику
    img 60203
    w
    img 60204
    whore_number_1 "Эй! Это моя одежда!"
    whore_number_1 "Это она украла ее! Воровка!"

    # Моника оказывается ближе, разговаривает с ними
    img 60205
    m "Что? Одежда?!"
    m "Это не одежда, а неприличные тряпки, которые стыдно носить такой леди как Я!"
    img 60206
    whore_number_1 "Ах ты!.."
    # ее перебивает мамочка (общается таинственно)
    img 60207
    mommy "Здравствуй, девочка..."
    mommy "Вот мы и снова встретились..."
    mommy "Как я вижу, жизнь преподнесла тебе явление своей... Непредсказуемости..."
    img 60208
    w
    img 60209
    # Моника смотрит на шлюху, затем на мамочку
    m "Я... Да, я..."
    m "Я пришла, чтобы поговорить с вами..."
    m "Мне нужна... Нужна кое-какая помощь..."
    mommy "Чем же старая женщина может помочь такой леди, как ты..."
    img 60210
    m "Мне... Мне нужна информация..."
    img 60211
    mommy "Мы здесь не продаем информацию, девочка..."
    img 60212
    mommy "Мы здесь продаем кое-что другое..."
    mommy "Ты ведь пришла просить о месте среди нас?"
    img 60213
    m "Я... Нет!"
    m "Как вы могли подумать?!"
    img 60214
    ## если Моника грубила серой мыши
    m "Это место для таких падших ничтожеств, как эта горе-модель!"
    img 60215
    # модель смотрит на нее обреченно
    m "Я - лицо самого популярного журнала моды!"
    m "Как вы смеете задавать мне такие вопросы?!"
    img 60214
    ## если Моника пожалела серую мышь
    m "Я понимаю, что неудачная карьера, например, этой модели..."
    m "Может привести на самое дно, в котором она оказалась..."
    m "Но, в моем понимании, нужно пытаться снова и снова, нежели просто сдаться!"
    m "Мне жаль эту девушку, но я не такая, как она!"
    m "Я - лицо самого популярного журнала моды!"
    img 60216
    # Мамочка оглядывает ее одежду
    mommy "Ты можешь цепляться за свою привычную жизнь..."
    mommy "Но все же ты оказалась здесь..."
    img 60217
    m "Я пришла задать вопрос!"
    img 60218
    mommy "Девочка, это не место для вопросов..."
    mommy "Здесь находятся те, кто уже получил все ответы и смирился..."
    img 60219
    m "Я не смирюсь!"
    m "Всего один вопрос!"
    img 60220
    mommy "..."
    img 60221
    m "Скажите, кто был рядом, когда я проходила здесь в тот день?!"
    mommy "В какой день, девочка?"
    m "В тот день, когда я проходила мимо в другой... Одежде."
    img 60222
    ## если обидела серую мышь
    m "Когда я заметила эту падшую модель и сделала комментарий об этом!"
    img 60222
    ## если не обижала
    m "Когда я пожалела эту модель, которая провалила все кастинги."
    img 60223
    m "Кто?! Кто видел это?!"
    m "Кто следил за мной?!"
    m "Вы должны были видеть это!"
    img 60224
    whore_number_1 "Пусть сначала вернет мои вещи!"
    img 60225
    w
    img 60226
    mommy "Девочка, прежде чем задавать вопросы, ты должна закрыть свои долги перед нами..."
    m "Какие еще долги?! Я ничего не должна вам!"
    # таинственно
    mommy "Твоя одежда, девочка..."
    mommy "Верни ее той, у кого взяла..."
    img 60227
    m "Но я... У меня нет другой одежды, черт возьми!"
    mommy "У нас нет для тебя ответов, девочка..."

    menu:
        "Достать пистолет.": # bitchiness
            # Моника достает пистолет
            img 60228
            m "Я попросила добрым словом... Дать ответ..."
            img 60229
            w
            img 60233
            m "Но, видимо, добрым словом и пистолетом я смогу добиться большего!"
            img 60232
            w
            img 60234
            mommy "У нас нет для тебя ответов, девочка..."

            menu:
                "Наставить пистолет на мамочку.":
                    img 60230
                    m "Ты дашь мне ответ, старая карга!"
                    m "Кто следил за мной?!"
                    img 60231
                    m "Говори, иначе выбью тебе все твои старые мозги!"
                    mommy "Я уже видела достаточно, чтобы завершить свой путь..."
                    img 60235
                    # Моника направляет пистолет на шлюху_1
                    m "Тогда я вышибу мозги ей!"
                    mommy "Хорошо... Я спасу тебя от ошибки..."
                    mommy "Никто не следил за тобой в тот день, девочка..."
                    img 60236
                    m "ЧТО?! ТЫ ВРЕШЬ!"
                    m "Кто-то следил за мной!"
                    mommy "Нет, девочка..."
                    mommy "Ты шла одна... По пустой дороге..."
                    mommy "И за тобой была только тень..."
                    mommy "Твоя тень, девочка..."
                    img 60237
                    w
                    img 60238
                    m "Черт возьми!"
                    m "Гребаные шлюхи!"
                    m "Что я здесь делаю?!"
                    m "Я сошла с ума, если пытаюсь найти ответы здесь!"
                    m "В этих трущобах одни идиоты!"

                "Наставить пистолет на себя.": # правильный выбор
                    img 60239
                    m "Я прошла... Очень многое..."
                    m "За последнее время..."
                    m "Той, кого ты называешь девочка, уже давно нет..."
                    m "Я прошла через все круги ада и решила для себя, что хватит..."
                    m "Ты хочешь, чтобы я разделась и снова осталась голой посреди улицы, как в тот раз..."
                    img 60240
                    # направляет пистолет на себя
                    m "Но я сделала выбор."
                    m "Я больше никогда не сдамся, никому!"
                    m "Я скорее убью себя, чем пойду на это!"
                    m "Если для меня и здесь нет ответов, тогда их нет нигде..."
                    m "Да, я была неправа... Очень часто была неправа..."
                    m "Но, если кто-то хочет снова поставить меня на колени, я не дамся!"
                    img 60241
                    # Моника закрывает глаза, собираясь застрелиться
                    m "Никто не увидит Монику Бакфетт, поднявшую руки! Никто..."
                    mommy "Никого не было, девочка..."
                    img 60242
                    # Моника открывает глаза
                    m "Что?"
                    img 60243
                    mommy "Никого не было за тобой..."
                    mommy "Никто за тобой не следил в тот день..."
                    m "Не может быть!"
                    m "Ты врешь!"
                    mommy "Девочка, я никогда не вру..."
                    mommy "Я не хочу, чтобы ты допустила ошибку и повторила мой путь..."
                    mommy "Иди с миром, оставь эту одежду себе..."
                    mommy "Твои ответы не здесь..."
                    img 60238
                    m "Что?!"
                    m "Но как же..."
                    m "Черт возьми!!!"

        "Достать пистолет. (Моника слишком приличная)": # bitchiness
            pass

        "Отказаться отдавать одежду.":
            menu:
                "Поставить условие.":
                    img 60244
                    m "Хорошо..."
                    m "Я отдам эту одежду, я..."
                    m "Я проходила кое-что и похуже этого..."
                    m "Но у меня есть условие..."
                    mommy "Ты торгуешься, девочка?"
                    m "Я не торгуюсь! Это мое условие!"
                    img 60245
                    whore_number_1 "Какое еще условие?! Отдавай мою одежду!"
                    img 60247
                    m "Иди к черту!"
                    img 60246
                    m "Условие, что ты назовешь того, кто следил за мной!"
                    mommy "Это невозможное условие, девочка..."
                    m "Почему это?!"
                    mommy "За тобой никто не следил в тот день..."
                    img 60248
                    m "ЧТО?! ТЫ ВРЕШЬ!"
                    m "Кто-то следил за мной!"
                    mommy "Нет, девочка..."
                    mommy "Ты шла одна... По пустой дороге..."
                    mommy "И за тобой была только тень..."
                    mommy "Твоя тень, девочка..."
                    img 60249
                    m "Я так и знала, что это бесполезно!"
                    whore_number_1 "Эй! Она ответила!"
                    whore_number_1 "Отдавай одежду!"
                    m "Нет!"
                    m "Вы не выполнили условие, да и не могли!"
                    m "Мне больше нечего делать здесь!"

                "Заплакать.": # правильный ответ
                    img 60250
                    m "Одежда... Снова отдать одежду..."
                    m "Когда я пришла сюда в прошлый раз..."
                    m "Я не предполагала, что когда-либо услышу подобные слова..."
                    m "Знаешь, кто в прошлый раз сказал мне их?"
                    m "Надзиратель! В тюрьме!"
                    m "Который сорвал с меня все!"
                    img 60251
                    # моника закрывает лицо руками
                    m "Мою одежду, мою гордость!.."
                    m "Все растоптали и смешали с грязью!"
                    m "У меня не осталось ничего!"
                    img 60252
                    # моника убирает руки
                    m "Ничего! Ты слышишь?!"
                    m "Ничего, кроме этой жалкой одежды!"
                    m "Но, не смотря на это, снова появился человек..."
                    m "Человек, который говорит мне, сними это!.. Отдай!"
                    m "И тебе не важно, что у меня ничего нет!"
                    img 60255
                    m "Хочешь, я сниму это?.."
                    m "Сниму, только ответь на мой вопрос, кто следил за мной?!"
                    m "Я хочу, хочу найти ответы!"
                    m "Пусть даже у меня не будет ничего, совсем ничего..."
                    m "Но у меня остаюсь Я!"
                    img 60253
                    # снова закрывает руками лицо
                    m "Я есть! Я жива!"
                    m "И саму себя никто не сможет у меня отнять!"
                    img 60254
                    mommy "Девочка... За тобой никто не следил в тот день..."
                    # убирает руки
                    img 60256
                    m "Что?"
                    mommy "Девочка, я точно не хочу быть той, кто заберет последнее у кого-либо..."
                    mommy "Я была на твоем месте и понимаю тебя..."
                    img 60257
                    m "Меня... Меня никто не сможет понять! Никто!"
                    mommy "Иди с миром, девочка..."
                    mommy "Я ответила тебе, ты была одна..."
                    mommy "Никто не следил за тобой..."
                    img 60258
                    m "Я найду, я найду ответы!"
                    m "Пусть не здесь, но где-нибудь!"
                    m "Я... Я знаю!"

        "Отказаться отдавать одежду. (Моника недостаточно приличная)":
            pass




    # Моника оказывается перед полицией
    # вид со спины, стоит перед входом поодаль (рядом будут плохие текстуры)
    img 60259
    mt "Я знаю, кто даст мне ответы на все вопросы..."
    mt "Зачем я хожу вокруг, когда могу спросить напрямую..."
    # вид на то что держит пистолет
    img 60260
    mt "Итак..."
    mt "Здесь сидит человек, один человек..."
    mt "Который знает все ответы..."
    mt "И я задам ему их..."
    img 60261
    # входит в участок, подходит к полицейской на входе
    m "Здравствуйте, я бы хотела пройти к Мистеру Маркусу..."
    policewoman "Мистер Маркус большой начальник и занятой человек!"
    policewoman "У вас есть к нему запись?"
    # Моника направляет пистолет
    img 60262
    m "Да, Мэм."
    m "Я записана к нему."

    # следующий кадр, Моника стоит в кабинете Маркуса.
    # рядом с ней полицейская, по краям полицейские держат ее на мушке.
    # также сбоку детектив
    # Маркус сидит на кресле, как обычно улыбаясь
    img 60311
    m "Мистер Маркус, позвольте Вас побеспокоить..."
    img 60312
    marcus "О, Миссис Бакфетт, какой сюрприз..."
    marcus "Я ждал вас..."
    img 60313
    m "Я тоже ждала... Долго..."
    img 60314
    marcus "Чего же вы ждали, Миссис Бакфетт?"
    marcus "И что привело Вас сюда сегодня?"
    img 60315
    m "Ответы! Мне нужны ответы, Маркус!"
    m "Кто стоит за всем этим?!"
    m "Как все это могло случиться со мной?!"
    img 60316
    w
    img 60318
    w
    img 60317
    marcus "Миссис Бакфетт, вы знаете все, что полагается знать девушке в вашем положении."
    img 60319
    m "Я хочу знать больше!"
    img 60320
    m "И у меня пистолет!"
    img 60321
    marcus "У вас пистолет?"
    marcus "Как интересно..."
    img 60322
    m "Не валяй дурака, Маркус!"
    m "Твоя жизнь висит на волоске!"
    img 60323
    marcus "Моя жизнь..."
    marcus "Миссис Бакфетт... Простите..."
    marcus "Но не вы распоряжаетесь ею..."
    img 60324
    m "!!!"
    img 60325
    marcus "Спасибо за то, что облегчили мне работу."
    marcus "Пожалуйста, пройдите в кабинет для допросов."
    marcus "Перед вашей отправкой на объект, я бы хотел провести с вами последнюю беседу."
    img 60329
    m "Я застрелю тебя, мерзавец!"
    img 60327
    marcus "Господа, проводите даму..."
    img 60328
    detective "Взять ее!"
    # к Монике начинают приближаться со всех сторон
    # напряженный момент, Моника направляет пистолет, решимость
    img 60330
    w
    img 60331
    w
    img 60332
    w
    img 60333
    w
    img 60326
    menu:
        "Выстрелить в Маркуса.":
            img 60341
            # щелчок, осечка
            m "Что?! Осечка?!"
            m "НЕТ!"
        "Опустить пистолет.":
            img 60334
            m "Я... Я не могу сделать это..."
            m "Черт!"

    img 60335
    marcus "Миссис Бакфетт, спасибо..."

    ## если отвечала мамочке неправильно
    # повтор сцены на ферме, где клеймят

    ## если сделала правильные выборы с мамочкой
    # звук двери
    # появляется мамочка mommmy
    img 60336
    w
    # все расступаются, удивленно
    img 60337
    detective "Что? Кто это?!"
    img 60338
    mommy "Маркус..."
    mommy "Сыночек..."
    img 60339
    # все стоят в оцепенении
    w
    img 60340
    mommy "Я прошу тебя..."
    mommy "Помоги этой девочке..."

    # затемнение

    # кабинет допросов. Моника сидит в одежде на стуле, Маркус за столом
    # перед Моникой лежит пистолет на столе
    img 60263
    m "И? Маркус..."
    m "Как все это понимать?"

    # Маркус напряжен, внутренняя борьба
    img 60264
    marcus "Миссис Бакфетт..."
    marcus "Видимо я действительно не зря сделал исключение для вас..."
    marcus "Когда пошел против воли остальных членов нашего общества и позволил вам выйти на свободу..."
    img 60265
    m "Это Дик! Дик добился свободы для меня!"
    marcus "Не совсем..."
    marcus "Это Я позволил сработать его плану, но мог бы этого и не делать..."
    marcus "Однако, что-то подсказывало мне, что вы сыграете заметную роль..."
    marcus "Только не мог предположить, что настолько заметную..."
    img 60266
    m "Что вы имеете ввиду, Маркус?"
    m "Эта женщина... Она назвала вам сыном?"
    img 60267
    marcus "Да, Миссис Бакфетт..."
    marcus "Она назвала меня так..."
    img 60268
    m "Она... Она всех так называет?"
    img 60269
    marcus "Нет, Миссис Бакфетт..."
    img 60270
    m "И что, это значит что... Что она..."
    img 60271
    marcus "Да, Миссис Бакфетт, это моя мать..."
    img 60272
    m "!!!"
    m "Значит, это она замешана в том, что случилось со мной?!"
    marcus "Нет, Миссис Бакфетт..."
    marcus "Я понимаю вашу логику, но она замешана только в том, что с вами НЕ СЛУЧИЛОСЬ..."
    marcus "Там наверху..."
    m "В смысле?"
    img 60273
    marcus "Видите ли, Миссис Бакфетт, моя жизнь... Она довольно длинная..."
    marcus "И довольно сложная..."
    marcus "Мое прошлое во многом туманно и загадочно для многих..."
    img 60274
    marcus "Но вы теперь кое-что знаете про меня..."
    marcus "Что я, в какой-то мере, миллионер из трущоб..."
    marcus "Хотя деньги для меня уже давно ничего не значат, Миссис Бакфетт..."
    marcus "Деньги - это... Это скучно..."
    marcus "Мои достижения весьма велики и связаны они... С другим..."
    img 60275
    w
    img 60276
    m "Хороший же сыночек, у которого мать работает сутенершей!"
    img 60277
    marcus "Видите ли, Миссис Бакфетт, это был ее выбор..."
    marcus "Наши отношения были... Сложными..."
    marcus "Когда я забирался наверх, я принимал решения..."
    marcus "Которые моя мать не всегда могла понять... И принять..."
    marcus "Это сказывалось на ней и ее судьбе..."
    marcus "Она не хотела знать меня..."
    marcus "Не хотела принимать помощь от меня..."
    img 60278
    m "Потому что вы эгоист! Больной эгоист, черт возьми!"
    img 60279
    marcus "Возможно, но я люблю ее..."
    marcus "И теперь, когда она пришла ко мне и попросила помочь вам..."
    marcus "После стольких лет..."
    img 60280
    w
    img 60281
    m "..."
    img 60282
    marcus "Для меня это действительно неожиданно..."
    marcus "И очень важно..."
    img 60283
    marcus "Что вы сделали для того, что она решила поступить так ради вас?"
    img 60284
    m "Я... Я ничего не делала!"
    m "Я попросила помочь!"
    img 60285
    marcus "Вы особенная женщина, Миссис Бакфетт."
    marcus "Вы сами не замечаете, как меняете людей вокруг вас..."
    marcus "Вы сильная, но кроме силы в вас есть что-то еще..."
    marcus "Что-то настолько особенное, что смогло сдвинуть естественный ход вещей..."
    img 60286
    m "Я... Я ненавижу вас, Маркус!"
    # смотрит на пистолет
    img 60287
    w
    img 60288
    w
    img 60289
    w
    img 60290
    marcus "Вы можете сделать это, если хотите."
    marcus "Он заряжен и взведен, как полагается..."
    img 60291
    m "!!!"
    m "Чего вы добиваетесь?!"
    m "Зачем вы все это рассказываете мне?!"
    m "И что вы хотите сделать со мной?!"
    img 60292
    marcus "Миссис Бакфетт, я хочу сделать то, о чем меня попросила моя мать..."
    marcus "Последний раз, когда она меня просила о чем-то - это подать ей мою руку..."
    marcus "Когда она была смертельно больна..."
    img 60293
    m "И в чем разница?"
    img 60294
    marcus "Разница в том, что в прошлый раз я не помог ей..."
    marcus "Затем я пытался сделать это тысячу раз, но она не просила меня..."
    marcus "И не принимала мою... Помощь..."
    img 60295
    m "А в этот раз?!"
    img 60296
    marcus "В этот раз я сделаю все, что в моих силах, чтобы выполнить ее просьбу..."
    img 60297
    m "Что это значит, Маркус?"
    m "Вы... Вы меня отпустите?"
    img 60298
    marcus "Отпустить? Вы свободны, Миссис Бакфетт, я не держу вас здесь..."
    marcus "Единственная моя просьба - это сказать мне..."
    img 60299
    m "Что сказать?!"
    img 60300
    marcus "Чем я могу помочь вам..."
    img 60301
    m "Что?.. Что это значит, Маркус?"
    m "Что за помощь вы мне предлагаете?"
    img 60302
    marcus "Миссис Бакфетт, как вы, наверное, уже давно поняли..."
    marcus "Я представляю некую организацию, весьма могущественную..."
    marcus "У меня есть много ресурсов, которые я могу задействовать..."
    img 60304
    marcus "Для решения любых ваших просьб..."
    marcus "Я в вашем распоряжении, Миссис Бакфетт..."
    img 60303
    m "Что это значит???"
    m "Дьявол встал на сторону добра?!"
    img 60305
    marcus "Зло и добро отличаются лишь точкой зрения на них, Миссис Бакфетт..."
    marcus "Но вы можете называть это, как захотите..."
    img 60306
    m "То есть... Погодите..."
    m "Я... Я могу вернуть назад все?"
    m "Мои документы... Мой дом... Мое..."
    img 60307
    marcus "Да, Миссис Бакфетт..."
    marcus "Более того, возможно, кто-то обидел вас..."
    img 60308
    marcus "Видите ли, место на объекте уже приготовлено..."
    marcus "И его должен кто-то занять..."
    img 60269
    marcus "Может быть, у вас есть идеи, кто?"

    # музыка, несолько кадров как Моника смотри на Маркуса
    img 60309
    m "Да, Мистер Маркус..."
    img 60310
    m "У меня много идей..."
    # затемнение to be continued
    return
