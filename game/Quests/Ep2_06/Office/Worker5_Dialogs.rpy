# мужик
label worker5_look:
    mt "Этот карьерист метит на место Босса в этом отделе?"
    mt "Наивный дурачок!"
    return

label worker5_dialogue_workplace:
#    m "Послушай, думаю ты знаешь, кто я, а вот я никого тут не знаю."
#    m ""
    m "Мне это не очень интересно. Я здесь не надолго."
    m "Но, все-же, расскажи мне про работников этого отдела."
    w5 "Миссис Бакфет! Вы сегодня прекрасно выглядите и обратились как раз по адресу."
    m "Я всегда хорошо выгляжу. Не подлизывайся к Боссу, тебе это не поможет."
    m "Итак?"
    w5 "Вон там сидит Марта. Она занимается отчетами."
    w5 "Близняшки Элла и Эмма.. Они тоже делают отчеты."
    w5 "Хотя что говорить... Мы все тут делаем отчеты."
    w5 "Эту толстуху зовут Грета. Она работает тут дольше всех."
    w5 "Вон там сидит Лин. Она у нас недавно."
    w5 "Нашего системного администратора ты, возможно, видела. Я даже не знаю как его зовут."
    w5 "Ну и наконец Я! Самый компетентный сотрудник в этом отделе и, думаю, скоро его глава."
    w5 "Меня зовут Джон."
    mt "Ну и мерзкий же ты тип, Джон."
    m "Я поняла, возвращайся к работе!"
    return

label worker5_dialogue_office:
    w5 "Миссис Бакфет, я бы хотел поговорить о моем повышении!"
    menu:
        "Давай поговорим.":
            m "Давай поговорим."
            w5 "Миссис Бакфет, Вы же знаете, я очень ответственный и без меня этот отдел просто развалится."
            w5 "Еще эта толстуха Грета так и наровит занять мое законное место."
            w5 "И я буду Вам бесконечно благодарен если Вы..."
            m "Достаточно..."
            m "Чем чаще ты задаешь мне такие вопросы тем дальше от тебя эта должность."
            mt "И что это вообще за должность? Почему он думает, что этому отделу нужен какой-то мифический начальник кроме меня?"
            w5 "Да, понял. Ухожу. Но знайте, миссис Бакфет, Вы всегда можете на меня расчитывать."
            return
        "Не в этой жизни.":
            m "Повышении?!"
            m "Не сегодня. Выйди и закрой за собой дверь."
            w5 "Хорошо. Понимаю, Вы очень заняты. Ну ничего, в другой раз."
            return
