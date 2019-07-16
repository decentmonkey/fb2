default worker3Option1Cnt = 0
default worker3Option2Cnt = 0

# близняшка 1
label worker3_look:
    img 20305
    with fade
    w
    img 20306
    with diss
    mt "Две близняшки."
    mt "Они думают что они красивые?"
    mt "Они ошибаются! Фи!"
    return

label worker3_dialogue_workplace:
    music Groove2_85
    img 20307
    with fade
    mt "У нее есть сестра... И обе они занимаются составлением каких-то бестолковых отчетов."
    mt "Мне не о чем с ней говорить."
    return

label worker3_dialogue_office:
    music ZigZag
    img 20342
    with fadelong
    w3 "Миссис Бакфет, можно?"
    menu:
        "Да, заходи.":
            $ worker3Option1Cnt += 1
            m "Да, заходи."
            img 20343
            with fade
            w3 "Миссис Бакфет, в офисе очень жарко, нам нужен кондиционер."
            img 20344
            m "А что, его нет?"
            img 20345
            with diss
            w3 "В этом помещении нет и никогда не было."
            music Groove2_85
            img 20346
            with fade
            m "Эту проблему очень просто решить!"
            m "Откройте окна!"
            img 20347
            with diss
            w3 "Да, но это не совсем..."
            img 20348
            with diss
            m "Отлично, а теперь иди и продолжай работать."
            img 20349
            with fade
            mt "Никчемные люди... Все время что-то требуют..."
#            mt "Да, без кондиционера работать не комфортно... Может стоит как-нибудь помочь им..."
            return
        "Я занята.":
            $ worker3Option2Cnt +=1
            m "Я занята, приходи завтра."
            img 20347
            with diss
            w3 "Ладно, но у меня проблема..."
            music Groove2_85
            img 20348
            with fade
            call bitch(1, "worker3_dialogue_office") from _call_bitch_187
            m "Ты что, плохо слышишь!? Я сейчас занята!"
            return
