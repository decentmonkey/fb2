
# Моника приходит в полицейский участок и остается там до утра в тюрьме
label ep27_dialogues_marcus1_1:
    # Моника заходит в локацию полиции

    mt "Мне страшно..."
    mt "У меня ноги подкашываются от ужаса..."
    mt "Стоит-ли мне идти туда..."
    return

label ep27_dialogues_marcus1_1a:
    # При нажатии на вход
    help "Вы уверены в том чтобы Моника вошла туда?"
    help "Этот набор событий необязателен для прохождения игры."
    menu:
        "Не рисковать.":
            return False
        "Все равно войти.":
            pass

    help "Пожалуйста, сохранитесь. Часть событий внутри полиции все еще в разработке."
    return True

label ep27_dialogues_marcus1_1b:
    # Если пытается зайти в участок вечером
    mt "Сейчас темно..."
    mt "Поздно вечером я точно не найду в себе смелость зайти туда."
    mt "{c}Лучше придти туда днем{/c}."
    return

label ep27_dialogues_marcus1_2:
    # Диалог с полицейской на входе
    img 14138
    policewoman "Да, гражданка?"
    policewoman "Что вам надо?"
    img 14139
    m "Я... Я..."
    img 14140
    policewoman "Ну же? Что молчишь?!"
    policewoman "Говори! Или выметайся!"
    policewoman "Здесь полицейский участок!"
    img 14141
    m "Я... Пришла..."
    m "Я пришла, чтобы... чтобы увидеть Мистера Маркуса..."
    img 14142
    policewoman "Мистер Маркус занятой человек."
    policewoman "У Вас к нему какое-то дело?"
    img 14143
    m "У меня... Я..."
    m "Да... У меня важное дело к нему..."
    img 14144
    policewoman "Я позову детектива и он решит что с Вами делать!"
    img 14145
    m "Да, Мэм... Конечно..."
    img 14146
    mt "О БОЖЕ!"
    mt "Может быть мне убежать, пока не поздно?!"
    img 14147
    menu:
        "Убежать!":
            return False
        "Остаться и дождаться детектива.":
            pass
    img 14148
    detective "Добрый день, Мэм."
    detective "Вы хотели увидеть Мистера Маркуса?"
    img 14149
    m "Да, Сэр..."
    m "Я бы... Я бы хотела увидеть его..."
    img 14150
    detective "Пожалуйста, скажите, как Вас зовут?"
    img 14151
    m "Меня зовут... Моника Бакфетт..."
    img 14152
    detective "Хорошо, Мэм."
    detective "Подождите минуту."
    img 14153
    m "Да, Сэр, конечно..."

    ## Проходит время
     img 14154
    detective "Мэм, Мистер Маркус сейчас занят и он попросил Вас подождать, пока он освободится."
    img 14155
    m "..."
    img 14156
    detective "Вы ведь не против подождать, пока Мистер Маркус освободится?"
    img 14157
    menu:
        "Согласиться подождать.":
            img 14158
            m "Да, Сэр..."
            m "Я подожду его."
            img 14159
            detective "Хорошо, Мэм."

        "Попытаться уйти.":
            img 14160
            m "Я зайду попозже, когда Мистер Маркус будет свободен."
            img 14159
            detective "Мэм, я попрошу Вас обождать."
            detective "Мистер Маркус настаивает, чтобы Вы подождали его."

    # Появляются полицейские
    img 14161
    w
    img 14162
    detective "Миссис Бакфетт."
    detective "Вас сейчас проводят в место, где Вам будет комфортно ожидать Мистера Маркуса."
    img 14163
    mt "О Боже!"
    mt "ЭТО ОНИ!"
    img 14164
    policeman1 "Пройдемте с нами, Мэм..."
    img 14165
    policeman2 "Рад тебя снова видеть, сучка..."
    img 14166
    mt "!!!"

    return

label ep27_dialogues_marcus1_3:
    # Монику приводят в тюрьму
    img 14167
    m "Это... Это место!"
    m "Но!"
    m "Мистер Маркус согласился встретиться со мной!"
    m "Зачем Вы привели меня сюда?!"
    img 14168
    policeman1 "Мистер Маркус освободится только завтра с утра."
    policeman1 "До этого времени ты подождешь его здесь."
    img 14169
    m "Зачем Я здесь?"
    img 14170
    policeman1 "Боб!"
    policeman1 "Эта сучка вернулась!"
    img 14171
    policeman1 "Представляешь? Сама!"
    img 14172
    policeman2 "Ха-ха-ха!"
    img 14173
    m "Нет! Я пришла к Мистеру Маркусу!"
    img 14174
    overseer "О! Это она?"
    overseer "У меня от нее все время болела голова!"
    overseer "И вот вы снова привели ее!"
    img 14175
    policeman1 "Не беспокойся, Боб!"
    policeman1 "Она у тебя ненадолго."
    policeman1 "После встречи с Мистером Маркусом она отправится на объект."
    img 14176
    m "НЕЕЕЕТ!"
    return

label ep27_dialogues_marcus1_4:
    img 14177
    w
    img 14178
    # Заходят в камеру
    img 14179
    policeman2 "Соскучилась по своей клетке, сучка?"
    policeman2 "Раздевайся, иначе порвем твое платье!"
    img 14180
    m "!!!"
    img 14181
    policeman1 "Снимай одежду, мы дадим тебе другую."
    img 14182
    m "Хорошо..."

    # Моника снимает одежду
    img 14183
    m "Что?"
    m "А где низ?"
    m "Дайте мне что-нибудь прикрыть низ?"
    img 14184
    policeman2 "Скажи спасибо за то что есть."
    img 14185
    policeman1 "Оставайся и веди себя хорошо."

    # уходят
    img 14186
    policeman2 "Одно нарушение порядка и мы сообщим об этом Мистеру Маркусу."
    return

label ep27_dialogues_marcus1_5:
    # Моника оказывается в клетке
    img 14187
    mt "О БОЖЕ!"
    mt "О БОЖЕ!!!"
    mt "Я снова здесь!"
    img 14188
    mt "..."
    mt "И я пришла сюда сама!"
    img 14189
    mt "Что же мне делать?!"
    img 14190
    mt "ОНИ СКАЗАЛИ ЧТО ОТСЮДА Я НАПРАВЛЮСЬ НА ОБЪЕКТ!!!"
    mt "Я УВЕРЕНА ЧТО ОНИ ГОВОРИЛИ ПРО ЭТУ ФЕРМУ!!!"
    mt "О БОЖЕ!!!"
    mt "Как мне спастись?!"
    img 14191
    mt "Зачем я пришла сюда?!"
    img 14192
    mt "..."
    img 14193
    mt "Так, Моника, стоп!"
    mt "Не паникуй!"
    mt "Мне посоветовала это сделать Мелани."
    img 14194
    mt "А Мелани, как мне кажется, знает что делает."
    mt "В конце концов, ей удалось выбраться оттуда."
    img 14195
    mt "С другой стороны, она могла сделать это специально, чтобы я попала в руки к Маркусу..."
    mt "Или она хотела наоборот помочь мне..."
    mt "На чьей же стороне Мелани?"
    img 14196
    mt "..."
    img 14197
    mt "Но, к черту!"
    mt "Эти мерзавцы специально пытаются вывести меня из равновесия."
    mt "Они пугают меня, думая что я сдамся!"
    mt "Но я не сдамся!"
    img 14198
    mt "Я - Моника Бакфетт!"
    mt "И я пройду через все! Я одержу победу!"
    mt "Завтра я встречусь с Маркусом."
    mt "Я ничего не нарушала, ни одного закона или правила!"
    mt "По крайней мере, Маркус не знает про некоторые исключения..."
    img 14199
    mt "..."
    img 14200
    mt "Я поговорю с ним и выйду отсюда!"
    mt "Я пришла сюда сама! И я смогу отсюда выйти!"
    return

label ep27_dialogues_marcus1_6:
    # Моника смотрит на унитаз
    img 14201
    mt "Эта жуткая штука!"
    mt "Не могу поверить что я снова здесь!"
    return

label ep27_dialogues_marcus1_7:
    
    mt "Кошмарная кровать..."
    mt "Хоть я и првыкла спать в подвале дома, но эта кровать очень жесткая и она плохо пахнет..."
    return

label ep27_dialogues_marcus1_8:
    mt "Решетка..."
    mt "Ее можно подергать, чтобы позвать этого кошмарного Боба..."
    return

label ep27_dialogues_marcus1_9:
    # Моника дергает за решетку
    # Подходит Боб
    overseer "Ну, что тебе?!"
    overseer "Теперь ты снова будешь целыми днями стучать?"
    overseer "А у меня болит голова!"
    overseer "Еще больше чем ранее!"
    mt "Дьявол! Я ненавижу этого урода!"
    mt "Но, по моему опыту, с ним лучше быть повежливее."
    mt "Хоть мне здесь и придется быть лишь до завтрашнего утра, но я уже проголодалась."
    mt "Здесь подают помои, но я немного отвыкла от вкусной еды."
    mt "Для девушки такого уровня как Я будет сложно есть такую пищу, но я научилась справляться с этим."

    m "Мистер Боб."
    m "Могли бы Вы принести мне немного Вашей вкусной еды?"
    overseer "Не положено! Сегодня заключенных уже кормили!"
    overseer "Жрать завтра!"
    mt "БОЖЕ! Ну и урод!"
    m "Спасибо, Мистер Боб... Я подожду до завтра..."
    mt "Не больно-то и хотелось есть его помои!"
    mt "И я рада, что он их не принес!"
    mt "Уж лучше немного подождать до завтра и поесть нормальную еду в городе!"
    return

label ep27_dialogues_marcus1_10:
    # Моника ложится спать
    mt "Я устала. Может быть лечь поспать?"

    return

label ep27_dialogues_marcus1_11:
    # Моника легла спать
    mt "Завтра новый день."
    mt "С утра я встречусь с Маркусом лицом к лицу и решу все мои проблемы."
    mt "Я сильная и я знаю что справлюсь..."
    mt "Все будет хорошо!"
    mt "А сейчас пора спать..."
    return




#$ jailCageBlackmailBoobsShowed
#$ jailCageBlackmailAssShowed
#$ jailCageBlackmailMonicaSaidSheIsAWhore










#
