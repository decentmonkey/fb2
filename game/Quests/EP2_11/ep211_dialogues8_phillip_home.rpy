default monicaShlut1PhillipBlowjob1 = False  # Моника согласилась на блоуджоб Филиппу со шлюхой номер 1
default monicaShlut1PhillipBlowjob2 = False  # Моника делала минет Филиппу со шлюхой номер 1

# если у Филиппа шлюха номер 1 и Моника оказалась на улице
# при выборе пункта 'Мне нужны эти деньги' в диалоге со шлюхой номер 1 (ep210_dialogues2_escort_start_Phillip_13)
# улица возле дома Филиппа
label ep211_dialogues7_Phillip_home_1:
    # Моника разговаривает с субботней шлюхой номер 1
    mt "Он платит этой шлюхе 200 долларов!"
    mt "А мне - какие-то жалкие 100!"
    mt "Мне! Самой красивой женщине этого города!!!"
    mt "!!!"
    menu:
        "Почему $ 50?!":
            pass
    m "А почему только 50 долларов?!"
    m "Если я тебе и буду помогать, то только за $ 100!"
    whore_number_1 "Если бы я тебе это не предложила..."
    whore_number_1 "Ты бы вообще сегодня осталась без заработка!"
    whore_number_1 "50 баксов и ни центом больше!"
    mt "Жадная сучка!"
    mt "!!!"
    whore_number_1 "Тем более, от тебя ничего сверхъестественного не требуется..."
    whore_number_1 "Поможешь отсосать у него и все."
    m "А зачем тебе моя помощь?"
    m "Сама не справляешься?"
    whore_number_1 "Я думаю, что ему понравится..."
    whore_number_1 "Это внесет немного разнообразия."
    whore_number_1 "И, возможно, он заплатит мне больше..."
    mt "Да как эта дешевая шлюха смеет предлагать мне такое?!"
    mt "То что она предлагает сделать - грязно и мерзко..."
    mt "Она что, думает что я соглашусь на подобное?"
    mt "..."
    mt "С другой стороны, я заработаю $ 50."
    mt "И, может быть, этот мерзавец Филипп станет платить и мне больше денег тоже..."
    whore_number_1 "Ну что? Пойдем?"
    menu:
        "А если об этом кто-то узнает?!":
            pass
    mt "Черт!"
    m "А об этом никто не узнает?"
    whore_number_1 "Не узнает."
    whore_number_1 "Я никому не рассказываю о своей подработке у Филиппа."
    whore_number_1 "Пошли."
    $ monicaShlut1PhillipBlowjob1 = True # Моника согласилась на блоуджоб Филиппу со шлюхой номер 1
    # заходят в дом Филиппа
    return


# Моника зашла в гостиную Филиппа со шлюхой номер 1, согласившись помочь ей удовлетворить его
label ep211_dialogues7_Phillip_home_2:
    mt "Мне даже думать противно о том, что мне предстоит сейчас сделать..."
    mt "Чтобы заработать какие-то жалкие 50 долларов."
    menu:
        "Двойной минет.":
            return
        "Групповой секс. (в следующем обновлении)":
            return
    return

# если выбран пункт 'Двойной минет'
label ep211_dialogues7_Phillip_home_3:
    call check_skip_scene("ep211_dialogues7_Phillip_home_2")
    if _return == True:
        return True
    # Филипп сидит на диване перед телеком, Моника и шлюха стоят перед ним
    philip "Почему так долго?"
    philip "И что здесь делает субботняя шлюха номер 2?"
    philip "Я велел этой шлюхе приходить ко мне через неделю..."
    philip "А субботняя шлюха номер 1 давно уже должна держать во рту мой член."
    mt "Козел!!!"
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
        "Промолчать.":
            pass
    # Моника стоит перед ним в нерешительности, шлюха номер 1 ведет себя с Филиппом уверенно
    m "..."
    whore_number_1 "Я решила устроить тебе небольшой сюрприз..."
    whore_number_1 "Если ты, конечно, не против."
    philip "Не люблю сюрпризы."
    philip "Что ты там придумала?"
    whore_number_1 "Я думаю, тебе понравится..."
    # шлюха номер 1 подходит к Филиппу, садится перед ним на колени, достает его член
    philip "А шлюха номер 2 будет стоять и смотреть?"
    philip "Это и есть твой сюрприз, шлюха номер 1?"
    whore_number_1 "Она тоже будет сосать твой член."
    philip "Я не собираюсь ей за это платить."
    whore_number_1 "Она сегодня сделает это за бесплатно."
    whore_number_1 "Я попросила ее сделать это."
    mt "Фу! Это так мерзко!"
    mt "!!!"
    mt "И как мы будем делать это вдвоем?!"
    # облизывает его член и поворачивается к Монике
    whore_number_1 "Иди сюда..." # и снова принимается за работу
    mt "..."
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            mt "Я не могу пойти на это!"
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            return False
        "Сделать Филппу минет вместе с шлюхой номер 1.":
            $ monicaShlut1PhillipBlowjob2 = True # Моника делала минет Филиппу со шлюхой номер 1
            pass
    # Моника смотрит на то, как шлюха номер 1 облизывает член
    mt "Ненавижу этого мерзавца!"
    mt "!!!"
    # подходит к нему и нерешительно садится рядом со шлюхой
    # тот, откинувшись на диван, самодовольно ухмыляется и смотрит на своих шлюх
    philip "Уверен, что идея с сюрпризом принадлежала не шлюхе номер 2..."
    philip "Она вряд ли додумалась бы до такого..."
    philip "Субботняя шлюха номер 1 молодец."
    philip "Она старается сделать мне приятное."
    philip "Шлюха номер 2, чего ты ждешь? Приступай!"
    # Шлюха рукой наклоняет голову Моники
    # Моника начинает тоже его облизывать
    mt "Это так... Грязно..."
    mt "Не могу поверить, что я делаю это."
    # сама продолжает, одна берет член в рот и двигает головой, вторая облизывает мошонку (Моника)
    # Шлюха продолжает рукой направлять Монику
    philip "Ммммм..."
    philip "Как же мои субботние шлюхи стараются..."
    philip "Даааа... Вот так..."
    philip "Шлюхи готовы за деньги сделать все..."
    philip "Ммммм..."
    philip "А теперь мои субботние шлюхи поменяются местами."
    # Моника стоит на коленях, вытирая губы недовольно
    # Шлюха смотрит на Филиппа, на Монику, затем берет и рукой направляет голову Моники Филиппу на член.
    # теперь Моника сосет, а шлюха облизывает его
    # Шлюха рукой заставляет Монику взять член очень глубоко. (Можно даже применить морф горла, в blowjob что-то там, в быстром меню)

    philip "Даааа..."
    philip "Еще... Еще..."
    philip "Вот так..."
    philip "Аааа..."
    philip "Аааааааа..."
    philip "ААААААА!!!" # кончает им на лица-?
    # Моника и шлюха номер 1 отстраняются от него, Моника брезгливо вытирает рот
    whore_number_1 "Ну как тебе мой сюрприз?" # игриво
    philip "Молодец, шлюха номер 1. Хорошая идея..."
    philip "Вот, держи 400 долларов."
    mt "400?! Он дал ей 400 долларов?!"

#    mt "Хочу забрать деньги и уйти отсюда."
#    mt "И забыть об этом поскорее!"
#    mt "Ни за что не соглашусь еще раз на подобное извращенство!"
    # Филипп дает деньги шлюхе номер 1
    philip "Это твой сегодняшний заработок."
    philip "Субботняя шлюха номер 1 может забрать свои деньги."
    philip "А субботняя шлюха номер 2 недостаточно старалась..."
    philip "Тем более, сегодня не ее очередь получать деньги."
    philip "Поэтому она сегодня ничего не заработала."
    mt "!!!"
    menu:
        "Почему я ничего не заработала?!":
            m "Филипп, я делала тоже самое, что и она!"
            m "Почему я не заработала денег?!"
            m "?!?!?!"
            # смотрит на нее
            philip "???"
            philip "Моей субботней шлюхе номер 2 нужны деньги?"
            philip "Приходи через неделю."
            # отворачивается
            mt "Вот мерзавец!!!"
            mt "Жадный ублюдок!!!"
            return True
        "Уйти.":
            pass
    philip "Можете идти."
    mt "Сволочь!"
    mt "!!!"
    # шлюха номер 1 забирает деньги и они уходят
    return

# улица возле дома Филиппа после двойного блоуджоба
label ep211_dialogues7_Phillip_home_4:
    # Моника разговаривает с субботней шлюхой номер 1
    m "Это было мерзко!"
    m "!!!"
    whore_number_1 "Зато мы заработали денег."
    whore_number_1 "Вот твои 50 баксов, как и договаривались..."
    # дает ей деньги
    m "Это несправедливо! Он дал тебе 400!!!"
    whore_number_1 "Ты сама согласилась сделать это за 50 баксов!"
    whore_number_1 "Тебя никто не заставлял!"
    mt "Сучка!!!"
    mt "!!!"
    whore_number_1 "Все, мне пора."
    whore_number_1 "До встречи."
    # шлюха 1 уходит
    return


# мысли Моники после двойного блоуджоба, шлюха 1 отдала ей 50 баксов и ушла
label ep211_dialogues7_Phillip_home_5:
    # не рендерить!
    mt "Почему этот мерзавец Филипп платит любой другой дешевой шлюхе меньше чем мне?!"
    mt "!!!"
    mt "Я заставлю пожалеть мерзавца Филиппа об этом!"
    mt "Он еще будет умолять меня о прощении!"
    mt "Ненавижу!!!"
    mt "!!!"
    return
