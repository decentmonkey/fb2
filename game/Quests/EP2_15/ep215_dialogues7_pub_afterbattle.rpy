# если уже был батлл на сцене с Молли и Моника стала королевой паба
# работа официанткой
# при клике на клиентов паба

# при диалогах с клиентами максимально используем имеющиеся арты!!

label customer1_afterbattle:
    m "Что будете заказывать?"
    customer1 "В твоем вопросе кое-чего не хватает..."
    customer1 "Разве обслуживающий персонал так должен обращаться с клиентами?"
    mt "Какого черта этот неудачник постоянно ко мне придирается?"
    mt "И вообще! Я не обслуживающий персонал!"
    mt "Я здесь Королева!"
    mt "!!!"
    menu:
        "Быть вежливой.":
            mt "Если я спрошу его вежливо, он быстрее сделает заказ."
            mt "И отстанет от меня со своими дурацкими замечаниями!"
            m "Добрый вечер, вы готовы сделать заказ?"
            customer1 "Так значит ты умеешь быть вежливой?"
            customer1 "Умница, детка!"
            customer1 "Принеси мне чего-нибудь на свой выбор."
            mt "Никчемный неудачник!"
            mt "Хочет, что бы перед ним выслуживались..."
            m "Одну минуту."
            # уходит, приносит бургер
            m "Пожалуйста, ваш заказ."
            mt "Специально для вас наши лучшие 'помои'..."
            customer1 "Стоп!"
            customer1 "Это еще не все..."
            mt "Чего еще ему нужно?!"
            customer1 "Я видел твои выступления на сцене..."
            m "И?"
            customer1 "И готов заплатить тебе $ 5..."
            customer1 "Если дашь мне потрогать твою ножку."
            m "..."
            menu:
                "Нет!":
                    m "Я Королева Shiny Hole!"
                    m "И никому не позволено прикасаться ко мне!"
                    m "Ни за 5 долларов, ни за 1 000 долларов!"
                    mt "Хотя..."
                    mt "За тысячу долларов я подумала бы об этом..."
                    customer1 "Ясно."
                    customer1 "Придется поговорить с Джо о привате с тобой..."
                    customer1 "Все, свободна!"
                    return
                "Согласиться.":
                    mt "Всего $ 5?!"
                    mt "Чтобы прикоснуться к моим шикарным ножкам?!"
                    mt "Жмот!"
                    mt "С другой стороны..."
                    mt "Эти деньги для меня не будут лишними..."
                    # оборачивается
                    mt "Надо только проследить, чтобы этого никто не заметил..."
                    m "Только потрогать и быстро!"
                    # клиент кладет руку ей на колено, сбоку
                    # и быстро проводит ею вверх, под юбку, и хватает за попу
                    m "Что ты делаешь?!"
                    # Моника резко от него отстраняется
                    m "!!!"
                    mt "Мерзавец!!!"
                    customer1 "Отличная упругая задница! Аха-ха!"
                    customer1 "Я ее себе именно такой и представлял!"
                    mt "Сволочь!"
                    # Моника злобно на него смотрит
                    $ add_tips(5.0)
                    customer1 "Вот, держи свои 5 баксов."
                    customer1 "Заслужила."
                    customer1 "Все, свободна!"
                    return
        "Ответить грубо":
            # Моника возмущенно
            mt "Этот пьяница опять решил учить меня манерам?"
            m "Полагаю, чего-то вежливого?"
            customer1 "Ага..."
            m "Нет в меню!"
            customer1 "Тогда я передумал делать заказ! Можешь идти!"
            mt "Жалкий неудачник!"
            # развернуться и уйти
            return
    return

label customer2_afterbattle:
    customer2 "Ну что, дорогуша!"
    customer2 "Я могу тебя поздравить! Ты стала королевой Shiny Hole!"
    customer2 "Видел твое выступление - папочке понравилось!"
    customer2 "Теперь, наверное, будешь перед всеми хвастаться в своей провинции?"
    customer2 "Жопой трясти - это тебе не картошку сажать... Или что там у вас?!"
    mt "Я же говорила, что я не из провинции! Болван!"
    mt "Что он вообще несет? Какая к черту картошка?"
    m "Я из этого города, а не из провинции..."
    customer2 "Всего пару недель и уже городская? Ик!"
    customer2 "Это так не работает..."
    customer2 "Эх... Вот все вы такие, глупые... Из этих своих провинций."
    customer2 "Ладно, неси пива."
    mt "Он вообще слышит, что я ему говорю?!"
    mt "Я - Моника Бакфетт, а не какая-то провинциалка!"
    mt "А ты - жалкий неудачник!"
    mt "И это отвратительное пиво - лучшее, на что ты можешь расчитывать!"
    # уходит - приходит
    m "Ваше пиво."
    customer2 "Спасибо, дорогуша."
    $ add_tips(1.0)
    customer2 "Вот тебе немного чаевых... Съездишь к себе домой, в провинцию..."
    mt "Пьяный болван!"
    customer2 "Не убегай так быстро, дорогуша!"
    customer2 "У меня есть к тебе еще небольшое дельце..."
    mt "Что еще?!"
    mt "!!!"
    customer2 "Меня заворожили твои королевские сиськи..."
    customer2 "Порадуй меня ими, дорогуша. Дай потрогать!"
    customer2 "Получишь за это парочку мистеров франклинов!" # подмигивает Монике
    # клиент тянет руку к Монике
    mt "Конечно, нет!"
    mt "Я - Королева Shiny Hole! А ты - никто!"
    mt "Да что ты позволяешь себе, животное!"
    m "Не смей прикасаться ко мне!"
    customer2 "Чего ты так взбесилась, дорогуша?"
    customer2 "Тебе не нужен мистер Франклин? "
    m "Я тебе не какая-то дешевка!"
    m "Чтобы позволять прикасаться ко мне за пару долларов!"
    customer2 "А... Ну так сразу бы и сказала...."
    customer2 "А что насчет Гамильтона?! Ик!"
    customer2 "За то, чтобы посмотреть на них?"
    menu:
        "Мое решение неизменно!":
            m "Мое решение неизменно!"
            m "Если это все, я ухожу!"
            customer2 "Ну и проваливай, Королева Hole!"
            mt "Грязное животное!!!"
            mt "!!!"
            return
        "Мне нужны деньги!":
            mt "Черт!"
            mt "Мне нужны эти деньги!"
            mt "Моя жизнь стала похожа на ужасный сон!"
            mt "Сон, в котором мне приходится считать каждый доллар!"
            mt "Когда этот кошмар закончится?!"
            m "!!!"
            m "Деньги вперед! И держи свои руки при себе!"
            # Моника забирает деньги
            # Моника оглядывается по сторонам что бы убедиться что никто не смотрит
            # показывает грудь
            customer2 "Оооо! У вас, провинциалок, сиськи что надо!"
            customer2 "Действительно королевские сиськи!!!"
            # клиент хватает ее за грудь
            # Моника отпрыгивает от него
            m "С тебя достаточно!!!"
            m "!!!"
            $ add_tips(10.0)
            # Мон уходит
            # доход 10 $
            return
    return

label customer3_afterbattle:
    customer3 "О, сама королева Shiny Hole будет меня обслуживать!"
    customer3 "Решила предложить мне приват?"
    m "Нет, я готова принять ваш заказ."
    customer3 "Тогда записывай. Я делаю заказ на приватный танец в твоем исполнении!"
    customer3 "Или снова будешь врать, что не танцуешь?"
    m "Я не танцую приватные танцы."
    m "Мои выступления проходят только на сцене."
    customer3 "Обманывать нехорошо, милочка!"
    customer3 "Давай так!"
    customer3 "Если я куплю приват с тобой..."
    customer3 "То ты сделаешь мне бесплатный минет за то, что обманываешь."
    m "ЧТООО?!?!!"
    m "НЕТ!"
    mt "Он совсем охренел?!"
    mt "?!?!?!"
    mt "А вдруг этот неудачник договорится с Джо?!"
    mt "Что же тогда делать!?"
    customer3 "АГА!!!"
    customer3 "ЗАНЕРВНИЧАЛА!?"
    customer3 "Но зато, если ты не обманщица, я заплачу тебе $ 10 моральной компенсации!"
    customer3 "Что скажешь?"
    mt "Думай, Моника! Думай!"
    mt "Возможно, стоит сказать, что я временно не танцую приваты?"
    mt "Или соврать, что приватный танец стоит $ 2000? Я же королева Shiny Hole..."
    mt "Вряд ли у кого-то в этой дыре найдутся такие деньги!"
    mt "А вдруг у него найдутся?!"
    customer3 "Хотя нет, у меня сейчас нет денег на приват с тобой..."
    customer3 "Неси заказ!"

    # уходит - приносит
    m "Ваш заказ."
    customer3 "Ага..."
    customer3 "На чаевые ты не заработала!"
    customer3 "Хотя..."
    customer3 "Если ты приспустишь трусики и покажешь мне свою попку..."
    customer3 "Я готов заплатить тебе $ 10!"
    m "..."
    menu:
        "Нет!":
            mt "Для тебя - ни за какие деньги на свете!"
            m "Я обнажаюсь только на сцене..."
            m "И только для танца!"
            customer3 "Ну тогда проваливай!"
            mt "Никчемный извращенец!!!"
            mt "Грубиян!!!"
            mt "!!!"
            # Моника злится
            pass
        "Мне нужны деньги...":
            mt "Эти $ 10 для меня не будут лишними..."
            m "Только быстро..."
            customer3 "Ага... Давай!"
            customer3 "Хоть посмотрю вблизи на королевску попку! Аха-ха!!"
            # Моника оглядывается что никто не смотрит
            # Задирает юбку сзади
            # потом быстро натягивает трусики обратно и опускает юбку
            m "Достаточно! Давай мои деньги!"
            customer3 "Отличная задница! У меня даже привстал! Аха-ха!"
            customer3 "Держи свои десять баксов!"
            # дает ей деньги
            $ add_tips(10.0)
            customer3 "И жди меня на привате в скором времени!" # подмигивает
            customer3 "Там ты не отделаешься так легко, королева! Аха-ха!!!"
            mt "Мерзавец!"
            mt "!!!"
            pass
    mt "Жалкий неудачник!"
    customer3 "Свободна!"
    mt "!!!"
    return

label customer4_afterbattle:
    m "Здравствуйте! Что будете заказывать?"
    customer4 "Привет, симпатичная мордашка!"
    customer4 "Принеси мне Ваш восхитительный Shiny бургер. Очень уж он мне нравится."
    mt "Восхитительный бургер?!" # Моника надменно улыбается
    # Моника поглощена воспоминаниями о изысканной жизни
    mt "Это фуа-гра с трюфелем восхитительны, болван! Но откуда тебе знать?"
    mt "Ты, наверное, и слов таких никогда не слышал..."
    mt "О, Моника! Ты достойна своей прежней роскошной жизни!"
    mt "Среди лоска и изыска..."
    mt "С шампанским и восхитительной изысканной высокой кухней!"
    # кадр на клиента
    customer4 "Эй, мордашка! Ты чего там зависла? Неси заказ!"
    mt "Вот черт..."
    mt "Я замечталась..."
    mt "..."
    mt "Грубиян!"
    customer4 "Знаешь, мордашка! Ты так сильно похожа на одну девицу из телика."
    mt "!!!"
    customer4 "Не будь ты официанткой..."
    customer4 "Как же ее звали? Погоди, сейчас вспомню..."
    customer4 "Ми... Ма..."
    customer4 "А, точно! МОНИКА!"
    # Мон в ужасе!!!!!
    mt "ОН УЗНАЛ МЕНЯ!!!"
    mt "УЗНАЛ!!!"
    customer4 "Да, Моника... Как я мог забыть?"
    mt "!!!"
    mt "МОНИКА, ЧТО ТЕПЕРЬ ДЕЛАТЬ!?"
    mt "АААААААА!!!"
    customer4 "В сериале каком-то снимается..."
    mt "Сериале?"
    customer4 "Хотя... Вот сейчас смотрю на тебя - совсем не похожа..."
    customer4 "Та, в телике, посимпатичнее была."
    mt "Посимпатичнее?!"
    mt "Я! Я самая красивая женщина этого города!"
    mt "И я не какая-то официантка, Я БИЗНЕС-ЛЕДИ! Я Моника Бакфетт!"
    mt "!!!"
    mt "С другой стороны, хорошо, что этот пьяный кретин меня не узнал..."
    customer4 "Не растраивайся, мордашка. Хочешь 5 баксов?"
    m "..."
    customer4 "Молчание - знак согласия."
    customer4 "Тогда дай потрогать твои сиськи."
    m "..."
    menu:
        "Нет!":
            mt "Он решил, что может облапать МЕНЯ, Королеву Shiny Hole?!"
            mt "За какие-то жалкие 5 долларов?!"
            mt "!!!"
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
            mt "Всего $ 5?!"
            mt "С другой стороны..."
            mt "Он ведь только прикоснется..."
            mt "Черт!"
            # Моника оглядывается что никто не смотрит
            # наклоняется к клиенту
            # клиент обеими руками обхватывает грудь Моники и тискает
            # Моника отпрыгивает
            m "Все! Этого достаточно!"
            customer4 "Отличные сиськи!"
            customer4 "Трахнуть бы тебя между ними!"
            mt "Фу! Извращенец!"
            mt "!!!"
            customer4 "Вот. Держи свои пять баксов..."
            $ add_tips(5.0)
            # дает ей деньги
            pass
    customer4 "Теперь неси скорее Ваш Shiny бургер!"
    # уходит - приносит
    customer4 "Держи доллар за красивую мордашку!"
    $ add_tips(1.0)
    customer4 "А где спасибо?"
    m "Спасибо..."
    mt "Придурок!"
    return

label customer5_afterbattle:
    m "Здравствуйте. Желаете сделать заказ?"
    customer5 "Оооо!"
    customer5 "Самая лучшая задница Shiny Hole ко мне пришла!"
    customer5 "Повернись ко мне своей сладкой попкой! Хочу с ней поздороваться!"
    mt "Мерзкий извращенец!"
    mt "!!!"
    m "Что будете заказывать?"
    customer5 "Неси пасту! А когда будешь идти, повиляй своей раскошной задницей... И подмигни мне."
    customer5 "Я хорошо приплачу тебе за это! $ 10!"
    m "..."
    menu:
        "Принести заказ как обычно.":
            # на лице Моники отвращение и раздраженность, она оскорблена
            m "Я принесу ваш заказ, но без виляний и подмигиваний."
            pass
        "$ 10? Хммм...":
            mt "$ 10 за то, чтобы пройтись и подмигнуть? Не самая плохая сделка..."
            mt "Боже, Моника! Не могу поверить!"
            mt "Ты готова выслуживаться за $ 10 перед каким-то грязным пьяньчугой?!"
            mt "Да что с тобой такое?!"
            mt "С другой стороны..."
            mt "А если на это согласится не Моника, а Королева Shiny Hole?"
            mt "..."
            m "Только деньги вперед!"
            $ add_tips(10.0)
            # он дает ей деньги, Моника удаляется за заказом виляя попой,
            # поворачивается и подмигивает
            pass
    # уходит-приходи с заказом
    m "Ваш заказ."
    customer5 "О, детка, смотри! Мой дружок оценил твою попку!"
    customer5 "Может потрешься об него? За $ 50. Что скажешь?"
    menu:
        "Отшить мерзавца!":
            mt "Грязный свин!"
            mt "Перевернуть бы эту пасту на его тупую голову!"
            mt "Но тогда Эшли меня сразу уволит..."
            mt "А мне пока нужны работа в этой грязной дыре!"
            m "Нет!" # высокомерно
            m "Внимание Королевы Shiny Hole стоит в десятки раз дороже!"
            customer5 "Даже так?!"
            customer5 "Хм... Я поговорю с Джо..."
            customer5 "Узнаю, сколько стоит твой приват..."
            mt "Тебе не по карману, неудачник!"
            mt "!!!"
            pass
        "Мне нужны деньги":
            mt "$ 50 звучит неплохо..."
            mt "Черт! Мне нужны эти деньги!"
            mt "!!!"
            m "..."
            #customer5 "Сойдет для первого раза."
            customer5 "Давай уже, не томи! Мой дружок тебя заждался!"
            # Моника садится к нему на колени,
            customer5 "Оооооо! Королевская жопа!!!"
            # хватает Мон за попу и та отпрыгивает
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
            customer5 "Хочу оставить отзыв о твоей работе..."
            mt "О боже, он хочет рассказать о том, что я только что сделала!"
            mt "Или этот мерзавец хочет заказать приват через Джо!?"
            customer5 "А знаешь что, я сам к нему подойду! Так что топай..."
            m "А деньги?!"
            customer5 "О, точно! Нууу, ты слегка коснулась своей попкой меня..."
            customer5 "А теперь деньги слегка коснутся твоей ручки..."
            # проводит деньгами по руке Мон и подмигивает ей, деньги не дает
            customer5 "А это, за сервис."
            $ add_tips(2.0)
            # Дает ей пару баксов
            pass
    # Моника злится и уходит
    # он шлепает по попе уходящую Мон, она отпрыгивает, куксит злую моську и уходит
    mt "Грязный извращенец!"
    mt "И ты, и все остальные мерзавцы!"
    mt "Вы все поплатитесь!!!"
    mt "Вы еще узнаете, кто такая Моника Бакффет!!!"
    mt "!!!"
    return

label customer78_afterbattle:
    m "Здравствуйте. Что будете заказывать?"
    customer7 "Эй, детка! Это твой костюмчик для сцены?"
    # пытается облапать Монику за грудь
    m "Эй! Что ты делаешь?!"
    m "Убери руки!"
    m "Я работаю здесь официанткой!!"
    m "Не смей ко мне прикасаться!"
    customer7 "Ладно, ладно... Остынь."
    customer7 "Официантка - это скучно."
    customer7 "Лучше полезай на сцену и сними с себя этот костюмчик!"
    customer7 "Как ты это умеешь делать. Аха-ха!"
    m "Я же уже сказала, что сегодня работаю здесь официанткой!"
    mt "Здесь одни извращенцы и пьяницы!"
    mt "Похоже я здесь единственный нормальный человек!"
    mt "Ну и Клэр еще..."
    customer7 "Ладно... Раз не хочешь танцевать, тогда хоть выпить нам принеси..."
    mt "Нахал! Может плюнуть ему в коктейль?"
    customer7 "Неси пару лонг-дринков! И покрепче!!"
    # уходит - приносит
    m "Пожалуйста, ваши коктейли!"
    customer7 "Умница, детка!"
    customer7 "Хочешь чаевых?"
    m "..."
    customer7 "Ну-ка, наклонись вперед!"
    customer7 "Я положу пару баксов тебе и твоим малышкам!"
    # Моника злобно смотрит
    m "..."
    menu:
        "Нет!":
            m "Оставь свои пару баксов себе!"
            m "Похоже, тебе они нужнее."
            customer7 "Эй, полегче!"
            customer7 "За такой сервис и цента не оставлю!"
            mt "Да пошли вы, два придурка!"
            mt "Уроды!"
            mt "!!!"
            # уйходит без чаевых
            pass
        "Сделать, как просят клиенты!":
            mt "Черт!"
            mt "Лишние деньги мне не помешают..."
            # Моника боязливо оглядывается, чтобы никто этого не увидел
            # наклоняется вперед, выставляя грудь на показ
            m "Быстрее!"
            customer7 "Отличные сиськи!"
            # засовывает деньги Монике между грудями
            customer7 "Держи, детка!"
            customer7 "Вот твои $ 5!"
            $ add_tips(5.0)
            customer7 "За шикарные королевские сиськи!"
            customer7 "Аха-ха!!!"
            mt "!!!"
            pass
    mt "Все так и норовят облапать меня!"
    mt "Почему меня, такую красивую и хорошую женщину..."
    mt "Окружают одни извращенцы!"
    mt "!!!"
    return

label customer9_afterbattle:
    m "Здравствуйте."
    m "Что будете заказывать?"
    customer9 "Ну здравствуй, горячая королевская киска!"
    customer9 "Я рад, что ты ко мне подошла."
    customer9 "Сегодня я принес тебе подарочек! Хочешь его получить?"
    customer9 "Присаживайся к Санте на колени."
    mt "К черту такого Санту!"
    m "Мне не нужен ваш подарок!"
    customer9 "Ладно, сегодня Санта добрый..."
    customer9 "Поэтому эта проказница все равно получит то, что принес ей Санта."
    # клиент показывает у себя в руках кружевные трусики
    m "Трусы?!"
    customer9 "Я хотел забрать твои трусики, когда ты выступала..."
    customer9 "Надеялся, ты кинешь их мне..."
    customer9 "Мммм... Трусики с твоей горячей киски..."
    mt "Фу! Грязный извращенец!!!"
    customer9 "Но не вышло..."
    customer9 "Поэтому я решил, что ты можешь поносить эти трусики для меня."
    customer9 "А я буду их нюхать и облизывать вечерами. И дрочить на них. Хе-хе!"
    customer9 "Ну как? Тебе нравится моя идея?"
    mt "!!!"
    mt "КАК ТАКОЕ ВООБЩЕ МОЖЕТ НРАВИТСЯ!?!?!"
    m "Я не буду этого делать!"
    m "Сам носи эти трусики и дро... И делай с ними, что хочешь!"
    customer9 "А если я заплачу тебе $ 50 за это?"
    customer9 "Ты их поносишь немного, а потом отдашь мне."
    customer9 "Что скажешь?"
    m "..."
    menu:
        "Отказаться!":
            m "Я уже сказала нет! Но могу повторить еще раз. НЕТ!"
            mt "Грязное животное!"
            customer9 "Горячая киска растроила Санту..."
            customer9 "Проваливай!"
            customer9 "Плохая киска!"
            # Моника уходит
            return
        "$ 50?":
            mt "У меня сейчас такое тяжелое положение... Каждый доллар на счету."
            mt "О, Боже!"
            mt "На какие ужасные вещи мне приходится идти, чтобы заработать!"
            mt "!!!"
            mt "Хм... А что, если..."
            mt "..."
            m "Я надену их только за $ 5 000!"
            customer9 "Эй! Эти трусы стоят 6 баксов! Откуда такие цены?!"
            m "А как ты хотел? Вообще-то, Я - Королева Shiny Hole!"
            m "!!!"
            customer9 "$ 200!"
            m "$ 4 000 и ни центом меньше!"
            customer9 "Я подумаю над этим предложением, детка..."
            # Моника уходит
            mt "Такая шикарная женщина, как Я, тебе не по карману!"
            mt "Неудачник!"
            return
    return

label customer10_afterbattle:
    m "Здравствуйте. Что будете заказывать?"
    customer10 "Моя Виолетта пришла поздоровоться?"
    customer10 "Или ты хочешь узнать, как мне твое выступление на сцене?"
    mt "Мне все равно, что думает об этом такой извращенец, как ты!"
    mt "!!!"
    customer10 "Не переживай, мне понравилось..."
    customer10 "А знаешь, что мне понравится еще больше?"
    customer10 "Если ты сейчас же запрыгнешь на этот пилон... Или на меня."
    m "!!!"
    m "Я не собираюсь танцевать!"
    customer10 "А я слышал, что танцуешь..."
    customer10 "И не только..."
    m "!!!"
    customer10 "Можем пойти в гримерку..."
    customer10 "Я намажу тебя маслом для выступления на сцене..."
    customer10 "Я хорошо промажу все твои формы."
    mt "Мерзавец! Как он смеет так со мной говорить!? "
    m "Если вы хотите сделать заказ на еду или выпивку, то я вас слушаю."
    m "В противном случае - я ухожу!"
    customer10 "Ты не в настроении что-ли?"
    customer10 "Так бы и сказала, что в следующий раз..."
    mt "Никакого следующего раза не будет!"
    customer10 "Сейчас принеси мне вискаря, а я посмотрю на твою задницу..."
    customer10 "А вечером буду представлять, как ты трешься ею об меня..."
    customer10 "И дрочить. Аха-ха!"
    mt "Он думает мне должно это нравится?!"
    mt "Это звучит омерзительно!"
    # уходит приходит
    m "Ваш заказ..."
    customer10 "Ага... Молодец..."
    customer10 "Дай я отблагодарю тебя своим горячим поцелуем, Виолетта!"
    mt "Фу! Нет!"
    mt "!!!"
    # Моника корчит моську отвращения
    customer10 "Или ты можешь подарить мне свой королевский поцелуй сама!"
    customer10 "$ 20 - достаточная цена королевы Shiny Hole?!"
    menu:
        "Нет!":
            m "Королевский поцелуй может подарить лишь [monica_pub_name]!"
            m "Она новая королева Shiny Hole!"
            m "А Виолетта не дарит королевские поцелуи!"
            m "Даже за $ 1 000!"
            customer10 "Овца!"
            mt "УРОД!"
            return
        "Эти $ 20 не будут лишними...":
            mt "Целовать это мерзкое существо..."
            mt "Фу! Он омерзителен мне!"
            mt "Но эти $ 20 не будут лишними..."
            # клиент тянеся губами к Монике
            m "Но только королевский поцелуй в щеку..."
            customer10 "На пилоне с голой жопой значит..."
            customer10 "А поцелуй, как от монашки?"
            customer10 "Такое кидалово и $ 5 не стоит, Виолетта!"
            customer10 "Давай королевский засос прямо в губы..."
            mt "Фу!"
            m "НЕТ!"
            customer10 "Тогда свободна!"
            return
    mt "Этот район кишит извращенцами и отбросами..."
    mt "Ненавижу их всех!"
    mt "!!!"
    return

label customer11_afterbattle:
    m "Здравствуйте. Готовы сделать заказ?"
    customer11 "Неужели! Наконец-то!"
    customer11 "Изволила подойти!"
    customer11 "Ты королева или официантка?!"
    customer11 "Видишь, что гость сидит?!"
    customer11 "Это значит, что нужно тащить свою задницу и принимать заказ!"
    # Мон злится
    mt "Похоже, в этом пабе собрались все хамы города..."
    customer11 "Неси мне... Знаешь что... Хммм..."
    # рука клиента заныривает под юбку Моники сзади
    mt "ОН ЧТО!!"
    mt "ЛАПАЕТ МЕНЯ!?!?!"
    menu:
        "Промолчать.":
            mt "Врезать бы ему!!!"
            mt "Как он посмел лапать МЕНЯ?!"
            mt "?!?!?!"
            mt "Так, Моника, спокойно!"
            mt "Теперь, когда я зарабатываю больше, я не могу потерять этот источник дохода!"
            mt "Просто сделай вид, что ничего не происходит..."
            m "Вы готовы сделать заказ?"
            customer11 "Так ты королева или официантка?"
            m "Теперь я Королева Shiny Hole!"
            customer11 "А киска у тебя тоже королевская?"
            customer11 "Хочу поверить..."
            customer11 "Сколько стоит свидание с твоей киской?"
            m "..."
            menu:
                "$ 100!":
                    mt "Он уже видел меня полностью голой со сцены..."
                    mt "И извращенка Эшли следит, чтобы я выслуживалась перед клиентами!"
                    m "$ 100 чтобы посмотреть!"
                    customer11 "Даааа... Цены у тебя королевские!"
                    customer11 "Я дам $ 20!"
                    menu:
                        "Да.":
                            pass
                        "Нет!":
                            mt "Иди в жопу, придурок!"
                            mt "!!!"
                            # уходит
                            return
                    m "$ 20 и ни центом меньше!"
                    customer11 "Договорились!"
                    customer11 "Показывай свою подружку..."
                    # Моника оглядывается, поверяет что никто не смотрит
                    # покзывает киску, приспуская трусики (быстро) спереди
                    customer11 "А сколько стоит лизнуть ее?"
                    m "Нисколько!!!"
                    m "Можно только смотреть!!!"
                    m "!!!"
                    customer11 "Тогда неси мне пива..."
                    customer11 "От ее вида у меня все пересохло во рту..."
                    customer11 "Горячая королевская киска!"
                    mt "Извращенец!"
                    # уходит приходит
                    m "Ваш заказ..."
                    customer11 "Как захочешь еще что-то показать, тащи сюда свой зад..."
                    customer11 "А сейчас брысь!"
                    $ add_tips(20.0)
                    # оплата
                    mt "Фу! Мерзость! И эти ужасы я должна терпеть!"
                    mt "!!!"
                    return
                "Нисколько!":
                    mt "Я больше не могу это терпеть!"
                    m "Свидание с моей к... Кхм..."
                    # клиент лезет к ней рукой, Моника отстраняется
                    m "Уберите свои руки!"
                    m "И делайте уже заказ, если вообще собирались его делать!"
                    customer11 "Проваливай! Грубиянка!"
                    customer11 "Не порть мне вечер!"
                    customer11 "Пошла вон!"
                    mt "Иди в жопу, придурок!"
                    mt "!!!"
                    return
    mt "Грубиян!"
    mt "Мерзкое инстинктивное животное!"
    mt "!!!"
    return


label customer12_afterbattle:
    # кадр на клиента. Он свистит и подзывает рукой
    customer12 "Эй ты! Тащи свои королевские сиськи сюда!"
    m "Меня зовут [monica_pub_name]."
    m "А не сис... Кхм..."
    m "Вы хотели сделать заказ?"
    customer12 "Нет. Хотел посмотреть на твои сиськи... Аха-ха!"
    m "Или делайте заказ или я ухожу!"
    customer12 "Ха! Я и жопу твою зацену, когда уходить будешь!"
    m "Я ухожу!"
    mt "Грубиян!"
    customer12 "Подожди! Я сделаю заказ!"
    customer12 "Хочу еще раз посмотреть на твои сиськи, когда ты принесешь мой заказ..."
    customer12 "Ну-ка! Давай быстро, как козочка, спрыгай мне за пивом!"
    mt "Грязное отродье!"
    mt "Обращается со мной, как с дешевкой какой-то!"
    mt "!!!"
    # уходит-приходит с пивом
    m "Ваш заказ."
    mt "Идиот!"
    customer12 "Спасибо! Отличные королевские сиськи! Аха-ха!"
    m "До свидания!"
    customer12 "Подожди!"
    customer12 "А жопа такая же королевская?"
    customer12 "А знаю... Ты же тут ничего бесплатно не делаешь..."
    customer12 "$ 20 устроит?"
    m "..."
    menu:
        "Нет!":
            mt "Для тебя ни за какие деньги на свете!"
            m "Я обнажаюсь только на сцене..."
            m "И только для танца!"
            customer12 "Цену набиваешь?"
            customer12 "Ну тогда я отсюда посмотрю на твой зад!"
            customer12 "Свободна!"
            # Моника злится
            pass
        "Мне нужны деньги...":
            mt "Теперь для меня даже $ 20 - большие деньги..."
            m "Я не стану ее оголять..."
            customer12 "А я и не просил..."
            customer12 "Но теперь подумаю об этом! Аха-ха!"
            # Моника оглядывается что никто не смотрит
            # Задирает юбку сзади
            # Клиент оттягивает трусы Моники  и они отстреливают ей по попе
            # Моника отпрыгивает
            m "Мерзавец!"
            mt "!!!"
            customer12 "Грубиянка!"
            pass
    customer12 "Грубиянки не получают чаевые! Аха-ха!"
    # клиент смеется
    # Моника злится
    mt "Сволочь! Он обманул меня!"
    mt "Он оставил меня без чаевых!"
    mt "Пусть в следующий раз сам себя обслуживает!"
    mt "Когда этот кошмар уже закончится?!"
    mt "?!?!?!"
    return
