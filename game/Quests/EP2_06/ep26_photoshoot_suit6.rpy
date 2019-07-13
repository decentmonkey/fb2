label ep26_photoshoot_suit6:
    img 20001
    m "Что это, Алекс?"
    # Что это?
    img 20002
    m "Это что, называется костюм для съемок?"
    # Это что, называется костюм для съемок?
    img 20003
    # А это что такое?
    m "А это что такое?"
    img 20004
    # Миссис Бакфетт, это реквизит и тд
    alex_photograph "Миссис Бакфетт, этот костюм называется Алая Жемчужина"
    alex_photograph "А этот реквизит олицетворяет раковину, в которой находится изысканная жемчужина!"
    alex_photograph "Это будет замечательная сцена, Миссис Бакфетт!"
    img 20005
    # И что мне делать на этой кушетке?
    m "И что мне делать на этой... раковине?"
    img 20006
    # Проходить фотосессию
    alex_photograph "Миссис Бакфетт, Вам надо принимать различные позы."
    alex_photograph "Читателям должно понравиться то, как Вы будете выглядеть!"

    img 20007
    # Ладно, Алекс!
    # Только на этот раз без пошлых поз!
    m "Ладно, Алекс."
    m "Только на этот раз без пошлых поз!"

    img 20008
    alex_photograph "Конечно, Миссис Бакфетт! Все будет очень прилично, как обычно!"
    alex_photograph "Итак, мотор!"

    #кадр
    img 20009
    # up
    img 20011
    # side
    img 20010
    # down
    img 20012

    # кадр
    img 20013
    # up
    img 20014
    # side
    img 20015
    # down
    img 20016

    # кадр +
    img 20017
    # up
    img 20019
    # side
    img 20018
    # down
    img 20020

    # кадр
    img 20021
    # up
    img 20022
    # side +
    img 20024
    # down
    img 20023

    # кадр
    img 20025
    # up
    img 20026
    # side
    img 20027
    # down
    img 20028

    # кадр
    img 20029
    # up
    img 20030
    # side
    img 20031
    # down
    img 20032

    # кадр
    img 20033
    # up
    img 20034
    # side
    img 20035
    # down +
    img 20036

    # кадр
    img 20037
    # up
    img 20038
    # side
    img 20039
    # down +
    img 20040

    # кадр
    img 20041
    # up
    img 20042
    img 20043
    # side
    img 20044
    img 20045
    # down +
    img 20046
    img 20047

    # кадр
    img 20048
    # up
    img 20049
    img 20050
    img 20051
    # side
    img 20052
    img 20053
    img 20054
    # down+
    img 20055
    img 20056
    #+
    img 20057
    img 20058
    img 20059

    # кадр +
    img 20060
    # up
    img 20061
    img 20062
    img 20063
    # side
    img 20064
    img 20065
    img 20066
    # down +
    img 20067
    img 20068
    img 20069
    #+
    img 20070
    img 20071


    img 20072
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 20073
    with fade
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            $ biffMonicaLastCastingSkipped = True
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if biffMonicaCastingsEnabled == True and corruption >= photoshoot4_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call ep26_photoshoot5_casting()
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot6_casting_corruption_required]) (disabled)" if biffMonicaCastingsEnabled == True and corruption < photoshoot6_casting_corruption_required:
            pass


label ep26_photoshoot6_casting:
    music Groove2_85
    sound highheels_short_walk
    img 20176
    with fadelong
    w
    img 20177
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."

    img 20178
    $ add_char_progress("Biff", PS6_BiffProgressCasting, "PS6_BiffProgressCasting_day" + str(day))
    $ shotsAmountCompleted = len(list(set(PS6_shoots_array)))
#    $ shotsTotalAmount

    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 20179
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 20180
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Алая Жемчужина..."
            $ add_char_progress("Biff", PS6_BiffProgressCastingChick, "PS6_BiffProgressCastingChick_day" + str(day))
            biff "Что Алая Жемчужина хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 6
            call ep22_casting()

            img 20183 #9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 20182 #9475
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 6
            $ chickMode = False
            call ep22_casting()
            img 20183 #9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
