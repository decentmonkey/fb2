label ep22_photoshoot1:
    img 8317
    m "Алекс, я уже снималась в этом платье..."
    img 8318
    alex_photograph "Мистер Биф сказал одеть его!"
    "Вы всем очень понравились на благотворительном вечере!"
    "Публика хочет еще Ваших фотографий в этом платье!"

    label ep22_photoshoot1_pose1:
        # кадр
        img 8319
        #up
        img 8320
        #side
        img 8321
        #down
        img 8322

    label ep22_photoshoot1_pose2:
        # кадр
        img 8323
        #up
        img 8324
        #side +
        img 8325
        #down
        img 8326

    label ep22_photoshoot1_pose3:
        # кадр
        img 8327
        #up +
        img 8328
        #side
        img 8329
        #down

    label ep22_photoshoot1_pose4:
        # кадр
        img 8330
        #up
        img 8331
        #side
        img 8332
        #down +
        img 8333

    label ep22_photoshoot1_pose5:
        #кадр
        img 8334
        #up
        img 8335
        #side +
        img 8336
        #down
        img 8337

    label ep22_photoshoot1_pose6:
        #кадр
        img 8338
        #up
        img 8339
        #side +
        img 8340
        #down
        img 8341

    label ep22_photoshoot1_pose7:
        #кадр
        img 8342
        #up +
        img 8343
        #side
        img 8344
        #down
        img 8345

    label ep22_photoshoot1_pose8:
        #кадр
        img 8346
        #up
        img 8347
        #side
        img 8348
        #down +
        img 8349


    label ep22_photoshoot1_end:
        img 6632
        alex_photograph "Мэм! Мы закончили фотосессию!"
        m "Наконец-то!!!"
        img 6631
        mt "Что теперь?"
        #Если кастинг у Бифа
        menu:
            "Переодеться назад...":
                call ep22_dialogue6_6()
                $ biffMonicaLastCastingSkipped = True
            "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)": #если есть кастинги
                mt "Биф ждет меня на свой дурацкий кастинг..."
                "Он говорил даст мне работу если я буду хорошей цыпочкой..."
                "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
                "Так может быть притвориться?"
                "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
                #если обещала
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot1_casting_corruption_required]) (disabled)"

    return

label ep22_photoshoot1_casting:
    img 8436
    w
    img 8437
    m "Привет, Биф. Я пришла..."
    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 8439
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 8440
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Моника Бакфетт с благотворительного вечера..."
            biff "Что Моника Бакфетт хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 1
            call ep22_casting()
            img 8446
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            img 8439
            m "Я пришла, потому что обещала хорошо вести себя..."
            #иначе
            img 8438
            m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            #
            biff "И что цыпочка будет делать?"
            $ castingCloth = 1
            $ chickMode = False
            call ep22_casting()
            img 8446
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
