

label customer9_1stmeeting:
    img 14394
    m "Здравствуйте! Что будете заказывать?"
    img 14395
    customer9 "Оу! Новенькая? Скажи, ты любишь подарки?"
    img 14396
    mt "Подарки? Вероятно, он о чаевых..."
    img 14397
    menu:
        "Ну да...":
            img 14398
            m "Да."
            img 14399
            сustomer9 "Я так и думал. Вот скажи, что тебе подарить?"
            img 14400
            m "У меня все есть, но чаевые были бы кстати."
            img 14401
            сustomer9 "Нет, я не о чаевых. Как насчет страстного поцелуя?"
            img 14402
            m "Нет, спасибо."
            img 14403
            mt "Да как он может такое спрашивать?"
            pass
        "Я не готова отвечать на этот вопрос.":
            img 14404
            m "Я не готова отвечать на этот вопрос."
            img 14405
            сustomer9 "Я понял... Свидетели... Хорошо, не отвечай, потом расскажешь!"
            pass
    # смотрит на монику
    img 14406
    customer9 "Ты любишь классический секс или в попу?"
    img 14407
    m "А?!"
    img 14408
    customer9 "Я понял! Это значит в попу...Иначе ты бы не работала в Shiny Hole."
    img 14403
    mt "Он нормальный?"
    img 14409
    customer9 "Мне пожалуй ничего, но я очень рад нашему знакомству!"
    img 14410
    mt "Не адекватный..."
    return

label customer9_serve1:
    img 14411
    m "Добрый день, что будете заказывать?"
    # чел резко хватает монику и садит себе на колени
    m "Ай!"
    сustomer9 "Скажи, ты была хорошей девочкой?"
    сustomer9 "Расскажи Санте!"
    сustomer9 "И возможно, Санта сделает тебе хороший подарок!"
    mt "Меня посадил к себе на колени незнакомый мужик! Возможно, стоит ему подыграть..."
    menu:
        "Быстро отпусти меня!":
            m "Быстро отпусти меня!"
            # моника вырывается
            сustomer9 "Ах вот ты как! Ну и вали! Ваше пиво кстати отстой!"
            mt "Что же ты его тогда пьешь?"
            return
        "Да, я была хорошей девочкой.":
            m "Да, я была хорошей девочкой."
            сustomer9 "Я так и думал! Уверен, ты обслужила очень много клиентов и они остались довольны."
            # кладет ей под чулок купюру
            customer9 "Ладно, беги, у меня еще есть пиво."
            mt "Он дал мне 20 долларов! Ничего себе..."
            return
