
#render+
#сон ночью
label sleep_scene1:
    #Дик, Моника и водитель в машине. День. Моника в платье AfterJail
    #белый экран
    music dream
    img white_screen
    with fade
    dick "Моника..."
    dick "Моника?"
    dick "Моника!"
    #Моника просыпается в машине
    music Power_Bots_Loop
    img 5905
    with Dissolve(1.0)
    m "А? ЧТО?"
    "ГДЕ Я???"

    img 5906
    m "ДИК???"
    "Что ты здесь делаешь?"

    img 5907
    dick "Моника, что значит что я здесь делаю?"
    "Я еду с тобой в ресторан."
    img 5908
    m "В какой ресторан?"

    img 5909
    dick "В самый лучший! В отеле La Grand!"
    img 5910
    dick "Моника, ты себя хорошо чувствуешь?"
    img 5911
    m "Я... Я не знаю..."

    img 5912
    dick "Моника, мне показалось что ты заснула."
    "Ты не выспалась сегодня?"

    img 5913
    m "Я... Заснула?..."
    "Это был сон???"

    img 5914
    dick "Сон? Дорогая, тебе что-то приснилось?"

    music RnB4_100
    img 5915
    with fade
    m "Мне... Да...."
    img 5916
    with Dissolve(0.5)
    "ЭТО БЫЛ СОН!!!"

    img 5917
    with fade
    fred "Мэм. С вами все в порядке?"

    music Stealth_Groover
    img 5918
    m "Фрэд?!?!"
    "ТЫ?!?!"

    img 5919
    fred "Да, мэм?"

    img 5920
    m "Ты уволен, Фред!!!"
    "Едь скорее на место и вон из машины!"

    img 5921
    dick "Дорогая???"
    img 5922
    fred "Миссис Бакфетт, но за что вы хотите уволить меня?"
    "В чем причина? Что за проступок я совершил?"

    img 5923
    m "Что за проступок, ты спрашиваешь?!?!"
    img 5924
    "Ты..."
    "Ты... Я не скажу что ты сделал..."
    img 5923
    "Но этого более чем достаточно для увольнения!"

    img 5925
    fred "Мэм, но я не понимаю..."

    music Hidden_Agenda
    img 5926
    with fade
    m "Значит это все-таки был сон!"
    "Получается Фред этого не делал?"
    img 5927
    "Но нет! Я не смогу находиться рядом с ним после того что я пережила, даже во сне!"

    music RnB4_100
    img 5928
    with fade
    "Сон!"
    "Ура! Сон!"

    music Stealth_Groover
    img 5929
    with fadelong
    m "Ты уволен, Фред!"

    dick "Дорогая???"

    img 5930
    m "Дик, не надоедай мне!"
    "Ты тоже хорош!"
    "Что ты здесь делаешь? Иди к своей секретарше!"

    img 5931
    "Ходи с ней по ресторанам! Ты не достоин меня!"

    img 5932
    dick "С какой секретаршей, Моника?!"
    "Мне нравишься ТЫ!"

    img 5933
    m "Так, Фред! Быстро останови машину!"
    img 5934
    with fade
    "Мистеру Дику надо выйти!"

    img 5935
    with Dissolve(0.5)
    "А мне надо позвонить!"

    img 5936
    dick "..."

    img 5937
    with fade
    m "Так, черт, где мой телефон?!"
    img 5938
    with Dissolve(0.5)
    "Дик, ты не видел его?"

    img 5939
    music Master_Disorder
    with fadelong
    dick "У тебя его не было, Моника."
    "Я не знаю почему, но ты не взяла его..."

    img 5940
    m "???"

    img 5941
    dick "Более того, ты почему-то не носишь свои украшения."
    img 5942
    music Villainous_Treachery
    with Dissolve(0.5)
    "А где твой браслет? Ты всегда одевала его..."
    img 5942
    show screen vignette_screen
    with Dissolve(1.5)
    w
    img 5943
    with Dissolve(0.5)
    m "..."

    img 5944
    with fade
    dick "И трусики, зачем-то ты их тоже не носишь."
    "Почему, Моника?"

    img 5945
    with fade
    m "..."
    img 5946
    with Dissolve(0.5)
    w
    img 5947
    with Dissolve(0.5)
    w
    img 5948
    with Dissolve(0.5)
    m "!!!"

    img 5949
    with fade
    m "Дик... Я..."
    img 5950
    with Dissolve(0.5)
    "Погоди, я не понимаю..."

    img 5951
    dick "Моника, дорогая!"
    "Не переживай!"
    "Все будет хорошо!"
    img 5952
    "Главное не забудь!"

    img 5953
    with fade
    m "Про что я не должна забыть, Дик?"

    img 5954
    with fadelong
    dick "Про галстук..."

    img 5955
    with Dissolve(0.5)
    m "!!!"

    img 5956
    with fade
    dick "У тебя все будет хорошо, Моника!"
    img 5957
    with Dissolve(0.5)
    "Главное помни про галстук и не разбей мое сердце..."

    img 5958
    with Dissolve(0.5)
    m "!!!"
    hide screen vignette_screen

    #Моника просыпается
    music Power_Bots_Loop
    sound snd_woman_scream1a
    if cloth != "Nude":
        img 5959
    else:
        img 7109
    with fade
    mt "АААААХХХ!!!!"

    mt "ГДЕ Я???"

    img 5960
    mt "Что это... что это за дыра?!?!"
    img 5961
    with fade
    mt "Где Юлия?!"

    mt "..."

    img 5962
    with fade
    mt "Черт! Я все вспомнила!"

    mt "Этого не может быть!!!"

    if cloth != "Nude":
        img 5963
    else:
        img 5964
    "НЕТ!!!"
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    #пауза
    #моника сидит думает на кровати, встает
    music Stealth_Groover
    if cloth != "Nude":
        img 5965
        with fade
    else:
        img 5966
        with fade
    mt "Стоп. Моника, не унывай!"

    "Давай подумаем что у нас есть на данный момент."

    if cloth != "Nude":
        img 5967
    else:
        img 5968
    with fade
    "У меня нет денег, нет документов."
    "Любой полцейский, который меня остановит, {b}может забрать меня к Маркусу{/b} и..."
    img 5969
    "Никаких И! Я не попаду к нему!"

    img 5970
    with fade
    "На самом деле, не все так плохо."
    "У меня есть крыша над головой, правда я не могу забыть какой ценой она досталась мне..."
    img 5971
    with Dissolve(0.5)
    "Этот Фред... Я убъю его!"
    "Но это потом... Моника, давай подумаем про то что делать сейчас..."

    if cloth != "Nude":
        img 5972
    else:
        img 5973
    with fade
    "Итак... Меня пустили в свой же дом при условии что {b}я буду убираться в нем{/b}..."

    if cloth != "Nude":
        img 5974
    else:
        img 5975
    "ЗА БЕСПЛАТНО!!!"
    img 5976
    "..." #злой взгляд

    if cloth != "Nude":
        img 5977
    else:
        img 5978
    with fade
    "Но хорошо... Если мне надо пройти через это, то я пройду..."
    "Они не знают кто я такая, поэтому моя гордость не сильно пострадает..."
    "Мне надо всего-лишь притвориться... Ненадолго..."
    "Сделать вид что я убираюсь."
    "В конце концов, эта семейка идиотов что здесь живет - она недалекого ума."
    "Притвориться перед ними и обхитрить их будет пустяковой задачей..."

    img 5979
    "Они глазом не успеют моргнуть, как вылетят отсюда, из этого дома."
    "А я займу свое достойное место здесь..."
    img 5980
    with Dissolve(0.5)
    "Потому что Я - Моника Бакфетт!"
    "А они - никто!"

    img 5981
    with fade
    "Эта Бетти..."
    "Черт... Хоть она и дура, но она следит за мной."
    "Куда бы я здесь ни пошла, она следует за мной по пятам..."
    "Так что крыша у меня над головой есть, но {b}еду мне придется доставать где-то еще...{/b}"

    if cloth != "Nude":
        img 5982
    else:
        img 5983
    with fade
    "Интересно где?..."

    "Может украсть еду у той {b}дуры на заправке{/b}?"
    "Но хочу-ли я воровать?..."

    if cloth != "Nude":
        img 5984
    else:
        img 5985
    with fade
    "Или может спросить еду у того {b}продавца кебабов{/b}?"
    "Я видела как он смотрит на меня..."

    img 5986
    if shawarmaTraderOffended1 == True:
        #
        "Животное, фу!"
    else:
        #
        "Маленькое ничтожество..."

    "Конечно ему никогда не светит прикоснуться к такой красоте как Я..."

    img 5987
    "Но... это можно использовать чтобы достать хоть какую-то пищу..."
    "Я никогда в жизни не пробовала такой еды, но сейчас выбирать не приходится."

    if cloth != "Nude":
        img 5988
    else:
        img 5989
    with fade
    "Даже она мне кажется вкусной сейчас, учитывая что я толком ничего не ела уже давно..."
    "И уж тем более не сравнится с теми помоями, что мне пришлось выпрашивать, когда я была в подвале у Маркуса..."

    if cloth != "Nude":
        img 5990
    else:
        img 5991
    with fade
    "И мне надо как-то придумать как вернуть назад свое положение..."

    img 5992
    with Dissolve(0.5)
    "Дик... Да уж, помощник!"
    "Этот подкаблучник теперь влюблен в свою новую секретаршу."

    if cloth != "Nude":
        img 5993
    else:
        img 5994
    "Эту сучку!"
    "Это ее происки по поводу галстука!"
    "Мне надо сходить к нему еще раз, может получится {b}отбить Дика у нее{/b}?"

    if cloth != "Nude":
        img 5996
    else:
        img 5997
    with fade
    "В конце концов, чтобы вернуть назад свои деньги, мне надо сначала отделаться от Маркуса!"
    "А в этом мне может помочь только Дик!"
    "Еще эти его дурацкие слова про галстук!"
    img 5995
    with Dissolve(0.5)
    "Уверена что Дик просто шутил!"
    "Не думаю что мне стоит всеръез воспринимать его слова об этом!"

    if cloth != "Nude":
        img 5998
    else:
        img 5999
    "..."
    "Мне интересно что там происходит в {b}моем офисе{/b}?"
    "Кто-то сменил код на лифте, но может я найду способ попасть туда?"

    if cloth != "Nude":
        img 6000
    else:
        img 6001
    with fade
    "Я хочу посмотреть на того смельчака, который посмел занять мое место!"
    "Да и как это вообще возможно?!"

    img 6002
    with Dissolve(0.5)
    "Я - Моника Бакфетт!"
    "Я - лицо модного журнала!"
    "Невозможно представить журнал без меня!"
    img 6003
    "Это невозможно! И, думаю, они это прекрасно понимают!"
    "Поэтому им не обойтись без меня!"
    "Это шанс для меня вернуть все назад..."

    img 6004
    with fade
    "Стив?..."
    "Нет, к этому слизняку в таком виде идти точно не стоит."
    "Этот мешок с дерьмом сделает все чтобы использовать это небольшое недоразумение в своих целях..."
    "Я его слишком хорошо знаю..."
    if janeTiffanyFirePlanned == True:
        #если была угроза увольнения Джейн и Тиффани
        "Плюс вокруг недо въются эти две проститутки..."
        "Тиффани и Джейн..."
        "После того как я угрожала уволить их, они могут быть пострашнее той секретарши у Дика..."
        "Жалкие ничтожества..."

    img 6005
    with fade
    "И мне вообще стоит поменьше показываться в таком виде перед людьми, которые мне знакомы."
    "Это касается и моих подружек Стефани и Ребекки..."
    "В конце концов, мне придется общаться со всеми ними когда я верну положение в обществе."
    "И вообще, надо бы найти одежду получше чем те тряпки, которые я схватила у той шлюхи..."

    if cloth != "Nude":
        img 6006
    else:
        img 6007
    "Не могу поверить что мне приходится ходить в этом по городу..."
    "Может лучше ходить в униформе Юлии?"
    "Как хорошо что меня никто не узнает в этом!"
    if cloth != "Nude":
        img 6008
    else:
        img 6009
    "Никто даже подумать не может что Моника Бакфетт может ходить по улице в униформе горничной..."
    "Или в одежде проститутки..."
    "Это мне на руку!"

    img 6010
    with Dissolve(0.5)
    "..."
    "Ральф..."
    "Его было бы очень просто отбить у этой провинциальной дуры."
    "После этого выкинуть того маленького недоноска и эту Бетти из дома."
    "А потом выкинуть и Ральфа..."

    img 6011
    "Но Бетти не дает возможности даже взять бутерброд на кухне, что уж говорить о том что она не даст даже близко приблизиться к Ральфу..."

    "..."

    img 6012
    "Барди..."
    "Этот мелкий неудачник даже не заслуживает внимания."
    "Он вертится вокруг как назойливая муха!"
    "Считает что я ему обязана тем что нахожусь здесь!"
    "Наивный дурачок!"
    "Надо как-то избавиться от него..."

    #играет музыка kill bill
    img 6013
    with fadelong
    m "Да, это все небольшое недоразумение..."
    "И, когда я решу его, я поквитаюсь со всеми вами!"
    "Клянусь!"

    #музка гаснет
    music stop
    img 6014
    with fade
    mt "..."
    music Stealth_Groover
    "Итак..."
    "Сейчас, думаю, надо {b}притвориться горничной{/b}."
    "Затем {b}пойти поискать еду{/b}..."
    img 6015
    with fade
    "Думаю мне необязательно все время убираться здесь..."
    "Эта семейка не привыкла к тем стандартам чистоты, которые требовала я от гувернанток."
    img 6016
    with Dissolve(0.5)
    "Но иногда убираться все-же стоит. Это может вызвать доверие у Бетти."
    "Хотя зачем мне ее доверие?"
    "Мне, почему-то, кажется что еду брать она все-равно не разрешит."
    return

label spot_monica_comment1:
    #Моника комментирует пятно на полу
    mt "Я не собираюсь убирать это пятно!"
    "Этот ковер надо менять!"
    "Думаю Бетти это прекрасно понимает, потому и не говорит про пятно."
    return


label cleaning_betty_comment1:
    #render+
    #комментарий Бетти hall2

    if char_info["Betty"]["level"] == 2:
        #если уровень2
        img 6018
        with fade
        betty "Моника, гувернантка."
        img 6019
        "Как я выгляжу?"
        img 6020
        "Тебе нравится?"
        img 6021
        mt "!!!"
        img 6022
        m "Да, Мэм. Вы выглядите великолепно."
        img 6023
        betty "Да, получше чем ты!"
        img 6024
        "Если ты будешь также стараться и дальше, то я возьму тебя с собой на фитнес."
        "Твою фигуру можно поправить."
        m "Да, Мэм..."
        "Спасибо..."
        img 6025
        w
        img 6026
        betty "Продолжай убираться."
        $ char_info["Betty"]["caption"]=_("Бетти подумывает взять Монику в фитнесс зал")
        $ remove_hook(label="betty_level2_onetime")
        return

    #если не набралось 3 дней уборки
    if len(cleaningLog) < 3:
        $ notif(_("Моника еще не проявила себя"))
        img 6017
        betty "Моника, гувернантка."
        "Продолжай убираться."
        return

    if get_cleaning_status(3) != False:
        #если нет пропущенных дней уборки за 3 дня
        img 6018
        betty "Моника, гувернантка."
        img 6019
        "Как я выгляжу?"
        img 6020
        "Тебе нравится?"
        img 6021
        mt "!!!"
        img 6022
        m "Да, Мэм. Вы выглядите великолепно."
        img 6023
        betty "Да, получше чем ты!"
        "Продолжай убираться."
        $ notif(_("Моника регулярно убирается"))
    return

    if get_cleaning_status(3) == False:
        #если есть пропущенные дни уборки за 3 последних дня
        img 6027
        $ notif(_("Моника плохо работает"))
        betty "Моника, гувернантка."
        "Ты плохо работаешь и нерегулярно убираешь, я вижу!"
        img 6028
        m "Мэм, простите..."
        "Я буду стараться лучше..."
        img 6029
        betty "Не знаю зачем Ральф тебя держит, Фи!"
        img 6021
        mt "..."
        if monicaBitch == True:
            $ notif_monica()
            "Сучка!"
        return


    return

label cleaning_bardie_comment1:
    #render+
    #иногда Барди появляется в комнате, где убирается Моника
    #комнаты floor1 (если нет Ральфа)
    $ store_music()
    music Marty_Gots_a_Plan high
    img 6030
    w
    img 6031
    w
    sound Jump2
    img 6032
    $ add_corruption(bardieCleaningUpskirtTryCorruption, "bardie_monica_upskirt_corruption_day_" + str(day))
    bardie "Моника! Покажи трусики!"
    music Pyro_Flow high
    img 6033
    with fade
    m "Как ты себе позволяешь общаться со старшими?!"
    img 6034
    bardie "Ты гувернантка! Я твой хозяин!"
    img 6035
    "Покажи что у тебя под юбочкой!"
    img 6036
    m "Здесь хозяин Мистер Ральф, а не ты, малявка!"
    "Исчезни, пока я тебя не прибила прямо здесь и сейчас!"
    music Marty_Gots_a_Plan high
    img 6037
    bardie "Ах ты так!"
    bardie_t "Ну она у меня попляшет!"
    $ restore_music()
    return

label cleaning_bardie_comment2:
    #render+
    #когда Моника убирает у Барди в комнате
    $ store_music()
    music Marty_Gots_a_Plan high
    img 6038
    w
    img 6040
    w
    img 6039
    w
    bardie "Моника! Убирайся в комнате хозяина как следует!"
    music Pyro_Flow
    img 6041
    with fade
    m "Ты здесь не хозяин, малявка!"
    img 6042
    bardie "Если ты мне покажешь трусики, то я разрешу тебе не убирать здесь."
    $ add_corruption(bardieCleaningUpskirtTryCorruption, "bardie_monica_upskirt_corruption_day_" + str(day))
    img 6043
    m "Нет уж! Я ни за что этого не сделаю!"
    "Лучше исчезни!"
    music Marty_Gots_a_Plan high
    img 6044
    bardie "Ах ты так!"
    bardie_t "Ну она у меня попляшет!"
    $ restore_music()
    return

label cleaning_bardie_comment3:
    #render+
    #когда Моника убирает в bedroom_second
    $ store_music()
    music Marty_Gots_a_Plan high
    img 6045
    w
    img 6047
    w
    img 6046
    w
    img 6048
    w
    sound Jump2
    img 6049
    w
    $ add_corruption(bardieCleaningUpskirtTryCorruption, "bardie_monica_upskirt_corruption_day_" + str(day))
    img 6050
    bardie "Моника! Покажи трусики!"
    music Pyro_Flow high
    img 6051
    with fade
    m "Как ты себе позволяешь общаться со старшими?!"
    img 6052
    bardie "Ты гувернантка! Я твой хозяин!"
    img 6053
    "Покажи что у тебя под юбочкой!"
    img 6054
    m "Здесь хозяин Мистер Ральф, а не ты, малявка!"
    "Исчезни, пока я тебя не прибила прямо здесь и сейчас!"
    img 6055
    music Marty_Gots_a_Plan high
    bardie "Ах ты так!"
    bardie_t "Ну она у меня попляшет!"
    $ restore_music()
    return

label cleaning_monica_goout1:
    #Моника пытается выйти из дома когда не закончена уборка
    if renpy.random.randint(1,2) == 1:
        mt "Мне надо закончить эту гребаную уборку, прежде чем уходить!"
    else:
        mt "Мне надо закончить уборку здесь прежде чем уходить."
        "Иначе Бетти уволит меня и я окажусь на улице!"

    return False

label cleaning_monica_finished1:
    #Моника закончила уборку
    mt "Я закончила уборку. Что там у нас дальше?"
    return

label cleaning_monica_comment:
    mt "Ненавижу убираться!!!"
    "Я королева и мне нельзя заниматься такой работой!"
    return False


label bardie_comment5:
    #Барди на улице
    mt "Я не собираюсь подходить к этой малявке!"
    return

label monica_goout1_governess_restrict:
    #render+
    #Street_House_Gate Моника у ворот в униформе горничной, Бетти ее догоняет
    #Рендер в зависимости от времени дня!
    if day_time == "day":
        img 6062
        with fadelong
        w
        $ store_music()
        music Power_Bots_Loop
        img 6063
        betty "Эй! Дорогуша!"
        "Куда это ты собралась?!"
        img 6064
        m "Миссис Робертс! Я..."
        img 6065
        "Я собиралась идти по свои делам и..."
        betty "Ты собралась вынести собственность дома за его пределы?"
        img 6066
        m "Что Вы имеете ввиду, Мэм?!"
        betty "Эта униформа! Это моя собственность!"
        img 6067
        "Кто разрешал тебе покидать территорию дома, {b}одетой в униформу{/b}?"
        "Ты решила украсть ее?!"
        img 6068
        m "Нет, Мэм! Я всего-лишь собиралась выйти ненадолго, чтобы..."
        $ add_char_progress("Betty", bettyTryOutInGovernessClothRegressAmount, "bettyTryOutInGovernessCloth_day_" + str(day), duplicate=True)
        img 6069
        betty "Собстенность дома не должна покидать его пределы!"
        "Я не понимаю что у тебя за дела за пределами этого дома."
        "Неужели ты уже закончила все дела?"

        #если есть пропущенные дни уборки за 3 последних дня
        if len(cleaningLog) >= 3 and get_cleaning_status(3) == False:
            $ notif(_("Моника нерегулярно убирается в доме"))
            img 6070
            "Я вижу как ты отлыниваешь от работы!"
            with fade

            img 6071
            "За такие деньги, что тебе платят, я думаю у тебя не должно быть свободного времени!"
            "Но если ты решила все-таки уйти, то, будь добра, {b}переоденься в свою одежду{/b}!!!"
            "ЯСНО ТЕБЕ?!"
        else:
            img 6071
        m "Да, Миссис Робертс... Я поняла..."

        $ restore_music()
        img 6072
        mt "Черт! Похоже, чтобы выйти, мне надо переодеться!"
    else:
    #вечер
        img 6073
        with fadelong
        w
        $ store_music()
        music Power_Bots_Loop
        img 6074
        betty "Эй! Дорогуша!"
        img 6075
        "Куда это ты собралась?!"
        img 6076
        m "Миссис Робертс! Я..."
        "Я собиралась идти по свои делам и..."
        betty "Ты собралась вынести собственность дома за его пределы?"
        m "Что Вы имеете ввиду, Мэм?!"
        $ add_char_progress("Betty", bettyTryOutInGovernessClothRegressAmount, "bettyTryOutInGovernessCloth_day_" + str(day), duplicate=True)
        img 6077
        betty "Эта униформа! Это моя собственность!"
        "Кто разрешал тебе покидать территорию дома, {b}одетой в униформу{/b}?"
        "Ты решила украсть ее?!"
        img 6078
        m "Нет, Мэм! Я всего-лишь собиралась выйти ненадолго, чтобы..."
        img 6079
        betty "Собстенность дома не должна покидать его пределы!"
        "Я не понимаю что у тебя за дела за пределами этого дома."
        "Неужели ты уже закончила все дела?"

        #если есть пропущенные дни уборки за 3 последних дня
        if len(cleaningLog) >= 3 and get_cleaning_status(3) == False:
            $ notif(_("Моника нерегулярно убирается в доме"))
            img 6080
            "Я вижу как ты отлыниваешь от работы!"

            img 6081
            "За такие деньги, что тебе платят, я думаю у тебя не должно быть свободного времени!"
            "Но если ты решила все-таки уйти, то, будь добра, {b}переоденься в свою одежду{/b}!!!"
            "ЯСНО ТЕБЕ?!"
        img 6082
        with fade
        m "Да, Миссис Робертс... Я поняла..."
        $ restore_music()
        img 6083
        mt "Черт! Похоже, чтобы выйти, мне надо переодеться!"
    return










#
