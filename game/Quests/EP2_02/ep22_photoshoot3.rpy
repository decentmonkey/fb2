label ep22_photoshoot3:

    img 8317
    m "Алекс, это что? Какая-то шутка?"
    "Кто-то перепутал коробку для нарядов с одеждой для рабочих???"
    img 8318
    alex_photograph "Нет, Мэм!"
    "Вы сегодня девушка-рабочий! Бригадир!"
    img 8386
    m "Какого черта, Алекс?!?!"
    "Ты не забыл вообще-то кто я такая?!"
    alex_photograph "Мэм! Это распоряжение Мистера Бифа!"
    "У нас контракт с крупной строительной компанией!"
    "И, в конце концов, это всего-лишь образ, Миссис Бакфетт!"
    img 8387
    m "Эти штуки... Какие-то... Я не знаю как они называются..."
    "Можно я сниму их? Я могу пораниться!"
    alex_photograph "Нет, Мэм! Это часть образа!"
    img 8388
    m "Ладно... Только давай без своих грязных ракурсов..."
    alex_photograph "Так точно, Мэм!"


    label ep22_photoshoot3_pose1:
        #кадр
        alex_photograph "Мотор!"
        img 8389
        #up
        img 8390
        #side
        img 8391
        #down
        img 8392


    label ep22_photoshoot3_pose2:
        #кадр
        img 8393
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        m "Алекс! Ты снова начинаешь?!"
        "Мы не успели начать, а у тебя уже двусмысленные позы!"
        alex_photograph "Мэм! Эти фото на календарь строительной компании!"
        "Вы будете стимулировать рабочих трудиться лучше!"
        "Вы должны быть соблазнительны!"

        m "Не вижу в этом ничего соблазнительного, Алекс!"
        mt "О БОЖЕ! Я фотографируюсь на календарь для рабочих!"
        "Я - МОНИКА БАКФЕТТ!!"
        "О БОЖЕ!!!"

        #up
        img 8394
        #side+
        m "Алекс! Не начинай!"
        #иначе
        img 8395

        #down+
        m "Алекс! Хватит!"
        #иначе
        img 8396

    label ep22_photoshoot3_pose3:
        #кадр
        img 8397
        alex_photograph "Следующая поза, Миссис Бакфетт!"

        #up
        img 8398

        #side
        img 8399

        #down
        img 8400

    label ep22_photoshoot3_pose4:
        #кадр
        img 8401
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        m "Алекс! Я не буду вставать в такую развратную позу!"
        "И это не обсуждается!"
        #иначе
        #up
        img 8402
        #side+
        m "Алекс! Я не буду делать такой кадр!"
        img 8403

        #down+
        m "Алекс! Забудь про такие ракурсы!"
        img 8403

    label ep22_photoshoot3_pose5:
        #кадр
        img 8405
        alex_photograph "Следующая поза, Миссис Бакфетт!"

        #up
        img 8406

        #side
        img 8407
        img 8408

        #down+
        m "Алекс! Я не буду делать такой кадр!"
        img 8409

    label ep22_photoshoot3_pose6:
        #кадр
        img 8410
        alex_photograph "Следующая поза, Миссис Бакфетт!"

        #up+ (жесткий)
        alex_photograph "Миссис Бакфетт!"
        "Возьмите, пожалуйста, молоток и сделайте вид, как-будто вы его лижите."
        "Сексуально."
        "Это будет самый популярный кадр!"
        #если не хватает
        m "ЧТО??!"
        "НИКОГДА!"
        alex_photograph "Миссис Бакфетт! Но молоток чистый! Это реквизит!"
        "Я специально подготовил его!"
        "НИКОГДА!"
        #иначе
        m "Алекс!"
        "Это последнее что я сделаю!"
        "Ты меня достал своей назойливостью!"
        img 8413
        img 8414
        img 8415
        img 8416
        img 8417

        #side
        img 8411

        #down+
        m "Алекс! Забудь про такие ракурсы!"
        img 8412


    label ep22_photoshoot3_pose7:
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        "Пожалуйста, сядьте на колени и выдвиньте одну ногу вперед!"
        m "Хорошо, звучит не так уж страшно..."
        img 8419 #пикча
        m "ЧТО?!?!"
        "ЧТО ТЫ СДЕЛАЛ, МЕРЗАВЕЦ???"
        "Куда ты поставил молоток!"
        "Ты хоть заметил куда в какое место он упирается мне?!?!"
        alex_photograph "Миссис Бакфетт!"
        "И сделайте, пожалуйста, такое лицо как когда Вы облизывали молоток..."
        #если не хватает
        m "ЧТО?!?!"
        "Иди ты к черту!"
        "Это называется фотосессия для календаря?!?!"
        "Может быть мне еще снять шорты и дать ему свободу войти туда куда он упирается сейчас?!"
        alex_photograph "..."
        m "Ах! Что я спрашиваю!"
        "Для тебя это было бы прекрасной новостью!"
        "НО НЕ ДЛЯ МЕНЯ?!?!"
        "Фотосессия закончена!!!"
        #уходим на конец фотосессии

        #если хватает
        alex_photograph "Мэм, я понимаю, может быть Вам неудобно как он упирается..."
        "Но если Вам чуточку приятно это, то, пожалуйста, высуньте язычок..."
        "Без него композиция будет неполной..."
        "А ведь Вы знаете, что от меня ждут лучших результатов."
        "Иначе Мистер Биф уволит меня..."
        "Поверьте, этот кадр выглядит прилично..."
        m "..."
        "Алекс, это точно выглядит прилично?"
        alex_photograph "Да, Мэм!"
        "Поверьте мне!"
        m "Мне это не нравится, Алекс..."
        alex_photograph "Миссис Бакфетт... Не переживайте, я сделаю кадры быстрее чем будет заметно что Вы стали влажной..."
        m "ЧТО?!?!..."
        alex_photograph "Я снимаю, Миссис Бакфетт!"
        "Пожалуйста, покажите эмоции!"
        m "Я...."
        "Ладно..."

        #кадр
        img 8418

        #up
        img 8420
        w
        img 8421
        w
        img 8422
        w
        img 8423
        w
        img 8424
        w

        #side
        img 8425
        w
        img 8426
        w
        img 8427
        w
        img 8428
        w

        #down
        img 8429
        w
        img 8430
        w
        img 8431
        w
        img 8432
        w
        img 8433
        w


    label ep22_photoshoot3_end:
        img 8434
        alex_photograph "Мэм! Мы закончили фотосессию!"
        m "Наконец-то!!!"
        img 8435
        mt "Что теперь?"
        #Если кастинг у Бифа
        menu:
            "Переодеться назад...":
                call ep22_dialogue6_6()
            "Идти на кастинг к Бифу и притвориться цыпочкой...": #если есть кастинги
                mt "Биф ждет меня на свой дурацкий кастинг..."
                "Он говорил даст мне работу если я буду хорошей цыпочкой..."
                "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
                "Так может быть притвориться?"
                "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
                #если обещала
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."



    return

label ep22_photoshoot2_casting:
    m "Привет, Биф. Я пришла..."
    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это девушка-рабочий с календаря, который будет висеть у каждого менеджера строительной компании..."
            biff "Что девушка с календаря хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 3
            call ep22_casting()
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            m "Я пришла, потому что обещала хорошо вести себя..."
            #иначе
            m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 3
            $ chickMode = False
            call ep22_casting()
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
