default monicaShlut1PhillipThreesome1 = False  # Моника делала куни шлюхе № 1 по приказу Филиппа
default monicaShlut1PhillipThreesome2 = False  # Моника согласилась на ass to mouth



# если у Филиппа шлюха номер 1 и Моника оказалась на улице
# при выборе пункта 'Мне нужны эти деньги' в диалоге со шлюхой номер 1 (ep210_dialogues2_escort_start_Phillip_13)
# повторяется их диалог, где шлюха номер 1 обещает ей заплатить 50 баксов за минет Филиппу (ep211_dialogues7_Phillip_home_1)

# Моника зашла в гостиную Филиппа со шлюхой номер 1, согласившись помочь ей удовлетворить его
# возникает меню ep211_dialogues7_Phillip_home_2, где пункт "Групповой секс" доступен

# если выбран пункт "Групповой секс"
label ep212_dialogues4_philip_threesome_1:
    call check_skip_scene("ep211_dialogues7_Phillip_home_2")
    if _return == True:
        return True
    # Филипп сидит на диване перед телеком, Моника и шлюха стоят в гостиной возле двери
    # шлюха номер 1 поворачивается к Монике и на ухо говорит
    whore_number_1 "Слушай, у меня появилась идея..."
    whore_number_1 "Как ты смотришь на то, чтобы заработать побольше?"
    whore_number_1 "Например, баксов 200?"
    # Моника смотрит на нее с подозрением
    m "200 долларов?"
    m "???"
    m "Почему ты решила заплатить в два раза больше?"
    m "Что еще за идея?"
    whore_number_1 "Все просто."
    whore_number_1 "Я тебе плачу 200 баксов, но тогда одним минетом ты не отделаешься..."
    m "Ты имеешь ввиду, заняться сексом? Всем вместе?"
    whore_number_1 "Ага." # довольная своей идеей
    mt "Дъявол!"
    mt "Получается, если я соглашусь заняться сексом, то заработаю больше денег."
    mt "Но мне даже думать об этом противно!"
    mt "Я Моника Бакфетт, а не какая-то проститука, которая готова на все ради денег!!!"
    mt "!!!"
    mt "С другой стороны, об этом ведь никто не узнает..."
    mt "А мне нужны деньги."
    mt "..."
    mt "В прошлый раз мерзавец Филипп заплатил этой вульгарной девке $ 400..."
    mt "В этот раз она готова отдать мне половину своего заработка..."
    mt "Я могу заработать $ 200, либо отказаться и остаться вообще без заработка сегодня."
    whore_number_1 "Ну? Чего ты тормозишь?"
    whore_number_1 "Ты согласна на 200 баксов?"
    # Моника нерешительно
    menu:
        "Об этом точно никто не узнает?":
            pass
    mt "Черт! Что же мне делать?"
    m "Об этом точно никто не узнает?!"
    whore_number_1 "Да точно-точно. Сколько уже можно спрашивать об этом..."
    whore_number_1 "Пошли!"
    # Филипп со скучающим видом обращается к шлюхе номер 1
    philip "Субботняя шлюха номер 1, ты думаешь я плачу тебе деньги за то..."
    philip "Что я должен смотреть, как вы там шепчетесь?!"
    philip "Я долго буду ждать, когда ты начнешь работать?"
    philip "И почему субботняя шлюха номер 2 опять сюда пришла?"
    philip "Шлюха номер 1 опять решила устроить мне сюрприз?"
    whore_number_1 "Да. Я уверена, что тебе понравится..." # игриво
    # Филипп со скучающим видом
    philip "Ну ладно, давай..."
    philip "Что на этот раз?"
    # шлюха номер 1 снимает с себя футболку, проводит по своей груди руками и улыбается игриво Филиппу
    # потом смотрит на Монику и подходит к ней
    mt "Что эта никчемная шлюха задумала?"
    # та трогает Монику за грудь, а Моника на нее зло смотрит
    mt "Какого черта я вообще согласилась на это?!"
    mt "С какой-то там шлюхой?!"
    mt "?!?!?!"
    # шлюха номер 1 снимает платье с Моники и трогает ее при этом
    # потом шлюха номер 1 запускает руку между ног Моники и трогает ее киску
    # Моника возмущенно смотрит на нее, но молчит
    mt "!!!"
    mt "Она не просто шлюха, она еще и лесбиянка! Фи!"
    mt "Ей действительно все это нравится?!"
    mt "Как же все это омерзительно!"
    # Моника стоит голая, Филипп расстегивает брюки и начинает подрачивать свой член
    # шлюха номер 1 убирает руку от киски Моники и говорит ей
    whore_number_1 "А теперь твоя очередь сделать мне приятное..."
    # Моника смотрит на нее непонимающе
    m "Я? Тебе?"
    m "Зачем?"
    whore_number_1 "Филиппу это понравится."
    whore_number_1 "Посмотри на его член. Его это возбуждает."
    m "..."
    menu:
        "Раздеть шлюху номер 1.":
            pass
    mt "Черт!"
    mt "Не могу поверить, что я делаю это..."
    # Моника трогает грудь шлюхи № 1, потом снимает с нее брюки, сидя на корточках перед ней
    # та показывает на свою киску
    whore_number_1 "Теперь поиграй с моей киской своим язычком."
    mt "?!?!?!"
    # Моника возмущенно
    m "Нет, мы так не договаривались."
    m "Я не буду этого делать!"
    m "!!!"
    philip "Шлюха номер 2, молчать!"
    # обе поворачиваются и смотрят на него
    philip "Шлюха номер 2 сейчас же перестанет спорить и полижет шлюху номер 1 между ног."
    philip "Я хочу посмотреть на это..."
    mt "Вот козел!!!"
    mt "!!!"
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            return False
        "Сделать, как требует Филипп.":
            $ monicaShlut1PhillipThreesome1 = True # Моника делала куни шлюхе № 1 по приказу Филиппа
            pass
    # Моника смотрит на киску шлюхи номер 1 в нерешительности
    mt "Долбанные извращенцы!"
    mt "Ненавижу их всех!"
    mt "!!!"
    # Моника начинает лизать киску
    whore_number_1 "Ммммм..."
    whore_number_1 "Как приятно..."
    whore_number_1 "А у тебя хорошо получается, шлюха номер 2..."
    whore_number_1 "Чувствуется, что у тебя уже есть опыт с кисками..."
    whore_number_1 "Ммммм..."
    # немного позже Филипп прерывает их
    philip "Достаточно!"
    philip "Сейчас обе мои шлюхи подойдут ко мне."
    # они подходят, Филипп уже снял одежду (или только брюки и расстегнул рубашку)
    whore_number_1 "Тебе нравится смотреть на нас?"
    philip "Да, еще больше мне понравится, если ты сейчас сядешь на меня, шлюха номер 1..."
    # шлюха номер 1 залезает на Филиппа и садится на его член своей киской
    philip "Нет, не так."
    philip "Сегодня я хочу трахнуть тебя в твою упругую задницу, шлюха номер 1."
    # та делает так, как говорит Филипп и насаживается на его член попой
    philip "Дааа. Вот тааак."
    philip "А шлюха номер 2 сядет рядом с нами и будет держать лицо около моего члена."
    # Моника непонимающе смотрит на него
    mt "???"
    mt "Что за бред?!"
    mt "Что этот извращенец хочет сделать?!"
    philip "Делай, что тебе говорят!"
    # Моника садится рядом так, что ее лицо находится рядом с их причиндалами
    whore_number_1 "Ооооо, как же хорошоооо!"
    whore_number_1 "О, Филипп, я обожаю когда ты во мне!"
    whore_number_1 "Давай, еще!"
    whore_number_1 "Трахай меня!!!"
    whore_number_1 "Ещееее!!!"
    # немного позже шлюха 1 привстает и Филипп говорит Монике
    philip "Открывай свой рот, шлюха номер 2."
    philip "Приглашай мой член войти в него."
    # Моника парится и с отвращением смотрит на его член, который он только что вытащил из попы шлюхи номер 1
    mt "Что?!"
    mt "О, нет!!!"
    mt "Фууу!!!"
    mt "Какая мерзость!!!"
    philip "Ну?!"
    # Моника с отвращением на лице
    m "..."
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            return False
        "Сделать, как требует Филипп.":
            $ monicaShlut1PhillipThreesome2 = True # Моника согласилась на ass to mouth
            pass
    # Моника открывает рот и Филипп засовывает туда свой член
    philip "Соси, шлюха номер 2!"
    # Моника делает несколько движений
    philip "Дааа..."
    philip "Хорошо, хватит."
    # после этого он снова входит в попу шлюхи номер 1
    # это повторяется несколько раз
    philip "Мне нравится, что мои субботние шлюхи стараются для меня..."
    philip "Сегодня субботние шлюхи хорошо работают..."
    # Моника смотрит на все происходящее с отвращением
    mt "Мерзкий грязный извращенец!!!"
    mt "!!!"
    philip "А теперь очередь шлюхи номер 2 быть оттраханной!"
    # он выходит из шлюхи номер 1, они оба встают и смотрят на Монику
    philip "Ложись, подставляй мне свою дырочку..."
    philip "Покажи, как ты хочешь почувствовать мой член внутри себя..."
    m "..."
    menu:
        "Лечь на диван и раздвинуть ноги.":
            pass
    mt "!!!"
    mt "Не могу поверить, что это происходит со мной..."
    # Моника ложится на спину и раздвигает ноги
    philip "Шлюха номер 1, проверь, готова ли шлюха номер 2 принять мой член?"
    philip "Ее отверстие достаточно влажное?"
    # шлюха номер 1 подходит к Монике и вводит в ее киску пальцы
    whore_number_1 "Недостаточно, но я сейчас подготовлю для тебя ее киску."
    # она водит пальцами туда-сюда в киске Монике, Филипп стоит смотрит на это и трется членом о попу шлюхи номер 1
    # та поглядывает на него, улыбается игриво
    whore_number_1 "Теперь она готова принять твой член."
    whore_number_1 "Что ты хочешь, чтобы я еще сделала?"
    philip "Я хочу, чтобы ты села на лицо шлюхи номер 2."
    # шлюха номер 1 садится на лицо Моники
    # Филипп раздвигает ноги Моники шире и входит в нее
    philip "Ммммм..."
    philip "Шлюха номер 1 хорошо подготовила для меня это отверстие."
    philip "Шлюха номер 1 молодец, она старается для меня."
    # шлюха номер 1 елозит у нее по лицу своей киской, трогает свою грудь, игриво смотрит на Филиппа
    whore_number_1 "О, как прикольно!!!"
    whore_number_1 "Даааа...."
    whore_number_1 "Ооооо... Какой каааайф!"
    mt "Скорее бы закончился этот кошмар!"
    mt "Как же это все грязно и мерзко!"
    mt "!!!"
    mt "Моника, никогда бы не подумала, что ты опустишься до подобного!"
    mt "И ради чего?! Из-за 200 долларов?!"
    mt "!!!"
    # Филипп кончает
    menu:
        "Кончить внутрь Моники.":
            philip "Аааа..."
            philip "Аааааааа..."
            philip "ААААААА!!!"
            pass
        "Кончить на киску Моники.":
            philip "Аааа..."
            philip "Аааааааа..."
            philip "ААААААА!!!"
            # Филипп отстраняется от Моники и смотрит на сперму на ее киске
            philip "А теперь я хочу, чтобы шлюха номер 1 слизала это все со шлюхи номер 2."
            # та слезает с лица Моники и выполняет приказ Филиппа, с довольным видом
            whore_number_1 "Ммммм..."
            pass
        "Кончить на грудь Моники.":
            philip "Аааа..."
            philip "Аааааааа..."
            philip "ААААААА!!!"
            # Филипп отстраняется от Моники и смотрит на сперму на ее груди
            philip "А теперь я хочу, чтобы шлюха номер 1 слизала это все со шлюхи номер 2."
            # та слезает с лица Моники и выполняет приказ Филиппа, с довольным видом
            whore_number_1 "Ммммм..."
            pass
    mt "Наконец-то, этот кошмар закончился!"
    mt "!!!"
    return

# после тройничка
label ep212_dialogues4_philip_threesome_2:
    # смена кадра, они уже в одежде
    # в руках у Филиппа деньги
    philip "Шлюха номер 1 снова проявила инициативу и ее идея мне понравилась."
    philip "Я, как и в прошлый раз, доволен ее работой."
    philip "Молодец, шлюха номер 1. Хорошо придумала..."
    philip "Вот, держи 700 долларов."
    # Филипп дает деньги шлюхе номер 1, шлюха стоит довольная
    mt "700?! Он дал ей 700 долларов?!"
    mt "?!?!?!"
    philip "Это твой сегодняшний заработок."
    philip "Субботняя шлюха номер 1 может забрать свои деньги."
    philip "А субботняя шлюха номер 2 недостаточно старалась..."
    philip "Ей учиться надо у шлюхи номер 1, как делать мне приятно."
    mt "!!!"
    philip "Тем более, сегодня не ее очередь получать деньги."
    philip "Поэтому она сегодня ничего не заработала."
    mt "!!!"
    menu:
        "Почему я ничего не заработала?!":
            m "Филипп, я делала все, что ты мне говорил!"
            m "Почему я не заработала денег?!"
            m "?!?!?!"
            # смотрит на нее
            philip "???"
            philip "Моей субботней шлюхе номер 2 нужны деньги?"
            philip "Приходи через неделю."
            # отворачивается
            mt "Вот мерзавец!!!"
            mt "Жадный ублюдок!!!"
            return
        "Уйти.":
            pass
    philip "Можете идти."
    mt "Сволочь!"
    mt "!!!"
    return

# на улице после сцены у Филиппа (диалог такой же, только сумма денег разная)
label ep212_dialogues4_philip_threesome_3:
    # Моника разговаривает с субботней шлюхой номер 1
    m "Это было мерзко!"
    m "!!!"
    whore_number_1 "Зато мы заработали денег."
    whore_number_1 "Вот твои 200 баксов, как и договаривались..."
    # дает ей деньги
    m "Это несправедливо! Он дал тебе 700 долларов!!!"
    whore_number_1 "Ты сама согласилась сделать это за 200 баксов!"
    whore_number_1 "Тебя никто не заставлял!"
    mt "Сучка!!!"
    mt "!!!"
    whore_number_1 "Все, мне пора."
    whore_number_1 "До встречи."
    # шлюха 1 уходит
    return

# мысли Моники после группового секса - ep211_dialogues7_Phillip_home_5
