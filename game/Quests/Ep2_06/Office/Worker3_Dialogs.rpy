# близняшка 1
label worker3_look:
    mt "Две близняшки."
    mt "Они думают что они красивые?"
    mt "Они ошибаются! Фи!"
    return

label worker3_dialogue_workplace:
    mt "У нее есть сестра... И обе они занимаются составлением каких-то бестолковых отчетов."
    mt "Мне не о чем с ней говорить."
    return

label worker3_dialogue_office:
    w3 "Миссис Бакфет, можно?"
    menu:
        "Да, заходи.":
            m "Да, заходи."
            w3 "Миссис Бакфет, в офисе очень жарко, нам нужен кондиционер."
            m "А что, его нет?"
            w3 "В этом помещении нет и никогда не было."
            m "Эту проблему очень просто решить!"
            m "Откройте окна!"
            w3 "Да, но это не совсем..."
            m "Отлично, а теперь иди и продолжай работать."
            mt "Никчемные люди... Все время что-то требуют..."
#            mt "Да, без кондиционера работать не комфортно... Может стоит как-нибудь помочь им..."
            return
        "Я занята.":
            m "Я занята, приходи завтра."
            w3 "Ладно, но у меня проблема..."
            m "Ты что, плохо слышишь!? Я сейчас занята!"
            return
