# 2 парня у шеста

label customer78_1stmeeting:
    m "Здравствуйте! Что будете заказывать?"
    customer7 "Заказ? Да, готовы, но мы скажем, что мы хотим официантке, а Вы поднимайтесь! Надоело уже смотреть на эту стриптизершу."
    # смотрит на монику
    m "Я и есть официантка..."
    customer7 "Да? Да быть не может! Ты гораздо эффектнее смотрелась бы на пилоне!"
    customer7 "Ты новенькая?"
    customer7 "Как тебя зовут?"
    m "Да, я тут недавно. Меня зовут [monica_pub_name]"
    customer7 "[monica_pub_name], ты хочешь заработать?"
    mt "Да я зарабатываю по больше чем вся твоя семья и твой товарищ!"
    m "Да, именно за этим я здесь."
    customer7 "Я так и думал... Просто для информации: гораздо больше можно заработать тут.." # показывает на шест
    m "Мне это не интересно."
    customer7 "Да, да, все так говорят, пока не узнают какие тут деньги..."
    mt "Неужели и правда большие?"
    menu:
        "И какие же?":
            m "И какие же?"
            customer7 "Ну за представление можно заработать 1000 долларов..."
            customer7 "Но все зависит от того, что ты покажешь..."
            m "Я поняла, мне это не интересно."
            mt "1000 долларов за вечер? Не малеькие деньги для такой дыры..."
            pass
        "Мне это не интересно.":
            m "Говорю же, мне это не интересно."
            customer7 "Конечно, конечно, это пока..."
            pass
    customer7 "А пока, принеси нам еды и пива. На свой вкус."
    m "Хорошо."
    # уходит принтсит
    customer7 "То что надо! Похоже, ты умеешь читать мысли!"
    customer7 "Вот, держи!" # дает доллар
    customer7 "Приходи к нам чаще! Я вижу в тебе потенциал."
    mt "Какой еще потенциал?"
    m "Хорошо."
    return

label customer78_serve1:
    m "Что будете..."
    сustomer5 "Нам два шота! И быстро! Хотим их выпить перед очередным выступлением!"
    m "Хорошо, один момент!"
    # уходит - приносит
    m "Вот, пожалуйста! Что нибудь еще?"
    сustomer5 "Да, вот еще что! Не могла бы ты в следующия раз быть побыстрее!"
    сustomer5 "Похоже тебя сюда взяли по двум причинам. Эти причины: сиськи и жопа! Но уж точно не скорость!"
    сustomer5 "А теперь иди, шоу уже началось!"
    mt "Козлы..."
    return

label customer78_serve2:
    m "Здравствуйте, Вы готовы сделать заказ?"
    customer7 "О, новенькая! Ты знаешь, у нас с товарищем небольшая проблема."
    customer7 "Ты же знаешь, что у вас при покупке двух шотов третий в подарок?"
    customer7 "А нас, как ты видишь двое...Выпей с нами!"
    m "Вы можете купить четыре шота, Вам принесут шесть и Вы их сможете выпить вдвоем."
    m "И мне нельзя пить на работе."
    customer7 "Да брось, детка! Напомни, тебя как зовут?"
    mt "Может быть стоит быть с ними полюбезнее, тогда они оставят на чай..."
    m "[monica_pub_name]"
    customer7 "Отлично, [monica_pub_name]! Ну дак что, выпьешь с нами? Ты ведь любишь чаевые?"
    mt "Конечно, я не фанат алкоголя, но что может быть от одного шота? К тому же они дадут чаевые..."
    mt "Хотя может быть не стоит, я довольно давно не пила..."
    menu:
        "Хорошо, я выпью с Вами.":
            m "Хорошо, я выпью с Вами."
            customer7 "Вот и славно!"
            # обращается к 8
            customer7 "Эй, дружище, сбегай к стойке за шотами."
            # 8 отходит, возвращается, с 3 маленькими шотами
            customer7 "Отлично! Ну что, выпьем?"
            # пьют моника морщится
            customer7 "Что, не понравился Shiny шот?! Ха-ха-ха!"
            customer7 "А по-моему он прекрасен!"
            m "Что нибудь еще?"
            customer7 "Да, тебя!"
            m "Что?"
            customer7 "Ха-ха-ха! Ладно, я пошутил, больше ничего не нужно!"
            customer7 "Вот, держи." # дает 10 баксов
            mt "Десять долларов? Маловато..."
            return
        "Я на работе, мне нельзя.":
            m "Я на работе, мне нельзя."
            customer7 "Ууу... Какая ты правильная... Тогда нам два пива!"
            m "Хорошо."
            # уходит за пивом, приносит.
            m "Вот, пожалуйста."
            customer7 "Можешь идти!"
            mt "Да, свои чаевые я не получила... Возможно стоило согласиться на их предложеине?"
            return
