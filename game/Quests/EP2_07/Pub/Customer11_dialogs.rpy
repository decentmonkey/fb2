
# подойдет и под каждодневную встречу. serve1 будет рандомно не очень часто
label customer11_1stmeeting:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14381
    with fadelong
    m "Вы готовы сделать заказ?"
    # рассматривает
    sound snd_whistle1
    img 14382
    with diss
    w
    music Groove2_85
    img 14383
    with diss
    customer11 "А ты конфетка!"
    customer11 "В общем все просто: мне пиво и бургер и быстро!"
    img 14384
    m "Да, конечно!"
    img 14385
    customer11 "И можно это делать без слов. Быстро пошла и принесла мой заказ."
    img 14386
    with diss
    mt "Грубиян..."
    # уходит приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14387
    with fade
    w
    sound snd_plates1
    img 14388
    with diss
    w
    sound snd_beer_table
    img 14389
    with diss
    w
    img 14390
    with fade
    customer11 "Вот видишь, все очень просто. Молодец, держи." # дает чай
    $ add_tips(3.0)
    img 14391
    with diss
    m "Спасибо."
    music Groove2_85
    img 14392
    with diss
    customer11 "Да, да... Иди уже..."
    img 14393
    with fade
    mt "Очередной придурок."
    return

# клиент делает заказ, сзади подхоит 6 и хватает за сиськи

#label customer11_serve1:
#    m "Здравствуйте, что будете заказывать?"
#    сustomer11 "Ты забыла? Мне пиво и бургер!"
#    m "Да, хорошо, сейчас сделаем."
#    # хватает 6
#    сustomer6 "О да! Твои сиськи как у моей бывшей! Только больше и мягче!"
#    # пару сек мнет моники сиськи. моника разворачивается, толкает 6, он паадет
#    Joe "Эй, [monica_pub_name]! Ты  зачем толкнула нашего хорошего клиента?"
#    m "Как это зачем? Он схватил меня за грудь!"
#    Joe "Возможно, но он тебя не толкал!"
#    # очухался 6
#    сustomer6 "Вообще то я немного потерял равновесие и схватился..."
#    m "Ты схватил меня за грудь!"
#    сustomer11 "Эй, мне долго ждать мой заказ?"
#    Joe "[monica_pub_name], возвращайся к работе!"
#    сustomer11 "Напоминаю, я заказал бургер и пиво."
#    mt "Я помню..."
#    # уходит приходит
#    сustomer11 "Профессиональные официантки не обращают внимания на такие мелочи!"
#    сustomer11 "Тебе ище расти и расти."
#    mt "Не обращают внимание?! Да как он может такое говорить?!"
#    сustomer11 "Не стой, на чай не получишь. Работай лучше."
#    mt "Скряга..."
#    return

label customer11_afterserve1:
    return
