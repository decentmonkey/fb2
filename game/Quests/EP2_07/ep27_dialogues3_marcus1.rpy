
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
    policewoman "Да, гражданка?"
    policewoman "Что вам надо?"
    m "Я... Я..."
    policewoman "Ну же? Что молчишь?!"
    policewoman "Говори! Или выметайся!"
    policewoman "Здесь полицейский участок!"
    m "Я... Пришла..."
    m "Я пришла, чтобы... чтобы увидеть Мистера Маркуса..."
    policewoman "Мистер Маркус занятой человек."
    policewoman "У Вас к нему какое-то дело?"
    m "У меня... Я..."
    m "Да... У меня важное дело к нему..."

    policewoman "Я позову детектива и он решит что с Вами делать!"
    m "Да, Мэм... Конечно..."

    mt "О БОЖЕ!"
    mt "Может быть мне убежать, пока не поздно?!"
    menu:
        "Убежать!":
            return False
        "Остаться и дождаться детектива.":
            pass

    detective "Добрый день, Мэм."
    detective "Вы хотели увидеть Мистера Маркуса?"
    m "Да, Сэр..."
    m "Я бы... Я бы хотела увидеть его..."
    detective "Пожалуйста, скажите, как Вас зовут?"
    m "Меня зовут... Моника Бакфетт..."
    detective "Хорошо, Мэм."
    detective "Подождите минуту."
    m "Да, Сэр, конечно..."

    ## Проходит время

    detective "Мэм, Мистер Маркус сейчас занят и он попросил Вас подождать, пока он освободится."
    m "..."
    detective "Вы ведь не против подождать, пока Мистер Маркус освободится?"
    menu:
        "Согласиться подождать.":
            m "Да, Сэр..."
            m "Я подожду его."
            detective "Хорошо, Мэм."

        "Попытаться уйти.":
            m "Я зайду попозже, когда Мистер Маркус будет свободен."
            detective "Мэм, я попрошу Вас обождать."
            detective "Мистер Маркус настаивает, чтобы Вы подождали его."

    # Появляются полицейские
    detective "Миссис Бакфетт."
    detective "Вас сейчас проводят в место, где Вам будет комфортно ожидать Мистера Маркуса."

    mt "О Боже!"
    mt "ЭТО ОНИ!"

    policeman1 "Пройдемте с нами, Мэм..."
    policeman2 "Рад тебя снова видеть, сучка..."
    mt "!!!"

    return

label ep27_dialogues_marcus1_3:
    # Монику приводят в тюрьму
    m "Это... Это место!"
    m "Но!"
    m "Мистер Маркус согласился встретиться со мной!"
    m "Зачем Вы привели меня сюда?!"

    policeman1 "Мистер Маркус освободится только завтра с утра."
    policeman1 "До этого времени ты подождешь его здесь."

    m "Зачем Я здесь?"

    policeman1 "Боб!"
    policeman1 "Эта сучка вернулась!"

    policeman1 "Представляешь? Сама!"
    policeman2 "Ха-ха-ха!"

    m "Нет! Я пришла к Мистеру Маркусу!"

    overseer "О! Это она?"
    overseer "У меня от нее все время болела голова!"
    overseer "И вот вы снова привели ее!"

    policeman1 "Не беспокойся, Боб!"
    policeman1 "Она у тебя ненадолго."
    policeman1 "После встречи с Мистером Маркусом она отправится на объект."

    m "НЕЕЕЕТ!"
    return

label ep27_dialogues_marcus1_4:
    # Заходят в камеру
    policeman2 "Соскучилась по своей клетке, сучка?"
    policeman2 "Раздевайся, иначе порвем твое платье!"
    m "!!!"
    policeman1 "Снимай одежду, мы дадим тебе другую."
    m "Хорошо..."

    # Моника снимает одежду

    m "Что?"
    m "А где низ?"
    m "Дайте мне что-нибудь прикрыть низ?"

    policeman2 "Скажи спасибо за то что есть."
    policeman1 "Оставайся и веди себя хорошо."

    # уходят
    policeman1 "Одно нарушение порядка и мы сообщим об этом Мистеру Маркусу."
    return

label ep27_dialogues_marcus1_5:
    # Моника оказывается в клетке
    mt "О БОЖЕ!"
    mt "О БОЖЕ!!!"
    mt "Я снова здесь!"
    mt "..."
    mt "И я пришла сюда сама!"

    mt "Что же мне делать?!"

    mt "ОНИ СКАЗАЛИ ЧТО ОТСЮДА Я НАПРАВЛЮСЬ НА ОБЪЕКТ!!!"
    mt "Я УВЕРЕНА ЧТО ОНИ ГОВОРИЛИ ПРО ЭТУ ФЕРМУ!!!"
    mt "О БОЖЕ!!!"
    mt "Как мне спастись?!"

    mt "Зачем я пришла сюда?!"

    mt "..."

    mt "Так, Моника, стоп!"
    mt "Не паникуй!"
    mt "Мне посоветовала это сделать Мелани."
    mt "А Мелани, как мне кажется, знает что делает."
    mt "В конце концов, ей удалось выбраться оттуда."

    mt "С другой стороны, она могла сделать это специально, чтобы я попала в руки к Маркусу..."
    mt "Или она хотела наоборот помочь мне..."
    mt "На чьей же стороне Мелани?"
    mt "..."
    mt "Но, к черту!"
    mt "Эти мерзавцы специально пытаются вывести меня из равновесия."
    mt "Они пугают меня, думая что я сдамся!"
    mt "Но я не сдамся!"
    mt "Я - Моника Бакфетт!"
    mt "И я пройду через все! Я одержу победу!"
    mt "Завтра я встречусь с Маркусом."
    mt "Я ничего не нарушала, ни одного закона или правила!"
    mt "По крайней мере, Маркус не знает про некоторые исключения..."
    mt "..."
    mt "Я поговорю с ним и выйду отсюда!"
    mt "Я пришла сюда сама! И я смогу отсюда выйти!"
    return

label ep27_dialogues_marcus1_6:
    # Моника смотрит на унитаз
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
