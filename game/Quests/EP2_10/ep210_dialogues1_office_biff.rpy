# Пункты меню окроются сразу 2 после достижения ур. 3 у Биффа. (после презентации) (мы добавляем 100)
label ep210_dialogues1_office_biff_1a:
#    menu:
#        "Раздеться и принимать различные модельные позы.":
	img 22908
    m "Биф, мне обязательно это делать?"
    biff "Если цыпочка хочет порадовать папочку, то да."
	img 22909
    biff "Давай, цыпочка. Я жду."
    mt "Сволочь!"
    # Моника раздевается и встает в позу лицом к Бифу
	img 22910
	img 22911
	img 22912
	img 22913
	img 22914
    biff "Зачетные сиськи, цыпочка. Теперь покажи свой зад папочке!"
    # Моника поворачивается к Бифу задом
	img 22915
	img 22916
	img 22917
	img 22918
    biff "Цыпочка старается, цыпочка хорошая."
    # принимает следующую позу
	img 22919
    biff "Надеюсь, в следующий раз цыпочка порадует папочку еще чем-нибудь."
	img 22920
    m "..."
    mt "Ненавижу этого придурка!"
    pass
    return

label ep210_dialogues1_office_biff_1b:
#        "Раздеться и встать на колени задом к Бифу.":
	img 22908
    m "Биф, мне обязательно это делать?"
    biff "Ты же знаешь, что обязательно."
	img 22909
    biff "Давай, без лишних разговоров. Не утомляй меня!"
    mt "Сволочь!"
    # Моника раздевается и встает на колени задом к Бифу
	img 22921
	img 22922
    biff "Теперь нагнись!"
	img 22923
	img 22924
	img 22925
	img 22926
	img 22927
	biff "Отличная задница!"
	img 22928
    # встает на четвереньки
	img 22929
	img 22930
    biff "Хорошая цыпочка!"
    biff "Надеюсь, в следующий раз я увижу что-нибудь новое от цыпочки..."
	img 22920
    m "..."
    mt "Ненавижу этого придурка!"
    pass
    return

label ep210_dialogues1_office_biff_1c:
#        "Раздеться и лечь на пол раздвинув ноги.":
	img 22908
    m "Биф, мне обязательно это делать?"
    biff "Ага. Чем сегодня ты порадуешь папочку?"
	img 22909
    mt "Сволочь!"
    # Моника раздевается и садится на пол лицом к Бифу
    biff "Покажи папочке, что там у тебя между ног."
	img 22931
	img 22932
	img 22933
	img 22934
	img 22935
	img 22936
	img 22937
    biff "Давай, давай. Пока ты меня ничем не удивила..."
    biff "Папочке становится скучно."
	img 22938
    mt "!!!"
    mt "Интересно, если я возьму эту бутылку с его стола..."
    mt "И долбану его по голове... Я сразу его убью?"
	img 22939
    mt "..."
	mt "Ладно, еще не время. Пока мне надо притворяться цыпочкой..."

    # Моника раздвигает ноги
	img 22940
	img 22941
    biff "Ну вот. Другое дело!"
	img 22942
    biff "Теперь я вижу, что цыпочка старается."
	img 22943
	img 22944
	img 22945
    biff "Надеюсь, в следующий раз цыпочка придумает еще что-нибудь интересное..."
	img 22920
    m "..."
    mt "Ненавижу этого придурка!"
    pass
    return
# Если уже был ур.2, то он станет 3
# Если не было ур.2, то становится 2 с чем-то, ждем 3
# Фотосесси дают максимум 100 (сделать проверку)


# если у Моники закончена фотосессия в последнем юбкае и она уже работает в офисе
# вечером, когда Моника приходит к Биффу просить его о работе (чтобы заработать 5к долларов)
# кабинет Биффа
label ep210_dialogues1_office_biff_1:
    # при выборе пункта меню "Спросить о работе"
    img 12783
    m "Биф..."
    m "Я хотела узнать у тебя..."
    m "Есть-ли еще работа?"
    m "Мне нужны деньги..."
    img 12785
    biff "У папочки всегда найдется работа."
    biff "Но для этого нужно быть хорошей цыпочкой."
    biff "И развлечь папочку. Папочке сегодня скучно..."
    img 13895
    mt "???"
    img 13900
    m "Что ты имеешь ввиду?"
    m "Эти кастинги после фотосесий?"
    img 12847
    biff "Нет. Фотосессии сегодня у цыпочки не будет..."
    img 13891
    m "Тогда о какой работе ты говоришь?" # удивленно
    img 13892
    biff "У меня для тебя есть другая работа."
    biff "Но об этом позже..."
    biff "Позови сюда Сиську!"
    # Моника удивленно смотрит на него
    img 12790
    m "..."
    img 12792
    mt "Что еще за работа?"
    mt "Что этот придурок придумал на этот раз?!"
    img 12829
    biff "Чего ты смотришь?! Давай быстрее!"
    # пару минут спустя заходит секретарша и встает рядом с Моникой перед столом Бифа
    img 15853
    secretary "Да, Мистер Биф. Вы меня звали?"
    # обе стоят перед Бифом и вопросительно на него смотрят
    img 15854
    biff "Значит так!"
    biff "Мне надоело смотреть на тебя в этом скучном юбкае." # обращается к Монике
    # Моника с секретаршей переглядываются удивленно
    img 15855
    m "???"
    secretary "???"
    img 12836
    biff "Я вот думаю, какую одежду для работы тебе дать..."
    biff "Мне кажется, что одежда Сиськи тебе очень подойдет!"
    img 15856
    m "ЧТО?!" # офигевает
    img 12841
    biff "Ага. Чего ты так удивляешься?" # обращается к Монике
    img 15857
    biff "Сиська! Снимай свои штаны!"
    biff "Пусть она их наденет!" # обращается к секретарше, тычет пальцем в сторону Моники
    img 15858
    secretary "Мистер Биф, прямо здесь? Сейчас?"
    img 15859
    biff "Да. Здесь и сейчас. Давай, снимай!"
    img 15860
    m "!!!"
    secretary "..."
    secretary "Но... Я... Мистер Биф..." # смущена, растерянно смотрит на него, потом на Монику
    img 15861
    m "Я не собираюсь надевать ничьи штаны!" # Моника возмущается
    m "И я не буду работать в таком виде!!!"
    img 15862
    m "Как ты себе это представляешь, Биф?!"
    m "!!!"
    img 15863
    biff "Если ты вообще хочешь работать здесь..."
    biff "То сейчас же заткнешься!"
    biff "И молча наденешь штаны Сиськи!"
    # Моника зло смотрит на него
    img 15864
    mt "Ненавижу!!!"
    mt "Как вообще мог этот тупой придурок оказаться в МОЕМ кресле???"
    mt "!!!"
    img 15865
    menu:
        "Сделать, как приказывает Биф.": #corruption
            pass
        "Я не собираюсь делать этого!":
            img 15866
            m "Нет, Биф!" # сердито
            m "Я не буду этого делать!"
            img 15867
            biff "Это еще почему?"
            biff "Цыпочка, Я тебе приказываю, значит ты должна это сделать!"
            biff "И твоего мнения тут никто не спрашивал!"
            img 15868
            m "Я могу носить другой офисный юбка..."
            m "Но не такой!"
            m "И мерять я подобное не собираюсь!"
            img 15869
            mt "Идиот! Придурок!!!"
            img 15870
            biff "Ты не получишь работу, пока я тебя не увижу в штанах Сиськи!"
            img 15871
            mt "Да пошел ты!"
            mt "Я найду другой способ заработать эти деньги!"
            # Моника уходит. В след. раз, когда Моника будет просить у Бифа работу, разговор возобновляется.
            return False
    # Моника молча смотрит на Бифа
    img 15872
    mt "Если я сейчас откажу ему..."
    mt "Он меня может выгнать с работы."
    mt "Конечно, я могу найти другой способ заработать эти деньги..."
    img 15873
    mt "Но тогда я упущу возможность работать здесь, в МОЕМ журнале."
    mt "А значит, могу упустить шанс выгнать эту сволочь отсюда!"
    mt "Черт!" # смотрит на секретаршу, та на нее
    img 15874
    secretary "..."
    secretary "Миссис Бакфетт?"
    secretary "Вы... Мне... Мне снимать свои брюки?"
    img 15875
    mt "!!!"
    m "Да!" # смотрит зло на Бифа, тот сидит довольный
    m "Только я надену их с трусиками!"
    img 15876
    biff "Нет, забудь про это."
    biff "Ты забыла, что я запретил тебе носить трусики на работе?"
    img 12865
    biff "Ты наденешь только штаны."
    biff "Про трусики разговора не было..."
    biff "Цыпочка." # улыбается
    # секретарша снимает штаны и стоит, зажавшись, прикрывшись руками
    img 15878
    w
    img 15877
    mt "!!!"
    mt "Моника, как могло такое произойти, что ты надеваешь брюки своей секретарши?!"
    mt "Прямо в своем кабинете по приказу какого-то никчемного Бифа?!"
    # Моника снимает с себя юбку и надевает брюки. встает лицом к Биффу
    # Биф оценивающе смотрит на нее
    img 15879
    w
    img 15880
    w
    img 15881
    biff "Слушай, цыпочка! А тебе идет! Аха-ха!"
    biff "А ну-ка, теперь повернись ко мне задом!"
    img 15882
    mt "!!!" # зло смотрит, поворачивается
    img 15883
    biff "А теперь нагнись! Покажи папочке, какая ты послушная цыпочка!"
    # секретарша на все это смотрит с ужасом
    img 15884
    mt "АААААА!!!" # злится
    mt "Ненавижу!!!" # нагибается
    # Биф разглядывает ее зад
    img 15885
    biff "Твой зад в этих штанах недостаточно хорошо видно."
    biff "Снимай! Я придумаю для тебя что-нибудь другое."
    # Моника с секретаршей одеваются, Моника бросает на Бифа злобные взгляды
    img 15861
    secretary "Я могу идти, Мистер Биф?"
    img 15886
    biff "Ага. Иди, Сиська."
    img 15887
    # секретарша уходит
    img 13906
    biff "Ты на сегодня тоже свободна."
    biff "Папочка рад, что цыпочка была послушной сегодня."
    img 13900
    mt "!!!"
    img 12907
    biff "Жду тебя здесь завтра."
    img 13896
    m "Биф... А что насчет работы?"
    img 13893
    biff "Говорю же тебе, приходи завтра!"
    img 12792
    mt "Сволочь!"
    mt "Надеюсь, завтра он даст мне работу... Мне нужны деньги..."
    # Моника уходит
    # открываются пункты "Раздеться и принимать различные модельные позы" и "Раздеться и встать на колени задом к Бифу"
    # в заданиях появляется "Зайти завтра к Бифу, узнать про работу."
    $ log1 = _("Зайти завтра к Бифу, узнать про работу.")
    return

# Моника вышла из кабинета Бифа после примерки штанов
# приемная, где сидит секретарша Бифа
label ep210_dialogues1_office_biff_2:
    # при клике на секретаршу
    img 12773
    secretary "Миссис Бакфетт, мне так неудобно, что вам пришлось делать это!"
    img 12769
    m "Ты ни в чем не виновата, дорогая."
    m "А этот Биф - редкостная сволочь!"
    m "Ну ничего. Еще немного и я верну себе свое место. И все станет, как прежде."
    return

# если Моника повторно подошла к Бифу в этот же день
label ep210_dialogues1_office_biff_2b:
    m "Биф... А что насчет работы?"
    biff "Говорю же тебе, приходи завтра!"
    mt "Сволочь!"
    mt "Надеюсь, завтра он даст мне работу... Мне нужны деньги..."
    return

# мысли Моники на след. день, если хочет уйти из офиса, не посетив Бифа
# не рендерить!
label ep210_dialogues1_office_biff_2a:
    mt "Мне нужно зайти к этой сволочи Бифу."
    mt "Он сказал, что есть работа для меня."
    return

# Моника приходит спросить Бифа о работе
# кабинет Биффа, вечер
# в диалоговых сценах про "показать зад" юзаем уже имеющиеся арты!!!
label ep210_dialogues1_office_biff_3:
    # Бифф, как обычно сидит за столом, ноги на столе
    img 15888
    m "Биф..."
    m "Я пришла узнать насчет работы..."
    img 12781
    biff "А, цыпочка пришла!"
    biff "Цыпочка хорошо себя вела вчера..."
    biff "Она надела штаны Сиськи и показала папочке свой зад. Аха-ха."
    img 15864
    mt "!!!"
    mt "Вот сволочь!"
    img 12907
    biff "Кстати, о заде цыпочки..."
    biff "Если цыпочка хочет остаться на этой работе и сидеть в кресле босса..."
    biff "А также зарабатывать хорошие деньги на фотосессиях."
    img 12785
    biff "А не стать снова двадцатидолларовой шлюхой, как ты привыкла..."
    biff "То ты должна провести одно мероприятие!"
    # Моника смотрит на Биффа подозрительно
    img 12799
    m "Что еще за мероприятие?"
    img 12808
    biff "Как тебе известно, Я руководитель Модного Журнала."
    biff "Это теперь детище папочки и он заботится о нем!"
    img 15869
    mt "Это мое детище, урод!!!"
    img 12845
    biff "Как самому лучшему руководителю, мне пришла в голову гениальная идея!"
    biff "Привлечь в журнал дополнительные средства!"
    biff "Завтра у нас состоится встреча с потенциальными инвесторами."
    img 12815
    biff "И цыпочке надо будет провести презентацию перед этими уважаемыми людьми."
    biff "Надо будет показать рост продаж нашего журнала. И правильность выбранного нами курса!"
    img 15889
    mt "Что за бред он несет?! О каком правильном курсе он говорит?!"
    mt "!!!"
    img 15890
    biff "В твоих интересах сделать так... Чтобы инвесторы согласились вложить свои деньги в развитие журнала!"
    biff "Поэтому именно ты проведешь эту презентацию."
    biff "И сделаешь ты это так, чтобы они ни на секунду не усомнились..."
    img 12829
    biff "Что ты и есть Моника Бакфетт, а не ее дешевая подделка!"
    biff "Хотя, тебе сложно адаптироваться к жизни в образе Моники Бакфетт..."
    # Моника злится, но молча слушает
    img 15891
    mt "!!!"
    img 13902
    biff "Все привыкли, что здесь босс Моника Бакфетт..."
    biff "А ты, кукла, очень похожа на нее, как ты помнишь."
    biff "И это, пока что, единственный твой талант..."
    img 13888
    biff "Возможно, у тебя еще есть что-нибудь..."
    biff "Но ты уже давно не развлекала папочку чем-нибудь новым."
    img 15892
    mt "Сволочь!"
    mt "!!!"
    img 15893
    biff "Короче, на презентации расскажешь им, что журнал успешен..."
    biff "Что раскупается огромными тиражами по всей стране..."
    img 15894
    biff "Что сейчас взят новый курс, который позволит выйти журналу на мировой уровень."
    biff "В общем, тебе надо открывать рот и говорить, что бизнес растет. И ничего более."
    # Моника злится, сверлит эту сволочь взглядом
    img 15895
    mt "Никчемный придурок, который решил, что легко соберет деньги с инвесторов!"
    mt "Я не собираюсь учавствовать в этом цирке!"
    img 15896
    m "Какая еще презентация, Биф?!"
    m "Какие еще уважаемые люди?!"
    m "Я не собираюсь кривляться перед кем-то и показывать дурацкие графики!"
    img 15897
    biff "Это уважаемые люди, которые вкладывают деньги в этот журнал, цыпочка!"
    biff "И, если ты, дешевая кукла, притворяющаяся леди..."
    biff "Хочешь, чтобы папочка и дальше платил за твои фотосессии такие деньги, как сейчас..."
    img 15898
    biff "А не столько же, сколько ты привыкла брать за то..."
    biff "Чтобы случайный прохожий засунул член в твой ротик."
    img 15899
    mt "!!!"
    img 15900
    biff "То тебе придется делать то что я тебе говорю!"
    m "Я не двадцатидолларовая шлюха, Биф! Хватит так называть меня!!!" # зло
    img 15901
    biff "Ты именно двадцатидолларовая шлюха!"
    biff "Которую я достал с самого дна и дал работу!"
    biff "Ты дешевая кукла без мозгов, которой я плачу слишком много денег!"
    img 15902
    biff "И, если ты не хочешь вернуться назад и сосать по 20 членов в день..."
    biff "То ты сейчас же заткнешься!!!"
    biff "И вообще! Ты что, решила спорить со мной?!"
    img 12803
    m "Биф, я..!!!" # возмущенно
    img 15903
    biff "Быстро скажи, что ты хорошая цыпочка! Или убирайся отсюда ко всем чертям!!!"
    img 12809
    mt "!!!"
    img 15904
    menu:
        "Я хорошая цыпочка.": #corruption
            pass
        "Я не буду говорить этого!":
            img 15905
            m "Я не собираюсь проводить эту чертову презентацию!" # бомбит
            m "Я не тебе не безмозглая кукла и не шлюха!"
            m "И не цыпочка!!!"
            img 15906
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не сделаешь то, что Я тебе говорю!"
            img 15869
            mt "Да пошел ты!"
            mt "Я найду другой способ зарабатывать деньги!"
            # Моника уходит. В след. визит к Бифу разговор возобновляется (Биф не дает ей фотосессии)
            return False
    # Моника сердито смотрит на Бифа
    img 15895
    mt "Биф ни черта не понимает в развитии журнала."
    mt "Как и не осознает бесполезность собрания инвесторов."
    mt "Хммм. А ведь я могу сделать так, что кто-то из этих инвесторов..."
    img 15907
    mt "Поддержит МЕНЯ - МОНИКУ БАКФЕТТ! И поможет мне вернуть МОЙ журнал!"
    mt "И вышвырнуть, наконец, этого никчемного Бифа с МОЕГО места!!!"
    # Моника улыбается Бифу
    img 12783
    m "Я хорошая цыпочка..."
    img 12785
    biff "Другое дело! А теперь вернемся к разговору о твоем заде, цыпочка..."
    img 15908
    mt "???"
    biff "Покажи мне его! Докажи, что ты хорошая цыпочка!"
    img 15864
    mt "!!!" # злится
    menu:
        "Сделать, как приказывает Биф.": #corruption
            pass
        "Не делать этого!":
            img 15869
            mt "Да сколько можно?!" # бомбит
            mt "Обозвал меня шлюхой и безмозглой куклой!"
            mt "А теперь я еще должна оголить свой зад для него?!"
            mt "Мое великолепное тело создано не для того, чтобы показывать его таким неудачникам, как он!"
            img 15896
            m "Биф, ты же сам говорил, что тебе неинтересно видеть одно и то же." # сердито
            m "Я совсем недавно тебе показывала свой зад в штанах секретарши."
            img 15893
            biff "Цыпочка, ты не получишь никакую другую работу..."
            biff "Пока не сделаешь то, что я тебе говорю!"
            img 15889
            mt "Да пошел ты!"
            mt "Я найду другой способ зарабатывать деньги!"
            # Моника уходит. В след. визит к Бифу разговор возобновляется (не дает больше работы)
            return False
    img 15892
    mt "Мне осталось терпеть издевательства этой сволочи совсем немного!"
    mt "Я не оставлю ему это все безнаказанным!"
    mt "Ненавижу!!!"
    # Моника показывает попу Бифу (юзаем имющиеся арты)
    img 20595
    w
    img 20596
    w
    img 20597
    w
    img 20598
    w
    img 20599
    w
    img 20600
    biff "Хорошая цыпочка. Теперь папочка доволен!"
    biff "Презентация назначена на завтра. Приходи завтра вечером."
    # Моника пристально смотрит на него
    # уход на движок, мысли
    img 12792
    mt "Бифф надеется, что с моей помощью привлечет инвесторов..."
    mt "Чтобы сделать из МОЕГО журнала дешевое порно!"
    mt "Сволочь!"
    mt "!!!"
    mt "Надеюсь, близок тот день, когда я снова займу свое место в этом кабинете..."
    # Моника уходит
    # в заданиях у Моники презентация перед инвесторами
    $ log1 = _("Провести презентацию журнала в кабинете Бифа.")
    return

# мысли Моники на след. день, если хочет уйти из офиса, не проводя презентацию
# не рендерить!
label ep210_dialogues1_office_biff_3a:
    mt "Мне нужно идти к Бифу и провести эту чертову презентацию!"
    return

# Моника заходит в кабинет Бифа (день проведения презентации)
label ep210_dialogues1_office_biff_4:
    # перед столом Бифа семь стульев, на противоположной стене от его стола экран
    img 15909
    m "Биф..."
    m "Я пришла на презентацию..."
    img 15910
    biff "А, цыпочка! Ты как раз вовремя!"
    biff "Позови сюда Сиську!"
    # через минуту заходит секретарша
    img 15911
    secretary "Мистер Биф, я принесла юбку, о которой Вы говорили."
    img 15912
    biff "Ага. Отдай ее этой цыпочке!" # улыбается, смотрит на Монику
    # секретарша протягивает Монике наряд для презентации, потом уходит
    # Моника спрашивает его,  ей сейчас нужно выступать перед инвесторами
    img 15913
    mt "???"
    m "Что это значит? Что еще за юбка?"
    # Бифф мерзко улыбается
    biff "Цыпочка долго не развлекала папочку чем-нибудь новым."
    biff "Папочка даст ей возможность исправить это!"
    img 15914
    mt "Что на этот раз?!"
    img 15915
    biff "Давай, кукла, переодевайся быстрее!"
    img 15916
    m "Что, прямо здесь?!"
    biff "Да-да! Шевели своим задом быстрее!"
    # Моника надевает на себя юбка с открытым задом, начинает возмущаться
    img 22907
    w
    img 15917
    m "ЧТО ЭТО?!"
    m "Я в ЭТОМ должна выступать перед инвесторами?!!!"
    m "!!!"
    img 15918
    mt "Эта сволочь Бифф совсем сдурел?!"
    mt "Что он себе позволяет?!!!"
    mt "Пусть сам надевает ЭТО и ведет презентацию!!!"
    img 15919
    m "Биф! Я не буду в ЭТОМ проводить презентацию!!!"
    # Бифф ей, улыбаясь
    img 15920
    biff "Конечно, будешь, цыпочка!"
    biff "Инвесторам очень понравится этот наряд Моники Бакфетт!"
    biff "Он соответствует новому курсу журнала. Аха-ха!"
    # Моника возмущенно
    img 15921
    m "Подобную юбку может носить только какая-нибудь шлюха! Я не собираюсь это надевать!"
    img 15922
    biff "Ты, видимо, забыла, что ты и есть дешевая двадцатидолларовая шлюха?!"
    biff "Думаешь, если ты похожа на Монику Бакфетт, то я тебя не вышвырну отсюда?!"
    img 15923
    m "!!!"
    biff "Если откажешься проводить презентацию в этой юбке..."
    biff "То можешь прямо сейчас убираться отсюда!"
    biff "Я распоряжусь и тебя сюда больше не пустят! Тебе все ясно, кукла?!"
    # Моника кипит от злости
    img 15924
    mt "ААААААА!!!"
    mt "Ненавижу!"
    img 15925
    m "..."
    m "Мне нужно надеть трусики!"
    biff "Я запретил тебе носить трусики на работе."
    img 15926
    biff "Я тебе каждый раз должен напоминать об этом?"
    # Моника возмущенно смотрит на Бифа и тут дверь открывается и заходят инвесторы
    img 15927
    w
    img 15929
    w
    img 15928
    mt "!!!"
    mt "НЕТ! Только не это!"
    mt "Черт!"
    # инвесторы подходят к ним с Бифом, среди них Стив и Филипп
    img 15930
    mt "Сволочь Биф специально все это подстроил!" # смотрит на Бифа злобно, тот улыбается ей в ответ
    mt "Как я теперь уйду отсюда?!"
    mt "Чтобы уйти, мне придется повернуться к ним спиной..."
    img 15931
    mt "И тогда все эти люди увидят мою... мою..."
    mt "Мою обнаженную попу... О УЖАС!!!"
    mt "!!!"
    # Стив подходит и здоровается с ней, хитро улыбаясь
    img 15932
    steve "Миссис Бакфетт, добрый день!"
    steve "Рад Вас видеть!"
    img 15933
    mt "Какого черта Стив тут делает?!"
    mt "Уж точно не в качестве инвестора... Кто его сюда пустил вообще?!"
    mt "Этот мешок с дерьмом не потратит ни цента на этот журнал!"
    img 15934
    # сама протягивает ему руку, приподнимая уголок губ в подобии улыбки
    # следом за ним подходит и тянет руку Филипп
    img 15935
    # если была сцена в туалете с ним
    if monicaMadeBlowjobToPhilip == True:
        img 15936
        mt "Только не он!!! Я поклялась, что расквитаюсь с этим мерзавцем!"
        mt "И я не буду Моникой Бакфетт, если я не сделаю этого!!!"
    #
    else:
    # если не было сцена в туалете
        img 15936
        mt "Это не тот мерзкий тип, который предлагал мне всякие гадости на вечере в отеле?"
        mt "Весь из себя такой интеллигентный, а на самом деле извращенец! Как и все!"
    #

    # она протягивает ему руку, Филипп наклоняется, целует ей руку, сам смотрит ей в глаза и ухмыляется
    img 15937
    philip "Мэм... Рад нашей встрече..."
    img 15938
    # остальные тоже подходят, здороваются, она слегка им улыбается
    img 15939
    mt "Я знаю многих из этих неудачников..."
    mt "Какой толк от какой-то презентации перед этими болванами?"
    mt "Биф что, думает, что они инвестируют в него хоть цент?!"
    # мужчины рассаживаются на стульях, лицом к экрану
    img 15940
    mt "..."
    mt "Так, Моника, соберись!"
    mt "Тебе нельзя поворачиваться спиной к ним..."
    mt "Просто не поворачиваться спиной и тогда никто не заметит выреза на юбке..."
    # Моника стоит у экрана лицом к мужчинам, на экране показан обычный график роста
    img 15941
    mt "Вроде никто не заметил выреза на моей юбке..."
    mt "Надо быстрее заканчивать с этой никому ненужной презентацией."
    mt "Сейчас я выступлю и уйду, не поворачиваясь спиной к ним."
    mt "Ненавижу сволочь Биффа!"
    mt "!!!"
    # на экране появляется ####1-й график####, Моника обращается к присутствующим
    img 15942
    m "Прошло не так много времени с момента выпуска первого номера журнала."
    m "И уже сейчас наша компания показывает стабильный рост и ежемесячно растущий спрос среди покупателей."
    m "Каждый новый номер нашего журнала расходится многотысячными тиражами по всей стране."
    img 15943
    m "И сейчас, когда СМИ узнали про смену курса журнала... Продажи и интерес со стороны публики только возрос."
    m "Что дает нам уверенность в том, что мы станем журналом номер один не только в стране... Но и во всем мире!"
    # Биф встает, подходит к Монике и дает ей указку, потом встает сзади нее и смотрит, улыбаясь
    img 15944
    w
    img 15945
    mt "!!!" # зло на Бифа
    img 15946
    m "Вы можете посмотреть на график..." # не поворачиваясь спиной к мужчинам, просто держит указку в руке
    img 15947
    mt "Что это за график?" # оглядывается на экран с графиком (рост биткоина)
    img 15948
    m "Который показывает стабильный рост..."
    # один из инвесторов, скрывая улыбку
    img 15949
    investor1 "Миссис Бакфетт..."
    investor1 "Это график роста биткоина..."
    img 15950
    mt "!!!" # снова зло на Бифа
    mt "Придурок!"
    img 15951
    m "Да... Все верно." # неуверенно
    m "..."
    m "Нашим аналитическим отделом был проведен анализ..."
    img 15952
    m "И... По итогу работы был замечен факт..." # неуверенно
    m "Что..."
    m "Что график роста биткоина и график роста продаж нашего журнала совпадают..."
    m "..."
    img 15953
    m "Это значит, что курс биткоина привязан к росту нашего журнала."
    m "Поэтому, инвестируя в журнал, вы обеспечиваете дальнейший уверенный рост наших продаж."
    m "А, следовательно, знаете как поведет себя курс крупнейшей криптовалюты."
    img 15954
    m "Проводя относительно небольшое вложение денег..."
    m "Вы получаете инструмент влияния на самый быстрорастущий рынок электронных платежных средств."
    m "..."
    # инвесторы смотрят на нее, как на дуру
    img 15955
    m "Сейчас, в подтверждение моих слов, мы продемонстрируем вам график роста наших продаж..."
    img 15956
    mt "!!!" # снова зло на Бифа
    # на экране появляется ####2-й график####. Моника оглядывается на экран, не поворачиваясь
    img 15957
    mt "!!!"
    mt "ИДИОТ!" # на Бифа
    img 15958
    m "..."
    m "Как вы видите, явно просматривается динамика роста..."
    # со стула встает Стив и подходит к Монике
    img 15959
    steve "Миссис Бакфетт, позвольте я взгляну поближе..."
    # за ним к Монике подходит Филипп
    img 15960
    philip "Пожалуй, я тоже более детально рассмотрю..."
    # Филипп и Стив встают с разных сторон от Моники и пока что смотрят на график, Биф продолжает стоять сзади
    img 15961
    mt "О нет!!!"
    mt "Они сейчас увидят, что я стою с голой попой!"
    mt "Что мне теперь делать?!"
    img 15962
    menu:
        "Повернуться спиной к Стиву.":
            # поворачивается лицом к Филиппу так, что голый зад видно только Стиву и Бифу
            img 15993
            mt "Об этом узнает только один из них..."
            mt "И пусть только попробует мерзавец Стив рассказать об этом!"
            # Стив поворачивает голову в сторону Моники, замечает вырез на юбке
            img 15994
            steve "!!!" # мерзко улыбается и остается на месте, рассматривая Монику
            img 15995
            w
            img 15996
            steve "Пожалуйста, продолжайте, Миссис Бакфетт. Мы внимательно Вас слушаем."
            img 15997
            m "..."
            img 15998
            m "По прогнозам наших аналитиков..."
            m "Уже через год рост продаж вырастет минимум в два раза..."
            # Филипп роняет телефон
            img 15999
            w
            img 16000
            w
            img 16001
            w
            img 16002
            w
            img 16003
            w
            img 16004
            m "..."
            # приседает и поднимает его, при этом замечает голый зад Моники и разглядывает его
            # Моника замечает это и злится, но продолжает
            img 16005
            mt "Черт!!!"
            mt "!!!"
            img 16006
            philip "Пожалуйста, продолжайте, Мэм..." # улыбаясь
            pass
        "Повернуться спиной к Филиппу.":
            # поворачивается лицом к Стиву так, что голый зад видно только Филиппу и Бифу
            img 15993
            mt "Об этом узнает только один из них..."
            mt "Лучше уж этот извращенец Филипп, чем мерзкий Стив!"
            mt "По крайней мере, есть надежда, что он никому ничего не расскажет..."
            # Филипп поворачивает голову в сторону Моники, замечает вырез на юбке
            img 16007
            philip "!!!" # мерзко улыбается и остается на месте, рассматривая Монику
            img 16008
            w
            img 16009
            philip "Пожалуйста, продолжайте, Миссис Бакфетт. Мы внимательно Вас слушаем."
            img 16010
            m "..."
            img 15998
            m "По прогнозам наших аналитиков..."
            m "Уже через год рост продаж вырастет минимум в два раза..."
            # Филипп роняет телефон
            img 15999
            w
            img 16000
            w
            img 16001
            w
            img 16002
            w
            img 16003
            w
            img 16004
            m "..."
            # приседает и поднимает его, разглядывая голый зад Моники
            # Моника замечает это и злится, но продолжает
            img 16005
            mt "Черт!!!"
            mt "!!!"
            img 16006
            philip "Пожалуйста, продолжайте, Мэм..." # улыбаясь
            pass
    # Стив и Филипп уходят и садятся на свои места
    # Моника берет себя в руки и продолжает
    img 16011
    m "Учитывая смену курса нашего журнала... Мы можем смело рассчитывать на результаты..."
    m "Сравнимые с всемирно известными модными журналами - законодателями в сфере моды..."
    img 15963
    m "Ваша поддержка сейчас принесет вам многомиллионную прибыль уже не более, чем через год."
    m "А ваше имя войдет в историю нашего журнала."
    img 15964
    w
    img 15965
    w
    img 15966
    w
    img 15967
    w
    img 15968
    w
    img 15969
    # Моника, жестикулируя, роняет указку и не приседает, а наклоняется за ней
    # поднимает ее, демонстрируя стоящим сзади все свои прелести
    # на экране появляется ####3-й график####. Моника оглядывается на экран
    img 15970
    mt "!!!" # на Бифа
    m "..."
    img 15971
    m "Как я уже говорила, курс биткоина привязан к росту нашего журнала...."
    m "И сейчас вы можете увидеть, что графики роста действительно совпадают..."
    m "..."
    img 15972
    mt "Не могла себя представить в более глупой ситуации!!!"
    img 15973
    investor2 "Миссис Бакфетт, а откуда такие смелые прогнозы?"
    img 15974
    m "..."
    img 15975
    investor2 "Прежде чем принять окончательное решение, я хотел бы взглянуть на отчеты."
    img 15976
    investor3 "Соглашусь. Меня тоже этот вопрос интересует."
    img 15977
    investor4 "У вас действительно такие высокие показатели?"
    investor4 "Думаю, тут одного вашего графика будет недостаточно."
    investor3 "Нам необходимо документальное подтверждение Ваших слов, Миссис Бакфетт."
    img 15972
    mt "Эти никчемные жадные неудачники еще и задают мне вопросы!!!"
    img 15970
    mt "!!!"  # смотрит зло на Биффа
    # потом смотрит на инвестора и выдавливает из себя улыбку
    img 1597
    m "Да, конечно. Вы сможете ознакомиться с отчетами. А также с прогнозами наших аналитиков."
    m "Я отдам распоряжение своему секретарю и все озвученные материалы будут персонально разосланы вам."
    m "Уверена, что после этого у вас не возникнет никаких сомнений, господа."
    # Моника улыбается, инвесторы продолжают смотреть на нее хмуро
    img 15979
    investor2 "Сначала посмотрим, а потом будем делать выводы, Миссис Бакфетт."
    # улыбка Моники тает
    img 15980
    mt "Кто он вообще такой, чтобы разговаривать со мной так!!!"
    # Бифф выходи из-за спины Моники, улыбаясь обращается к инвесторам
    img 15981
    biff "Господа, поблагодарим Миссис Бакфетт за ее великолепную презентацию!"
    # все хлопают, Моника смотрит на зрителей без эмоций
    # Биф, пока все хлопают, наклоняется к ней и на ухо говорит
    img 15982
    biff "Теперь задача цыпочки сделать так, чтобы все они согласились."
    biff "И мне без разницы, как ты это сделаешь."# отстраняется от нее и улыбается ей
    img 15983
    mt "Что?! Вот скотина!"
    mt "Ненавижу!"
    mt "Ненавижу его!!!"
    img 15984
    mt "!!!"
    mt "Надо подождать пока все уйдут, мне не выйти отсюда в этой дурацкой юбке!"
    # инвесторы встают со стульев и уходят
    img 16370
    biff "До встречи, господа."
    img 16371
    investor4 "До свидания."
    biff "Надеюсь, вы примите верное решение и поддержите наш журнал."
    img 16372
    investor1 "Не сомневаюсь, что приму верное решение. Не факт, что в вашу пользу."
    biff "До свидания. Спасибо, что пришли."
    # Бифф смотрит на Монику, не скрывая насмешки
    # открывается следующий пункт в меню Бифа
    return

# после презентации в кабинете Бифа
label ep210_dialogues1_office_biff_5:
    # Моника стоит в кабинете Бифа, он рядом
    # Моника смотрит на него недовольно, сложив руки
    img 15985
    mt "Теперь я еще должна уговаривать этих всех неудачников инвестировать в журнал!!!"
    mt "Ненавижу их всех!!!"
    mt "!!!"
    img 15986
    mt "Что этот слизняк Стив и этот мерзкий Филипп делали на презентации?!"
    mt "Я не желаю ни одного, ни другого видеть здесь!"
    mt "!!!"
    img 15987
    biff "Папочка доволен своей цыпочкой. Цыпочка хорошо справилась с презентацией."
    biff "Да, кстати!" # смотрит на ее попу
    img 15988
    biff "Папочке было бы очень приятно..."
    biff "Если бы цыпочка носила эту юбку на работе в офисе!"
    biff "Я еще посмотрю на твое поведение..."
    biff "Будешь плохой цыпочкой - заставлю собирать в нем отчеты у сотрудников. Аха-ха!"
    img 15989
    mt "!!!"
    img 15990
    biff "Да, цыпочка теперь должна позаботиться о том..."
    biff "Чтобы все инвесторы вложили свои деньги в журнал!"
    img 15991
    biff "Если хоть один из них откажется..."
    biff "Вышвырну тебя с работы!"
    # Моника смотрит на него с ненавистью
    img 15992
    mt "Ненавижу эту сволочь Биффа!"
    mt "!!!"
    mt "Надо скорее снять с себя эту ужасную юбку!!!"
    return




######### в след. версиях
    # один из инвесторов обратиться к Биффу по вопросу проведения фотосессии Моники для него
    # если Моника соглашается, то открывается очередной пункт меню кастинга у Биффа
