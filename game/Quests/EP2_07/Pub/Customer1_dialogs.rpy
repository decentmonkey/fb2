# чел в синей куртке

label customer1_serve1:
    m "Что будете заказывать?"
    customer1 "Ох, я не знаю... У вас тут все такое вкусное..."
    m "Это так. Выбирайте!"
    customer1 "А что Вы посоветуете? Расскажите мне обо всех блюдах."
    m "Хорошо. Ну во-первых, у нас есть суп харчо, очень вкусный..."
    customer1 "Да, отлично..."
#######    # клиент отускает руки и дотрагивается до юбки моники, она пока не чувствует
    # клиент опускает руку и протягивает ее к ноге Моники (снизу, гораздо ниже попы)
    m "Также есть паста..."
    customer1 "Тоже очень вкусная?"
    m "У нас все вкусное."
    customer1 "Да, я слышал... У вас также вроде бы есть какое-то фирменное блюдо..."
#######    # клиент трогает попу моники так, что она чувствует
    # клиент трогает рукой за ногу Моники
    mt "Он что, меня лапает?! Какого черта?!"
    menu:
        "Ничего не делать.":
            mt "Черт, он трогает меня за ногу!"
            mt "В этом месте тоже одни извращенцы... Я так и знала..."
#            Думаю, он даст хорошие чаевые..."
            mt "С другой стороны, если он даст хорошие чаевые, то..."
            mt "И он трогает мой чулок, он не прикасается к моей коже..."
            m "Да, наше фирменное блюдо Shiny Бургер."
            # продолжает лапать
            customer1 "Отлично! Тогда я возьму его. И пиво."
            customer1 "Можешь идти..."
            mt "Я убью тебя, если ты не дашь мне хорошие чаевые..."
            # уходит, приносит
            customer1 "Да, умничка! Вот, держи!"
            # дает на чай
            return
        "Какого черта?!":
            # моника психанула
            m "Какого черта?!"
            customer1 "Что случилось?"
            m "Ты меня лапал!"
            customer1 "Я?! Неет... Тебе показалось..."
            m "Я уверена! Ты меня лапал!"
            customer1 "Ну не знаю, рука соскользнула, стол был не вытерт, а это работа официанток!"
            customer1 "И вообще, я передумал делать заказ! Можешь идти!"
            mt "Извращенец!"
            return
