# близняшка 1
label worker3_look:
    img 20305
    w
    img 20306
    mt "Две близняшки."
    mt "Они думают что они красивые?"
    mt "Они ошибаются! Фи!"
    return

label worker3_dialogue_workplace:
    img 20307
    mt "У нее есть сестра... И обе они занимаются составлением каких-то бестолковых отчетов."
    mt "Мне не о чем с ней говорить."
    return

label worker3_dialogue_office:
    img 20342
    w3 "Миссис Бакфет, можно?"
    menu:
        "Да, заходи.":
            m "Да, заходи."
            img 20343
            w3 "Миссис Бакфет, в офисе очень жарко, нам нужен кондиционер."
            img 20344
            m "А что, его нет?"
            img 20345
            w3 "В этом помещении нет и никогда не было."
            img 20346
            m "Эту проблему очень просто решить!"
            m "Откройте окна!"
            img 20347
            w3 "Да, но это не совсем..."
            img 20348
            m "Отлично, а теперь иди и продолжай работать."
            img 20349
            mt "Никчемные люди... Все время что-то требуют..."
#            mt "Да, без кондиционера работать не комфортно... Может стоит как-нибудь помочь им..."
            return
        "Я занята.":
            m "Я занята, приходи завтра."
            img 20347
            w3 "Ладно, но у меня проблема..."
            img 20348
            m "Ты что, плохо слышишь!? Я сейчас занята!"
            return
