
default monicaBiffInvestorsPhotoshoot1 = False # Моника согласилась провести презентацию перед инвесторами
default monicaBiffInvestorsPhotoshoot2 = False # Моника согласилась на фотосессию перед инвесторами
default monicaBiffInvestorsPhotoshoot3 = False # Моника со 2-го раза согласилась фотографироваться перед инвесторами
default monicaBiffInvestorsPhotoshoot4 = False # Моника согласилась сдвинуть трусики на фотосессии
default monicaBiffInvestorsPhotoshoot5 = False # Моника со 2-го раза согласилась сдвинуть трусики перед инвестором

#call ep213_dialogues4_biff_1() # Моника в кабинете у Бифа
#call ep213_dialogues4_biff_2() # день презентации, мысли Моники
#call ep213_dialogues4_biff_3() # презентация
#call ep213_dialogues4_biff_4() # мысли Моники, когда идет на любую другую локацию, кроме фотостудии
#call ep213_dialogues4_biff_5() # если кликнуть на Алекса до того, как переоделась
#call ep213_dialogues4_biff_6() # гримерка
#call ep213_dialogues5_photoshoot_7() # если Моника отказалась фотографироваться, потом передумала и пришла к Бифу
#call ep213_dialogues4_biff_8() # фотосессия
#call ep211_dialogues3_photoshoot_9() # если Моника отказалась сдвигать трусики перед инвестором, потом передумала и пришла к Бифу
#call ep213_dialogues4_biff_10() # если после фотосессии заходит к Бифу в кабинет
#call ep213_dialogues4_biff_11() # мысли Моники, когда вышла из офиса после проведения фотосессии


# если уже была фотосессия в платье Королева сердец перед инвестором Кэмпбеллом
# Моника приходит в кабинет Бифа
label ep213_dialogues4_biff_1:
    # использовать имеющиеся арты
    # при выборе пункта меню "Спросить о работе"
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Groove2_85
    imgfl 12789
    m "Биф..."
    m "Я хотела узнать у тебя..."
    m "Есть-ли еще работа?"
    m "Мне нужны деньги..."
    imgf 12796
    biff "Для хорошей цыпочки у папочки всегда найдется работа."
    biff "Ты же хорошая цыпочка?"
    m "..."
    imgd 12844
    biff "Только это не очередное кривляние перед камерой..."
    biff "За которое я тебе плачу неимоверно дорого."
    imgd 13893
    biff "И вообще! Я уже начинаю сомневаться в том, что цыпочка хорошая!"
    biff "Почему из всех инвесторов только один согласился инвестировать в мой журнал?!"
    # Моника зло смотрит
    music Power_Bots_Loop
    imgf 15864
    mt "Это МОЙ журнал!"
    mt "Кретин!"
    mt "И, когда им управляла Я, мне не было нужды искать каких-то никчемных тупых инвесторов для него!"
    mt "!!!"
    music Groove2_85
    imgd 13908
    biff "При этом тебя еще пришлось заставлять делать нужные кадры!"
    biff "Все приходится делать за тебя!"
    biff "..."
    imgf 12810
    m "..."
    imgd 12811
    biff "Я собираю всех инвесторов завтра."
    biff "Тебе нужно будет выступить перед ними."
    imgf 12812
    m "Очередная презентация с графиками?"
    m "???"
    music Hidden_Agenda
    imgd 12865
    biff "Нет, на этот раз презентация будет не с графиками..."
    biff "А с твоими фотографиями."
    # Моника возмущенно
    music Power_Bots_Loop
    img 12797 hpunch
    m "ЧТО?!"
    m "?!?!?!"
    music Groove2_85
    imgf 12815
    biff "Что слышала, кукла!"
    biff "Мистер Кэмпбелл очень доволен резким ростом продаж..."
    biff "После выхода журнала с твоими голыми сиськами на обложке."
    biff "Аха-ха!!!"
    music Power_Bots_Loop
    imgd 12817
    mt "АААААА!!!"
    mt "Мерзкая сволочь!"
    mt "!!!"
    music Groove2_85
    imgf 13893
    biff "Короче, слушай, кукла..."
    biff "Я заручился поддержкой Мистера Кэмпбелла."
    biff "Он согласился поддержать нас перед другими инвесторами..."
    biff "Чтобы подтолкнуть их к принятию правильного решения - инвестировать в мой журнал."
    imgd 13895
    mt "МОЙ журнал!!!"
    imgf 12883
    biff "Все, что от тебя требуется, кукла безмозглая - это стоять перед слайдами с твоими фотографиями и улыбаться."
    biff "Справишься с таким сложным для тебя делом, а?"
    biff "Это посложнее, чем сосать члены за $ 20!"
    biff "Надеюсь у тебя для этого хватит мозгов?"
    # Моника возмущенно
    imgd 15896
    m "Перестань называть меня так!"
    m "Я не безмозглая кукла, Биф!"
    m "!!!"
    imgf 15897
    biff "Ты безмозглая, глупая шлюшка с физиономией, похожей на сучку Бакфетт!"
    biff "А Я здесь Босс!"
    # Самовлюбленно (взять кадры из вау)
    music Stealth_Groover
    imgd 12847
    biff "Да, я Босс..."
    biff "Босс, вау..."
    #
    # Резко указывает на Монику зло
    music Groove2_85
    img 12787
    biff "Не смей спорить со мной!!!"
    biff "Ты должна сделать так, чтобы согласились ВСЕ инвесторы!"
    biff "Конечно, если ты хочешь остаться на этой работе, бесполезная кукла!"
    m "!!!"
    imgf 12907
    biff "Завтра вечером они будут здесь."
    biff "Придешь, встанешь перед экраном."
    biff "Скажешь про отличные ракурсы, выгодно подчеркивающие платье, предоставленное Кэмпбеллом..."
    imgd 15893
    biff "Вот тебе список со сценарием."
    biff "Сначала ты проведешь презентацию, потом у тебя будет фотосессия."
    imgf 15891
    m "Что за фотосессия?"
    imgd 15898
    biff "Что за вопросы?!"
    biff "Перед инвесторами, конечно! Кукла безмозглая!"
    biff "Больше от тебя ничего не требуется... Пока что..."
    biff "Тебе все понятно?!"
    img 15899
    m "!!!"
    $ menu_corruption = [monicaPresentation2Choice1]
    menu:
        "Да, понятно.": #corruption
            $ monicaBiffInvestorsPhotoshoot1 = True # Моника согласилась провести презентацию перед инвесторами
            pass
        "НЕТ!":
            music Power_Bots_Loop
            img 15900 vpunch
            m "Я не тебе не кукла!"
            m "И я не буду кривляться перед инвесторами!!!"
            m "!!!"
            music Groove2_85
            imgd 15901
            biff "Ты не получишь никакую другую работу!"
            biff "Пока не сделаешь то, что Я тебе говорю!"
            music Power_Bots_Loop
            imgf 15907
            mt "Да пошел ты!"
            mt "Я найду другой способ зарабатывать деньги!"
            # Моника уходит. В след. визит к Бифу разговор возобновляется (Биф не дает ей фотосессии)
            return False
    # Моника медлит
    music Groove2_85
    imgf 15891
    mt "..."
    mt "Что мне теперь делать?!"
    mt "Моника, неужели ты способна согласиться на такое?!"
    mt "Этот кретин заставляет тебя практически раздеться перед инвесторами!"
    mt "..."
    imgd 15892
    mt "Я думала, что обнаженные кастинги и откровенные фотосессии - это макисмум, на что он пойдет..."
    mt "Мне казалось, что до этого еще очень далеко..."
    mt "А оказалось, что это только начало!"
    mt "Я вынуждена слушать глупые приказы Бифа, чтобы он еженедельно платил $ 5000 для Виктории!"
    mt "И это какой-то замкнутый круг!"
    mt "!!!"
    imgd 15895
    mt "Мне нужно подумать, как я могу разорвать этот круг!"
    mt "Это не может продолжаться бесконечно!"
    mt "!!!"
    mt "Мне нужен какой-то план."
    mt "Но сейчас..."
    music Power_Bots_Loop
    mt "Если я откажусь от презентации, этот кретин меня выгонит из моего же офиса!"
    mt "Мерзавец!"
    mt "Ненавижу его!!!"
    mt "!!!"
    music Groove2_85
    imgf 15896
    m "..."
    m "Мне все понятно, Биф."
    imgd 15901
    biff "Так-то лучше."
    music Hidden_Agenda
    biff "И вообще, цыпочка! Ты испортила папочке настроение!"
    biff "Как ты собираешься это исправлять, а?"
    # Моника сквозь зубы
    music Groove2_85
    imgf 12790
    mt "Безмоглый кретин!"
    mt "!!!"
    # меню кастинга, кастинг.

    call ep213_dialogues4_biff_12() from _rcall_ep213_dialogues4_biff_12
label ep213_dialogues4_biff_1b:
    # после кастинга
    imgd 15904
    biff "Я жду тебя завтра, цыпочка."
    m "..."
    return True

# след. рабочий день
# мысли Моники (из лейбла ep210_dialogues1_office_biff_3a)
label ep213_dialogues4_biff_2:
    # не рендерить!!
    if ep213_dialogues4_biff_2_day == day:
        return
    $ remove_hook()
    mt "Мне нужно идти к Бифу и провести эту чертову презентацию!"
    return

# Моника заходит в кабинет Бифа (день проведения презентации)
label ep213_dialogues4_biff_3:
    # перед столом Бифа семь стульев, на стене экран
    # Биф, как в прошлый раз, стоит возле экрана
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Groove2_85
    imgfl 15909
    m "Я пришла..."
    imgf 15910
    biff "А, цыпочка!"
    biff "Ты где ходишь?!"
    biff "Инвесторы придут с минуты на минуты!"
    m "..."
    imgd 18253
    biff "Давай, быстрее!"
    biff "Я приготовил наряд для тебя..."
    # но тут Биф прерывается на полуслове, т.к. заходят инвесторы
    # Биф наклоняется к Монике и недовольно говорит
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 0.5
    sound man_steps
    pause 0.5
    sound man_steps
    pause 2.0
    music Groove2_85
    imgfl 18254
    w
    imgf 18255
    biff "Черт! Ты теперь не успеешь переодеться!"
    biff "Где тебя носило все это время?! Не могла прийти пораньше?!"
    m "..."
    mt "Да пошел ты, сволочь!"
    mt "!!!"
    imgd 18256
    biff "Ладно, будешь выступать в этом."
    biff "Надеюсь, ты компенсируешь свой скучный вид тем, что будешь показывать и говорить..."
    biff "Ну или другими талантами, которых у тебя не так много..."
    biff "Кроме сосания членов за 20 баксов."
    music Power_Bots_Loop
    img 18257
    mt "Мерзавец!"
    mt "!!!"
    # Биф поворачивается к входящим инвесторам и улыбается
    music Groove2_85
    sound man_steps
    imgf 18258
    biff "Добрый вечер, господа!"
    biff "Рады вас видеть!"
    biff "Присаживайтесь, пожалуйста."
    # затемнение, звук мужских шагов
    # смена кадра
    # Моника в своем рабочем костюме стоит перед экраном
    # инвесторы сидят на стульях и смотрят на нее
    # Биф либо стоит сбоку от Моники, либо сидит в своем кресле
    # на экране кадр с фотосессии в костюме Черный лебедь
    # Моника про себя в панике
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    # экран investors_1_2
    imgfl 18259
    w
    sound camera_lens1
    imgf 18260
    mt "Неужели этот кретин Биф собирается показать все кадры оттуда?!"
    mt "В том числе и последние?!"
    music Villainous_Treachery
    imgd 18261
    mt "!!!"
    mt "И все эти неудачники будут смотреть на ЭТО?!"
    mt "?!?!?!"
    # инвестор, который был в номере отеля, когда Моника работала реквизитом, внимательно смотрит на нее
    music Groove2_85
    imgf 18262
    investor3 "..."
    imgd 18263
    mt "..."

    # если Моника работала реквизитом Линды в номере отеля
    if monicaEscortLindaTable1 == True:
        #
        $ notif(t_("Моника работала реквизитом Линды в номере отеля Ле Гранд."))
        #
        imgf 18264
        mt "Почему этот неудачник так смотрит на меня?!"
        mt "Вдруг он меня узнает?!"
        mt "А потом расскажет об этом всем!"
        mt "!!!"
    if monicaEscortLindaTable3 == True:
        # если Моника ударила инвестора в номере отеля
        #
        $ notif(t_("Моника ударила инвестора и убежала из номера."))
        #
        music Power_Bots_Loop
        imgd 18264
        mt "Надо было ударить его не только по яйцам, но и по голове!"
        mt "Чтобы у него отшибло память!"
        mt "!!!"

    # Моника переводит взгляд на Бифа, тот самодовольно улыбается
    music Groove2_85
    imgf 18265
    biff "Можете начинать, Миссис Бакфетт."
    imgd 18266
    mt "Ненавижу скотину Бифа!!!"
    mt "!!!"
    # Филипп смотрит на Монику с мерзкой ухмылочкой
    imgf 18267
    philip "Да, Миссис Бакфетт."
    philip "Мы с нетерпением ждем Вашей презентации."
    if monica_philip_visited_last_day > 0:
        # если Моника работает у него субботней шлюхой
        #
        $ notif(t_("Моника работает у Филиппа субботней шлюхой номер 2."))
        #
        music Power_Bots_Loop
        imgd 18268
        mt "Ненавижу мерзавца Филиппа!"
        mt "Отвратительный самодовольный жадный извращенец! Как и все они!"
        mt "!!!"
    else:
        # если не работает шлюхой, и не было сцены в туалете ресторана

        #
        $ notif(t_("Филипп предлагал Монике деньги за секс в ресторане Ле Гранд."))
        #
        imgd 18268
        mt "Это тот мерзкий тип, который постоянно пытается предложить мне какую-нибудь извращенскую гадость!"
        mt "Какой же он отвратительный!"
        #

    # Моника смотрит на экран
    # экран investors_1_2, меняется на
    # экран investors_1_1
    music Groove2_85
    sound camera_lens1
    imgf 18269
    mt "Черт!"
    mt "И как я должна комментировать эти кадры?!"
    music Loved_Up
    imgd 18270
    m "..."
    m "Господа, взгляните на экран..."
    # Моника говорит и кадры меняются
    imgd 18271
    m "Перед вами костюм, разработанный одним из известных дизайнеров нашего города."
    m "Черный лебедь." # кадр
    # меняется на investors_1_3
    sound camera_lens1
    imgd 18272
    m "Посмотрите на то, как прекрасно он смотрится. #он - it" # кадр
    # меняется на investors_1_4
    sound camera_lens1
    imgd 18273
    m "Какие плавные линии..." # кадр
    # меняется на investors_1_5
    sound camera_lens1
    imgd 18274
    m "Какое внимание к деталям..." # кадр
    # меняется на investors_1_6
    sound camera_lens1
    imgd 18275
    m "Этот костюм подчеркивает всю изящность и плавность линий моей... Кхм... Фигуры модели..." # кадр
    # откровенный кадр
    # меняется на investors_1_7
    music Groove2_85
    sound camera_lens1
    imgd 18276
    with hpunch
    investor2 "Ого!"
    investor4 "Ух ты!"
    music Power_Bots_Loop
    imgd 18277
    mt "!!!"
    mt "Биф мерзавец!" # гневно смотрит на Бифа
    music Hidden_Agenda
    imgd 18278
    biff "Продолжайте, Миссис Бакфетт..." # мерзко улыбается
    music Groove2_85
    imgf 18279
    m "На этом кадре..."
    m "..."
    m "Раскрывается вся... Вся красота и женственность модели..."
    m "А этот изысканный костюм ее выгодно подчеркивает... #ее - it" # кадр
    m "!!!"
    img 18280 hpunch
    mt "Я убью мерзавца Бифа!!!"

    # кадры фотосессии в костюме Черный лебедь меняются на кадры в платье Королева сердец
    # меняется на investors_1_8
    sound camera_lens1
    imgf 18300
    mt "Наконец-то, он сменил эти ужасные кадры!"
    mt "Я сейчас сгорю от стыда, О БОЖЕ!"
    mt "!!!"
    imgd 18301
    m "Эта серия фотографий была сделана благодаря Мистеру Кэмпбеллу."
    m "Который предоставил платье 'Королева сердец' из своей новой коллекции."
    m "Посмотрите на экран..."
    # меняется на investors_1_9
    sound camera_lens1
    imgd 18302
    m "Мы видим перед собой уверенную в себе, красивую, современную женщину без комплексов..."
    # меняется на investors_1_10
    sound camera_lens1
    imgd 18303
    m "Такой, как она, в глубине души мечтает стать любая женщина." # новый кадр
    # меняется на investors_1_11
    sound camera_lens1
    imgd 18304
    m "Такой женщиной, как она, мечтает обладать любой мужчина." # новый кадр
    m "Посмотрите на следующий кадр..."
    # меняется на investors_1_12
    sound camera_lens1
    imgd 18305
    m "На следующем кадре мы видим, что она постепенно раскрывается..." # новый кадр, откровеннее
    # меняется на investors_1_13
    sound camera_lens1
    imgd 18306
    m "Показывая нам свою уверенность, раскованность и сексуальность." # новый кадр
    music Loved_Up
    imgd 18307
    steve "Вау!"
    steve "Миссис Бакфетт, шикарные кадры!"
    imgf 18308
    investor4 "Поддерживаю..."
    investor3 "Это настоящее искусство, Миссис Бакфетт."
    imgd 18309
    investor2 "А меня больше восхищает Ваша смелость и раскованность, Мэм..."
    # Моника натягивая улыбку
    imgf 18310
    m "Благодарю вас, господа..."
    music Power_Bots_Loop
    img 18311 hpunch
    mt "О БОЖЕ!"
    mt "Они рассматривают эти ужасные кадры!"
    mt "!!!"
    fadeblack 2.0
    music Groove2_85
    imgfl 18312
    m "На этом кадре очень удачно выбран ракурс, раскрывающий всю красоту и оригинальность платья." # новый кадр
    imgd 18314
    mt "Моника, какой бред ты несешь!"
    mt "!!!"
    imgf 18313
    m "С этим номером журнала зафиксировано рекордное количество продаж."
    m "Тираж разошелся в кратчайшие сроки."
    m "И рост продаж продолжает увеличиваться с каждым новым номером."
    m "..."
    img 18315
    biff "???"
    m "!!!"
    # Шепчет
    img 18316 vpunch
    biff "Ну же, кукла! Ты помнишь сценарий!"
    imgd 18317
    m "В ближайшем будущем мы планируем провести фотосессию с привлечением модели мужчины."
    m "Что, несомненно, сделает кадры более... Более интересными для любой аудитории."
    # Биф вскакивает и перебивает Монику
    imgd 18318
    biff "Благодарю, Миссис Бакфетт."
    biff "А теперь я хочу дать слово нашему многоуважаемому мистеру Кэмпбеллу..."
    biff "Чье платье было представлено для проведения фотосессии."
    # Моника отходит немного в сторону, Кэмпбелл выходит к экрану
    sound man_steps
    imgf 18319
    w
    imgd 18320
    campbell "Эта фотосессия дала рост продаж моей дизайнерской одежды."
    campbell "Значительно увеличилась прибыль и возросла клиентская база."
    # кадр с фотосессии меняется на график
    # campbell_chart
    sound camera_lens1
    imgf 18321
    campbell "Вы можете посмотреть на график, представленный моими аналитиками."
    campbell "Это график продаж."
    campbell "На нем можно наблюдать резкий скачок в день выхода номера с Миссис Бакфетт в платье 'Королева сердец'. #нем - it"
    imgd 18322
    campbell "Господа, это действительно выгодная сделка."
    campbell "По расчетам моих аналитиков мои вложения полностью окупятся..."
    campbell "Причем за более краткие сроки, чем можно было предполагать."
    # инвесторы заинтересованы
    imgf 18323
    investor4 "Перспективы достаточно заманчивы..."
    investor2 "Да, рост продаж впечатляющий, Мистер Кэмпбелл."
    philip "Я, честно сказать, несколько удивлен..."
    investor3 "Мистер Кэмпбелл, действительно ли платье предоставлялось из Вашей последней коллекции?"
    imgd 18324
    campbell "Да. Это лимитированная коллекция для особых случаев."
    campbell "И я совсем не ожидал к ней такого интереса покупателей. #ней - it"
    campbell "Я вижу в этом заслугу Миссис Бакфетт..."
    campbell "Которая сделала такую великолепную фотосессию."
    # включается следующий слайд, где Моника сидит с широко раздвинутыми ногами
    # меняется на investors_1_13
    # Кэмпбелл заканчивает свою речь
    sound camera_lens1
    imgf 18326
    campbell "Я лично контролировал проведение фотосессии..."
    campbell "Хочу сказать, что остался очень доволен работой команды этого журнала."
    # Моника зло смотрит на Бифа, он довольно улыбается
    music Power_Bots_Loop
    img 18325
    mt "Биф! Ублюдок!"
    mt "!!!"
    # Биф подходит к Кэмпбеллу
    music Groove2_85
    imgf 18327
    biff "Спасибо, Мистер Кэмпбелл. Отличная речь!"
    biff "Господа! Добавлю, что Миссис Бакфет готова сотрудничать в любом формате."
    imgd 18328
    investor3 "Действительно ли это так, Миссис Бакфетт?"
    philip "Миссис Бакфетт, это Ваше следование новому курсу журнала не является притворством?"
    # Моника вынуждена сказать что нет и что
    music Pyro_Flow
    imgf 18329
    mt "Чертов Филипп!"
    mt "!!!"
    mt "Может, сказать им всю правду?"
    mt "Сказать, что Биф меня заставляет, угрожая увольнением?"
    mt "..."
    imgd 18330
    mt "Нет, мне лучше заручиться поддержкой одного из них."
    mt "Как я и планировала ранее."
    mt "Это будет лучший способ вышвырнуть Бифа из МОЕГО кресла!"
    mt "..."
    menu:
        "Это не притворство.":
            pass
    fadeblack 1.5
    music Groove2_85
    imgfl 18331
    m "..."
    m "Это не притворство, Мистер Филипп, я..."
    # Биф снова ее перебивает
    biff "Мы с Миссис Бакфетт хотим доказать вам серьезность наших намерений."
    biff "Господа, прошу вас пройти в фотостудию..."
    biff "Чтобы лично поприсутствовать на фотосессии Миссис Бакфетт в костюме..."
    biff "Который нам любезно предоставил Мистер Кэмпбелл."
    # Биф поворачивается к Монике
    imgd 18332
    biff "Миссис Бакфетт, благодарю вас за выступление перед нашими многоуважаемыми господами."
    biff "Вы можете идти переодеваться к фотосессии."
    # Моника зло на него смотрит
    music Power_Bots_Loop
    img 18333
    mt "Я заставлю тебя, сволочь, молить у меня прощения!"
    mt "За каждый откровенный кадр!"
    mt "И за эти унизительные презентации!"
    mt "Сволочь!"
    mt "!!!"
    # Моника выходит
    return

# мысли Моники, когда идет на любую другую локацию, кроме фотостудии
label ep213_dialogues4_biff_4:
    # не рендерить!!
    mt "Мне нужно идти в гримерную комнату и переодеться."
    return False

# если кликнуть на Алекса до того, как переоделась
label ep213_dialogues4_biff_5:
    # использовать имеющиеся арты
    music Groove2_85
    imgfl 12766
    m "Алекс, где костюм для фотосесии?"
    imgf 12763
    alex_photograph "Миссис Бакфетт, костюм в гримерной комнате."
    alex_photograph "Для фотосессии уже все готово."
    imgd 12764
    mt "Черт!"
    mt "!!!"
    return

# гримерка
label ep213_dialogues4_biff_6:
    # затемнение, звук переодевания
    # Моника осматривает костюм на себе
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 4.0
    img 18281 hpunch
    sound plastinka1b
    mt "Это что такое?"
    mt "Это костюм?!"
    music Power_Bots_Loop
    img 18282
    mt "?!?!?!"
    mt "Биф совсем охренел?!"
    mt "!!!"
    # заходит Биф
    sound man_steps
    fadeblack 2.0
    music Groove2_85
    imgfl 18283
    biff "Цыпочка уже переоделась?"
    biff "Отлично!"
    # Монику бомбит
    music Power_Bots_Loop
    img 18284 hpunch
    m "Ничего не отлично!"
    m "Я не собираюсь фотографироваться в ЭТОМ!!!"
    music Groove2_85
    imgf 18285
    biff "Так, кукла безмозглая!"
    biff "Еще слово - вылетишь из этого офиса ко всем чертям!"
    biff "Только попробуй сорви эту фотосессию!"
    imgd 18286
    biff "Я лично скажу инвесторам, что ты дешевая шлюха и готова отсосать у них за 5 баксов!"
    biff "Тебе все понятно?!"
    imgf 18287
    biff "И только попробуй открыть свой рот и что-то возразить во время фотосессии!"
    biff "Заставлю отсасывать у инвесторов за 5 центов!"
    biff "Шлюха!"
    img 18288
    m "!!!"
    $ menu_corruption = [monicaPresentation2Choice2]
    menu:
        "Понятно!": #corruption
            $ monicaBiffInvestorsPhotoshoot2 = True # Моника согласилась на фотосессию перед инвесторами
            pass
        "Пошел он к черту!":
            music Power_Bots_Loop
            sound anger2
            img 18289
            w
            sound snd_punch_face1
            imgd 18290
            w
            img 18291 hpunch
            w
            imgf 18292
            m "Я тебе не кукла и не шлюха, мерзавец!"
            m "Никакой фотосессии не будет!!!"
            m "!!!"
            music Groove2_85
            img 18293 vpunch
            biff "Ты не получишь никакую другую работу!"
            biff "Пока не сделаешь то, что Я тебе говорю!"
            music Power_Bots_Loop
            imgf 18294
            sound highheels_short_walk
            m "Пошел к черту!"
            mt "Я найду другой способ зарабатывать деньги!"
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не сделает эту фотосессию
            return False
    # Моника медлит
    music Hidden_Agenda
    imgf 18295
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "Где я смогу заработать деньги для сучки Виктории?"
    imgd 18296
    m "Я..."
    m "Я проведу эту фотосессию..."
    music Groove2_85
    imgf 18297
    biff "Ну вот, цыпочка."
    biff "Совсем другое дело!"
    biff "Быстро иди в фотостудию! Тебя уже все ждут!"
    # Биф выходит из гримерки
    sound man_steps
    imgd 18298
    w
    fadeblack 1.5
    music Power_Bots_Loop
    imgf 18299
    mt "Мерзкий ублюдок!!!"
    mt "Ненавижу его!!!"
    mt "Убью его!!!"
    mt "!!!"
    return


# если Моника отказалась фотографироваться и оказалась на улице, но потом передумала и пришла к Бифу
# офис, кабинет Бифа
label ep213_dialogues5_photoshoot_7:
    # использовать имеющиеся арты
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Hidden_Agenda
    imgfl 15888
    m "Биф..."
    m "Мне нужна работа."
    music Groove2_85
    imgf 15890
    biff "Я дам тебе работу, если ты согласишься на фотосессию..."
    biff "В том же костюме и в присутствии всех остальных инвесторов."
    imgd 15891
    m "..."
    imgd 15904
    biff "Ты согласна?"
    mt "!!!"
    $ menu_corruption = [monicaPresentation2Choice2]
    menu:
        "Согласна.": #corruption
            $ monicaBiffPhotoshootInvestor3 = True # Моника со 2-го раза согласилась фотографироваться перед инвесторами
            pass
        "Я не буду участвовать в этом!!!":
            music Power_Bots_Loop
            imgf 15906
            m "Нет! Я не буду фотографироваться в ЭТОМ!"
            music Groove2_85
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            imgd 15902
            biff "Если будешь и дальше спорить со мной..."
            biff "Я заставлю тебя фотографироваться с членом во рту!"
            music Power_Bots_Loop
            imgf 15892
            mt "!!!"
            mt "НЕНАВИЖУ!"
            mt "!!!"
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не сделает эту фотосессию
            return False
    music Pyro_Flow
    imgf 15892
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "Где я смогу заработать деньги для сучки Виктории?"
    imgd 15896
    m "Я..."
    m "Я проведу эту фотосессию..."
    music Groove2_85
    imgf 15893
    biff "Ну вот, цыпочка."
    biff "Совсем другое дело!"
    biff "Иди переодевайся."
    biff "Я пока позвоню инвесторам, чтобы они приехали на съемку."
    mt "..."
    #$ log1 = t_("Идти в фотостудию и провести фотосессию.")
    return


# фотостудия
# расставлены стулья, на них сидят все инвесторы
# Биф стоит сбоку
label ep213_dialogues4_biff_8:
    # ep213_photoshoot10.rpy
    return


# если Моника отказалась сдвигать трусики перед инвестором, но потом передумала и пришла к Бифу
# офис, кабинет Бифа
label ep211_dialogues3_photoshoot_9:
    # использовать имеющиеся арты
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Hidden_Agenda
    imgfl 15888
    m "Биф..."
    m "Мне нужны деньги..."
    m "Есть какая-нибудь работа?"
    music Groove2_85
    imgf 15890
    biff "Я дам тебе работу, если ты согласишься на условие Господина Инвестора..."
    biff "Наденешь тот же костюм и сдвинешь трусики."
    biff "А Алекс сделает снимок."
    imgd 15904
    m "..."
    biff "Ты согласна?"
    mt "!!!"
    $ menu_corruption = [monicaPresentation2Choice3]
    menu:
        "Согласна.": #corruption
            $ monicaBiffPhotoshootInvestor5 = True # Моника со 2-го раза согласилась сдвинуть трусики перед инвестором
            pass
        "Нет! Я не буду делать ЭТОГО!!!":
            music Power_Bots_Loop
            imgf 15905
            m "Нет! Я не буду делать ЭТОГО!"
            music Groove2_85
            imgd 15906
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не выполнишь условие Господина Инвестора!"
            music Power_Bots_Loop
            imgf 15892
            mt "НЕНАВИЖУ!"
            mt "!!!"
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не сделает эту фотосессию
            return False
    music Pyro_Flow
    imgf 15892
    mt "..."
    mt "У меня есть шанс сделать так, что еще один инвестор согласится на инвестицию в мой журнал!"
    mt "Но не таким же способом!"
    mt "А вдруг этот снимок станет общедоступным?!"
    mt "Что тогда, Моника?!"
    imgd 15895
    mt "?!"
    mt "Дьявол!"
    mt "Но если я сейчас откажусь..."
    mt "Где я потом смогу зарабатывать $ 5000 каждую неделю?!"
    imgd 12800
    m "Биф..."
    m "Я..."
    m "Я сделаю это..."
    music Groove2_85
    imgf 12815
    biff "Ну вот, цыпочка."
    biff "Совсем другое дело!"
    biff "Иди переодевайся."
    biff "Я пока позвоню инвестору, чтобы он приехал."
    mt "..."
    return True

# если после фотосессии заходит к Бифу в кабинет
# кабинет Бифа
label ep213_dialogues4_biff_10: # частично из лейбла ep211_dialogues3_photoshoot_8
    # использовать имеющиеся арты!
    # Биф сидит на своем месте, довольный
    music Groove2_85
    imgfl 12796
    biff "Папочка доволен, что цыпочка смогла убедить второго инвестора."
    biff "Но папочка недоволен тем, что осталось еще четыре колеблющихся инвесторов..."
    imgf 12868
    biff "Цыпочка должна проявить свои таланты убеждения..."
    biff "Полученные ею в прошлой жизни на грязной улице."
    biff "Иначе цыпочка рискует вернуться к ней!"
    # Моника зло на него смотрит
    music Power_Bots_Loop
    imgd 15864
    mt "Вот сволочь!!!"
    mt "!!!"
    return

# мысли Моники, когда вышла из офиса после проведения фотосессии
label ep213_dialogues4_biff_11:
    # не рендерить!
    mt "Моника, я не могу поверить, что ты сделала ЭТО!!!"
    mt "Как ты могла допустить подобное?!"
    mt "?!?!?!"
    mt "Мне нужно придумать, как прекратить это издевательство Бифа!"
    mt "Это не может продолжаться бесконечно!"
    mt "Я должна отомстить ему!"
    mt "И забрать обратно МОЙ журнал!!!"
    mt "!!!"
    return


label ep213_dialogues4_biff_12:
    $ menu_corruption = [biffFlashCardQuestReportBoobsCorruptionRequired, biffFlashCardQuestReportAssCorruptionRequired, biffCastingModelPosesCorruptionRequired, biffCastingKneesCorruptionRequired, biffCastingFloorCorruptionRequred]
    menu:
        "Показать грудь.": # corruption
            img 12783
            with fade
            w
#            m "Сегодня цыпочка-Босс пришла показать папочке свою грудь..." #-
            # Показывает грудь (нексолько кадров)
            music Loved_Up
            sound snd_fabric1
            img 13917
            with fadelong
            w
            img 13918
            with diss
            w
            img 13919
            with diss
            w
            img 13920
            with diss
            w
            img 12844
            with fade
            biff "Папочка доволен." #+

        "Показать попу.": #corruption
            img 12783
            with fade
            w
#            m "Сегодня цыпочка-Босс пришла показать папочке свою попу..." #-
            # Показывает Бифу попу (несколько кадров)
            music Loved_Up
            sound snd_fabric1
            img 20595
            with fadelong
            w
            img 20596
            with diss
            w
            img 20597
            with diss
            w
            img 20598
            with diss
            w
            img 20599
            with diss
            w
            img 20600
            with diss
            w
            img 12844
            with diss
            biff "Папочка доволен." #+

        "Раздеться и принимать различные модельные позы." if char_info["Biff"]["level"] >= 2 and biffLevel3Opened == True:
            $ store_music()
            call ep210_dialogues1_office_biff_1a() from _rcall_ep210_dialogues1_office_biff_1a_2
            $ restore_music()
            img 8445
            biff "Хорошо, папочка доволен!"
            if biffCastingStage < 1:
                $ biffCastingStage = 1
        "Раздеться и принимать различные модельные позы. (требуется ур.2) (disabled)" if char_info["Biff"]["level"] < 2 or biffLevel3Opened != True:
            pass
        "Раздеться и встать на колени задом к Бифу." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 1:
            $ store_music()
            call ep210_dialogues1_office_biff_1b() from _rcall_ep210_dialogues1_office_biff_1b_2
            $ restore_music()
            img 8445
            biff "Хорошо, папочка доволен!"
            if biffCastingStage < 2:
                $ biffCastingStage = 2
        "Раздеться и встать на колени задом к Бифу. (disabled)" if char_info["Biff"]["level"] < 2 or biffCastingStage < 1:
            pass
        "Раздеться и лечь на пол раздвинув ноги." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 2:
            $ store_music()
            call ep210_dialogues1_office_biff_1c() from _rcall_ep210_dialogues1_office_biff_1c_2
            $ restore_music()
            img 8445
            biff "Хорошо, папочка доволен!"
            if biffCastingStage < 3:
                $ biffCastingStage = 3
        "Раздеться и лечь на пол раздвинув ноги. (disabled)" if char_info["Biff"]["level"] < 2 or biffCastingStage < 2:
            pass
        "Раздеться и сесть на стол." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 3:
            $ menu_corruption = [0, biffCastingOneLegOnTheTable, biffCastingTableLegsOpen, biffCastingTableBack, biffCastingTableBlowjob]
            menu:
                "Назад.":
                    jump ep213_dialogues4_biff_12
                "Поставить на стол одну ногу." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 3:
                    $ store_music()
                    call ep212_dialogues7_biff1() from _rcall_ep212_dialogues7_biff1_2
                    $ restore_music()
                    img 8445
                    biff "Хорошо, папочка доволен!"
                    if biffCastingStage < 4:
                        $ biffCastingStage = 4
                "Поставить на стол одну ногу. (disabled)" if char_info["Biff"]["level"] < 2 and biffCastingStage < 3:
                    pass
                "Сесть на стол лицом к Бифу, широко раздвинув ноги." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 4:
                    $ store_music()
                    call ep212_dialogues7_biff2() from _rcall_ep212_dialogues7_biff2_2
                    $ restore_music()
                    img 8445
                    biff "Хорошо, папочка доволен!"
                    if biffCastingStage < 5:
                        $ biffCastingStage = 5
                "Сесть на стол лицом к Бифу, широко раздвинув ноги. (disabled)" if char_info["Biff"]["level"] < 2 and biffCastingStage < 4:
                    pass
                "Сесть на стол спиной к Бифу." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 5 and monicaOutfitsEnabled[9] == True:
                    $ store_music()
                    call ep216_dialogues0_biff1() from _rcall_ep216_dialogues0_biff1_2
                    $ restore_music()
                    if biffCastingStage < 6:
                        $ biffCastingStage = 6
                    if char_info["Biff"]["level"] <= 3:
                        $ add_char_progress("Biff", 50, "ep216_dialogues0_biff1" + str(day))
                    "Сесть на стол спиной к Бифу. (disabled)"  if char_info["Biff"]["level"] < 2 or biffCastingStage < 5 or monicaOutfitsEnabled[9] != True:
                    pass
                "Сесть на стол, достать член Бифа и взять его в рот."  if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 6 and monicaOutfitsEnabled[9] == True:
                    $ store_music()
                    call ep216_dialogues0_biff2() from _rcall_ep216_dialogues0_biff2_2
                    $ restore_music()
                    if _return == -1: # убежала, закрываем доступ в офис на неделю
                        call ep216_quests_biff_block_office() from _rcall_ep216_quests_biff_block_office_2
                        return -1
                    if biffCastingStage < 7:
                        $ biffCastingStage = 7
                    if char_info["Biff"]["level"] <= 3:
                        $ add_char_progress("Biff", 50, "ep216_dialogues0_biff2" + str(day))
                "Сесть на стол, достать член Бифа и взять его в рот. (disabled)" if char_info["Biff"]["level"] < 2 or biffCastingStage < 6 or monicaOutfitsEnabled[9] != True:
                    pass
                "Сесть на стол. достать член Бифа и возить им по киске." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 7 and monicaOutfitsEnabled[9] == True:
                    $ store_music()
                    call ep219_dialogues6_biff_1()
                    $ restore_music()
                    if _return == True:
                        if biffCastingStage < 8:
                            $ biffCastingStage = 8
                        if char_info["Biff"]["level"] <= 4:
                            $ add_char_progress("Biff", 50, "ep216_dialogues0_biff2" + str(day))
                "Сесть на стол. достать член Бифа и возить им по киске. (disabled)" if char_info["Biff"]["level"] < 2 or biffCastingStage < 7 or monicaOutfitsEnabled[9] != True:
                    pass
    return

label ep213_dialogues4_biff_13:
    mt "Эта сволочь Бифф совсем сдурел?!"
    mt "Что он себе позволяет?!!!"
    return
