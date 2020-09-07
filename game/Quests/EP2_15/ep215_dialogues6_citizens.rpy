default monicaCitizens14Slums1 = False  # Моника согласилась привести к себе домой алкаша
default monicaCitizens14Slums2 = False  # Моника согласилась выпить стопку на один бакс
default monicaCitizens14Slums3 = False  # Моника согласилась выпить вторую стопку за бакс
default citizen14BlockedByDay = 0
#call ep215_dialogues6_citizens_1() # при клике на алкаша на улице


# при клике на алкаша на улице
label ep215_dialogues6_citizens_1:
#    fadeblack 1.5
    music Groove2_85
    imgl Dial_begin35_18
    m "Черт, что это еще за тело лежит здесь?! Я чуть не споткнулась о тебя!"
    imgr Dial_Citizen_14_1
    citizen14 "Эй, стой!"
    citizen14 "О, привет, красотка!"
    citizen14 "Хочешь немного подзаработать?"
    imgl Dial_begin35_17
    m "Возможно... Но это тебя не касается!"
    imgr Dial_Citizen_14_3
    imgl Dial_Monica_Whore_1
    citizen14 "Тогда у меня к тебе есть дело..."
    citizen14 "Давай отойдем в тихое место?"
    m "..."
    $ menu_corruption = [monicaCorruptionCitizen14Agree1]
    menu:
        "Пойти с ним.":
            imgl Dial_begin35_21
            mt "Что может мне предложить этот никчемный неудачник?"
            mt "Хммм..."
            m "Пошли..."
            # затемнение
            pass
        "Нет!":
            music Stealth_Groover
            imgl Dial_begin35_16
            mt "Фу, какой он мерзкий!"
            m "Нет!"
            m "Я не собираюсь никуда с тобой отходить!"
            music Groove2_85
            imgr Dial_Citizen_14_2
            citizen14 "Я так и знал..."
            citizen14 "Но если захочешь подзаработать, ты знаешь, где меня найти."
            return 0
    # стоят у пилона
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 32163
    w
    imgf 32164
    citizen14 "Я сегодня богат! Я нашел целых 30 баксов на улице!"
    citizen14 "Я могу себе позволить снять хату с блекджеком и шлюхами!"
    citizen14 "Но я подумал..."
    citizen14 "Почему бы мне не разделить эту радость с такой красоткой, как ты?"
    citizen14 "Заодно сэкономлю на хате и на шлюхе, м?"
    # подмигивает Монике
    imgd 32165
    m "Я не шлюха, а мой дом не притон для алкашей!"
    m "Иди в Shiny Hole! Эта вонючая дыра как раз для тебя!"
    m "Или можешь пить на улице, как раньше!"
    citizen14 "На улице мне нельзя..."
    citizen14 "Копы сказали, что загребут, если увидят меня пьющим."
    citizen14 "Я могу вознаградить тебя за помощь..."
    imgf 32166
    m "Вознаградить?"
    m "..."
    $ menu_corruption = [monicaCorruptionCitizen14Agree2]
    menu:
        "Согласиться.":
            # если Моника не арендует квартиру у Джека
            if slumsApartmentsRentActive == False:
                imgd 32167
                mt "Хммм..."
                mt "Деньги за то, что бы ему было где выпить - это лучше, чем танцевать у пилона."
                mt "..."
                mt "Черт! Но мне некуда его вести!"

                mt "А здесь я это делать не собираюсь!"
                music Groove2_85
                #
                $ notif(t_("Монике некуда вести клиентов."))
                #
                imgf 32168
                m "Мне некуда тебя вести!"
                citizen14 "Давай тогда выпьем с тобой здесь! Ик!"
                citizen14 "Я заплачу тебе! Ик!"
                # выглядывает мамочка
                music Master_Disorder
                img 24343 vpunch
                w
                imgd 24344
                w
                imgd 32169
                m "Я не собираюсь с тобой пить здесь."
                m "Мне не нужны проблемы из-за тебя!"
                return -1
            # если арендует квартиру у Джека
            $ monicaCitizens14Slums1 = True # Моника согласилась привести к себе домой алкаша
            pass
        "Мой дом не место для алкашей с улицы!":
            music Stealth_Groover
            imgd 32167
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            imgf 32168
            m "Нет!"
            m "Мой дом не место для алкашей с улицы!"
            citizen14 "Видимо тебе не нужны ни деньги, ни хорошая выпивка."
            return -1
    # Моника в сомнениях
    music Stealth_Groover
    imgd 32170
    mt "Хммм..."
    mt "Деньги за то, что бы ему было где выпить - это лучше, чем танцевать у пилона."
    mt "..."
    mt "Вот дьявол!"
    mt "Если я ему откажу сейчас, то вообще ничего не заработаю..."
    mt "А мне нужны деньги..."
    # выглядывает мамочка
    music Master_Disorder
    img 24344 vpunch
    mt "И эта старая карга следит за мной..."

    #
    $ notif(_("Моника должна выплачивать Перри долг в размере $ 50 000."))
    imgd 24343
    mt "Я должна выплачивать долг этой мерзкой извращенке Перри!"
    #
    music Groove2_85
    # если Монику выгнали с эскорта
    if ep212_escort_monica_fired == True:
        #
        $ notif(_("Моника больше не работает в ВИП-эскорте."))
        #
        imgd 32167
        mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
        #
    imgd 32167
    mt "Моника, что же делать?"
    mt "С другой стороны..."
    mt "Он ведь хочет просто выпить и уйти..."
    mt "Еще и денег мне за это заплатит..."
    mt "..."
    imgf 32171
    m "Сколько ты мне заплатишь за это?"
    citizen14 "10 баксов, моя спасительница!"
    m "Черт!"
    m "!!!"
    m "Пошли!"
    $ add_money(10.0)
    # !!! render отсюда!!!
    # затемнение
    # в квартире Моники
    # алкаш и Моника стоят в ее гостиной
    fadeblack 1.5
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 32172
    w
    imgf 32173
    m "Пей там..."
    # Моника указывает на столик рядом с раскладушкой
    music Stealth_Groover
    imgd 16959
    mt "Нужно следить за тем, чтобы этот алкаш не стал здесь все громить..."
    mt "Когда напьется..."
    mt "И чтобы не украл ничего..."
    mt "И еще мне нужно переодеться. Надоели уже эти тряпки!"
    # фраза Моники о том, что она идет переодеваться и чтобы он ничего не трогал, и его ответ что он накроет стол
    music Groove2_85
    imgf 32174
    m "Я сейчас вернусь, а ты ничего здесь не трогай!"
    m "Если хоть пальцем к чему-то притронешься - выгоню сразу же!!"
    m "Тебе все ясно?!"
    sound Jump1
    imgd 32175
    citizen14 "Без проблем, красотка!"
    citizen14 "Я пока накрою на стол."
    # алкаш садится на стул
    fadeblack
    sound highheels_short_walk
    pause 1.5
    sound snd_fabric1
    pause 2.0
    music Stealth_Groover
    imgfl 32177
    w
    imgf 32176
    w
    imgd 32178
    w
    imgd 32179
    mt "Какой же он жалкий! Фи!"
    music Groove2_85
    imgf 32180
    citizen14 "А ты что, так и будешь стоять в стороне?"
    citizen14 "Иди сюда, я угощу тебя чудесным напитком..."
    m "Я не пью!"
    citizen14 "Да ладно тебе!"
    citizen14 "Ты же просто составишь мне компанию."
    citizen14 "А я буду платить тебе по $ 1 за каждую выпитую рюмку..."
    music Stealth_Groover
    imgd 32181
    mt "$ 1 за то, что бы я вливала эти помои в свое прекрасное тело?"
    mt "Моника, стоит ли это того?"
    mt "Я и этот алкаш... Отброс общества!"
    mt "Такая богиня, как Я, привыкла вкушать изысканные шампанские вина среди элиты общества..."
    mt "А это пойло совсем не для леди с прекрасными манерами и утонченным вкусом ..."
    music Groove2_85
    imgd 32180
    citizen14 "Одна стопка и бакс у тебя в кармане."
    mt "Черт!"
    mt "!!!"
    $ menu_corruption = [0, monicaCorruptionCitizen14Agree3]
    menu:
        "Я же сказала, что не пью!":
            music Stealth_Groover
            imgf 32182
            m "Тебе нужно было место для пьянки, так что сиди и пей!"
            m "И больше не предлагай мне эти дешевые помои."
            citizen14 "Ты мне портишь весь натстрой!"
            sound man_steps
            imgd 32183
            citizen14 "Я, пожалуй, найду более приветливого собутыльника!"
            $ add_money(-10.0)
            # алкаш уходит
            imgd 32184
            mt "Да пошел ты!"
            mt "Грязный жалкий отброс общества! Фи!"
            mt "!!!"
            fadeblack
            sound snd_door_locked1
            pause 1.5
            return -2
        "Видимо этот неудачник не отстанет от меня...":
            $ monicaCitizens14Slums2 = True # Моника согласилась выпить стопку за один бакс
            pass
    # Моника в сомнениях
    music Groove2_85
    imgf 16997
    mt "Со мной же ничего не случится из-за одной стопки этой гадости..."
    mt "..."
    mt "Мне придется выпить одну, чтобы он от меня отстал!!!"
    music Stealth_Groover
    mt "Зато я заработаю доллар..."
    mt "Знал бы этот мерзкий неудачник, КТО сидит с ним сейчас!"
    mt "Любой мужчина в этом городе мечтал бы оказаться на его месте!"
    mt "!!!"
    imgd 32182
    m "Давай мне эту гадость!"
    m "Но только одну! Не больше!"
    # алкаш обрадованно
    fadeblack 1.0
    music Groove2_85
    imgf 32185
    citizen14 "Ну вот! Другое дело!"
    # звук - наливает жидкость в стопку
    fadeblack
    sound pour_wine
    pause 2.0
    music Groove2_85
    imgfl 32186
    citizen14 "Вот, держи..."
    citizen14 "Выпивай эту стопку и я плачу тебе бакс как договаривались."
    # Моника выпивает и морщится
    sound snd_drinking_water
    imgf 32187
    w
    $ add_money(1.0)
    imgd 32188
    mt "ФУУУУУ!"
    mt "Эти помои еще хуже, чем я предполагала!!!"
    mt "!!!"
    mt "Надеюсь, я сейчас не умру от отравления!"
    $ blur_effect = 1
    imgd 32188
    w
    mt "Ох..."
    mt "Какое-то странное ощущение..."
    $ blur_effect = 0
    imgd 32188
    mt "..."
#    $ blur_effect = False
    # алкаш на заднем плане бормочет
    $ blur_effect = 1
    imgf 32189
    citizen14 "Вот..."
    citizen14 "И я, значит, ему говорю... Ик!"
    citizen14 "Ты... Ик! Рыбу веслом по башке... Ик!"
    citizen14 "А, ты уже выпила?!"
    citizen14 "Ну вообще, красотка!"
    imgd 32190
    citizen14 "Вот, еще одна стопка!"
    citizen14 "И я дам тебе еще бакс! Ик!"
    mt "..."
    $ menu_corruption = [0, monicaCorruptionCitizen14Agree4]

    menu:
        "Прогнать этого алкаша пока не поздно!":
            $ blur_effect = 0
            music Pyro_Flow
            imgf 32191
            m "Забирай свое пойло и уходи!"
            citizen14 "Куда я пойду?! Мы же только сели!!"
            citizen14 "Я думал, что на балалайке тебе сыграю..."
            citizen14 "И уже по второй нам налил..."
            music Power_Bots_Loop
            img 32192 hpunch
            m "ВОН!!!"
            m "НЕМЕДЛЕННО!!!"
            m "!!!"
            citizen14 "Шлюха - предательница, а не спасительница! Ик!"
            fadeblack 1.5
            music Loved_Up
            $ blur_effect = 2
            imgf 32193
            sound man_steps
            mt "Ох! Что-то мне нехорошо..."
            mt "Мне надо немного отдохнуть..."
            $ blur_effect = 0
            sound Jump2
            img 32194 vpunch
            w
            imgf 32195
            w
            imgd 32196
            w
            # алкаш уходит
            # Моника ложится на постель
            return -3
        "Еще бакс?":
            $ monicaCitizens14Slums3 = True # Моника согласилась выпить вторую стопку за бакс
            pass
    $ blur_effect = 0
    music Groove2_85
    imgf 32197
    mt "Еще доллар за то, чтобы я выпила?"
    citizen14 "Ага!"
    $ blur_effect = 1
    imgd 32197
    mt "Что это он бормочет..."
    $ blur_effect = 2
    imgd 32197
    mt "Ох... Что-то голова кружится..."
    mt "И такое приятное тепло внутри..."
    $ blur_effect = 0
    imgd 32198
    m "Я хотела сказать..."
    citizen14 "Да помню я, милая... Помню..."
    citizen14 "Одна стопка и еще один бакс твой... Ик!"
    m "Что..."
    imgf 32199
    mt "Что это за мерзость?!"
    mt "Почему она так воняет?!"
    $ blur_effect = 2
    imgd 32199
    mt "Или..."
    imgd 32189
    citizen14 "Давай пей..."
    citizen14 "Я помогу тебе! И рраз!"
    # Моника выпивает вторую рюмку
    fadeblack 1.5
    music Groove2_85
    $ blur_effect = 0
    sound snd_drinking_water
    imgf 32187
    w
    $ add_money(1.0)
    imgd 32188
    w
    fadeblack 1.5
    music Groove2_85
    imgfl 32200
    citizen14 "Ик! Так вот..."
    citizen14 "Мы пошли значит с этой... Ик! Старой шлюхой..."
    imgf 32201
    mt "Что за бред он несет?"
    mt "???"
    $ blur_effect = 1
    imgd 32202
    citizen14 "А у нее... Ик!"
    citizen14 "И сиськи... Во!"
    citizen14 "Не то, что у тебя... Ик!"
    imgd 32203
    mt "Что за странный привкус во рту..."
    $ blur_effect = 2
    imgd 32203
    mt "И почему вся комната... Ик!"
    mt "Ой!"
    # алкаш дает третью рюмку
    $ blur_effect = 0
    imgf 32204
    citizen14 "Ты это... Ик!"
    citizen14 "Быстро что-то... На, держи!"
    $ blur_effect = 2
    imgd 32199
    mt "Что проис... Что это? Ик!"
    mt "Что он напивает мне?"
    $ blur_effect = 2
    fadeblack 2.0
    # Моника выпивает третью рюмку
    sound snd_drinking_water
    imgf 32187
    w
    $ blur_effect = 4
    imgd 32188
    w
    $ add_money(1.0)
    fadeblack 1.5
    return 1

label ep215_dialogues6_citizens_1b:
    music stop
    img black_screen
    with Dissolve(1)
    call textonblack(t_("Утро...")) from _rcall_textonblack_69
    scene black_screen
    with Dissolve(1)
    sound lick3
    pause 1.5
    music Groove2_85


    # затемнение
    # Моника просыпается голая на кровати, а между ног голова алкаша и он спит
    # рядом валяется пустая бутылка
    # Моника ВСКАКИВАЕТ И В УЖАСЕ ХВАТАЕТСЯ ЗА ГОЛОВУ
    $ blur_effect = 2
    imgfl 32206
    w
    $ blur_effect = 0
    imgd 32206
    sound lick3
    imgf 32207
    w
    music stop
    sound plastinka1b
    img 32208 hpunch
    w
    music Pyro_Flow
    imgf 32209
    w
    imgd 32210
    w
    imgf 32211
    w
    music Loved_Up
    imgd 32212
    citizen14 "Ммммм..."
    citizen14 "Какая закуска... Ммммм... Вкусная..."
    w
    imgd 32213
    w
    sound lick3
    imgd 32214
    w
    imgd 32213
    w
    sound lick3
    imgd 32214
    w
    imgd 32213
    w
    sound lick3
    imgd 32214
    w
    imgd 32213
    w
    sound lick3
    imgd 32214
    w
    imgf 32215
    w
    music Pyro_Flow
    imgd 32216
    w
    sound Jump2
    img 32217 vpunch
    mt "О УЖАС!!!"
    mt "!!!" # оглядывается в растерянности и недоумении
    mt "ЧТО ЗДЕСЬ ПРОИЗОШЛО?!"
    mt "?!?!?!"
    imgd 32218
    mt "МОНИКА!"
    mt "Я НЕ МОГУ ПОВЕРИТЬ!"
    mt "ТЫ И КАКОЙ-ТО АЛКАШ С УЛИЦЫ!!!"
    mt "!!!"
    mt "ТЫ УПАЛА НА САМОЕ ДНО, МОНИКА!!!"
    mt "КАК ТАКОЕ МОГЛО СЛУЧИТЬСЯ?!"
    imgd 32219
    mt "МОЯ ЖИЗНЬ ПРЕВРАТИЛАСЬ В БЕСКОНЕЧНЫЙ КОШМАР!!!"
    mt "КОШМАР, КОТОРЫЙ НИКАК НЕ ЗАКАНЧИВАЕТСЯ!!!"
    mt "И Я... Я..."
    mt "О БОЖЕ!!!"
    mt "Я ДОЛЖНА СОБРАТЬСЯ!!!"
    mt "!!!"
    music Stealth_Groover
    imgf 32221
    mt "ЭТО... ЭТО..."
    mt "ЭТО ПРОСТО ВРЕМЕННЫЕ ТРУДНОСТИ!"
    mt "Я - МИССИС МОНИКА БАКФЕТТ!!!"
    mt "Я - БИЗНЕС ЛЕДИ!!!"
    mt "Я ПОЛОЖУ ЭТОМУ КОНЕЦ!!!"
    mt "!!!"
    # с ненавистью смотрит на спящего алкаша
    imgd 32220
    mt "И начну я с этого грязного отродья!!!"
    mt "!!!"
    # Моника дает поджопник спящему алкашу
    # алкаш подскакивает и пытается прийти в себя
    music Turbo_Tornado
    imgf 32222
    w
    imgd 32223
    sound anger2
    w
    sound snd_kick_fred1
    img 32224 hpunch
    w
    sound Jump1
    img 32225 vpunch
    citizen14 "Эй! Ик! Ты чего?!"
    m "ПРОВАЛИВАЙ ИЗ МОЕЙ КВАРТИРЫ!!!"
    m "МЕРЗКИЙ АЛКАШ!!!"
    citizen14 "Чего ты обзываешься?"
    music Power_Bots_Loop
    imgf 32226
    m "ТЫ РЕШИЛ ВОСПОЛЬЗОВАТЬСЯ СНАЧАЛА МОЕЙ ДОБРОТОЙ!"
    m "А ПОТОМ И МОИМ ТЕЛОМ?!"
    m "?!?!?!"
    m "ПРОВАЛИВАЙ ОТСЮДА, ГРЯЗНОЕ ЖИВОТНОЕ!!!"
    # алкаш полупьяный
#    music Groove2_85
    music Turbo_Tornado
    citizen14 "У нас ничего не было!"
    citizen14 "Давай сначала здоровье поправим! У тебя выпивка в доме есть?"
    citizen14 "Хорошо же сидели! Я хотел тебе еще на балалайке сыграть..."
    imgd 32227
    w
    sound Jump1
    imgd 32228
    w
    sound Jump1
    imgd 32227
    w
    # алкаш болтает языком верх-вниз намекая на куни
    imgf 32229
    sound running
    m "АХ ТЫ СВОЛОЧЬ!!!"
    m "У МЕНЯ НЕТ БАЛА... БАЛАЛАЛА..."
    m "БАЛАЛАЙКИ!!!!"
    sound snd_kick_fred1
    img 32230 hpunch
    m "А НУ ПРОВАЛИВАЙ!!!"
    m "!!!"
    fadeblack
    sound snd_door_locked1
    pause 1.5
    music Pyro_Flow
    # Моника дает еще поджопник
    # алкаш убегает
    # Моника в гневе
    img 32231 vpunch
    mt "КОГДА Я ВЕРНУ СЕБЕ СВОЮ ЖИЗНЬ!!!"
    mt "Я СРАВНЯЮ ЭТОТ МЕРЗКИЙ РАЙОН С ЗЕМЛЕЙ!!!"
    mt "СО ВСЕМИ ЕГО МЕРЗКИМИ ОБИТАТЕЛЯМИ!!!"
    mt "МЕРЗКИМИ!"
    mt "БЕСПОЛЕЗНЫМИ!"
    mt "НИКЧЕМНЫМИ!!!"
    mt "ААААААААА!!!"
    return

label ep215_dialogues6_citizens_1c:
    mt "Не могу поверить, что это происходит со мной..."
    return
