# китаянка
label worker7_dialogue_workplace:
    mt "Кажется, я ее где-то видела..."
    mt "Может быть она когда-то приходила ко мне на кастинг..."
    mt "Или нет, она работала официанткой в моем любимом ресторане..."
    mt "И где я ее могла видеть?"
    if (Была манекеном):
        mt "Черт! Она же была покупательницей в этом ужасном магазине!"
        mt "А я там была манекеном!"
        mt "Кошмар, хоть бы она меня не узнала..."
    else:
        mt "Кажется, я ее видела в трущебах..."
        mt "Но и она меня могла видеть..."
    mt "Лучше не буду с ней говорить."
    return

label worker7_dialogue_office:
    w7 "Миссис Бакфет, можно?"
    mt "Она может меня узнать... Лучше не говорить с ней долго."
    mt "Думаю, лучше будет ее вежливо выпроводить."
    m "Кажется, тебя зовут Лин?"
    w7 "Да, мэм."
    m "Лин, я сейчас очень занята. Если ты принесли отчет, положи пожалуйста его мне на стол. Я его обязательно посмотрю."
    w7 "Хорошо. (Меня не покидает мысль, что где то я видела эту миссис Бакфет...)"
    return
