default dialogue_5_dance_strip_20_flag1 = False

# Паб. Разговор с Эшли (Моника украла чаевые).
label dialogue_5_dance_strip_1:
    # Эшли орет на Монику, что та украла чаевые (ep27_dialogues7_pub8)
    # после их диалога появляется меню выбора, где строка "отработать на сцене" кликабельна
    # выбор Моники: отработать на сцене
    # Моника шокирована, что ей нужно будет танцевать, как стриптизерше, да еще и на сцене
    mt "На сцене?!" # растерянно
    mt "!!!"
    m "Я должна буду выйти на сцену?!"
    m "Но..."
    ashley "Никаких 'но'!" # раздраженно
    ashley "Или ты идешь на сцену или убираешься отсюда!"
    m "Как я буду танцевать? Я... Я не смогу..."
    mt "Я, Моника Бакфетт! Буду танцевать стриптиз! На сцене в грязном пабе в трущобах!"
    mt "Это немыслимо!!!"
    mt "Одно дело танцевать у пилона для одного-двух неудачников в подворотне..."
    mt "Они все равно никогда не узнают, кто я такая..."
    mt "А сцена..."
    mt "Это все равно, что фотосессия для обложки журнала, который увидят миллионы!"
    mt "Боже! А вдруг меня кто-нибудь узнает!!!"
    mt "!!!"
    m "Я ни разу не танцевала... Я не знаю, как... Я стесняюсь!" # неуверенно
    ashley "А чего здесь стесняться?"
    ashley "Вышла, задом покрутила у пилона и дело сделано!"
    ashley "Тем более, с таким задом, как у тебя..." # многозначительно улыбается
    ashley "Ты быстро сможешь отработать долг и даже заработать неплохие деньги."
    ashley "Так что попробуй. Тут нет ничего страшного."
    ashley "А я с удовольствием посмотрю на твою попку на сцене!"
    mt "Черт! Если я сейчас откажусь, она меня выгонит с работы..."
    mt "Как подумаю, что мне нужно выйти на сцену..."
    ashley "Ну? Чего ты ждешь? Иди в гримерку."
    ashley "Тебе сначала нужно подготовиться к выступлению, переодеться..."
    ashley "Вернее, раздеться!" # улыбается
    mt "..."
    # Моника в растерянности. Выбор: идти в гримерку или уйти
    menu:
        "Идти в гримерку.":
            pass
        "Уйти.":
            mt "Нет! Я не смогу!!!"
            mt "Я не опущусь до уровня этих девушек у пилона!"
            m "Я... Мне нужно время подумать..."
            m "Сегодня я точно не готова это сделать..."
            return 1
    # Моника выбирает идти в гримерку
    mt "С другой стороны..."
    mt "Если и правда получится быстро отработать долг перед Эшли..."
    mt "..."
    mt "Схожу сначала в гримерку. Возможно, там есть приличные сценические костюмы..."
    mt "Хотя сомневаюсь что в этой дыре есть что-то подходящее для такой леди как Я..."
    $ log1 = _("Идти в гримерку, чтобы подготовиться к выступлению на сцене.")
    $ log1 = _("Мне нужно отработать долг $500, выступая на сцене в пабе.")
    return

# Паб. Гримерка танцовщиц. Разговор Моники с рыжей стриптизершой.
# После того, как Моника не отдала чаевые и была наказана. Появляется меню отработать чаевые на сцене.
# После этого, танцует каждый день только рыжая до этого диалога.
label dialogue_5_dance_strip_2:
    # Моника стоит в дверях гримерки, рыжая сидит возле зеркала боком к ней, полуголая
    # cмотрит с пренебрежением
    mt "Фи, это же просто подсобка, а не гримерка!"
    mt "И все такое... старое!"
    mt "Как здесь можно готовиться к выступлениям?!"
    # к Монике поворачивается рыжая, смотрит на нее неприветливо
    stripper "Это ты новая танцовщица что-ли?.." #осматривает Монику с ног до головы
    stripper "М, понятно..."
    mt "???"
    # и отворачивается
    stripper "Увижу тебя рядом со своими вещами - скажу Джо, что ты у меня украла что-нибудь." # не глядя на Монику
    stripper "Советую держаться подальше."
    # Моника неприятно удивлена таким теплым приемом
    mt "..."
    mt "И я рада познакомиться..."
    mt "Как грубо!"
    mt "Всего лишь какая-то стриптизерша из трущоб!"
    mt "Ей, видимо, неизвестно, что такое воспитание и манеры..."
    # Моника зло смотрит на нее и проходит в гримерку
    mt "Мне надо надеть сценический костюм. Которого у меня нет..."
    mt "Что же делать?"
    mt "Попросить у этой хамки что-нибудь из одежды?"
    # Моника смотрит на рыжую
    mt "..."
    # рыжая поворачивается к Монике
    stripper "Чего уставилась?!" #разговаривает высокомерно
    stripper "Тебе на сцену через пять минут, чего ты ждешь?"
    stripper "Или ты пойдешь в этом наряде для бомжей?"
    # Моника смотрит на нее с неприязнью
    m "Мне не выдали сценический костюм. Я не знаю, в чем выходить на сцену."
    stripper "Сценический костюм?!"
    stripper "Аха-ха!!!"
    stripper "Может, тебе еще личного ассистента и гримера предоставить?!"
    stripper "Аха-ха-ха!"
    mt "..." #Моника убивает ее взглядом
    # рыжая снова отворачивается к зеркалу
    stripper "Ты же не думаешь, что я тебе дам свою одежду?!"
    stripper "Иди танцуй голая!"
    mt "Вот стерва!!!"
    mt "!!!" # отворачивается от рыжей
    mt "Что же мне теперь делать?" # растерянно
    mt "Выйти на сцену в этой одежде?"
    mt "Но я не могу идти на сцену в таком виде!"
    mt "Кто-нибудь из этих неудачников узнает меня!"
    # с негодованием
    mt "И не хватало еще, чтобы мое лицо узнал кто-то за пределами этих трущоб..."
    mt "..."
    mt "Где эта Эшли?!"
    mt "В чем, по ее мнению, я должна танцевать?!"
    $ log1 = _("Спросить у Эшли костюм для выступления.")
    $ log1 = _("Эта рыжая стриптизерша слишком многое себе позволяет. Как она смеет так общаться со мной?!")
    return

# гримерка - один выход. Перед танцами выход ведет ко сцене. После танцев выход ведет к диалогу с Эшли или Джо (если ловит ее)
# Далее Моника оказывается в локации паба (как обычно)
# Локация сцены (крупным планом сцена и Моника стоит перед ней). Для танцев надо нажать на цену (look или walk)
# walk - начало танца
# выйти назад в гримерку

# Мысли Моники, когда смотрит на сцену.
label dialogue_5_dance_strip_4n:
    # не рендерить!
    mt "Грязная заляпанная сцена! Фи!"
    mt "Я не верю, что мне приходится танцевать на ней!"
    mt "Мне! Монике Бакфетт!!!"
    return

# Моника после первого посещения гримерки идет к барной стойке к Эшли. Ей нужен костюм для выступления.
# Паб. Возле барной стойки. Эшли там нет, только Джо. Разговор Моники с Джо.
label dialogue_5_dance_strip_3:
    # Моника с негодованием
    m "Где Эшли?"
    joe "[monica_pub_name], можешь спросить у меня. Что ты хотела?"
    joe "Я тебе помогу решить любой вопрос!"
    m "Мне не в чем выступать на сцене!"
    m "В этой одежде я выходить туда не собираюсь!"
    m "..."
    # Джо улыбается
    joe "Не вижу здесь никакой проблемы."
    joe "Иди голая! У тебя тогда будет больше чаевых."
    # Моника зло
    m "Конечно, нет! Я ни за что не буду танцевать голая!"
    m "!!!"
    m "Мне нужна какая-нибудь одежда для сцены!"
    # Джо удивленно
    joe "Ну, а я чем могу помочь?"
    joe "Попроси одежду у другой стриптизерши."
    m "Она сказала, что не даст мне ничего..."
    m "..." # ждет от него ответа
    joe "Ну хорошо. Сегодня на сцену можешь не выходить."
    joe "Эшли я скажу, что ты будешь отрабатывать долг, начиная с завтрашнего дня."
    joe "{c}Приходи завтра{/c}."
    joe "Будет работать Клэр. Она тебе даст что-нибудь из одежды."
    # Джо отворачивается, продолжает свою работу. Моника сердито
    mt "{c}Завтра{/c} мне предстоит снова вернуться в эту ужасную гримерку, фи!"
    mt "Да еще и придется знакомиться с еще одной хамкой!"
    mt "!!!"
    $ log1 = _("Поговорить в пабе с другой стриптизершей.")
    return

# Мысли Моники на сцене. В зависимости от уровня corruption.
label dialogue_5_dance_strip_4a:
    mt "Мне хочется спрятаться подальше от всех этих похотливых взглядов!"
    return
label dialogue_5_dance_strip_4b:
    mt "Я должна держаться! Я сильная!"
    return
label dialogue_5_dance_strip_4c:
    mt "Мне просто нужно сделать несколько движений у пилона."
    mt "Они же просто будут смотреть."
    return
label dialogue_5_dance_strip_4d:
    mt "Нужно относиться к этому как Клэр. Я просто позволяю этим мужчинам смотреть на свою красоту..."
    mt "...недоступную для них красоту!"
    return
label dialogue_5_dance_strip_4e:
    mt "Сегодня хочется сделать так, чтобы у этой рыжей не осталось поклонников в этой дыре!"
    mt "Звезда здесь может быть только одна - Я. А она даже не конкурентка мне... У меня вообще не может быть конкуренток!!!"
    return
label dialogue_5_dance_strip_4f:
    mt "И не забывать про Молли... Надо поставить ее на место... В подворотню со шлюхами!"
    return
label dialogue_5_dance_strip_4g:
    mt "Я не буду снимать с себя жилет!"
    mt "Не хватало еще, чтобы эта толпа неудачников пялилась на мою прекрасную грудь!!!"
    return
label dialogue_5_dance_strip_4h:
    mt "Если я сниму жилет, то заработаю больше денег..."
    mt "Они же просто будут смотреть... на голую грудь [monica_pub_name]."
    return
label dialogue_5_dance_strip_4i:
    mt "Я не буду так крутиться на пилоне! Это пошло!"
    return
label dialogue_5_dance_strip_4j:
    mt "Я не буду вставать в такую откровенную позу!"
    return
label dialogue_5_dance_strip_4k:
    mt "Я не готова так позировать! Это уже слишком!"
    return
label dialogue_5_dance_strip_4l:
    mt "Я ни за что не буду танцевать голой! Ни за какие деньги!"
    return
label dialogue_5_dance_strip_4m:
    mt "Все! С меня хватит!!!"
    mt "Я на сегодня наработалась [monica_pub_name]!"
    mt "Не хочу больше видеть эту толпу пьяных неудачников!"
    return

# Крики посетителей из зала во время выступления Моники.
label dialogue_5_dance_strip_5a:
    customers "Эй, смотри, какая телка!"
    return
label dialogue_5_dance_strip_5b:
    customers "Охренеть!"
    return
label dialogue_5_dance_strip_5c:
    customers "Кто это такая? Я ее раньше не видел!"
    return
label dialogue_5_dance_strip_5d:
    customers "Это новая стриптизерша? Вау!"
    return
label dialogue_5_dance_strip_5e:
    customers "Давай, покрути своей задницей!"
    return
label dialogue_5_dance_strip_5f:
    customers "Давай, покажи класс, детка!"
    return
label dialogue_5_dance_strip_5g:
    customers "О, да! Вот это сиськи!"
    return
label dialogue_5_dance_strip_5h:
    customers "Детка, спускайся сюда! У меня для тебя есть кое-что!"
    return
label dialogue_5_dance_strip_5i:
    customers "Эй, хочешь этих хрустящих купюр? Снимай свои трусики!"
    return
label dialogue_5_dance_strip_5j:
    customers "Покажи нам свою киску!"
    return
label dialogue_5_dance_strip_5k:
    customers "Эй, красотка, иди к нам!"
    return
label dialogue_5_dance_strip_5l:
    customers "Снимай с себя эти тряпки и пошли в приват!"
    return
label dialogue_5_dance_strip_5m:
    customers "О да! Детка, ты супер!"
    return

# Паб. Моника возвращается в паб на другой день, после знакомства с рыжей.
# Она еще не танцевала на сцене. Нужен костюм. При клике на Джо или Эшли начинается диалог с Эшли.
label dialogue_5_dance_strip_6:
    # Эшли вопросительно
    ashley "А, ты пришла?"
    ashley "Я уже думала, ты не вернешься..."
    ashley "В прошлый раз я так и не увидела эту попку на сцене голой..." # с улыбочкой
    mt "Ты ее и не увидишь голой!"
    mt "Тем более, на этой сцене!!!" # сердито
    m "Мне не в чем было выходить на сцену..."
    m "..."
    ashley "Так в чем проблема?" # удивленно
    ashley "У девочек в гримерке полно одежды для выступления."
    ashley "Иди в гримерку и попроси что-нибудь из их шмоток."
    ashley "А лучше выходи на сцену вообще без одежды... Будет больше чаевых!" # многозначительно улыбается
    mt "!!!"
    m "Я не буду танцевать без одежды!" # сердито
    ashley "Тогда иди в гримерку и договаривайся с Клэр."
    ashley "Или отдавай $ 500 и можешь не танцевать."
    mt "..."
    # Моника в растерянности. Выбор: отдать деньги, идти в гримерку или уйти
    menu:
        "Отдать деньги":
            m "Эшли..."
            m "Вот $ 500..."
            ashley "Я так и знала, ха-ха!"
            ashley "Ладно, так уж и быть. Теперь ты можешь снова работать здесь."
            ashley "Но не испытывай моего терпения!"
            return 1
        "Идти в гримерку.":
            pass
        "Уйти.":
            mt "Нет! Я не смогу!!!"
            mt "Я не опущусь до уровня этих девушек у пилона!"
            m "Я... Мне нужно время подумать..."
            m "Сегодня я точно не готова это сделать..."
            return 0
    # Моника выбирает пойти в гримерку
    mt "Возможно, у этой Клэр найдется приличный костюм..."
    $ log1 = _("Идти в гримерку, чтобы подготовиться к выступлению на сцене.")
    return 2


# Паб. Моника возвращается в паб на другой день, после того, как отказалась выйти на сцену.
# Она еще не была в гримерке. При клике на Джо или Эшли начинается диалог с Эшли.
label dialogue_5_dance_strip_7:
    # Эшли вопросительно
    ashley "А, ты пришла?"
    ashley "Ты, наконец-то, решила отработать деньги?"
    ashley "Или ты готова вернуть долг?"
    m "Мне нужна работа..." # растерянно
    ashley "Тогда чего ты ждешь? Иди в гримерку!"
    ashley "Тебе сначала нужно подготовиться к выступлению, переодеться..."
    ashley "Вернее, раздеться!" # улыбается
    mt "!!!"
    # Моника в растерянности. Выбор: отдать деньги, идти в гримерку или уйти
    menu:
        "Отдать деньги":
            m "Эшли..."
            m "Вот $ 500..."
            ashley "Я так и знала, ха-ха!"
            ashley "Ладно, так уж и быть. Теперь ты можешь снова работать здесь."
            ashley "Но не испытывай моего терпения!"
            return 1
        "Идти в гримерку.":
            pass
        "Уйти.":
            mt "Я, Моника Бакфетт, на этой грязной сцене?!"
            mt "Нет! Я не смогу!!!"
            mt "Я не опущусь до уровня этих шлюх у пилона!"
            m "Я... Мне нужно время подумать..."
            m "Сегодня я точно не готова это сделать..."
            return 0
    # Моника выбирает идти в гримерку
    mt "Если это единственный способ быстро отработать долг перед Эшли..."
    mt "..."
    mt "Схожу сначала в гримерку. Возможно, там есть приличные сценические костюмы..."
    $ log1 = _("Идти в гримерку, чтобы подготовиться к выступлению на сцене.")
    $ log1 = _("Мне нужно отработать долг $ 500, выступая на сцене в пабе.")
    return


# Паб. Гримерка. Разговор Моники со второй стриптизершей.
# Следующий приход после начала цепочки квестов
label dialogue_5_dance_strip_8:
    # брюнетка стоит спиной к Монике, переодевается, Моника стоит в дверях
    mt "Это и есть вторая стриптизерша?"
    mt "Надо приготовиться к знакомству со второй хамкой." # с воинственным настроем
    mt "Она, наверное, тоже возомнила себя звездой, как та рыжая стерва..."
    mt "Звездой в грязном пабе в трущобах!.." # высокомерно
    # Брюнетка поворачивается к Монике, она после выступления в черной маске
    stripper "Привет." # без улыбки, спокойно
    stripper "Молли мне говорила, что у нас новенькая. Это ты?"
    # Моника готовилась не к такому знакомству, растерянно
    m "..."
    m "Д-да... Привет..."
    stripper "Я Клэр. А ты?"
    m "Я [monica_pub_name]. А Молли это та рыжая стриптизерша?"
    clare "Да." # с ехидной улыбкой
    clare "Она тут звезда и очень гордится этим."
    clare "С ней лучше дружить и не вставать у нее на пути."
    mt "Звезда! Ха-ха! Стриптизерша со звездной болезнью!"
    mt "Похоже, эта Клэр единственная в этой дыре, кто может нормально общаться."
    clare "Ты давно в стриптизе, [monica_pub_name]?"
    m "Нет. Сегодня будет мое первое выступление..."
    mt "Танцы у пилона на улицах трущоб - не в счет!" # если были сцены в трущобах с ситизенами
    clare "Не волнуйся." # дружелюбно
    clare "Я выступаю уже несколько лет и мне очень нравится."
    m "Нравится?!" # удивленно
    m "Я думала такое делают только из-за денег..."
    clare "Для меня это искусство. Мне нравится делиться своей красотой и видеть восторженные взгляды мужчин."
    clare "Это занятие не является источником денег для меня."
    mt "Хм... Искусство?.."
    mt "Возможно, если так к этому относиться, то намного проще выходить на сцену."
    mt "Но я не представляю себе такого отношения к этому."
    mt "Сами по себе танцы полуголой на публике отвратительны."
    mt "И я не изменю своего отношения к этому никогда!"
    mt "!!!"
    clare "[monica_pub_name], почему ты не переодеваешься?"
    clare "В чем ты будешь выступать?"
    clare "Тебе уже пора выходить на сцену."
    # Моника проходит в гримерку и подходит к Клэр. Та стоит возле вешалки.
    m "У меня нет одежды для сцены..."
    m "Эшли сказала, что я могу спросить одежду у тебя."
    clare "Без проблем. Ты можешь взять вот это." # отворачивается к вешалке, потом кладет одежду для Моники на стул рядом
    # Моника в это время смотрит на ее фигуру
    mt "А из этой Клэр получилась бы неплохая модель..."
    mt "Конечно, до Мелани, а тем более до меня, ей далеко, но все же."
    mt "И что она забыла в этой дыре, тем более, что она тут не из-за денег..."
    # Клэр поворачивается к Монике
    clare "К вещам Молли лучше не приближайся."
    clare "Наша звезда очень ревностно к этому относится." # с ехидной улыбкой
    clare "У меня полно подобных шмоток."
    clare "Можешь этот костюм оставить себе."
    m "Серьезно?!" # удивленно
    m "..." # смотрит на вещи на стуле
    mt "Мне придется надевать на себя ЭТО?"
    mt "Фи! Какой вульгарный костюм!"
    mt "Да еще и после стриптизерши!"
    mt "Какой ужас!"
    mt "Я, Моника Бакфетт, буду танцевать полуголая! В дешевом пабе для толпы неудачников!!!"
    mt "Я не могу поверить в это!"
    menu:
        "Надеть костюм с жилетом.":
            pass
        "Надеть только трусики.":
            m "Я не выйду на сцену с голой грудью!!!"
            return False
    # Клэр отвернулась к вешалке, Моника снимает с себя свою одежду
    mt "Одно дело трущобы..." # если были сцены в трущобах с ситизенами
    mt "Там, конечно, приходилось показывать себя всяким неудачникам."
    mt "Но тут сцена!"
    mt "И этих неудачников целая толпа!!!"
    mt "Для меня быть на сцене - это все-равно что позировать на фотосессии перед всем миром."
    mt "Это не идет ни в какое сравнение с тихой подворотней, где меня никто не знает."
    mt "!!!"
    # Моника надевает костюм
    mt "..."
    mt "Я очень надеюсь, что в этой маске мое лицо никто не узнает..."
    mt "..."
    mt "Так, мне надо собраться и сделать это!"
    mt "Это не я, а [monica_pub_name]."
    mt "Для [monica_pub_name] в этом нет ничего страшного."
    # Клэр поворачивается и смотрит на переодетую Монику
    clare "Отлично. Только..."
    # внимательно смотрит на Монику
    clare "Кое-чего тебе не хватает."
    clare "Сразу видно, что у тебя нет опыта выступления на сцене."
    mt "???"
    # Клэр берет со столика в руки флакон
    clare "Тебе нужно намазать тело этим маслом."
    clare "Тогда ты будешь выглядеть более эффектно на сцене."
    clare "[monica_pub_name], давай я тебе помогу?"
    menu:
        "Взять у Клэр масло и намазаться самой.":
            pass
        "Позволить Клэр намазать меня маслом.":
            # Клэр намазывает ее маслом
            clare "А у тебя отличная фигура, [monica_pub_name]."
            mt "Она что, ко мне пытается пристать, как Эшли?!"
            mt "Я не хочу связываться с еще одной лесбиянкой!"
            clare "Мужчины в зале с ума сойдут, когда тебя увидят."
            mt "Я к этому привыкла."
            mt "Мужчины всегда сходили по мне с ума..."
            clare "Ты сегодня будешь звездой, [monica_pub_name]."
            mt "Конечно, буду! Мне нет здесь равных!"
            mt "И не только здесь! Мне нет равных нигде!"
            clare "Таким шикарным ногам и такой попе, как у тебя, позавидует любая модель."
            clare "Ты просто создана для обложки какого-нибудь модного журнала."
            mt "Хм... Хорошо, что она их не читает."
            mt "Боюсь себе даже представить, если меня здесь кто-нибудь узнает."
            return 1
    # Клэр, осматривая Монику
    clare "Вот теперь ты выглядишь на миллион баксов!"
    mt "Я всегда выгляжу на миллион баксов... И не только выгляжу... Я и стою..."
    mt "Миллиарды..."
    mt "Но, думаю Клэр не умеет даже считать до стольки..."
    clare "Давай, тебя там уже ждут!"
    mt "Черт. Черт! Черт!!!"
    $ log1 = _("Выйти на сцену паба и танцевать.")
    $ log1 = _("Похоже, Клэр единственная в этой дыре, с кем можно нормально общаться.") # квест лог
    return

# Паб. Перед сценой. Разговор Моники с Джо.
# Джо ловит Монику перед подъемом на сцену первый раз
label dialogue_5_dance_strip_9a:
    # Моника смотри на Джо у сцены
    # не рендерить!
    mt "Что это Джо делает здесь?"
    mt "Зачем этот жирный слизняк вертится у сцены?"
    return

label dialogue_5_dance_strip_9:
    # Джо стоит перед выходом на сцену
    joe "[monica_pub_name], а ты горячая штучка!"  # смотрит похотливо
    m "..." # раздраженно
    joe "Только, жилет этот тут лишний."
    joe "Если хочешь чаевых, то сними это с себя!"
    joe "Местные девочки танцуют без одежды."
    # если видел грудь Моники
    if pubMonicaWaitressTipsPunishmentJoeStage >= 2:
        $ notif(_("Моника показывала Джо свою грудь."))
        joe "А твоих малышек наши посетители очень оценят, я их уже оценил!"
    #
    # если видел попу Моники
    if pubMonicaWaitressTipsPunishmentJoeStage >= 3:
        $ notif(_("Моника показывала Джо свою попу."))
        joe "И твоя попа также бесподобна. Тебе не стоит прятать ее от наших ребят!"
    #
    m "???" # удивленно и зло
    menu:
        "Выйти на сцену в жилете.":
            pass
        "Снять жилет.":
            m "Я не выйду на сцену с голой грудью!!!"
            return False
    return

# Паб. Гримерка танцовщиц. Моника, после выступления.
label dialogue_5_dance_strip_10:
    # не рендерить!
    # Моника возвращается в гримерку, там уже нет Клэр
    mt "Чувствую себя такой грязной после всех взглядов и криков этих пьяниц!"
    mt "Мне хочется поскорее отмыться!!!"
    mt "Надо немного потерпеть... Это когда-нибудь закончится."
    mt "И я смогу выбраться из этого кошмарного дна... Я все сделаю для этого!!!"
    return


# Паб. Моника выходит из гримерки. Если пытается снова пойти на сцену, хотя уже танцевала
label dialogue_5_dance_strip_11:
    # не рендерить!
    mt "На сегодня уже достаточно танцев."
    mt "Вернусь сюда в другой день. Возможно, удастся заработать больше чаевых."
    return

# Паб. Моника выходит из гримерки. Если идет в сторону барной стойки, появляется Эшли.
# Разговор с Эшли после первого выступления Моники.
label dialogue_5_dance_strip_12:
    # Эшли требовательно
    ashley "Ну что, [monica_pub_name], сколько ты заработала сегодня?"
    m "???"
    m "Что значит 'заработала'?! Я танцевала здесь!!!"
    m "Разве этого не достаточно?!" # возмущенно
    ashley "Здесь надо не просто танцевать, а зарабывать деньги!"
    ashley "Если бы ты показала публике свою грудь или голую попку..."
    ashley "То тебе определенно дали бы несколько долларов."
    m "Я не собираюсь этого делать!!!"
    ashley "А придется! Как ты собираешься возвращать мне долг?"
    ashley "Ты думала, что будешь просто танцевать?"
    ashley "Ты мне будешь отдавать свои чаевые, а я буду постепенно списывать твой долг."
    m "!!!" # Моника офигевает
    ashley "Надеюсь, в следующий раз ты заработаешь хоть что-то на чай..."
    ashley "Для этого достаточно будет снять жилетку на сцене."
    m "..."
    return

# Паб. Моника выходит из гримерки. Если идет в сторону барной стойки, появляется Эшли.
# Регулярный разговор с Эшли после выступлений Моники.
label dialogue_5_dance_strip_13:
    # Эшли требовательно
    ashley "[monica_pub_name], сколько ты заработала сегодня?"
    m "Сегодня я заработала [monica_strip_tips_today]."
    ashley "Тебе осталось отдать мне еще [monica_strip_forgiveness_money_left]."
    ashley "Если бы ты повертела своей попкой без трусиков, то отработала бы деньги гораздо быстрее..."
    ashley "А я с удовольствием посмотрела бы на это." # с улыбочкой
    m "Я не собираюсь этого делать!!!" # возмущенно
    m "!!!"
    mt "Одни извращенцы вокруг!"
    ashley "На сегодня ты свободна, [monica_pub_name]."
    ashley "Приходи завтра."
    return


# Паб. Гримерка танцовщиц. Разговор Моники с рыжей Молли.
# Далее, после первого выступления, танцует только рыжая
label dialogue_5_dance_strip_14:
    # рыжая сидит возле зеркала, Моника стоит в дверях
    mt "Черт, я совсем забыла, что сегодня здесь звезда трущоб!"
    mt "Я не хочу разговаривать с этой хамкой!"
    # Моника проходит в гримерку и молча переодевается в одежду Клэр
    # рыжая смотрит на Монику высокомерно
    molly "Тебя здороваться не учили?.."
    # рыжая отворачивается
    molly "Понабирают на работу шлюх из подворотни..."
    # Моника поворачивается и зло смотрит на нее
    mt "!!!"
    menu:
        "Клэр предупреждала, что лучше не конфликтовать с ней":
            # отворачивается от Молли, послав ей убийственный взгляд
            pass
        "Да, Клэр предупреждала, но я же не могу просто проигнорировать такую наглость":
            m "Ты это сейчас про себя, да?" # со злостью
            m "Я такого же мнения после нашего с тобой так сказать 'знакомства'!"
            mt "Этой хамке самое место в подворотне со шлюхами! Как она здесь оказалась?"
            # рыжая поворачивается к Монике и смотрит вопросительно и высокомерно
            molly "Мне послышалось или ты что-то сейчас мне сказала?"
            # Моника ей также высокомерно в ответ
            m "Мне не о чем разговаривать с такой как ты!"
            m "И, тем более, о чем-то спорить!"
            m "Я не собираюсь опускаться до твоего уровня!!!"
            m "!!!"
            # рыжая офигевает от такого, ничего не отвечает и зло смотрит на Монику
            molly "!!!"
    # Моника отворачивается от нее
    mt "Не могу выносить ее присутствия!"
    mt "Надо скорее одеться и идти на сцену."
    menu:
        "Надеть костюм с жилетом.":
            pass
        "Надеть только трусики.":
            mt "Я не выйду на сцену с голой грудью!!!"
            return False
    $ log1 = _("Выйти на сцену паба и танцевать.")
    return

# Паб. Гримерка танцовщиц. Моника, после выступления.
label dialogue_5_dance_strip_15:
    # не рендерить!
    # Моника возвращается в гримерку, там уже никого нет
    mt "В этот раз уже было попроще... Не хватало еще привыкнуть к этому!"
    mt "Надо немного потерпеть... Это когда-нибудь закончится."
    mt "И я смогу выбраться из этого кошмарного дна... Я все сделаю для этого!!!"
    return


# Паб. Гримерка танцовщиц. Разговор Моники с брюнеткой Клэр.
# Следующий приход после второго разговора с рыжей танцовщицей
label dialogue_5_dance_strip_16:
    # брюнетка стоит спиной к Монике, переодевается, Моника стоит в дверях
    # Моника задумчиво смотрит на Клэр
    mt "Эта Клэр могла бы являть свою красоту с обложки журнала..."
    mt "А не танцуя в пабе перед толпой пьяных неудачников!"
    # Клэр в маске поворачивается к Монике, с улыбкой
    clare "Привет, [monica_pub_name]. Ну как ты?"
    clare "Эшли говорит, что у тебя уже лучше получается. Она тобой довольна."
    m "Хм. Я не удивлена, что Эшли довольна мной."  # проходит в гримерку и начинает раздеваться
    mt "Еще бы она была недовольна! Она теперь может на меня пялиться." # сердито
    mt "Как и ее муж-неудачник!"
    clare "Надеюсь, у тебя не было конфликтов с ней?"
    clare "Про Эшли ходят не очень хорошие слухи."
    clare "Так что, лучше не связывайся с ней..."
    m "Да? Я не знала..." # удивленно
    m "Спасибо за предупреждение..."
    mt "Эта озабоченная Эшли со своим таким же озабоченным мужем уже достали меня!"
    mt "Кто бы предупредил меня заранее, что с ними не стоит связываться?!"
    # Моника переодевается
    menu:
        "Надеть костюм с жилетом.":
            pass
        "Надеть только трусики.":
            m "Я не выйду на сцену с голой грудью!!!"
            return False
    # Клэр берет со столика в руки флакон
    clare "Ты забыла намазаться маслом для тела..."
    clare "[monica_pub_name], давай я тебе помогу?"
    menu:
        "Взять у Клэр масло и намазаться самой.":
            pass
        "Позволить Клэр намазать меня маслом.":
            # Клэр намазывает ее маслом
            clare "Какая же у тебя отличная фигура, [monica_pub_name]."
            mt "Она что, снова ко мне пытается пристать, как Эшли?!"
            clare "Мужчины в зале с ума сойдут, когда тебя увидят."
            mt "Я к этому привыкла."
            mt "Мужчины всегда по мне с ума сходили..."
            clare "Ты сегодня будешь звездой, [monica_pub_name]."
            mt "Конечно, буду! Мне нет здесь равных!"
            mt "И не только здесь! Мне нигде нет равных!"
            clare "Таким шикарным ногам и такой попе, как у тебя, позавидует любая модель."
            clare "Ты просто создана для обложки какого-нибудь модного журнала."
            mt "Хм... Хорошо, что она их не читает."
            mt "Боюсь себе даже представить, если меня здесь кто-нибудь узнает."
            return 1
    # Клэр, осматривая Монику
    clare "Выглядишь сногсшибательно."
    clare "Иди и покажи им, кто здесь звезда."
    mt "Черт! Снова эта сцена! И толпа пьяных неудачников!"
    $ log1 = _("Выйти на сцену паба и танцевать.")
    return

# Джо перехватывает Монику перед входом на сцену
# Паб. Перед сценой. Разговор Моники с Джо.
label dialogue_5_dance_strip_17:
    # Джо стоит перед выходом на сцену
    joe "[monica_pub_name], это костюм Клэр?"  # смотрит похотливо
    m "Да." # раздраженно
    joe "Я смотрю, ты с ней подружилась..."  # подмигивает
    m "Тебе что с этого?" # раздраженно
    joe "Выяснишь для меня, как к ней подкатить?"
    m "???" # смотрит на него как на идиота
    joe "Она тут ни с кем не общается..."
    joe "И никого к себе не подпускает..."
    joe "На приваты не соглашается, хотя предложений много..."
    joe "А она тут работает уже не один год. И я все это время не знаю, как подойти к ней..."
    # выходит Клэр с нагайкой, включает строгую училку
    clare "Что здесь происходит?!" # смотрит на Джо строго
    clare "Тебе чего надо от [monica_pub_name]?!" # ткнув его в грудь нагайкой
    joe "Я... Мне... Я просто..." # растерянно мямлит и смотрит на нагайку
    clare "Я просто пойду сейчас к твоей жене!" #с угрозой
    clare "И расскажу, чем ТЫ тут занимаешься!"
    joe "Ч-ч-чем???"
    clare "Пристаешь к [monica_pub_name]!!!"
    joe "Я... Я не пристаю!"
    joe "Не надо ничего говорить Эшли!"
    clare "Тогда пошел отсюда! Быстро!!!" # ткнув его снова нагайкой
    joe "!!!"
    # Джо растерян, уходит
    clare "Вот кобель!"
    clare "!!!"
    # смотрит на Монику, улыбается
    clare "Если снова будет приставать, скажи мне. Он меня боится."
    m "Спасибо, Клэр."
    # Клэр уходит
    mt "Когда я выберусь из этого дна, заведу себе такой же хлыст от извращенцев!"
    return


# Паб. Гримерка танцовщиц. Моника, после выступления.
label dialogue_5_dance_strip_18:
    # не рендерить!
    # Моника возвращается в гримерку, там уже никого нет
    mt "В этот раз уже было попроще... Не хватало еще привыкнуть к этому!"
    mt "Надо немного потерпеть... Это когда-нибудь закончится."
    mt "И я смогу выбраться из этого кошмарного дна... Я все сделаю для этого!!!"
    return


# Паб. Моника выходит из гримерки. Если идет в сторону барной стойки, появляется Эшли.
# Разговор с Эшли после третьего (?) выступления Моники. Эшли прощает Монику (только первый раз)
label dialogue_5_dance_strip_19:
    # Эшли требовательно
    ashley "[monica_pub_name], сколько ты заработала сегодня?"
    m "Сегодня я заработала [monica_strip_tips_today]."
    ashley "Тебе осталось отдать мне еще [monica_strip_forgiveness_money_left]."
    ashley "Но я решила, что прощу тебе остаток долга." # улыбается
    m "Простишь?" # удивленно
    m "???"
    ashley "В дни твоих выступлений в пабе всегда полно посетителей."
    ashley "И это приносит моему пабу хорошую выручку."
    ashley "Поэтому, если ты продолжишь танцевать, то сможешь зарабатывать."
    m "Я смогу забирать чаевые?"
    ashley "Да. Так что не спеши отказываться от танцев."
    ashley "Официанткой ты столько не заработаешь..."
    ashley "А на сцене... Да еще и с голой попкой..."
    ashley "Ты будешь настоящей звездой, [monica_pub_name]!"
    m "Я не собираюсь выступать голая!!!"
    m "!!!"
    mt "Эта извращенка так и ждет, когда я выйду голая на сцену!"
    mt "Я не буду танцевать голой!"
    mt "Если меня кто-нибудь узнает, несмотря на мою маску..."
    mt "Боюсь даже думать о последствиях!"
    mt "!!!"
    $ log1 = _("Эшли простила мне долг. Теперь я могу зарабатывать, выступая на сцене в пабе Shiny Hole. Неужели для меня это теперь нормально?")
    return

# После этого появляется пункт выбора: Танцевать на сцене
label dialogue_5_dance_strip_20:
    menu:
        "Танцевать на сцене в Shiny Hole.":
            pass
    m "Эшли..."
    ashley "А, это ты..."
    m "Я пришла работать на сцене."
    ashley "Хорошо, [monica_pub_name]."
    ashley "Иди в гримерку. Готовься к выступлению."
    if dialogue_5_dance_strip_20_flag1 == True:
        ashley "Не забудь потом отдать мне часть чаевых."
        ashley "Ты тут вертишь голым задом у пилона не просто так, [monica_pub_name]!"
    $ dialogue_5_dance_strip_20_flag1 = True
    mt "Я не хочу даже спорить с этой хамкой..."
    return


# Паб. Моника выходит из гримерки после выступления на сцене по желанию. Если идет в сторону барной стойки, появляется Эшли.
# Разговор с Эшли после первого выступления по желанию. ОДИН РАЗ!
label dialogue_5_dance_strip_21:
    # Эшли требовательно
    ashley "[monica_pub_name], сколько ты заработала сегодня чаевых?"
    m "Зачем тебе это нужно знать?" # удивленно
    ashley "Ты забыла, что ты здесь работаешь за 30 процентов от чаевых?."
    m "???"
    m "Но ты же говорила, что я смогу забирать чаевые!"
    m "МОИ чаевые! Которые я заработала, выступая на сцене!"
    ashley "Ага. Ты забираешь 30 процентов чаевых, остальное - мне."
    ashley "Тебя что-то не устраиваает?!"
    m "..." # сердито смотрит на Эшли
    mt "Если я сейчас ей откажу, она запретит мне работать здесь..."
    mt "А мне нужна эта работа..."
    mt "Как же меня достала эта Эшли!"
    mt "!!!"
    ashley "Чего ты ждешь?!"
    ashley "Сейчас же давай сюда чаевые или можешь убираться отсюда навсегда!"

    # Моника отдает чаевые
    if monica_strip_tips_today == 0:
        m "Мне никто не дал чевых сегодня..."
        ashley "Надеюсь, в следующий раз ты заработаешь чаевые..."
        ashley "Для этого достаточно будет получше покрутить задом у пилона."
        ashley "Голым задом..."
        m "Я не собираюсь ТАК зарабатывать чаевые!!!"
        ashley "Хм. Все девочки сначала так говорят..." # c улыбкой
        ashley "Завтра приходи работать еще."
    else:
        $ add_money(-monica_strip_tips_today)
        m "Вот чаевые, которые я смогла получить..."
        $ tipsBack = round_down(float(monica_strip_tips_today)*pubMonicaDanceTipsKoeff, 0.05)
        if tipsBack == 0.0:
            $ tipsBack = 0.05
        $ add_money(tipsBack)
        ashley "Хорошо. Вот твои [pubMonicaDanceTipsKoeffText] процентов."
        ashley "И не забывай, что для твоей попки у меня найдется еще работа..." # подмигивает
        m "Меня не интересуют другие способы подработки!"
        mt "Она опять намекает на какую-то грязную работу!"
        mt "Извращенка!"
        mt "!!!"
        ashley "Завтра приходи работать еще."
    return

# Паб. Моника выходит из гримерки после выступления на сцене по желанию.
# Регулярный разговор с Эшли после выступления по желанию. При клике на Джо или Эшли
label dialogue_5_dance_strip_22:
    m "Эшли, я закончила работу."
    ashley "Сколько ты заработала сегодня чаевых, [monica_pub_name]?"
    if monica_strip_tips_today == 0:
        m "Мне никто не дал чевых сегодня..."
    else:
        $ add_money(-monica_strip_tips_today)
        m "Вот чаевые, которые я смогла получить..."
        $ tipsBack = round_down(float(monica_strip_tips_today)*pubMonicaDanceTipsKoeff, 0.05)
        if tipsBack == 0.0:
            $ tipsBack = 0.05
        $ add_money(tipsBack)
        ashley "Хорошо. Вот твои [pubMonicaDanceTipsKoeffText] процентов."
        ashley "Завтра приходи работать еще."
    return



# Моника может уйти, не отдавая чаевые.
label dialogue_5_dance_strip_23:
    menu:
        "Уйти и не отдавать чаевые хозяевам бара.":
            mt "Я не собираюсь отдавать никому мои чаевые!"
            return False
        "Остаться.":
            return True
    return


# Паб. Моника находится в гримерке после выступления на сцене по желанию. Появляется Джо.
# Моника заработала на сцене хорошие чаевые.
label dialogue_5_dance_strip_24:
    # Джо смотрит на Монику похотливо
    joe "[monica_pub_name], ты сегодня заработала хорошие чаевые..."  # с улыбкой
    m "Да. А тебе какое дело до этого, Джо?" # раздраженно
    joe "[monica_pub_name], ты хочешь заработать настоящие деньги?"
    joe "А не эти жалкие несколько баксов?"
    m "На что ты намекаешь, Джо?" # с подозрением
    joe "Есть один клиент..."
    joe "Он хочет, чтобы ты станцевала для него..."
    joe "Только для него."  # подмигивает
    m "Приватный танец?!" # зло
    m "Ты за кого меня принимаешь?!"
    mt "Как он смеет предлагать мне подобное?!"
    mt "Чтобы Моника Бакфетт танцевала приват!!!"
    mt "И для кого?! Для какого-нибудь неудачника?!"
    mt "Для которого лучшее развлечение в жизни - придти в эту дыру и выпить пива?!"
    mt "!!!"
    mt "Ни за какие деньги Я не стану этого делать!!!"
    m "Я не собираюсь зарабатывать ТАКИМ способом, Джо!" # сердится
    m "И не хочу слышать больше подобных предложений!!!"
    m "!!!"
    joe "[monica_pub_name], может ты все-таки подумаешь хорошо?"
    joe "Это и правда неплохие деньги..."
    m "???" # смотрит на него как на идиота
    m "Нет!!!"
    joe "Хорошо, [monica_pub_name]."
    joe "Но если подобные предложения от клиентов еще будут, то я тебе скажу об этом."
    joe "Вдруг ты передумаешь..." # Джо подмигивает и уходит
    m "..."
    return

version

##### в 0.10
# Паб. Гримерка танцовщиц. Разговор Моники с рыжей Молли.
label dialogue_5_dance_strip_5:
    # рыжая сидит возле зеркала, Моника стоит в дверях
    # Моника думает, черт, я совсем забыла, что сегодня здесь звезда трущоб. не хочу разговаривать с этой хамкой
    # Моника проходит в гримерку и молча переодевается в одежду Клэр
    # рыжая ей, не поворачиваясь, "Эшли говорит, что твоими выступлениями якобы довольны посетители паба и хотят видеть тебя чаще на сцене..."
    # Моника поворачивается и зло смотрит на нее "И что?"
    # Моника про себя, на что эта хамка намекает? злится, что она может быть уже и не звезда?
    # рыжая смотрит на Монику зло "Я тебя предупреждаю, шлюха, если из-за тебя я потеряю хотя бы один цент от своего заработка,
    # я сделаю все, что бы тебя выкинули отсюда... или отправлю тебя за решетку... где тебе и место!
    # Моника ей высокомерно в ответ "Что я слышу?.. Мне угрожает сама звезда паба Шайни хол!" "Ты серьезно?! Думаешь, что ТЫ можешь испугать меня чем-то?"
    # рыжая офигевает от такого, ничего не отвечает и зло смотрит на Монику, "!!!"
    # Моника отворачивается, одевается, намазывается сама маслом и выходит на сцену
    return


# Паб. Гримерка танцовщиц. Моника, после выступления.
label dialogue_5_dance_strip_5_2:
    # Моника возвращается в гримерку, там уже никого нет
    # Моника, в этот раз уже было попроще, не хватало еще привыкнуть к этому!
    # думает о том, что надо немного потерпеть, это когда-нибудь закончится и она сможет выбраться из этого кошмарного дна. она все сделает для этого!!!
    return


    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    return
