# чел в синей куртке
default customer1_dance_comment_stage = 0

label customer1_1stmeeting:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14203
    with fadelong
    mt "Надо пересилить себя..."
    m "Что будете заказывать?"
    img 14202
    with diss
    customer1 "Вообще-то я ничего не хотел, но теперь думаю, что что-то закажу."
    customer1t "И откуда этот говнюк Джо достал такую красотку?"
    customer1 "Как тебя зовут?"
    m "Меня зовут [monica_pub_name]."
    music Groove2_85
    img 14204
    with fade
    customer1 "Отлично, [monica_pub_name]"
    customer1 "Думаю, ты тут для того, чтобы заработать, так?"
    img 14205
    with diss
    m "Ну, да..."
    mt "Надо быть осторожнее с этими пьяницами..."
    img 14206
    with fade
    customer1 "Я так и думал. Вообще, чтобы получать хорошие чаевые, нужно как минимум быть вежливой."
    customer1 "Например ты должна была сказать:"
    img 14207
    customer1 "Здравствуйте, меня зовут [monica_pub_name]..."
    customer1 "Понятно?"
    img 14208
    m "Да."
    img 14209
    with diss
    mt "Да кем он себя возомнил?"
    mt "Очередной придурок..."
    img 14210
    with fade
    customer1 "Хорошо. Думаю, в следующий раз ты будешь более вежливой. Кстати, я передумал делать заказ."
    img 14211
    with diss
    mt "Что за урод? Только зря потратила время..."
    return

label customer1_serve1:
    music Hidden_Agenda
    sound highheels_short_walk

    img 14212
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer1_dance_comment_stage == 1:
        m "второй разговор"

    if monicaStartedStripDanceFlag == True and customer1_dance_comment_stage == 0:
        customer1 "А не тебя я видел виляющей попой у пилона?"
        m "Нет, Вы меня с кем-то путаете."
        m "Я работаю здесь официанткой..."
        customer1 "Только официанткой?"
        m "Еще... Еще я мою посуду..."
        $ customer1_dance_comment_stage = 1

    #

    m "Что будете заказывать?"
    img 14213
    customer1 "Ну нет, разве я так тебя учил?"
    customer1 "Будь вежливой, скажи как тебя зовут..."
    img 14214
    $ menu_bitchiness
    menu:
        "Быть вежливой." if bitchmeterValue <= maxBitchness / 2:
            img 14215
            with fade
            mt "Насколько знаю, официантки ведут себя вежливо."
            mt "Попытаюсь притвориться, насколько у меня хватит сил..."
#            mt "Возможно, так правильнее, я совсем не знаю как работают официантки."
            img 14216
            with diss
            m "Здравствуйте, меня зовут [monica_pub_name]..."
            img 14217
            with fade
            customer1 "Отлично, [monica_pub_name]."
            customer1 "А теперь, [monica_pub_name], принеси мне пива."
            img 14218
            with diss
            m "Хорошо."
            # уходит, приносит
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.0
            music Hidden_Agenda
            sound snd_plates1
            img 14219
            with fade
            w
            sound snd_beer_table
            img 14220
            with diss
            w
            img 14221
            with diss
            customer1 "Запомни, быть хорошей официанткой очень сложно. Некоторые получают по 100 долларов чаевых за заказ. А пока держи..."
            $ add_tips(0.25)
            # дает 0.25
            img 14209
            with fade
            mt "Четвертак? Сколько же бокалов я должна принести, чтобы ты дал мне 100 долларов?"
#            if monicaBitch == True:
            mt "Урод..."
            return True
        "Быть вежливой. (Моника недостаточно приличная) (disabled)" if bitchmeterValue > maxBitchness / 2:
            pass
        "Отказаться.":
            music Groove2_85
            img 14222
            with fade
            mt "Я не собираюсь слушаться этого деревенщину!"
            # развернуться и уйти
            sound highheels_short_walk
            img 14223
            with diss
            customer1 "Эй, ты куда?"
            return False

#label customer1_serve2:
#    m "Что будете заказывать?"
#    customer1 "Ох, я не знаю... У вас тут все такое вкусное..."
#    m "Это так. Выбирайте!"
#    customer1 "А что Вы посоветуете? Расскажите мне обо всех блюдах."
#    m "Хорошо. Ну во-первых, у нас есть суп харчо, очень вкусный..."
#    customer1 "Да, отлично..."
#    # клиент опускает руку и протягивает ее к ноге Моники (снизу, гораздо ниже попы)
#    m "Также есть паста..."
#    customer1 "Тоже очень вкусная?"
#    m "У нас все вкусное."
#    customer1 "Да, я слышал... У вас также вроде бы есть какое-то фирменное блюдо..."
#    # клиент трогает рукой за ногу Моники
#    mt "Он что, меня лапает?! Какого черта?!"
#    menu:
#        "Ничего не делать.":
#            mt "Черт, он трогает меня за ногу!"
#            mt "В этом месте тоже одни извращенцы... Я так и знала..."
##            Думаю, он даст хорошие чаевые..."
#            mt "С другой стороны, если он даст хорошие чаевые, то..."
#            mt "И он трогает мой чулок, он не прикасается к моей коже..."
#            m "Да, наше фирменное блюдо Shiny Бургер."
#            # продолжает лапать
#            customer1 "Отлично! Тогда я возьму его. И пиво."
#            customer1 "Можешь идти..."
#            mt "Я убью тебя, если ты не дашь мне хорошие чаевые..."
#            # уходит, приносит
#            customer1 "Да, умничка! Вот, держи!"
#            # дает на чай
#            return
#        "Какого черта?!":
#            # моника психанула
#            m "Какого черта?!"
#            customer1 "Что случилось?"
#            m "Ты меня лапал!"
#            customer1 "Я?! Неет... Тебе показалось..."
#            m "Я уверена! Ты меня лапал!"
#            customer1 "Ну не знаю, рука соскользнула, стол был не вытерт, а это работа официанток!"
#            customer1 "И вообще, я передумал делать заказ! Можешь идти!"
#            mt "Извращенец!"
#            return

label customer1_afterserve1:
    mt "Тупой коротышка..."
    return
