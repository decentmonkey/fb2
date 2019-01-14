label ep22_casting:
    label ep22_dialogue6_6_loop1:
        #первый вызов
        help "Пока доступна только одна возможность. Другие пункты будут доступны в следующих версиях игры."
        menu:
            "Показать обнаженную грудь.":
                #Моника показывает грудь в зависимости от одежды
                if castingCloth == 1:
                    if chickMode == True:
                        img 8441
                        with Dissolve(0.5)
                        m "Моника Бакфетт хочет показать папочке грудь..."
                        img 8442
                        with fade
                        w
                        img 8444
                        with Dissolve(0.5)
                        w
                    else:
                        img 8441
                        with Dissolve(0.5)
                        m "Я покажу тебе грудь, потому что ты заставил меня..."
                        img 8442
                        with fade
                        w
                        img 8443
                        with Dissolve(0.5)
                        w
                if castingCloth == 2:
                    if chickMode == True:
                        sound snd_fabric1
                        img 8460
                        with fade
                        m "Леди Нуар хочет показать папочке грудь..."
                        img 8461
                        biff "Давай, Леди Нуар! Показывай свои сиськи!"
                        "Не прячь их от папочки!"
                        img 8456
                        with Dissolve(0.5)
                        w
                        img 8457
                        with Dissolve(0.5)
                        w
                        img 8458
                        with Dissolve(0.5)
                        w
                        img 8459
                        with Dissolve(0.5)
                        w

                    else:
                        sound snd_fabric1
                        img 8453
                        with fade
                        m "Биф, мне обязательно это делать?"
                        img 8454
                        biff "Давай, Леди Нуар! Показывай свои сиськи!"
                        "Не прячь их от папочки!"
                        "А то я заставлю Леди Нуар показать еще кое-что!"
                        img 8455
                        with fade
                        w
                        img 8445
                        biff "Я жду!"
                        img 8455
                        with fade
                        w
                        img 8456
                        with Dissolve(0.5)
                        w
                        img 8457
                        with Dissolve(0.5)
                        w
                        img 8458
                        with Dissolve(0.5)
                        w
                        img 8459
                        with Dissolve(0.5)
                        w
                if castingCloth == 3:
                    if chickMode == True:
                        img 8473
                        with fade
                        m "Девушка с календаря хочет показать папочке грудь..."
                        sound snd_fabric1
                        img 8477
                        with Dissolve(0.5)
                        w
                        img 8478
                        with Dissolve(0.5)
                        w
                        img 8479
                        with Dissolve(0.5)
                        w
                    else:
                        img 8469
                        with fade
                        m "Я знаю, я должна показать тебе грудь..."
                        "Но можно я не буду делать этого?"
                        img 8470
                        biff "Давай! Девушка с календаря!"
                        "Показывай свои сиськи!"
                        "Иначе я скажу Алексу чтобы эти голые сиськи смотрели с прямо с календаря!"
                        img 8471
                        with fade
                        mt "Черт! У меня молоток... Может убить этого мерзавца?!"
                        "Сколько мне терпеть это???"
                        "..."
                        "Нет... Слишком опасно..."
                        img 8472
                        biff "Ну же! Сиськи!"
                        img 8471
                        with fade
                        w
                        img 8474
                        with Dissolve(0.5)
                        w
                        img 8475
                        with Dissolve(0.5)
                        m "На, смотри..."
                        img 8476
                        with Dissolve(0.5)
                        w
                        "Мне не нужны проблемы..."
                        w

                img 8445
                biff "Хорошо, папочка доволен!"
                #если уже несколько раз
                biff "Но папочке начинает надоедать одно и то же..."
            "Показать обнаженную попу. (disabled)":
                pass
            "Раздеться и принимать различные модельные позы. (disabled)":
                pass
            "Раздеться и встать на колени задом к Бифу. (disabled)":
                pass
            "Раздеться и лечь на пол раздвинув ноги. (disabled)":
                pass
            "Раздеться и сесть на стол.":
                menu:
                    "Поставить на стол одну ногу. (disabled)":
                        pass
                    "Сесть на стол лицом к Бифу, широко раздвинув ноги. (disabled)":
                        pass
                    "Сесть на стол спиной к Бифу. (disabled)":
                        pass
                    "Сесть на стол, достать член Бифа и взять его в рот. (disabled)":
                        pass
                    "Сесть на стол. достать член Бифа и возить им по киске. (disabled)":
                        pass
                    "Сесть на стол, достать член Бифа и вставить его в свою киску. (disabled)":
                        pass
                    "Сесть на стол, достать член Бифа и вставить его в анальное отверстие. (disabled)":
                        pass
                    "Назад.":
                        jump ep22_dialogue6_6_loop1
            "Раздеться и сесть на Бифа.":
                menu:
                    "Сесть к Бифу на коленки лицом к нему. (disabled)":
                        pass
                    "Сесть к Бифу на коленки спиной. (disabled)":
                        pass
                    "Сесть Бифу киской на лицо. (disabled)":
                        pass
                    "Достать член Бифа и сесть на него лицом к Бифу (disabled)":
                        pass
                    "Достать член Бифа и сесть на него спиной к Бифу (disabled)":
                        pass
                    "Достать член Бифа и сесть на него анальным отверстием (disabled)":
                        pass
                    "Назад.":
                        jump ep22_dialogue6_6_loop1
            "Полизать папочке зад. (disabled)":
                pass
            "Позвать секретаршу.":
                label ep22_dialogue6_6_loop2:
                    menu:
                        "Поцеловать секретаршу. (disabled)":
                            pass
                        "Полизать секретарше грудь. (disabled)":
                            pass
                        "Полизать секретарше киску. (disabled)":
                            pass
                        "Засунуть секретарше язык глубоко в анальное отверстие. (disabled)":
                            pass
                        "Достать член Бифа и засунуть его в секретаршу. (disabled)":
                            pass
                        "Засунуть член в ее киску, затем вытащить и облизать его. (disabled)":
                            pass
                        "Засунуть член в ее анальное отверстие, затем вытащить и облизать его. (disabled)":
                            pass
#                        "Назад.":
#                                jump ep22_dialogue6_6_loop2
                        "Назад.":
                            jump ep22_dialogue6_6_loop1
    return
