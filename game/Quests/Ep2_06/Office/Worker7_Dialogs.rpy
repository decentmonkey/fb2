# китаянка
label worker7_look:
    img 20316
    if shopVisitorStage10 >= 3:
        mt "Лучше держаться от нее подальше."
    else:
        mt "Похоже, это какой-то стажер."
        if monicaBitch == True:
            mt "Бесполезный и никчемный..."
    return

label worker7_dialogue_workplace:
    img 20317
    mt "Кажется, я ее где-то видела..."
    mt "Может быть она когда-то приходила ко мне на кастинг..."
    mt "Или нет, она работала официанткой в моем любимом ресторане..."
    mt "И где я ее могла видеть?"
    img 20318
    if shopVisitorStage10 >= 3:
        mt "Черт! Она же была покупательницей в этом ужасном магазине, где я работала манекеном!"
        mt "Кошмар, надеюсь она меня не узнает..."
        mt "Хотя... Не думаю что можно связать Монику Бакфетт с какой-то продавщицей в трущобах..."
        mt "В любом случае, надо поменьше общаться с ней. Вдруг она, все-же, узнает меня..."
    else:
        mt "Кажется, я ее видела в трущобах..."
        mt "Но и она меня могла видеть..."
    mt "Лучше держаться от нее подальше."
    return

label worker7_dialogue_office:
    img 20371
    w7 "Миссис Бакфет, можно?"
    if shopVisitorStage10 >= 3:
        img 20372
        mt "Она может меня узнать... Лучше не говорить с ней долго."
        mt "Думаю, лучше будет ее вежливо выпроводить."
    img 20373
    m "Кажется, тебя зовут Лин?"
    img 20374
    w
    img 20375
    w7 "Да, мэм."
    img 20376
    m "Лин, я сейчас очень занята. Если ты принесла отчет, положи пожалуйста его мне на стол. Я его обязательно посмотрю."
    img 20377
    w7 "Хорошо, Мэм."
    if shopVisitorStage10 >= 3:
        img 20378
        w7t "(Меня не покидает мысль, что где то Я видела эту миссис Бакфет...)"
    return
