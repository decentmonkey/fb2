default photoshoot4_count = 0

label ep22_photoshoot4:
    $ shotsAmount = PS4_shots_amount
    $ shotsTotalAmount = 21

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True


    # переоделась
    img 8840
    img 8841


    label tempaaa1:
        #кадр
        img 8842
        #up
        img 8843
        #side
        img 8844
        #down
        img 8845

        #кадр
        img 8846
        #up
        img 8847
        #side
        img 8848
        #down+
        img 8849


        #кадр
        img 8850
        #up
        img 8851
        #side
        img 8852
        #down
        img 8853

        #кадр
        img 8854
        #up
        img 8855
        #side
        img 8856
        #down
        img 8857

        #кадр+ кладет руку на грудь
        img 8858
        #up
        img 8859
        #side
        img 8860
        #down+
        img 8861

        #кадр
        img 8862
        #up
        img 8863
        #side
        img 8864
        #down+
        img 8865

        #кадр
        img 8866
        #up
        img 8867
        #side
        img 8868
        #down+
        img 8869

        #кадр
        img 8870
        #up
        img 8871
        #side
        img 8872
        #down+
        img 8873



        #кадр - жесткая поза
        img 8874
        #up
        img 8876
        #side
        img 8875
        #down+
        img 8877
        img 8878



    music Stealth_Groover
    img 8879
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 8880
    mt "Что теперь?"
    #Если кастинг у Бифа

    return

label ep23_photoshoot4_casting:
    music Groove2_85
    sound highheels_short_walk
    img 9470
    with fadelong
    w
    img 9471
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."

    img 9472
    $ add_char_progress("Biff", PS4_BiffProgressCasting, "PS4_BiffProgressCasting_day" + str(day))
    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 9473
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 9474
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Роза Надежды..."
            $ add_char_progress("Biff", PS4_BiffProgressCastingChick, "PS4_BiffProgressCastingChick_day" + str(day))
            biff "Что Роза Надежды хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 4
            call ep22_casting()
            img 9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 9475
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 4
            $ chickMode = False
            call ep22_casting()
            img 9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
