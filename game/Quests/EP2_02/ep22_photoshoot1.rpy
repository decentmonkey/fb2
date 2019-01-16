label ep22_photoshoot1:
    img 8317
    with fade
    m "Алекс, я уже снималась в этом платье..."
    img 8318
    alex_photograph "Мистер Биф сказал одеть его!"
    "Вы всем очень понравились на благотворительном вечере!"
    "Публика хочет еще Ваших фотографий в этом платье!"

    $ shotsAmount = PS1_shots_amount
    $ shotsTotalAmount = 24
#    music Molten_Alloy_low
    music stop

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    img 8319
    with fadelong
    label ep22_photoshoot1_pose1:
        # кадр
        img 8319
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8323
            with fadelong
            jump ep22_photoshoot1_pose2
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot1_pose1
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8320
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose1
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8321
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose1
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8322
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose1

    label ep22_photoshoot1_pose2:
        # кадр
        img 8323
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8327
            with fadelong
            jump ep22_photoshoot1_pose3
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot1_pose2
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8324
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose2
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8325
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose2
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8326
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose2

    label ep22_photoshoot1_pose3:
        # кадр
        img 8327
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8330
            with fadelong
            jump ep22_photoshoot1_pose4
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot1_pose3
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8535
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose3
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8328
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot1_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS1_monica_shot1_corruption_required)
                jump ep22_photoshoot1_pose3
            w
            $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot1_progress")
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose3
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8329
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose3


    label ep22_photoshoot1_pose4:
        # кадр
        img 8330
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8334
            with fadelong
            jump ep22_photoshoot1_pose5
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot1_pose4
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8331
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose4
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8332
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose4
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8333
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot2_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS1_monica_shot2_corruption_required)
                jump ep22_photoshoot1_pose4
            w
            $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot2_progress")
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose4


    label ep22_photoshoot1_pose5:
        #кадр
        img 8334
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8338
            with fadelong
            jump ep22_photoshoot1_pose6
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot1_pose5
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8335
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose5
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8336
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot3_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS1_monica_shot3_corruption_required)
                jump ep22_photoshoot1_pose5
            w
            $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot3_progress")
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose5
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8337
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose5


    label ep22_photoshoot1_pose6:
        #кадр
        img 8338
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8342
            with fadelong
            jump ep22_photoshoot1_pose7
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot1_pose6
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8339
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose6
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8340
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot4_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS1_monica_shot4_corruption_required)
                jump ep22_photoshoot1_pose6
            w
            $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot4_progress")
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose6
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8341
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose6


    label ep22_photoshoot1_pose7:
        #кадр
        img 8342
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8346
            with fadelong
            jump ep22_photoshoot1_pose8
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot1_pose7
        #up+
        if result == "up":
            sound camera_lens1
            $ photoImage = 8343
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot5_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS1_monica_shot5_corruption_required)
                jump ep22_photoshoot1_pose7
            w
            $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot5_progress")
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose7
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8344
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose7
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8345
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose7


    label ep22_photoshoot1_pose8:
        #кадр
        img 8346
        if shots == 0 or shotsAmount == 0:
            return
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot1_pose8
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8347
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose8
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8348
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose8
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8349
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot6_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS1_monica_shot6_corruption_required)
                jump ep22_photoshoot1_pose8
            w
            $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot6_progress")
            call photoshoot_flash_count()
            $ PS1_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot1_pose8

    return

label ep22_photoshoot1_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot

    music Stealth_Groover
    img 6632
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 6631
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            $ biffMonicaLastCastingSkipped = True

            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if biffMonicaCastingsEnabled == True and corruption > photoshoot1_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            "..."
            "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call ep22_photoshoot1_casting()
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot1_casting_corruption_required]) (disabled)" if biffMonicaCastingsEnabled == False or corruption < photoshoot1_casting_corruption_required:
            pass

return

label ep22_photoshoot1_casting:
    music Groove2_85
    sound highheels_short_walk
    img 8436
    with fadelong
    w
    img 8437
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."
    $ add_char_progress("Biff", PS1_BiffProgressCasting, "PS1_BiffProgressCasting_day" + str(day))
    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 8439
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 8440
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Моника Бакфетт с благотворительного вечера..."
            $ add_char_progress("Biff", PS1_BiffProgressCastingChick, "PS1_BiffProgressCastingChick_day" + str(day))
            biff "Что Моника Бакфетт хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 1
            call ep22_casting()
            img 8446
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                img 8439
                with fade
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 8438
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
                #
            biff "И что цыпочка будет делать?"
            $ castingCloth = 1
            $ chickMode = False
            call ep22_casting()
            img 8446
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return

label photoshoot_flash_count:
    call photoshop_flash()
    $ shotsAmount -= 1
    $ shots -= 1
    return

label corruption_required(required1):
#    $ notif(str(required1) + __(" corruption required!"))
    empty "[required1] corruption required!"
    return
