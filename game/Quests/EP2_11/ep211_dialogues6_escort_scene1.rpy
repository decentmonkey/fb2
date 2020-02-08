default monicaEscortClientHotel1 = False  # Моника согласилась пойти с клиентом в номер


# Моника сидит за столиком в ожидании клиента
label ep211_escort_scene1_1:
    mt "Так, Моника. Соберись!"
    mt "Не надо так нервничать."
    mt "Ты в любой момент можешь послать всех к черту и уйти."
    # к столику подходит полный мужчина, очкарик. в приличном костюме. с виду интеллигентный интеллигент
    client "Добрый вечер, Мисс."
    client "Я Вас раньше здесь не видел. Как вас зовут?"
    m "Добрый вечер, Мистер."
    m "Меня зовут [monica_hotel_name]."
    client "[monica_hotel_name]. Какое прекрасное имя. Как и его обладательница."
    client "Я очень рад, что сегодня проведу вечер с Вами, [monica_hotel_name]."
    # Моника смотрит на него, размышляя
    mt "Хмм... Разговаривает вежливо, выглядит вполне прилично."
    mt "Думаю, от него не стоит ожидать никаких извращений..."
    client "Позволите мне сразу пригласить Вас в номер, [monica_hotel_name]?"
    mt "..."
    menu:
        "Уйти отсюда!":
            # Моника нерешительно
            mt "Нет! Я не могу это сделать!"
            m "Я..."
            m "Я не смогу с Вами пойти..."
            m "Я... Я не работаю здесь!"
            m "Я просто зашла поесть в ресторан..."
            client "О, извините, Мисс."
            client "Наверное, я перепутал столик."
            # Моника встает и уходит
            return False
        "Пойти в номер с клиентом.":
            $ monicaEscortClientHotel1 = True # Моника согласилась пойти с клиентом в номер
            pass
    mt "Это же совсем нестрашно."
    mt "Это просто обычный неудачник."
    mt "Наверное, приходит сюда раз в месяц в день зарплаты. Фи!"
    mt "Что-то пойдет не так - я просто уйду отсюда."
    mt "Хммм..."
    mt "Они мне тогда сказали, что будут давать мне заказы..."
    mt "Только с проблемными клиентами."
    mt "..."
    mt "Мне нужно сказать этой никчемной администраторше, что у меня клиент."
    mt "Может, она скажет, что с ним не так."
    # Моника смотрит на клиента
    m "Да, мы можем пойти в номер."
    m "Только мне нужно отойти на пару минут."
    client "Конечно, [monica_hotel_name]."
    client "Я буду ждать тебя у лифта."
    return

# Моника приходит на ресепшн
label ep211_escort_scene1_2:
    m "У меня клиент. Он зовет пойти с ним в номер..."
    reception "Я уже в курсе..."
    reception "Это один из наших постоянных клиентов."
    reception "Девочки не любят работать с ним."
    m "Почему?"
    mt "Вроде он не похож на извращенца."
    reception "У него не встает, но он никак не хочет смириться с этим..."
    reception "Он всегда заказывает девочек и мурыжит их до утра."
    reception "И, как правило, безрезультатно."
    reception "Потом скандалит и обвиняет девочек в том, что они плохо работают."
    mt "!!!"
    m "То есть... Если он скажет, что я плохо работаю, то..."
    reception "Штраф."
    mt "Вот сучка!"
    m "Ты же сама говоришь, что дело в клиенте, а не в девочках!"
    m "Какой еще штраф?!"
    reception "Это правило нашего ВИП Эскорта."
    mt "Что за бред!!!"
    reception "И я переоделась бы на твоем месте..."
    reception "Иди в служебный коридор."
    reception "Там можно найти что-нибудь, что возбудит этого клиента."
    m "Но..."
    reception "Все! Иди. Не заставляй клиента ждать тебя!"
    m "..."
    reception "Быстро!"
    # затемнение, прошло 5 мин, Моника выходит из служебного коридора
    # идет мимо ресепшена в сторону лифта, под платьем видно черное белье с поясом и чулками
    return


# Моника с клиентм возле лифтов в отеле
label ep211_escort_scene1_3:
    client "[monica_hotel_name], я Вас уже заждался."
    client "Пройдемте в номер!"
    client "Мне уже не терпится посмотреть, что у Вас под платьем..."
    mt "..."
    mt "Так, Моника, соберись!"
    mt "Тебе надо представить, что ты [monica_hotel_name]."
    mt "А не Моника Бакфетт."
    mt "А это просто обычный неудачник."
    mt "Наверное, приходит сюда раз в месяц в день зарплаты. Фи!"
    mt "Что-то пойдет не так - я просто уйду отсюда."
    return

# Моника с клиентом в номере отеля
label ep211_escort_scene1_4:
    # клиент сидит на кровати, Моника растерянно стоит перед ним
    m "Что мне нужно сделать?"
    mt "Дал бы денег просто так и отпустил бы..."
    mt "У меня нет никакого желания делать для него что-то."
    mt
    client "Для начала [monica_hotel_name] должна снять платье..."
    mt "Моника, не переживай."
    mt "Тебе нечего стесняться. У тебя великолепное тело."
    mt "..."
    mt "Он, наверняка, никогда не видел такой красивой женщины, как я."
    # она снимает платье и стоит перед клиентом голая
    # тот ее рассматривает внимательно
    mt "Сейчас он разденется и начнет лапать мое прекрасное тело. Фу!"
    # клиент не раздевается
    client "[monica_hotel_name], присаживайтесь рядом со мной."
    # Моника садится на кровать, клиент опускается на колени на пол перед ней
    client "Если [monica_hotel_name] позволит мне целовать ее ножку..."
    client "Я буду щедр с Мисс."
    # Моника смотрит на него удивленно
    mt "Он хочет целовать мне ноги?"
    mt "Да еще и платить за это?!"
    mt "Он это серьезно?!"
    mt "???"
    mt "Может, я ослышалась?"
    m "Мистер, Вы хотите целовать мою ногу?"
    client "Да, Мисс. Позвольте Вашу ножку."
    m "..."
    # Моника протягивает ему ногу и он начинает целовать ее, берет пальчики в рот, облизывает
    # Монике приятно
    mt "О, как же это..."
    m "Ммммм..."
    mt "Это приятно..."
    mt "Черт!"
    mt "Я готова работать так каждый вечер."
    # клиент отстраняется от ее ноги
    client "А теперь [monica_hotel_name] возьмет мой палец в свой ротик..."
    client "И пососет его..."
    # Моника смотрит удивленно на его руку, он улыбается
    mt "???"
    menu:
        "Нет, я не смогу!":
            # Моника нерешительно
            mt "Фу! Нет! Я не могу это сделать!"
            m "Я..."
            m "Я не смогу..."
            m "Я... Я не предоставляю такую услугу!"
            client "Но, Мисс... Мне сказали, что..."
            m "Нет. Я не буду этого делать!"
            # Моника встает и уходит
            return False
        "Сделать, как требует клиент.":
            pass
    # Моника с отвращением смотрит на его руку
    mt "Это унизительно и..."
    mt "Противно!"
    mt "Но он сказал, что будет щедр..."
    mt "Все же это не какое-то там гадкое извращенство..."
    # Моника с отвращением, но все приближает губы к его руке
    mt "Главное, чтобы меня не стошнило прямо на него."
    # она прикасается к его руке губами и берет в рот его палец
    client "Соси его!"
    client "Оооооо!!!"
    client "О, дааааа!"
    client "Как же приятно! Ещееее!!!"
    # в процессе он другой рукой расстегивает ширинку, достает член и дрочит, пока Моника сосет его палец
    # клиент дрочит, пока его палец во рту у Моники, и кончает на постель
    client "ААААААА!!!"
    mt "Фу! Это было мерзко!"
    # клиент доволен, застегивает штаны
    client "[monica_hotel_name] старалась и мне очень понравилось."
    # Моника молча смотрит на него, вытирается
    m "..."
    # он встает и оставляет на кровати купюры
    client "Здесь 700 долларов. Я обязательно приду к Вам еще раз, [monica_hotel_name]." # уходит
    # Моника смотрит на деньги
    mt "700 долларов?!"
    mt "Я заработала 700 долларов, облизывая палец незнакомому мужчине!"
    mt "..."
    mt "Меньше всего хочется отдавать половину этой сучке на ресепшене..."
    mt "Может, уйти и больше просто не приходить сюда?"
    mt "Что она мне сделает?"
    mt "С другой стороны, здесь я за вечер могу заработать такие большие деньги."
    mt "А она меня больше не пустит в ресторан."
    mt "Нет, мне не стоит пока терять эту возможность заработка."
    $ log1 = _("Пойти на ресепшн и отдать 50 процентов от заработка администратору.")
    return

# Моника после клиента идет на ресепшен
label ep211_escort_scene1_5:
    # китаянка стоит за стойкой ресепшена
    m "Клиент заплатил 700 долларов."
    reception "И остался доволен."
    reception "Ты хорошо поработала ртом."
    mt "!!!"
    m "Откуда ты?.."
    reception "Я все знаю..."
    reception "Это моя работа!"
    reception "Вот твои деньги."
    # отдает ей 350 долларов
    reception "Завтра можешь приходить снова."
    reception "На сегодня все. Клиенты не любят использованный товар."
    mt "Вот сучка!"
    mt "Откуда она знает, что я... Работала ртом?!"
    mt "Она подглядывала?!"
    mt "!!!"
    # Моника уходит
    return

# если Моника хочет уйти, не отдавая денег
label ep211_escort_scene1_6:
    mt "Я пока не могу так рисковать!"
    mt "Эта сучка меня не пустит больше в ресторан, если я не отдам ей 50 процентов."
    mt "А мне не выгодно терять такой заработок."
    mt "Но я обязательно потом что-нибудь придумаю: чтобы не делиться с ней!"
    mt "..."
    return

# в неделю максимальный заработок 5500 баксов
# если заработала 5500 в отеле, то фотосессии и контракт со Стивом недоступны

# Моника, выйдя из отеля после того, как обслужила клиента
label ep211_escort_scene1_7:
    # не рендерить!
    mt "Я сегодня за вечер заработала 350 долларов."
    mt "Неплохой заработок, учитывая мою временную ситуацию."
    mt "Возможно, мне стоит пересилить себя и поработать здесь еще какое-то время."
    mt "Быть может, у меня получится зарабатывать еще больше."
    mt "Мне нужно будет прийти сюда завтра."
    mt "..."
    mt "Я ведь в любой момент смогу отказаться и уйти."
    return

# Моника, выйдя из отеля после того, как отказалась обслуживать клиента
label ep211_escort_scene1_8:
    # не рендерить!
    mt "Я никогда не смогу решиться на такое!"
    mt "Я Моника Бакфетт, а не какая-то проститутка!"
    return
