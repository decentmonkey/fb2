default monicaGotJoint = False
label citizen3_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_3_1
            if monicaGotJoint == True:
                imgr Dial_Citizen_3_4
                citizen3 "Тебе нужно к Найджелу..."
                return
            if citizen3_offered_last_day == day:
                imgr Dial_Citizen_3_4
                citizen3 "В другой раз, я занят!"
                return
            citizen3 "Да, конечно, красотка!"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen3_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
#                    if renpy.random.randint(0, 3) =:
                    imgr Dial_Citizen_3_4
                    citizen3 "Не хочу, мне он не нужен."
                    imgl Dial_Monica_Sandwich_0
                    menu:
                        "Попросить вежливо.":
                            #img Моника спрашивает
                            imgl Dial_Monica_Sandwich_1
                            m "Мистер, пожалуйста, возьмите флаер, Вы меня очень выручите."
                            imgr Dial_Citizen_3_2
                            citizen3 "Хорошо, я помогу тебе в обмен на небольшую услугу."
                            m "Какую еще услугу? Ты всего лишь возьмешь у меня флаер..."
                            citizen3 "Да, и попрошу тебя кое что передать моему другу Найджелу. Он на другой стороне улицы и ты его узнаешь по синему пуховику, в котором он круглый год."
                            imgl Dial_Monica_Sandwich_0
                            m "И что же я должна ему передать?"
                            mt "(Что за ?! )"
                            # citizen3показывает монике косяк
                            imgr Dial_Citizen_3_joint
                            m "Что это? Наркотики?!"
#                            imgr Dial_Citizen_3_3
                            citizen3 "(Шепотом) С каких пор травку слали приравнивать к наркотикам? Она абсолютно легальна. Ну дак что, поможешь мне?"
                            menu:
                                "Ладно.":
                                    m "(Всего несколько метров...)Хорошо, я сделаю это."
                                    #Моника берет косяк и отдает флаер.
                                    $ add_inventory("joint", 1, True)
                                    imgr Dial_Citizen_3_2
                                    citizen3 "Не забудь сказать, что ты от Джека."
                                    m "Хорошо"
                                    citizen3 "Да, и самое главное: Ты должна будешь сказать Найджелу наш пароль, чтобы он понял, что все чисто."
                                    m "Какой еще пароль?"
                                    imgr Dial_Citizen_3_3
                                    citizen3 "Потрогай мою сиську."
                                    imgl Dial_Monica_Sandwich_2
                                    m "(Что за?)"
                                    imgl Dial_Monica_Sandwich_0
                                    menu:
                                        "Черт с ним.":
                                            imgl Dial_Monica_Sandwich_0
                                            m "И у кого хватило ума придумал такой пароль?!"
                                            citizen3 "А ты как думаешь? Конечно Найджел, но не переживай, как только ты произнесешь пароль, он сразу все поймет."
                                            call reduce_flyers() from _call_reduce_flyers_13
                                            m "Ладно, но если ты меня обманываешь..."
                                            #citizen33
                                            imgr Dial_Citizen_3_4
                                            citizen3 "Что ты, детка, зачем мне это?"
                                            $ monicaGotJoint = True
                                            return
                                        "Ну уж нет, это слишком.":
                                            imgl Dial_Monica_Sandwich_2
                                            #злая моника
                                            $ remove_inventory("joint", 1, True)
                                            m "Я не буду говорить такие вещи!"
                                            return
                                "Ну уж нет.":
                                    imgl Dial_Monica_Sandwich_2
                                    m "Ты что, за дуру меня держишь?"
                                    # смена арта у ситизена
                                    imgr Dial_Citizen_3_4
                                    citizen3 "Возвращайся, если передумаешь."
                                    $ kebabWorkMonicaRefusedAmount += 1
                                    return
                        "Попросить настойчиво.":
                            imgl Dial_Monica_Sandwich_1
                            #img Моника спрашивает с недовольным выражением лица.
                            m "Неужели для Вас это так сложно?!."
                            imgr Dial_Citizen_3_4
                            citizen3 "Отвали."
                            imgl Dial_Monica_Sandwich_0
                            mt "(Вот засранец.)"
                            imgr Dial_Citizen_3_2
                            $ kebabWorkMonicaRefusedAmount += 1
#                        call reduce_flyers()
#                        citizen3 "Хорошо."
#                        img Dial_Citizen_3_3
#                        citizen3 "А что на нем? Ваш номер телефона?"
#                        "Вы девочка по вызову?"
#                        label citizen3_loop1:
#                            menu:
#                                "НЕТ!":
#                                    #img Моника злится
#                                    m "НЕТ!"
#                                "В общем нет, но... (disabled)":
#                                    jump citizen3_loop1
#                    else:
#                        img Dial_Citizen_3_3
#                        citizen3 "Я занят! Пожалуйста, не отвлекайте меня!"
        "Уйти.":
            pass
    return

# диалог доступен только когда моника не работает на раздаче флаеров
label citizen3_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_3_1
    m "Привет! Ты меня помнишь?"
    citizen3 "Конечно, помню, тебя сложно забыть."
    m "Могу тебе, кое что показать."
    citizen3 "Детка, ты говоришь о том, что я думаю?"
    imgr Dial_Citizen_3_3
    m "Возможно..."
    citizen3 "У меня много дел, но такое я пропустить не могу."
    # уходят к пилону.
    citizen3 "Ну что, тетя..."
    label .loop3:
    menu:
        "Покажи сиськи.":
            citizen3 "Покажи ка свои сиськи!"
            if corruption < 50:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется 50 corruption"
                jump .loop3
            m "Я не собираюсь раздеваться, только так."
            # img показывает сиськи
            citizen3 "Детка, нет слов! Теперь сними свою курточку."
            m "Ну уж нет."
            citizen3 "Надо же с чего-то начинать..."
            jump .loop3
        "Покажи попу.":
            citizen3 "Детка, повернись ко мне спиной. И покажи свою попку."
            if corruption < 70:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется 70 corruption"
                jump .loop3
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            citizen3 "Детка, ты красотка!"
            jump .loop3
        "Достаточно на сегодня.":
            citizen3 "Ты сделала мой день, отлично потрудилась."
            # дает монике копейку если были показы
            m "Что?! Так мало? Ну ничего, скоро я стану богатой и верну свою жизнь..."
            #если не было
            citizen3 "Похоже, я только зря потратил с тобой время..."
    return
