default questOffendMonicaFlyersCitizen12Started = False
default questOffendMonicaFlyersCitizen12Completed = False

label citizen12_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_12_1
            if citizen12_offered_last_day == day:
                imgr Dial_Citizen_12_4
                citizen12 "Я тороплюсь! Мне некогда!"
                return
            citizen12 "Да, Крошка? Что ты хочешь от меня?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen12_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if questOffendMonicaFlyersCitizen12Started == True:
                        citizen12 "Конечно, крошка, а ты не хочешь ничего у меня взять?"
                        m "Вы это о чем?"
                        citizen12 "Сейчас, я покажу..."
                        img 8484
                        #звук падения тела
                        w
                        img 8485
                        m "Аххх!!!"
                        # img хватает монику за плечи и сажает на колени
                        img 8486
                        m "Что ты себе позволяешь?! Что ты делаешь?"
                        img 8487
                        with fade
                        #звук ширинки
                        citizen12 "Расслабься, уверен, тебе это не впервой."
                        # img ситизен расстегивает ширинку
                        img 8488
                        mt "Черт, из за дурацкой рекламы мне сложно двигаться..."
                        img 8489
                        m "Помогите! Кто-нибудь! Полиция!"
                        img 8490
                        mt "Черт! Какая еще полиция?! Мне нельзя полицию!"
                        img 8491
                        citizen12 "Крошка, сейчас сделаешь мне минет и получишь свои 5 долларов."
                        img 8492
                        w
                        img 8493
                        m "Что ты сказал?! ПОМОГИТЕ, КТО НИБУДЬ!"
                        # img появлятеся citizen6
                        img 8494
                        citizen6 "Что здесь происходит?"
                        img 8495
                        citizen12 "Эй, мужик, иди своей дорогой, или присоединяйся!"
                        img 8496
                        m "Пожалуйста, помогите мне! Я не шлюха!"
                        img 8497
                        citizen6 "А что мне за это будет?"
                        img 8498
                        m "Все, что захочешь, только помоги мне!"
                        # citizen6 бьет citizen12 и тд тп
                        img 8499
                        #звук удара
                        w
                        img 8500
                        #звук падения тела
                        w
                        img 8501
                        w
                        img 8502
                        with fade
                        w
                        img 8503
                        w
                        img 8504
                        w
                        img 8505
                        with fade
                        m "Спасибо, спасибо большое!"
                        citizen6 "Ага, подойдешь ко мне, обсудим мою награду."
                        m "Что?"
                        citizen6 "Ну ты же сама обещала, что у меня будет все, что я захочу..."
                        $ questOffendMonicaFlyersCitizen12Started = False # и это событие больше не появляется
                        $ questOffendMonicaFlyersCitizen12Completed = True
                        return
                    if rand(0, citizen12_refuse_probability) > 0:
                        imgr Dial_Citizen_12_2
                        citizen12 "Ээээ... взять что?"
                        m "Возьмите, пожалуйста, этот флаер..."
                        call reduce_flyers() from _call_reduce_flyers_3
                        citizen12 "Ок..."
                        imgr Dial_Citizen_12_3
                        citizen12 "И все? А как же развлечься?"
                        menu:
                            "Я никого не собираюсь развлекать!":
                                $ kebabWorkHarassmentAmount +=1
                                imgl Dial_Monica_Sandwich_2
                                #img Моника злится
                                m "Я никого не собираюсь развлекать!"
                            "Чем тебя развлечь?":
                                m "Ты это о чем?"
                                citizen12 "Да все просто, отойдем в сторонку, покажешь сиськи, может что еще."
                                m "Не сегодня, засранец!"
                                citizen12 "Да ладно тебе! Подумай об этом. Это быстрый способ заработать."
                    else:
                        imgr Dial_Citizen_12_4
                        citizen12 "Мне неинтересны никакие флаеры!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return

label citizen12_dialogue_pilon:
    imgl Dial_begin35_22
    m "Он хотел меня изнасиловать... Ни за что к нему не подойду..."
    return

label citizen12_dialogue_refuse_after_offend: #Когда подходит в кебабе после нападения
    imgl Dial_begin35_22
    m "Он хотел меня изнасиловать... Ни за что к нему не подойду..."
    return
