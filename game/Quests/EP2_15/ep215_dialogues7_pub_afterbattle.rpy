# если уже был батлл на сцене с Молли и Моника стала королевой паба
# работа официанткой
# при клике на клиентов паба


#call label customer1_afterbattle() # трогает ножку-жопку








# при диалогах с клиентами максимально используем имеющиеся арты!!

label customer1_afterbattle:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 14202
    w
    imgf 14203
    m "Что будете заказывать?"
    imgd 14204
    customer1 "В твоем вопросе кое-чего не хватает..."
    customer1 "Разве обслуживающий персонал так должен обращаться с клиентами?"
    music Pyro_Flow
    imgf 14209
    mt "Какого черта этот неудачник постоянно ко мне придирается?"
    mt "И вообще! Я не обслуживающий персонал!"
    mt "Я здесь Королева!"
    mt "!!!"
    menu:
        "Быть вежливой.":
            music Groove2_85
            imgd 14205
            mt "Если я спрошу его вежливо, он быстрее сделает заказ."
            mt "И отстанет от меня со своими дурацкими замечаниями!"
            imgf 14216
            m "Добрый вечер, вы готовы сделать заказ?"
            customer1 "Так значит ты умеешь быть вежливой?"
            customer1 "Умница, детка!"
            customer1 "Принеси мне чего-нибудь на свой выбор."
            music Pyro_Flow
            imgd 14211
            mt "Никчемный неудачник!"
            mt "Хочет, что бы перед ним выслуживались..."
            m "Одну минуту."
            # уходит, приносит пиво
            fadeblack
            sound highheels_run2
            pause 1.5
            music Groove2_85
            music2 pub_noise1_low
            pause 1.5
            sound snd_plates1
            imgfl 14219
            w
            sound snd_beer_table
            imgf 14220
            m "Пожалуйста, ваш заказ."
            mt "Специально для вас наши лучшие 'помои'..."
            imgd 14221
            customer1 "Стоп!"
            customer1 "Это еще не все..."
            mt "Чего еще ему нужно?!"
            customer1 "Я видел твои выступления на сцене..."
            m "И?"
            customer1 "И готов заплатить тебе $ 5..."
            customer1 "Если дашь мне потрогать твою ножку."
            imgf 14215
            m "..."
            menu:
                "Нет!":
                    music Pyro_Flow
                    imgd 32232
                    m "Я Королева Shiny Hole!"
                    m "И никому не позволено прикасаться ко мне!"
                    m "Ни за 5 долларов, ни за 1 000 долларов!"
                    imgf 14222
                    mt "Хотя..."
                    mt "За тысячу долларов я подумала бы об этом..."
                    imgd 14223
                    customer1 "Ясно."
                    customer1 "Придется поговорить с Джо о привате с тобой..."
                    customer1 "Все, свободна!"
                    return
                "Согласиться.":
                    music Hidden_Agenda
                    imgd 14222
                    mt "Всего $ 5?!"
                    mt "Чтобы прикоснуться к моим шикарным ножкам?!"
                    mt "Жмот!"
                    mt "С другой стороны..."
                    mt "Эти деньги для меня не будут лишними..."
                    # оборачивается
                    sound Jump1
                    pause 0.5
                    sound Jump1
                    imgf 32233
                    mt "Надо только проследить, чтобы этого никто не заметил..."
                    m "Только потрогать и быстро!"
                    # клиент кладет руку ей на колено, сбоку
                    # и быстро проводит ею вверх, под юбку, и хватает за попу
                    music Loved_Up
                    imgd 32234
                    w
                    imgf 32235
                    w
                    sound Jump2
                    imgd 32236
                    w
                    music stop
                    sound plastinka1b
                    img 32237  hpunch
                    pause 1.5
                    music Pyro_Flow
                    music2 pub_noise1_low
                    m "Что ты делаешь?!"
                    # Моника резко от него отстраняется
                    m "!!!"
                    mt "Мерзавец!!!"
                    customer1 "Отличная упругая задница! Аха-ха!"
                    customer1 "Я ее себе именно такой и представлял!"
                    mt "Сволочь!"
                    # Моника злобно на него смотрит
                    $ add_tips(5.0)
                    imgf 32238
                    customer1 "Вот, держи свои 5 баксов."
                    customer1 "Заслужила."
                    customer1 "Все, свободна!"
                    return
        "Ответить грубо":
            # Моника возмущенно
            music Pyro_Flow
            imgd 14215
            mt "Этот пьяница опять решил учить меня манерам?"
            imgf 14216
            m "Полагаю, чего-то вежливого?"
            customer1 "Ага..."
            m "Нет в меню!"
            imgf 14217
            customer1 "Тогда я передумал делать заказ! Можешь идти!"
            mt "Жалкий неудачник!"
            # развернуться и уйти
            fadeblack
            sound highheels_short_walk
            stop music2
            return
    return

label customer2_afterbattle:
    img 14225
    w
    img 14229
    customer2 "Ну что, дорогуша!"
    customer2 "Я могу тебя поздравить! Ты стала королевой Shiny Hole!"
    customer2 "Видел твое выступление - папочке понравилось!"
    customer2 "Теперь, наверное, будешь перед всеми хвастаться в своей провинции?"
    customer2 "Жопой трясти - это тебе не картошку сажать... Или что там у вас?!"
    img 14228
    mt "Я же говорила, что я не из провинции! Болван!"
    mt "Что он вообще несет? Какая к черту картошка?"
    m "Я из этого города, а не из провинции..."
    img 14226
    customer2 "Всего пару недель и уже городская? Ик!"
    customer2 "Это так не работает..."
    customer2 "Эх... Вот все вы такие, глупые... Из этих своих провинций."
    customer2 "Ладно, неси пива."
    img 14227
    mt "Он вообще слышит, что я ему говорю?!"
    mt "Я - Моника Бакфетт, а не какая-то провинциалка!"
    mt "А ты - жалкий неудачник!"
    mt "И это отвратительное пиво - лучшее, на что ты можешь расчитывать!"
    # уходит - приходит
    img 14236
    m "Ваше пиво."
    img 14238
    customer2 "Спасибо, дорогуша."
    $ add_tips(1.0)
    customer2 "Вот тебе немного чаевых... Съездишь к себе домой, в провинцию..."
    mt "Пьяный болван!"
    customer2 "Не убегай так быстро, дорогуша!"
    customer2 "У меня есть к тебе еще небольшое дельце..."
    img 14230
    mt "Что еще?!"
    mt "!!!"
    img 32239
    customer2 "Меня заворожили твои королевские сиськи..."
    customer2 "Порадуй меня ими, дорогуша. Дай потрогать!"
    customer2 "Получишь за это парочку мистеров франклинов!" # подмигивает Монике
    # клиент тянет руку к Монике
    img 14239
    mt "Конечно, нет!"
    mt "Я - Королева Shiny Hole! А ты - никто!"
    mt "Да что ты позволяешь себе, животное!"
    img 32240
    m "Не смей прикасаться ко мне!"
    customer2 "Чего ты так взбесилась, дорогуша?"
    customer2 "Тебе не нужен мистер Франклин? "
    m "Я тебе не какая-то дешевка!"
    m "Чтобы позволять прикасаться ко мне за пару долларов!"
    img 32241
    customer2 "А... Ну так сразу бы и сказала...."
    customer2 "А что насчет Гамильтона?! Ик!"
    customer2 "За то, чтобы посмотреть на них?"
    menu:
        "Мое решение неизменно!":
            img 32242
            m "Мое решение неизменно!"
            m "Если это все, я ухожу!"
            customer2 "Ну и проваливай, Королева Hole!"
            img 14227
            mt "Грязное животное!!!"
            mt "!!!"
            return
        "Мне нужны деньги!":
            img 32243
            mt "Черт!"
            mt "Мне нужны эти деньги!"
            mt "Моя жизнь стала похожа на ужасный сон!"
            mt "Сон, в котором мне приходится считать каждый доллар!"
            mt "Когда этот кошмар закончится?!"
            img 32244
            m "!!!"
            m "Деньги вперед! И держи свои руки при себе!"
            # Моника забирает деньги
            img 32245
            w
            img 32246
            # Моника оглядывается по сторонам что бы убедиться что никто не смотрит
            # показывает грудь
            img 32247
            w
            img 32248
            w
            img 32249
            w
            img 32250
            customer2 "Оооо! У вас, провинциалок, сиськи что надо!"
            customer2 "Действительно королевские сиськи!!!"
            # клиент хватает ее за грудь
            # Моника отпрыгивает от него
            img 32251
            w
            img 32252
            m "С тебя достаточно!!!"
            m "!!!"
            $ add_tips(10.0)
            # Мон уходит
            # доход 10 $
            return
    return

label customer3_afterbattle:
    img 14249
    w
    img 14250
    customer3 "О, сама королева Shiny Hole будет меня обслуживать!"
    customer3 "Решила предложить мне приват?"
    m "Нет, я готова принять ваш заказ."
    customer3 "Тогда записывай. Я делаю заказ на приватный танец в твоем исполнении!"
    customer3 "Или снова будешь врать, что не танцуешь?"
    img 14251
    m "Я не танцую приватные танцы."
    m "Мои выступления проходят только на сцене."
    img 14252
    customer3 "Обманывать нехорошо, милочка!"
    customer3 "Давай так!"
    customer3 "Если я куплю приват с тобой..."
    customer3 "То ты сделаешь мне бесплатный минет за то, что обманываешь."
    img 14256
    m "ЧТООО?!?!!"
    m "НЕТ!"
    mt "Он совсем охренел?!"
    mt "?!?!?!"
    mt "А вдруг этот неудачник договорится с Джо?!"
    mt "Что же тогда делать!?"
    img 14257
    customer3 "АГА!!!"
    customer3 "ЗАНЕРВНИЧАЛА!?"
    customer3 "Но зато, если ты не обманщица, я заплачу тебе $ 10 моральной компенсации!"
    customer3 "Что скажешь?"
    img 14258
    mt "Думай, Моника! Думай!"
    mt "Возможно, стоит сказать, что я временно не танцую приваты?"
    mt "Или соврать, что приватный танец стоит $ 2000? Я же королева Shiny Hole..."
    mt "Вряд ли у кого-то в этой дыре найдутся такие деньги!"
    mt "А вдруг у него найдутся?!"
    img 14254
    customer3 "Хотя нет, у меня сейчас нет денег на приват с тобой..."
    customer3 "Неси заказ!"
    img 14266
    w
    img 14267
    w
    img 14268
    # уходит - приносит
    img 14270
    w
    img 14271
    w
    img 14272
    m "Ваш заказ."
    img 14273
    customer3 "Ага..."
    customer3 "На чаевые ты не заработала!"
    customer3 "Хотя..."
    customer3 "Если ты приспустишь трусики и покажешь мне свою попку..."
    customer3 "Я готов заплатить тебе $ 10!"
    img 14281
    m "..."
    menu:
        "Нет!":
            img 14286
            mt "Для тебя - ни за какие деньги на свете!"
            img 14279
            m "Я обнажаюсь только на сцене..."
            m "И только для танца!"
            customer3 "Ну тогда проваливай!"
            img 14296
            mt "Никчемный извращенец!!!"
            mt "Грубиян!!!"
            mt "!!!"
            # Моника злится
            pass
        "Мне нужны деньги...":
            img 14278
            mt "Эти $ 10 для меня не будут лишними..."
            img 14274
            m "Только быстро..."
            customer3 "Ага... Давай!"
            customer3 "Хоть посмотрю вблизи на королевску попку! Аха-ха!!"
            # Моника оглядывается что никто не смотрит
            # Задирает юбку сзади
            # потом быстро натягивает трусики обратно и опускает юбку
            img 32253
            w
            img 32254
            w
            img 32255
            w
            img 32256
            w
            img 32257
            w
            img 32255
            w
            img 32254
            w
            img 32253
            w
            img 14280
            m "Достаточно! Давай мои деньги!"
            customer3 "Отличная задница! У меня даже привстал! Аха-ха!"
            customer3 "Держи свои десять баксов!"
            # дает ей деньги
            img 32258
            $ add_tips(10.0)
            customer3 "И жди меня на привате в скором времени!" # подмигивает
            customer3 "Там ты не отделаешься так легко, королева! Аха-ха!!!"
            img 14286
            mt "Мерзавец!"
            mt "!!!"
            pass
    img 14296
    mt "Жалкий неудачник!"
    customer3 "Свободна!"
    mt "!!!"
    return

label customer4_afterbattle:
    img 14320
    m "Здравствуйте! Что будете заказывать?"
    customer4 "Привет, симпатичная мордашка!"
    customer4 "Принеси мне Ваш восхитительный Shiny бургер. Очень уж он мне нравится."
    img 14339
    mt "Восхитительный бургер?!" # Моника надменно улыбается
    # Моника поглощена воспоминаниями о изысканной жизни
    mt "Это фуа-гра с трюфелем восхитительны, болван! Но откуда тебе знать?"
    mt "Ты, наверное, и слов таких никогда не слышал..."
    mt "О, Моника! Ты достойна своей прежней роскошной жизни!"
    mt "Среди лоска и изыска..."
    mt "С шампанским и восхитительной изысканной высокой кухней!"
    # кадр на клиента
    img 14323
    customer4 "Эй, мордашка! Ты чего там зависла? Неси заказ!"
    img 14324
    mt "Вот черт..."
    mt "Я замечталась..."
    mt "..."
    mt "Грубиян!"
    img 14321
    customer4 "Знаешь, мордашка! Ты так сильно похожа на одну девицу из телика."
    mt "!!!"
    customer4 "Не будь ты официанткой..."
    customer4 "Как же ее звали? Погоди, сейчас вспомню..."
    customer4 "Ми... Ма..."
    customer4 "А, точно! МОНИКА!"
    # Мон в ужасе!!!!!
    img 32259
    mt "ОН УЗНАЛ МЕНЯ!!!"
    mt "УЗНАЛ!!!"
    customer4 "Да, Моника... Как я мог забыть?"
    mt "!!!"
    mt "МОНИКА, ЧТО ТЕПЕРЬ ДЕЛАТЬ!?"
    mt "АААААААА!!!"
    customer4 "В сериале каком-то снимается..."
    mt "Сериале?"
    img 32260
    customer4 "Хотя... Вот сейчас смотрю на тебя - совсем не похожа..."
    customer4 "Та, в телике, посимпатичнее была."
    img 14342
    mt "Посимпатичнее?!"
    mt "Я! Я самая красивая женщина этого города!"
    mt "И я не какая-то официантка, Я БИЗНЕС-ЛЕДИ! Я Моника Бакфетт!"
    mt "!!!"
    mt "С другой стороны, хорошо, что этот пьяный кретин меня не узнал..."
    img 14326
    customer4 "Не растраивайся, мордашка. Хочешь 5 баксов?"
    m "..."
    customer4 "Молчание - знак согласия."
    customer4 "Тогда дай потрогать твои сиськи."
    m "..."
    menu:
        "Нет!":
            img 14327
            mt "Он решил, что может облапать МЕНЯ, Королеву Shiny Hole?!"
            mt "За какие-то жалкие 5 долларов?!"
            mt "!!!"
            img 14328
            m "Нет!"
            m "Я не оказываю подобные услуги!"
            m "Я здесь Королева, а не какая-нибудь дешевая проститутка!"
            m "Хочешь протрогать грудь - иди к этой рыжей Молли!"
            m "Она тебе за 5 долларов сделает все, что захочешь!"
            customer4 "Она мне уже надоела!"
            m "Ничем не могу помочь!"
            customer4 "Это мы еще посмотрим..."
            pass
        "Согласиться.":
            img 14342
            mt "Всего $ 5?!"
            mt "С другой стороны..."
            mt "Он ведь только прикоснется..."
            mt "Черт!"
            # Моника оглядывается что никто не смотрит
            # наклоняется к клиенту
            # клиент обеими руками обхватывает грудь Моники и тискает
            # Моника отпрыгивает
            img 32261
            w
            img 32262
            w
            img 32263
            w
            img 32264
            m "Все! Этого достаточно!"
            customer4 "Отличные сиськи!"
            customer4 "Трахнуть бы тебя между ними!"
            mt "Фу! Извращенец!"
            mt "!!!"
            customer4 "Вот. Держи свои пять баксов..."
            $ add_tips(5.0)
            # дает ей деньги
            pass
    img 32265
    customer4 "Теперь неси скорее Ваш Shiny бургер и пиво!"
    # уходит - приносит
    img 14336
    w
    img 14334
    w
    img 14337
    customer4 "Держи доллар за красивую мордашку!"
    $ add_tips(1.0)
    img 14338
    customer4 "А где спасибо?"
    m "Спасибо..."
    mt "Придурок!"
    return

label customer5_afterbattle:
    img 14298
    w
    img 14302
    m "Здравствуйте. Желаете сделать заказ?"
    customer5 "Оооо!"
    customer5 "Самая лучшая задница Shiny Hole ко мне пришла!"
    customer5 "Повернись ко мне своей сладкой попкой! Хочу с ней поздороваться!"
    img 14299
    mt "Мерзкий извращенец!"
    mt "!!!"
    m "Что будете заказывать?"
    img 14300
    customer5 "Неси бургер! А когда будешь идти, повиляй своей раскошной задницей... И подмигни мне."
    customer5 "Я хорошо приплачу тебе за это! $ 10!"
    m "..."
    menu:
        "Принести заказ как обычно.":
            # на лице Моники отвращение и раздраженность, она оскорблена
            img 14307
            m "Я принесу ваш заказ, но без виляний и подмигиваний."
            pass
        "$ 10? Хммм...":
            img 14301
            mt "$ 10 за то, чтобы пройтись и подмигнуть? Не самая плохая сделка..."
            mt "Боже, Моника! Не могу поверить!"
            mt "Ты готова выслуживаться за $ 10 перед каким-то грязным пьяньчугой?!"
            mt "Да что с тобой такое?!"
            mt "С другой стороны..."
            mt "А если на это согласится не Моника, а Королева Shiny Hole?"
            mt "..."
            img 14304
            m "Только деньги вперед!"
            $ add_tips(10.0)
            # он дает ей деньги, Моника удаляется за заказом виляя попой,
            # поворачивается и подмигивает
            img 32270
            w
            img 32271
            pass
    # уходит-приходи с заказом
    img 32266
    m "Ваш заказ."
    img 32267
    customer5 "О, детка, смотри! Мой дружок оценил твою попку!"
    customer5 "Может потрешься об него? За $ 50. Что скажешь?"
    menu:
        "Отшить мерзавца!":
            img 32268
            mt "Грязный свин!"
            mt "Перевернуть бы этот бургер на его тупую голову!"
            mt "Но тогда Эшли меня сразу уволит..."
            mt "А мне пока нужны работа в этой грязной дыре!"
            img 32269
            m "Нет!" # высокомерно
            m "Внимание Королевы Shiny Hole стоит в десятки раз дороже!"
            customer5 "Даже так?!"
            customer5 "Хм... Я поговорю с Джо..."
            customer5 "Узнаю, сколько стоит твой приват..."
            mt "Тебе не по карману, неудачник!"
            mt "!!!"
            pass
        "Мне нужны деньги":
            img 32272
            mt "$ 50 звучит неплохо..."
            mt "Черт! Мне нужны эти деньги!"
            mt "!!!"
            m "..."
            img 32273
            #customer5 "Сойдет для первого раза."
            customer5 "Давай уже, не томи! Мой дружок тебя заждался!"
            # Моника садится к нему на колени,
            img 32274
            customer5 "Оооооо! Королевская жопа!!!"
            img 32275
            W
            img 32276
            # хватает Мон за попу и та отпрыгивает
            img 32277
            m "Достаточно! А теперь плати!"
            customer5 "Ух, какая ты горячая штучка!"
            customer5 "Что насчет привата, а?"
            # Мон раздражительно
            m "Я не танцую приваты!"
            m "Ты и так уже получил достаточно внимания от королевы Shiny Hole!!!"
            customer5 "Раньше ты говорила, что на сцене не танцуешь..."
            customer5 "А теперь ты - Королева Shiny Hole... Хе-хе..."
            customer5 "Ладно, Королева, позови Джо!"
            m "Зачем вам Джо?"
            img 32278
            customer5 "Хочу оставить отзыв о твоей работе..."
            mt "О боже, он хочет рассказать о том, что я только что сделала!"
            mt "Или этот мерзавец хочет заказать приват через Джо!?"
            customer5 "А знаешь что, я сам к нему подойду! Так что топай..."
            m "А деньги?!"
            img 32280
            customer5 "О, точно! Нууу, ты слегка коснулась своей попкой меня..."
            customer5 "А теперь деньги слегка коснутся твоей ручки..."
            # проводит деньгами по руке Мон и подмигивает ей, деньги не дает
            img 32279
            W
            img 32281
            W
            img 32280
            customer5 "А это, за сервис."
            $ add_tips(2.0)
            # Дает ей пару баксов
            pass
    # Моника злится и уходит
    # он шлепает по попе уходящую Мон, она отпрыгивает, куксит злую моську и уходит
    img 32282
    mt "Грязный извращенец!"
    mt "И ты, и все остальные мерзавцы!"
    mt "Вы все поплатитесь!!!"
    mt "Вы еще узнаете, кто такая Моника Бакффет!!!"
    mt "!!!"
    return

label customer78_afterbattle:
    img 14425
    W
    img 14427
    m "Здравствуйте. Что будете заказывать?"
    img 32283
    customer7 "Эй, детка! Это твой костюмчик для сцены?"
    # пытается облапать Монику за грудь
    m "Эй! Что ты делаешь?!"
    m "Убери руки!"
    m "Я работаю здесь официанткой!!"
    m "Не смей ко мне прикасаться!"
    img 14433
    customer7 "Ладно, ладно... Остынь."
    customer7 "Официантка - это скучно."
    customer7 "Лучше полезай на сцену и сними с себя этот костюмчик!"
    customer7 "Как ты это умеешь делать. Аха-ха!"
    m "Я же уже сказала, что сегодня работаю здесь официанткой!"
    img 14431
    mt "Здесь одни извращенцы и пьяницы!"
    mt "Похоже я здесь единственный нормальный человек!"
    mt "Ну и Клэр еще..."
    img 14430
    customer7 "Ладно... Раз не хочешь танцевать, тогда хоть выпить нам принеси..."
    mt "Нахал! Может плюнуть ему в коктейль?"
    customer7 "Неси пару лонг-дринков! И покрепче!!"
    # уходит - приносит
    img 14464
    W
    img 14465
    W
    img 14466
    m "Пожалуйста, ваши коктейли!"
    img 14467
    customer7 "Умница, детка!"
    customer7 "Хочешь чаевых?"
    m "..."
    customer7 "Ну-ка, наклонись вперед!"
    customer7 "Я положу пару баксов тебе и твоим малышкам!"
    # Моника злобно смотрит
    m "..."
    menu:
        "Нет!":
            img 14469
            m "Оставь свои пару баксов себе!"
            m "Похоже, тебе они нужнее."
            customer7 "Эй, полегче!"
            customer7 "За такой сервис и цента не оставлю!"
            img 14475
            mt "Да пошли вы, два придурка!"
            mt "Уроды!"
            mt "!!!"
            # уйходит без чаевых
            pass
        "Сделать, как просят клиенты!":
            img 14468
            mt "Черт!"
            mt "Лишние деньги мне не помешают..."
            # Моника боязливо оглядывается, чтобы никто этого не увидел
            # наклоняется вперед, выставляя грудь на показ
            img 32284
            m "Быстрее!"
            img 32285
            w
            img 32286
            customer7 "Отличные сиськи!"
            # засовывает деньги Монике между грудями
            customer7 "Держи, детка!"
            customer7 "Вот твои $ 5!"
            img 32287
            $ add_tips(5.0)
            customer7 "За шикарные королевские сиськи!"
            customer7 "Аха-ха!!!"
            mt "!!!"
            pass
    img 14459
    mt "Все так и норовят облапать меня!"
    mt "Почему меня, такую красивую и хорошую женщину..."
    mt "Окружают одни извращенцы!"
    mt "!!!"
    return

label customer9_afterbattle:
    img 14394
    m "Здравствуйте."
    m "Что будете заказывать?"
    img 14395
    customer9 "Ну здравствуй, горячая королевская киска!"
    customer9 "Я рад, что ты ко мне подошла."
    customer9 "Сегодня я принес тебе подарочек! Хочешь его получить?"
    customer9 "Присаживайся к Санте на колени."
    img 14396
    mt "К черту такого Санту!"
    img 14397
    m "Мне не нужен ваш подарок!"
    customer9 "Ладно, сегодня Санта добрый..."
    customer9 "Поэтому эта проказница все равно получит то, что принес ей Санта."
    # клиент показывает у себя в руках кружевные трусики
    img 32293
    w
    img 32294
    m "Трусы?!"
    customer9 "Я хотел забрать твои трусики, когда ты выступала..."
    customer9 "Надеялся, ты кинешь их мне..."
    customer9 "Мммм... Трусики с твоей горячей киски..."
    img 32295
    mt "Фу! Грязный извращенец!!!"
    img 32296
    customer9 "Но не вышло..."
    customer9 "Поэтому я решил, что ты можешь поносить эти трусики для меня."
    customer9 "А я буду их нюхать и облизывать вечерами. И дрочить на них. Хе-хе!"
    customer9 "Ну как? Тебе нравится моя идея?"
    mt "!!!"
    mt "КАК ТАКОЕ ВООБЩЕ МОЖЕТ НРАВИТСЯ!?!?!"
    img 14402
    m "Я не буду этого делать!"
    m "Сам носи эти трусики и дро... И делай с ними, что хочешь!"
    customer9 "А если я заплачу тебе $ 50 за это?"
    customer9 "Ты их поносишь немного, а потом отдашь мне."
    customer9 "Что скажешь?"
    m "..."
    menu:
        "Отказаться!":
            img 14407
            m "Я уже сказала нет! Но могу повторить еще раз. НЕТ!"
            mt "Грязное животное!"
            img 14401
            customer9 "Горячая киска растроила Санту..."
            customer9 "Проваливай!"
            customer9 "Плохая киска!"
            # Моника уходит
            return
        "$ 50?":
            img 14403
            mt "У меня сейчас такое тяжелое положение... Каждый доллар на счету."
            mt "О, Боже!"
            mt "На какие ужасные вещи мне приходится идти, чтобы заработать!"
            mt "!!!"
            mt "Хм... А что, если..."
            mt "..."
            img 14404
            m "Я надену их только за $ 5 000!"
            customer9 "Эй! Эти трусы стоят 6 баксов! Откуда такие цены?!"
            m "А как ты хотел? Вообще-то, Я - Королева Shiny Hole!"
            m "!!!"
            customer9 "$ 200!"
            m "$ 4 000 и ни центом меньше!"
            img 14405
            customer9 "Я подумаю над этим предложением, детка..."
            # Моника уходит
            img 14410
            mt "Такая шикарная женщина, как Я, тебе не по карману!"
            mt "Неудачник!"
            return
    return

label customer10_afterbattle:
    img 14359
    m "Здравствуйте. Что будете заказывать?"
    customer10 "Моя Виолетта пришла поздоровоться?"
    customer10 "Или ты хочешь узнать, как мне твое выступление на сцене?"
    img 14366
    mt "Мне все равно, что думает об этом такой извращенец, как ты!"
    mt "!!!"
    img 14361
    customer10 "Не переживай, мне понравилось..."
    customer10 "А знаешь, что мне понравится еще больше?"
    customer10 "Если ты сейчас же запрыгнешь на этот пилон... Или на меня."
    img 14364
    m "!!!"
    m "Я не собираюсь танцевать!"
    customer10 "А я слышал, что танцуешь..."
    customer10 "И не только..."
    m "!!!"
    img 14370
    customer10 "Можем пойти в гримерку..."
    customer10 "Я намажу тебя маслом для выступления на сцене..."
    customer10 "Я хорошо промажу все твои формы."
    mt "Мерзавец! Как он смеет так со мной говорить!? "
    m "Если вы хотите сделать заказ на еду или выпивку, то я вас слушаю."
    m "В противном случае - я ухожу!"
    img 14368
    customer10 "Ты не в настроении что-ли?"
    customer10 "Так бы и сказала, что в следующий раз..."
    mt "Никакого следующего раза не будет!"
    customer10 "Сейчас принеси мне пива, а я посмотрю на твою задницу..."
    customer10 "А вечером буду представлять, как ты трешься ею об меня..."
    customer10 "И дрочить. Аха-ха!"
    img 14377
    mt "Он думает мне должно это нравится?!"
    mt "Это звучит омерзительно!"
    # уходит приходит
    img 14372
    w
    img 14373
    w
    img 14374
    m "Ваш заказ..."
    customer10 "Ага... Молодец..."
    customer10 "Дай я отблагодарю тебя своим горячим поцелуем, Виолетта!"
    img 14375
    mt "Фу! Нет!"
    mt "!!!"
    # Моника корчит моську отвращения
    customer10 "Или ты можешь подарить мне свой королевский поцелуй сама!"
    customer10 "$ 20 - достаточная цена королевы Shiny Hole?!"
    menu:
        "Нет!":
            img 14379
            m "Королевский поцелуй может подарить лишь [monica_pub_name]!"
            m "Она новая королева Shiny Hole!"
            m "А Виолетта не дарит королевские поцелуи!"
            m "Даже за $ 1 000!"
            customer10 "Овца!"
            img 14377
            mt "УРОД!"
            return
        "Эти $ 20 не будут лишними...":
            img 14380
            mt "Целовать это мерзкое существо..."
            mt "Фу! Он омерзителен мне!"
            mt "Но эти $ 20 не будут лишними..."
            # клиент тянеся губами к Монике
            img 32288
            w
            img 32289
            m "Но только королевский поцелуй в щеку..."
            img 32290
            customer10 "На пилоне с голой жопой значит..."
            customer10 "А поцелуй, как от монашки?"
            customer10 "Такое кидалово и $ 5 не стоит, Виолетта!"
            customer10 "Давай королевский засос прямо в губы..."
            img 32291
            mt "Фу!"
            m "НЕТ!"
            customer10 "Тогда свободна!"
            return
    img 32292
    mt "Этот район кишит извращенцами и отбросами..."
    mt "Ненавижу их всех!"
    mt "!!!"
    return

label customer11_afterbattle:
    img 32297
    m "Здравствуйте. Готовы сделать заказ?"
    img 32298
    customer11 "Неужели! Наконец-то!"
    customer11 "Изволила подойти!"
    customer11 "Ты королева или официантка?!"
    customer11 "Видишь, что гость сидит?!"
    customer11 "Это значит, что нужно тащить свою задницу и принимать заказ!"
    # Мон злится
    img 32299
    mt "Похоже, в этом пабе собрались все хамы города..."
    img 32300
    customer11 "Неси мне... Знаешь что... Хммм..."
    # рука клиента заныривает под юбку Моники сзади
    img 32301
    w
    img 32302
    mt "ОН ЧТО!!"
    mt "ЛАПАЕТ МЕНЯ!?!?!"
    menu:
        "Промолчать.":
            img 32303
            mt "Врезать бы ему!!!"
            mt "Как он посмел лапать МЕНЯ?!"
            mt "?!?!?!"
            mt "Так, Моника, спокойно!"
            mt "Теперь, когда я зарабатываю больше, я не могу потерять этот источник дохода!"
            mt "Просто сделай вид, что ничего не происходит..."
            img 32304
            m "Вы готовы сделать заказ?"
            customer11 "Так ты королева или официантка?"
            m "Теперь я Королева Shiny Hole!"
            customer11 "А киска у тебя тоже королевская?"
            customer11 "Хочу поверить..."
            customer11 "Сколько стоит свидание с твоей киской?"
            m "..."
            menu:
                "$ 100!":
                    img 32299
                    mt "Он уже видел меня полностью голой со сцены..."
                    mt "И извращенка Эшли следит, чтобы я выслуживалась перед клиентами!"
                    img 32298
                    m "$ 100 чтобы посмотреть!"
                    customer11 "Даааа... Цены у тебя королевские!"
                    customer11 "Я дам $ 20!"
                    menu:
                        "Да.":
                            pass
                        "Нет!":
                            img 32305
                            mt "Иди в жопу, придурок!"
                            mt "!!!"
                            # уходит
                            return
                    img 32306
                    m "$ 20 и ни центом меньше!"
                    customer11 "Договорились!"
                    customer11 "Показывай свою подружку..."
                    # Моника оглядывается, поверяет что никто не смотрит
                    # покзывает киску, приспуская трусики (быстро) спереди
                    img 32307
                    w
                    img 32308
                    w
                    img 32309
                    w
                    img 32310
                    w
                    img 32311
                    customer11 "А сколько стоит лизнуть ее?"
                    m "Нисколько!!!"
                    m "Можно только смотреть!!!"
                    m "!!!"
                    customer11 "Тогда неси мне бургер и пива..."
                    customer11 "От ее вида у меня все пересохло во рту..."
                    customer11 "Горячая королевская киска!"
                    mt "Извращенец!"
                    # уходит приходит
                    img 14387
                    w
                    img 14389
                    m "Ваш заказ..."
                    img 14390
                    customer11 "Как захочешь еще что-то показать, тащи сюда свой зад..."
                    customer11 "А сейчас брысь!"
                    $ add_tips(20.0)
                    # оплата
                    img 14386
                    mt "Фу! Мерзость! И эти ужасы я должна терпеть!"
                    mt "!!!"
                    return
                "Нисколько!":
                    img 32312
                    mt "Я больше не могу это терпеть!"
                    img 32313
                    m "Свидание с моей к... Кхм..."
                    # клиент лезет к ней рукой, Моника отстраняется
                    m "Уберите свои руки!"
                    m "И делайте уже заказ, если вообще собирались его делать!"
                    img 32314
                    customer11 "Проваливай! Грубиянка!"
                    customer11 "Не порть мне вечер!"
                    customer11 "Пошла вон!"
                    img 32305
                    mt "Иди в жопу, придурок!"
                    mt "!!!"
                    return
    img 32305
    mt "Грубиян!"
    mt "Мерзкое инстинктивное животное!"
    mt "!!!"
    return


label customer12_afterbattle:
    # кадр на клиента. Он свистит и подзывает рукой
    img 32315
    customer12 "Эй ты! Тащи свои королевские сиськи сюда!"
    img 14412
    m "Меня зовут [monica_pub_name]."
    m "А не сис... Кхм..."
    m "Вы хотели сделать заказ?"
    img 14414
    customer12 "Нет. Хотел посмотреть на твои сиськи... Аха-ха!"
    m "Или делайте заказ или я ухожу!"
    img 14413
    customer12 "Ха! Я и жопу твою заценю, когда уходить будешь!"
    m "Я ухожу!"
    mt "Грубиян!"
    img 14417
    customer12 "Подожди! Я сделаю заказ!"
    customer12 "Хочу еще раз посмотреть на твои сиськи, когда ты принесешь мой заказ..."
    customer12 "Ну-ка! Давай быстро, как козочка, спрыгай мне за пивом!"
    img 14422
    mt "Грязное отродье!"
    mt "Обращается со мной, как с дешевкой какой-то!"
    mt "!!!"
    # уходит-приходит с пивом
    img 14446
    m "Ваш заказ."
    mt "Идиот!"
    img 14447
    customer12 "Спасибо! Отличные королевские сиськи! Аха-ха!"
    m "До свидания!"
    img 14448
    customer12 "Подожди!"
    customer12 "А жопа такая же королевская?"
    customer12 "А знаю... Ты же тут ничего бесплатно не делаешь..."
    customer12 "$ 20 устроит?"
    m "..."
    menu:
        "Нет!":
            img 14449
            mt "Для тебя ни за какие деньги на свете!"
            img 14450
            m "Я обнажаюсь только на сцене..."
            m "И только для танца!"
            customer12 "Цену набиваешь?"
            customer12 "Ну тогда я отсюда посмотрю на твой зад!"
            customer12 "Свободна!"
            # Моника злится
            pass
        "Мне нужны деньги...":
            img 14449
            mt "Теперь для меня даже $ 20 - большие деньги..."
            img 32316
            m "Я не стану ее оголять..."
            customer12 "А я и не просил..."
            customer12 "Но теперь подумаю об этом! Аха-ха!"
            # Моника оглядывается что никто не смотрит
            # Задирает юбку сзади
            # Клиент оттягивает трусы Моники  и они отстреливают ей по попе
            # Моника отпрыгивает
            img 32317
            w
            img 32318
            w
            img 32319
            w
            img 32320
            w
            img 32321
            m "Мерзавец!"
            mt "!!!"
            customer12 "Грубиянка!"
            pass
    img 32322
    customer12 "Грубиянки не получают чаевые! Аха-ха!"
    # клиент смеется
    # Моника злится
    img 14423
    mt "Сволочь! Он обманул меня!"
    mt "Он оставил меня без чаевых!"
    mt "Пусть в следующий раз сам себя обслуживает!"
    mt "Когда этот кошмар уже закончится?!"
    mt "?!?!?!"
    return
