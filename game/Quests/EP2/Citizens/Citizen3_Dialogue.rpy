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
                                            citizen3 "А ты как думаешь? Конечно Найджел, но не переживый, как только ты произесешь пароль, он сразу все поймет."
                                            call reduce_flyers() from _call_reduce_flyers_3
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
