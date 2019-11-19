# лысый чел слева
default customer2_dance_comment_stage = 0

label customer2_1stmeeting:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14225
    with fadelong
    m "Что будете заказывать?"
    img 14224
    with diss
    customer2 "Новенькая?"
    # смотрит на монику
    music Groove2_85
    img 14226
    with fade
    customer2 "Ну что сказать: нормально."
    customer2 "И откуда же ты приехала в нашу дыру?"
    img 14227
    mt "Я ни откуда не приезжала! Я просто живу в тех районах, куда такие как ты не заходят."
    img 14228
    with diss
    m "Я из этого города."
    img 14229
    with fade
    customer2 "Из этого говоришь? Я знаю всех в этом районе и ты тут недавно..."
    customer2 "Думаешь, наше знакомство лучше начать с обмана?"
    img 14230
    mt "Думаю, лучше соврать..."
    img 14231
    with diss
    m "Да, Вы правы. Я приехала недавно на заработки."
    img 14232
    with fade
    customer2 "Да, это похоже на правду."
    customer2 "И ты, похоже не из городских, иначе что тебе тут делать?"
    customer2 "Похоже, ты из какой-то деревни, коих тысячи."
    img 14233
    with diss
    mt "Из деревни здесь только ты..."
    if monicaBitch == True:
        mt "Урод..."
    img 14234
    with fade
    $ add_tips(0.5)
    customer2 "Ладно, девочка, вот тебе полбакса и принеси мне пиво. Считай, это в честь первого знакомства."
    # уходит - приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14235
    with fade
    w
    sound snd_plates1
    img 14236
    with diss
    w
    sound snd_beer_table
    img 14237
    with diss
    m "Вот, пожалуйста."
    img 14238
    with fade
    customer2 "Спасибо, можешь идти. Кстати, у тебя большой потенциал, ха-ха-ха. Буду ждать тебя на сцене."
    img 14239
    with diss
    mt "Не дождешься..."
    return

label customer2_serve1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14240
    with fade
    customer2 "Эй, официантка! Мне еще пива! Кстати, как тебя зовут?"
    # если не первый раз
    if get_pub_visitor_visits(obj_name) > 2:
        customer2 "Я все время забываю!"
    img 14241
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14242
    with fade
    customer2 "И постарайся успеть, пока я не допил свой бокал!"
    # уходит - приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14243
    with fade
    w
    sound snd_plates1
    img 14244
    with diss
    w
    sound snd_beer_table
    img 14245
    with diss
    m "Ваше пиво."
    music Groove2_85
    img 14246
    with fade
    customer2 "Ага, могла бы и побыстрее, хотя все вы, деревенщины медлительные."
    img 14247
    with diss
    m "Вообще-то я не из деревни."
    img 14248
    with fade
    customer2 "Ну да, рассказывай. Если бы ты была не из деревни, тебя бы здесь не было!"
    customer2 "Свободна! И подходи ко мне время от времени, я быстро пью."
    customer2 "И, если будешь хорошо работать, может и заработаешь..."
    img 14239
    with diss
    mt "Да что ты знаешь про меня? Неудачник!"
    return

#ситуация : моника идет к нему, ее окликает другой  клиент, она поворачивает голову, отвечает,
#но после этого слегка толкает клиента, который в это время подносил бокал пива ко рту
#этого хватает, чтобы чел слегка облмлся
#label customer2_serve1:
#    mt "Может быть тот лысый хочет еще пива... Думаю, стоит спросить."
#    customer2 "Эй, официантка! Мне еще пива!"
#    m "Да, одну секунду."
#    m "Ой!"
#    # врезается
#    customer2 "Черт! Я вылил на себя все пиво! Что за неуклюжая официантка!"
#    m "Извините, я не хотела..."
#    customer2 "Еще бы ты хотела! Что мне теперь делать? У меня нет пива и я весь сырой!"
#    m "Хотите, я принесу Вам еще пива."
#    customer2 "Конечно хочу! Но я весь сырой! Я также хочу, чтобы ты вытерла меня!"
#    customer2 "У вас тут ничего нет кроме салфеток."
#    mt "Что же мне делать?"
#    menu:
#        "Сделать так, как просит клиент(это ведь из-за меня он разлил пиво).":
#            m "Да, хорошо..."
#            # моника берет салфетки и начинает все вытирать...рубашку, брюки
#            customer2 "У тебя золотые ручки, деточка!"
#            customer2 "Мой дружок начинает просыпаться!"
#            mt "Какой еще дружок?!"
#            m "Все, вы уже не сырой."
#            customer2 "Не страшно, ты можешь продолжить!"
#            customer2 "Хотя ты и так молодец! Держи!"
#            # дает деньги
#            customer2 "Я даже рад, что ты разлила мое пиво, делай так почаще! Ха-ха-ха!"
#            customer2 "Я сегодня уже ничего не хочу, можешь идти."
#            return
#        "Нет уж, пусть сам все вытирает.":
#            m "Я думаю, Вам стоит впредь быть аккуратнее."
#            m "Вот Вам салфеточка, а я пока принесу Вам пива."
#            customer2 "Но я..."
#            # моника уходит и приходит клиент уже сухой
#            m "Вот Ваше пиво."
#            customer2 "..."
#            m "Что-нибудь еще?"
#            customer2 "Да, проваливай!"
#            m "Приходите к нам еще!"
#            mt "Козел!"
#            return

label customer2_after_serve1:
    mt "Лысый болван..."
    return
