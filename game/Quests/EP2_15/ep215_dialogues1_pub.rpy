default monicaMollyBattle1 = False # Моника узнала от Эшли о том, что Молли не платит проценты
default monicaMollyBattle2 = False # Моника пошла на 1-й батл с Молли
default monicaMollyBattle3 = False # Моника с Молли дерутся в гримерке - catfight
default monicaMollyBattle4 = False # Моника пошла на 2-й батл с Молли



# при условии, что был обнаженный приват всех девочек Shiny Hole перед банкиром
# возле сцены
# Моника перед выходом на сцену, а Молли уже уходит
label ep215_dialogues1_pub_1:
    # Молли подходит к Эшли, она в одежде
    img 31964
    w
    img 31965
    w
    img 31966
    # делает вид, как-будто Моника - пустое место, обращается к Эшли
    img 31967
    molly "Эшли, я на сегодня все."
    # Эшли ей улыбается
    ashley "Хорошо, Молли. Сколько ты сегодня заработала?"
    molly "Сегодня не так много... 90 баксов."
    img 31968
    ashley "А ты выполнила свои королевские обязанности?"
    molly "Конечно, Эшли..."
    ashley "Молодец, детка."
    molly "Ну ладно, я пошла. Давай, пока."
    # Молли бросает ехидный взгляд на Монику и уходит
    img 31969
    # Моника возмущена
    img 31970
    m "В смысле 'пока'?!"
    m "?!?!?!"
    m "А почему она не заплатила процент от чаевых?"
    ashley "Молли - королева Shiny Hole."
    ashley "Она самая лучшая девочка здесь."
    ashley "Неужели ты думаешь, что я буду брать проценты у нее?"
    img 31971
    m "Что за бред?!"
    m "Почему я плачу, а эта рыжая стерва все себе забирает?!"
    ashley "Это не бред, [monica_pub_name], а королевская привилегия."
    ashley "Если бы ты поменьше качала тут права и поактивнее работала на сцене..."
    ashley "Твоя попка могла бы занять место Молли."
    ashley "Но пока Молли королева Shiny Hole, она пользуется этой привилегией."
    m "!!!"
    img 31972
    ashley "Все, [monica_pub_name]. Ты на сегодня свободна. Можешь идти."
    # Эшли уходит
    # Моника стоит злая
    img 31973
    mt "Эта охреневшая шлюха все это время не платит процент?!"
    mt "Королевская привилегия?!"
    mt "Какая-то шлюха не платит, а я - Моника Бакфетт, плачу процент?!"
    mt "Потому что, видите-ли, она королева?!"
    mt "БЕСИТ!"
    mt "НЕНАВИЖУ!!!"
    mt "!!!"
    $ monicaMollyBattle1 = True # Моника узнала от Эшли о том, что Молли не платит проценты
    return

# после этого диалога, другой день
# Моника приходит в гримерку в день, работает Молли
# при клике на Молли
label ep215_dialogues1_pub_2:
    # Моника стоит у двери
    img 16130
    mt "Ненавижу эту сучку!"
    mt "!!!"
    # Молли поворачивается к Монике и опять начинает цеплять Монику
    img 16132
    w
    img 22815
    molly "О, пришла любительница потрясти своим голым задом на сцене!"
    molly "Аха-ха-ха!"
    # Моника зло
    img 22818
    m "Иди в жопу, Молли!"
    # Молли продолжает издеваться
    img 19194
    molly "Ты мне просто завидуешь, сучка. Признайся."
    molly "Мне не нужно полностью раздеваться на сцене, чтобы заинтересовать посетителей бара."
    molly "И заработать много чаевых."
    molly "А вот у тебя получается сделать это, только сняв трусы перед всеми!"
    img 19195
    molly "Кстати, зачем они тебе? Может быть ты вообще не будешь носить их?"
    molly "Аха-ха-ха!"
    # Моника злобно на нее смотрит
    img 19196
    mt "Она что, что-то знает?.."
    mt "Нет, не думаю..."
    m "!!!"
    # Молли продолжает веселиться
    img 19197
    molly "Поэтому ты и воруешь у меня деньги, сучка!"
    molly "Тебе со мной, королевой Shiny Hole, не сравниться! Никогда!"
    molly "И ты всегда будешь получать жалкие пару долларов за то, что голая кривляешься на сцене!"
    molly "Неудачница!"
    molly "Аха-ха-ха!"
    # Монику бомбит
    img 19198
    m "Это я неудачница?!"
    m "Ты совсем охренела, стерва?!?!?!!?"
    m "Ты думаешь, раз ты надела корону в этой грязной дыре, куда ходят одни алкаши!.."
    m "То значит ты здесь лучшая?!"
    img 19199
    m "Если я только захочу, я с тебя эту корону сниму в два счета!"
    m "Поняла, сучка!!!"
    # Молли язвительно
    img 19200
    molly "Если только в твоих снах! Аха-ха!"
    molly "Даже не мечтай об этом!"
    molly "Тебе никогда со мной не сравниться, поняла!"
    # Моника злится
    img 18225
    mt "Эта сучка с каждым днем все отвратительнее себя ведет!"
    mt "Хабалка! Ненавижу!"
    mt "Не имеющая вкуса, не разбирающаяся в моде дешевая шлюха!"
    mt "Мне нужно поставить эту стерву на место!"
    mt "!!!"
    img 19201
    m "Что?! Это мне с тобой не сравниться?!"
    m "Выйди со мной на сцену и мы посмотрим, кто здесь настоящая королева!"
    m "Уверена, это будешь не ты! Даже если разденешься догола!"
    # Молли ведет себя уверенно и с вызовом говорит
    img 19202
    molly "Ты хочешь соревноваться на сцене со мной? С самой королевой Shiny Hole?"
    img 19203
    m "Да! Или ты боишься потерять свою корону?!"
    img 19195
    molly "Аха-ха-ха!"
    molly "Не смеши меня!"
    molly "Ты же неудачница. Что бы ты на сцене не сделала, ты обречена на провал!"
    molly "Так что мне не о чем переживать, сучка!"
    # Молли отворачивается от Моники к своему зеркалу
    img 18224
    mt "Мерзкая рыжая стерва!"
    mt "Я сделаю все, чтобы лишить ее короны!"
    mt "Здесь только одна королева - Я, Моника Бакфетт!"
    mt "!!!"
    return

# при клике на Молли после этого диалога
# меню возникает единовременно, пока это событие не произойдет
label ep215_dialogues1_pub_3:
    # Моника стоит у двери
    img 22813
    molly "Ну что, сучка?!"
    molly "Тебе не терпится опозориться на сцене?"
    m "!!!"
    menu:
        "Батл с Молли.":
            img 22814
            m "Опозориться?!"
            m "Сегодня королевой стану Я!!!"
            img 16136
            molly "Я на твоем месте не была бы так уверена в этом!"
            molly "Ты вообще себя в зеркало видела?!"
            molly "Аха-ха!"
            img 22823
            mt "ААААААА!"
            mt "Тварь!!!"
            mt "!!!"
            $ monicaMollyBattle2 = True # Моника пошла на 1-й батл с Молли
            pass
        "Не сегодня.":
            img 22814
            m "Еще чего!"
            m "У меня сегодня нет времени на тебя, сучка."
            img 22816
            molly "Правильно, неудачница, иди зарабатываей свои несчастные центы."
            img 22820
            molly "И не забудь отдать процент Эшли!"
            molly "Аха-ха!"
            return
    img 16138
    m "Да пошла ты, сучка!"
    if monicaPubMollyDanceNude5 == True:
        img 22679
        molly "Сучка из нас двоих только одна. Это ТЫ!"
        molly "И ты сама в этом призналась."
        #
        $ notif(_("Моника признала себя сучкой перед Молли."))
        #
    img 22679
    m "!!!"
    img 16135
    molly "Пойдем, я надеру тебе задницу перед всеми!"
    return

# Моника и Молли у сцены, обе в жилетах
label ep215_dialogues1_pub_4:
    # Моника ведет себя спокойно, Молли не перестает ее цеплять и ехидничать
    # на сцене они ведут себя также
    img 31837
    w
    img 31838
    molly "Готова к провалу, сучка?!"
    img 31839
    m "Заткнись, Молли!"
    m "Сегодня ты останешься без своей короны!"
    return

# Моника и Молли на сцене
# выигрыш определяется криками толпы и баром
label ep215_dialogues1_pub_5:
    # Моника ведет себя спокойно, Молли ехидничает и заметно нервничает
    img 31840
    w
    img 31841
    w
    img 31842
    molly "Я начну первой, как и подобает королеве Shiny Hole!"
    img 31843
    molly "Смотри и учись, неудачница!"
    m "Да пошла ты!"
    # 1-й раунд
    # Молли в одежде, Моника в одежде
    # Молли начинает танцевать первая, делает три движения
    # потом Моника выходит, загораживая ее
    img 31844
    w
    img 31845
    w
    img 31846
    m "И это все, на что ты способна?!"
    m "Фи!"
    # Моника делает три движения
    # по крикам толпы Моника проигрывает, шкала бара у Молли выше
    img 31847
    ## здесь были правильны мысли Моники о том, почему эти плебеи недовольны и что то нужно предпринять##
    molly "Аха-ха!"
    molly "Поняла!? Уступи место настоящей королеве!"
    # 2-й раунд
    # Моника не отходит, а снимает жилет и делает еще три движения
    img 31848
    w
    img 31849
    w
    img 31850
    # публика кричит ВАУ
    # Молли злится и отталкивает Монику
    img 31851
    molly "Иди отсюда, сучка!"
    molly "Сейчас моя очередь!"
    img 31852
    m "Давай, покажи свои силиконовые сиськи."
    img 31853
    molly "Молчи, куда тебе со своими прыщиками до меня?!"
    # Молли тоже снимает жилет и танцует три движения
    # толпа кричит, что Молли королева, шкала бара у Молли выше
    # 3-й раунд
    img 31854
    w
    img 31855
    mt "Черт! Эта сучка уже второй раз выигрывает!"
    mt "Я не позволю этой дряни обойти меня, Монику Бакфетт!"
    mt "!!!"
    # Моника отталкивает Молли, начинает танцевать и снимает трусики
    img 31856
    w
    img 31857
    w
    img 31859
    w
    img 31858
    w
    img 31860
    w
    img 31861
    # толпа орет, что Моника королева
    # Моника торжествующе смотрит на Молли
    # Молли злится
    img 31862
    w
    img 31863
    molly "Ах ты дрянь!"
    molly "Думаешь, что покажешь свою голую задницу, как ты привыкла это делать, и обыграешь меня?!"
    molly "Я тебе не позволю этого, сучка!"
    img 31864
    w
    img 31865
    # Молли тоже раздевается, танцует, но выигрыша нет, шкала бара у Моники становится выше
    # Молли зло смотрит на Монику, ее бомбит, Моника спокойна
    # 4-й раунд
    img 31866
    w
    img 31867
    w
    img 31868
    molly "Это будет МОЯ победа!"
    molly "И корона только МОЯ!!!"
    # Молли со злостью срывает с себя маску и начинает грязно позировать
    img 31869
    w
    img 31870
    # толпа орет, что Молли королева, шкала бара у Молли выше, чем у Моники
    # Моника смотрит на нее с отвращением
    img 31871
    mt "Вот тварь!"
    mt "!!!"
    menu:
        "Снять маску.":
            img 31872
            mt "Я не готова снять маску!"
            mt "Вдруг меня кто-то узнает?!"
            mt "Я даже не хочу думать о последствиях!!!"
            mt "!!!"
            pass
        "Не делать этого!":
            img 31872
            mt "Я не буду делать этого!"
            mt "Это отвратительно и грязно!"
            mt "!!!"
            pass
    # Молли с видом победительницы подходит к Монике
    img 31873
    w
    img 31874
    molly "Ну что, сучка, уяснила, кто из нас настоящая королева?!"
    molly "Тебя здесь хотят видеть только из-за того..."
    molly "Что ты готова танцевать перед любой публикой с голой задницей!"
    molly "Ради популярности!"
    # Моника злобно на нее смотрит
    img 31875
    m "Ненавижу тебя!"
    m "Подлая сука!!!"
    m "!!!"
    return

# крики толпы
label ep215_dialogues1_pub_6:
    # 1-й раунд (в одежде) - Молли выигрывает
    customers1 "ВАУ!!! Битва сучек!" # танцует Молли
    customers3 "Охренительно, детка! Ты настоящая королева!" # танцует Молли
    customers2 "Да, рыжая королева! Покрути жопой! Вот так! ДАААА!" # танцует Молли
    customers4 "Давай, раздевайся, крошка!" # танцует Моника
    customers5 "Покажи нам свои сиськи!" # танцует Моника
    # 2-й раунд (в трусиках и масках) - Молли выигрывает
    customers1 "ВАААУ!" # танцует Моника
    customers5 "Потряси своими сиськами для нас! Давай еще!" # танцует Моника
    customers4 "Королева Молли! Покажи класс!" # танцует Молли
    customers3 "ДААА! Настоящая королева Shiny Hole!" # танцует Молли
    customers2 "ДА! Покажи нам свою королевскую попку!!!" # танцует Молли
    # 3-й раунд (только в масках) - Моника выигрывает
    customers5 "Вот она, королева! Охренительно, детка!" # танцует Моника
    customers2 "ДААА! Точно! Она королева!" # танцует Моника
    customers1 "Королева Shiny Hole! А где вторая голая попка?" # танцует Моника
    customers4 "Вау!!! Какая горячая детка!" # танцует Молли
    customers3 "Покажи нам свою киску, крошка!" # танцует Молли
    # 4-й раунд (Молли без маски) - Молли выигрывает
    customers5 "ДААААААА!" # танцует Молли
    customers4 "МОЛЛИ, КРОШКА, ТЫ ЭТО СДЕЛАЛАААААА!" # танцует Молли
    customers3 "МОЯ КОРОЛЕВА!" # танцует Молли
    customers2 "ДААА! КОРОЛЕВА SHINY HOLE!" # танцует Молли
    customers1 "ВАААААУ!" # танцует Молли
    return

# гримерка, после батла
# Моника и Молли стоят вдвоем
label ep215_dialogues1_pub_7:
    # Молли смотрит на Монику и ехидно хихикает
    img 19204
    molly "Неудачница!"
    molly "Аха-ха-ха!"
    img 19205
    m "Заткнись, сучка!"
    # в гримерку забегает Эшли, она в восторге
    img 19206
    ashley "Вот это вы устроили!!!"
    ashley "Так держать, девочки!!!"
    ashley "Красотки!!!"
    # Эшли смотрит на Молли
    img 19207
    ashley "Молли, детка, сколько заплатили эти денежные мешки?"
    img 19208
    molly "Что-то около 150 баксов..."
    img 19209
    ashley "Отлично!"
    ashley "Молли, раз ты победила, то забираешь все чаевые, что вы заработали!"
    # Моника возмущенно
    img 19210
    m "ВСЕ?!"
    m "?!!!?!?"
    # Молли ехидно смотрит на Монику
    img 19211
    molly "Хорошо, Эшли. Мне же не нужно платить тебе проценты? Все как обычно?"
    img 19212
    ashley "Конечно не нужно, крошка!"
    img 19213
    ashley "У королевы Shiny Hole есть свои привилегии!"
    # Эшли смотрит на Монику, потом подмигивает Молли и хлопает по попе
    img 19214
    ashley "Учись, [monica_pub_name], как нужно зарабатывать деньги!"
    img 19215
    w
    img 19216
    w
    img 19367
    molly "Хи-хи-хи!"
    img 19368
    w
    img 19217
    ashley "Королева, не забудь ко мне зайти перед уходом."
    ashley "Я соскучилась по твоей попке."
    # Эшли уходит
    # Моника зло смотрит на Молли
    img 19218
    m "Сучка!"
    # Молли самодовольно
    img 19219
    molly "Может я и сучка, но я все заработанные деньги оставляю у себя..."
    # Молли уходит
    # Монику бомбит про себя
    img 19220
    mt "Почему эта рыжая шлюха не платит проценты Эшли?!"
    mt "А Я должна платить!"
    mt "Еще эта сучка при каждом удобном случае подставлет меня перед Эшли!"
    mt "И я отдаю ей ВЕСЬ СВОЙ ЗАРАБОТОК!!!"
    img 19221
    mt "Это несправедливо!!!"
    mt "Почему?!"
    mt "Почему меня оружают эти мерзкие люди?!"
    mt "Почему такая добрая и изысканная натура как я должна страдать из-за них?!"
    mt "!!!"
    mt "Если она мне скажет еще хоть слово!.."
    mt "Я ее убью!!!"
    mt "!!!"
    return

# при клике на Эшли, когда Моника отдает чаевые в день 1-го батла с Молли
label ep215_dialogues1_pub_8:
    img 31974
    w
    img 31975
    ashley "[monica_pub_name], стой!"
    # Моника зло
    m "Я сегодня ничего не заработала!"
    # Эшли ей игриво
    img 31976
    ashley "А я сегодня болела за тебя, [monica_pub_name]..." # подмигивает
    ashley "Если бы ты выиграла, то стала бы королевой Shiny Hole..."
    ashley "А королева вообще не платит чаевые, как это сейчас делает Молли."
    ashley "Конечно, у королевы есть не только привилегии, но и определенные обязанности..." # взгляд на попу Моники
    ashley "Но это уже мелочи."
    img 31977
    mt "Мне плевать на эти обязанности!"
    mt "Я стану здесь королевой и со мной никто не сможет сравниться!"
    mt "!!!"
    return

# при условии, что был перый батл с Молли
# след. рабочий день, когда смена Молли
# клик на Молли
label ep215_dialogues1_pub_9:
    # Молли снова начинает цеплять Монику
    img 31924
    w
    img 31925
    molly "Пришла?"
    molly "Я думала, что ты постыдишься выходить на сцену после своего провала!"
    molly "Аха-ха!"
    # Моника злобно
    img 31926
    m "!!!"
    molly "Мало того, что неудачница, еще и воровка! Хи-хи!"
    molly "Мне, в отличие от тебя, не нужно платить проценты Эшли..."
    molly "Или воровать чужие деньги. Хи-хи!"
    molly "Давай, иди виляй своей голой жирной задницей, шлюха."
    img 31927
    m "!!!"
    menu:
        "Проигнорировать рыжую шлюху!":
            img 31928
            mt "Я не хочу разговаривать с этой сучкой!"
            mt "Она специально провоцирует меня, чтобы снова подставить перед Эшли!"
            mt "И вообще, Моника!"
            img 31929
            mt "Тебе не стоит опускаться до уровня этой тупой провинциалки, которая возомнила из себя королеву!"
            mt "Ты таких, как она, даже к кастингу в свой журнал не допускала!"
            mt "Мерзкая рыжая дрянь!"
            img 31930
            m "Иди в жопу, Молли!"
            # не будет доступна ни драка, ни второй батл
            return
        "Врезать ей!":
            $ monicaMollyBattle3 = True # Моника с Молли дерутся в гримерке - catfight
            pass
    # Монику бомбит, Молли надменно
    img 31931
    m "Ты, сучка! Ты победила только потому что сняла маску и опозорилась перед всем Shiny Hole!"
    m "И ты сверкала своей голой задницей!"
    img 31932
    molly "Мою задницу и меня любит весь Shiny Hole."
    molly "Я королева здесь, а ты - жалкая подстилка."
    molly "Твое дело - разносить пиво за пару центов чаевых..."
    img 31933
    molly "И ты снова грубо разговариваешь со мной."
    molly "Пожалуй, попрошу Эшли снова заставить тебя просить прощения передо мной."
    molly "Также, попрошу ее повысить процент, который она забирает с твоих чаевых."
    molly "Дешевая уличная шлюха..."
    # Моника в бешенстве
    img 31934
    m "ТВАРЬ!"
    # подбегает к Молли


# интерактивная сцена драки,
# меню выбора действий Моники в зависимости от бичности
# зациклить драку в одном из пунктов меню
# возможность проиграть или выиграть в зависимости от выбора игрока
label ep215_dialogues1_pub_9_loop1:
    menu:
        "Толкнуть сучку!": # высокая бичность
            img 31934
            m "Мерзкая дешевая потаскуха!!!"
            # толкает Молли, та падает со стула
            img 31935
            m "Никчемная шлюха!!!"
            img 31936
            # та вскакивает и толкает Монику в ответ
            img 31937
            w
            img 31938
            w
            img 31939
            w
            img 31940
            w
            img 31941
            molly "АХ ТЫ ДРЯНЬ!!!"
                menu:
                    "Вцепиться в ее волосы!": # высокая бичность
                        # Моника хватает Молли за волосы
                        img 31942
                        w
                        img 31943
                        w
                        img 31944
                        w
                        img 31945
                        m "МЕРЗКАЯ СУКА!!!"
                        img 31946
                        molly "ААААА!!!"
                        molly "СУЧКАААА!!!"
                        # Молли в ответ хватает Монику за волосы
                        img 31982
                        w
                        img 31983
                        w
                        img 31984
                            menu:
                                "Ударить эту сучку по груди!": # высокая бичность
                                    # Моника бьет Молли по груди
                                    img 31985
                                    m "НЕНАВИЖУ!!!"
                                    img 31986
                                    w
                                    img 31987
                                    m "УБЬЮ ТЕБЯ!!!"
                                    img 31988
                                    # Молли ослабляет свою хватку
                                    menu:
                                        "Врезать ей по лицу!": # высокая бичность
                                            img 31989
                                            w
                                            img 31990
                                            w
                                            img 31991
                                            w
                                            img 31992
                                            w
                                            img 31993
                                            w
                                            img 31994
                                            w
                                            img 31995
                                            # Моника с размаху бьет Молли по лицу, та теряет равновесия и падает на пол
                                            # падая, хватается за жилет Моники и срывает его
                                            # Молли на полу, Моника с размаху бьет ее ногой в живот
                                            img 31996
                                            w
                                            img 31997
                                            w
                                            img 31998
                                            m "Получай, шлюха!"
                                            img 31997
                                            w
                                            img 31998
                                            m "Ненавижу!"
                                            img 31997
                                            w
                                            img 31998
                                            m "Тварь!!!"
                                            # Молли скрючивается от боли, но потом хватает Монику за ногу в момент след удара
                                            # Моника теряет равновесие и падает на пол
                                            img 31999
                                            w
                                            img 32000
                                            w
                                            img 32001
                                            w
                                            img 32002
                                            pass
                                        "Толкнуть ее!":
                                            # Моника толкает Молли, та теряет равновесия и падает на пол
                                            img 32003
                                            w
                                            img 32004
                                            # падая, хватается за грудь Моники, срывает жилет
                                            img 32005
                                            w
                                            img 32006
                                            # Моника хватается за грудь, а Молли в это время бьет ее по ногам и Моника тоже падает
                                            img 32008
                                            w
                                            img 32007
                                            w
                                            img 32009
                                            m "АААА!!!"
                                            pass
                                    # Моника на полу бьет локтем Молли по лицу
                                    img 32010
                                    w
                                    img 32011
                                    w
                                    img 32012
                                    # та закрывается от боли
                                    img 32013
                                    molly "Сукаааа!!!"
                                    molly "Аааа!!!"
                                    # Моника лезет на Молли, садится сверху и хватает ее за шею
                                    img 32014
                                    w
                                    img 32015
                                    w
                                    img 32016
                                    w
                                    img 32017
                                    # Молли вцепляется ногтями в лицо Моники и сталкивает ее с себя
                                    img 32018
                                    w
                                    img 32019
                                    w
                                    img 32020
                                    w
                                    img 32021
                                    w
                                    img 32022
                                    pass
                                "Попытаться увернуться от Молли.": # Моника приличная
                                    # Моника пытается увернуться от Молли, которая пытается вцепится в ее волосы
                                    
                                    m "ААААА!!!"
                                    # но Молли хватает ее за волосы, резко опускает ее голову и бьет коленом по лицу
                                    molly "Получай, шлюха!"
                                    m "АААААА!!!"
                                        menu:
                                            "Ударить ее чем-нибудь!":
                                                # Моника тянется за стулом, но Молли опережает ее и отталкивает Монику
                                                # Моника падает на пол
                                                # Молли подбегает к Монике, садится сверху нее и начинает душить
                                                molly "Сукаааа!!!"
                                                molly "Убью тебяяяяя!!!"
                                                m "АААА!!!"
                                                pass
                                            "Толкнуть ее!":
                                                # Моника толкает Молли, но та бьет Монику по лицу
                                                molly "Сучка!!!"
                                                # Моника падает и хватается за трусы Молли, стаскивает их
                                                molly "ААА!!!"
                                                # Молли падает вслед за ней, потом быстро садится на Монику сверу и начинает душить
                                                m "АААА!!!"
                                                pass
                                    # Молли сидит на Монике сверху и душит ее
                                    # Моника вцепляется ногтями в лицо Молли и сталкивает ее с себя
                                    pass
        "Дать ей пощечину!": # Моника приличная
            m "Ах ты дрянь!!!"
            # размахивается и бьет Молли ладонью по лицу
            m "Как ты смеешь?!"
            molly "Ну все, сучка!"
            molly "Ты за это ответишь!"
            # Молли размахивается и бьет Моника в ответ по лицу кулаком
            # Моника едва удерживается на ногах
            # в шоке смотрит на Молли
            # переход на начальное меню, где доступен пункт "Толкнуть сучку!"
            jump ep215_dialogues1_pub_9_loop1
        "Уйти.":
            mt "Я не хочу разговаривать с этой сучкой!"
            mt "Она специально провоцирует меня, чтобы снова подставить перед Эшли!"
            m "Иди в жопу, Молли!"
            # Моника уходит
            return


    # обе лежат на полу снова вцепившись друг другу в волосы
    # они толкаются, таскают друг друга за волосы
    # тут забегает Эшли и начинает орать на них
    ashley "А ну-ка хватит!!!"
    ashley "Битву сучек надо устраивать на сцене!"
    ashley "Это, по крайней мере, приносит деньги!"
    ashley "А не устраивать тут драку!"
    ashley "Вы что, совсем охренели, такой шум тут подняли!?!?!?"
    # Молли с Моникой, несмотря на крики Эшли продолжают таскать друг друга за волосы
    menu:
        "Врезать сучке коленом в живот!":
            # Моника пытается пнуть Молли ногой, но у нее не получается
            m "Ненавижу!!!"
            # Молли вцепляется ногтями в грудь Моники
            m "АААА!!!"
            # Моника отпускает Молли и резко отстраняется
            # при этом она задевает Эшли, та теряет равновесие и падает между ними, юбка задирается
            pass
        "Вцепиться ногтями в ее грудь!": # высокая бичность
            # Моника убирает руки от волос Молли и вцепляется в ее грудь когтями
            molly "АААААА!!!"
            molly "ТВААААРЬ!!!"
            # Молли отпускает Монику и резко отстраняется
            # при этом она задевает Эшли, та теряет равновесие и падает между ними, юбка задирается
            pass
    # все трое на полу, Эшли пытается выбраться
    ashley "Мать вашу!!!"
    # начинают колотить друг друга на полу, один удар перепадает Эшли, которая пытается встать
    # Молли через Эшли пытается дотянуться до лица Моники и расцарапать его
    menu:
        "Укусить ее!": # Моника приличная
            # в тот момент, когда рука Молли рядом с лицом Моники, Моника зубами вцепляется в ее руку
            # Молли орет
            molly "СУУУУКААА!!! Я ТЕБЕ СЕЙЧАС!!!"
            # Молли облокачивается на Эшли, которая так и не может встать, перегибается через нее и колотит Монику по голове
            m "АААААА!!!"
            # Моника пытается закрываться от ударов
            # Эшли отталкивает с себя Молли, Эшли встает и начинает орать
            pass
        "Врезать ей!": # высокая бичность
            # Эшли уже почти удалось встать, но Моника толкает ее локтем, Эшли снова падает
            # Моника цепляется за рубашку Эшли, рубашка задирается (рвется?), грудь Эшли выскакивает наружу
            # Моника облокотившись на груди Эшли начинает колотить Молли куда попало - лицо, голова, грудь
            m "На!"
            m "Получай!"
            m "Мразь!"
            m "Тварь!"
            # Эшли отталкивает с себя Монику, Эшли встает и начинает орать
            pass
    ashley "Быстро прекратили!"
    ashley "[monica_pub_name]!"
    ashley "Мне что, вызвать полицию, чтобы вас разнять?!"
    # Эшли хватает Монику и поднимает ее на ноги
    # Моника злая, как собака, и лохматая, стоит рядом с Эшли, готова набросится на Молли, Эшли ее удерживает
    ashley "ХВАТИТ!"
    # Молли встает с пола
    ashley "[monica_pub_name]!"
    ashley "Молли!"
    ashley "Быстро на сцену! Обе!"
    ashley "Выясняйте отношения там!!!"
    # Моника с Молли зло смотрят друг на друга
    m "!!!"
    menu:
        "Батл с Молли.":
            m "Сегодня я точно надеру тебе задницу, мерзкая шлюха!"
            molly "За свою задницу беспокойся, сучка!"
            mt "Тварь!!!"
            mt "!!!"
            $ monicaMollyBattle4 = True # Моника пошла на 2-й батл с Молли
            pass
        "Отказаться.":
            m "Еще чего!"
            m "С меня достаточно!"
            m "Я не собираюсь делить сцену с этой сучкой!!!"
            molly "Правильно, неудачница, иди зарабатываей свои несчастные центы."
            molly "И не забудь отдать процент Эшли!"
            molly "Аха-ха!"
            # Эшли уходит
            ashley "[monica_pub_name], тогда иди быстро на сцену!"
            ashley "Какого черта ты до сих пор тут?!"
            # Моника идет танцевать одна
            # если не идти на батл, а снова кликнуть на Молли, то можно будет повторить сцену драки
            return
    ashley "Быстро тащите свои задницы на сцену!"
    # Моника с Молли переглядываются зло и идут к выходу с гримерки
    # Эшли выходит на ними следом
    return

# Моника и Молли на сцене
# выигрыш определяется криками толпы и баром
label ep215_dialogues1_pub_10:
    # Моника ведет себя спокойно, Молли ехидничает и заметно нервничает
    img 31876
    w
    img 31877
    w
    img 31878
    molly "У тебя нет шансов победить меня, сучка!"
    img 31876
    m "Снова будешь ползать по сцене своей голой задницей, шлюха?"
    molly "Заткнись!!!"
    # 1-й раунд
    # Молли в одежде, Моника в одежде
    # Молли начинает танцевать первая, делает три движения
    img 31879
    # потом Моника выходит, загораживая ее
    img 31880
    w
    img 31881
    m "Все? Покривлялась, сучка?!"
    img 31882
    w
    img 31883
    m "Иди отсюда!"
    img 31884
    # Моника делает три движения
    # по крикам толпы Моника проигрывает, шкала бара у Молли выше
    img 31885
    w
    ## возможно уместны какие-нибудь мысли Моники о том, почему она проигрывает ##
    img 31886
    w
    img 31887
    molly "Моя очередь!"
    molly "Убери свою жирную задницу!"
    # 2-й раунд
    # Моника не отходит, а снимает жилет и делает еще три движения
    img 31888
    w
    img 31889
    w
    img 31890
    # Молли злится и отталкивает Монику
    img 31891
    w
    img 31892
    molly "Убирайся отсюда!"
    molly "Неудачница!"
    img 31893
    w
    img 31894
    m "Да пошла ты, жирная корова!"
    # Молли тоже снимает жилет и танцует три движения
    # толпа кричит, что Молли королева, шкала бара у Молли выше
    # 3-й раунд
    img 31895
    w
    ## может какие-нибудь мысли Молли ##
    img 31896
    w
    img 31897
    mt "Я должна сегодня выиграть эту битву!"
    mt "Иначе я не Моника Бакфетт!!!"
    mt "!!!"
    # Моника отталкивает Молли, начинает танцевать и снимает трусики
    img 31898
    w
    img 31899
    w
    img 31900
    w
    img 31901
    w
    img 31902
    # толпа орет, что Моника королева
    # Моника торжествующе смотрит на Молли
    # Молли злится
    img 31903
    w
    img 31904
    molly "Думаешь, ты кого-то удивишь своей голой задницей?!"
    molly "Она здесь всем уже надоела!"
    molly "Аха-ха!"
    # Молли тоже раздевается, танцует, но выигрыша нет, шкала бара у Моники становится выше
    img 31905
    w
    img 31906
    w
    img 31907
    w
    img 31908
    w
    img 31909
    # Молли зло смотрит на Монику, ее бомбит, Моника спокойна
    # 4-й раунд
    img 31910
    molly "Ты снова опозорилась, неудачница!!!"
    molly "Грязная воровка!!!"
    # Молли со злостью срывает с себя маску и начинает грязно позировать 3 движения
    img 31911
    w
    img 31912
    # толпа орет, что Молли королева, шкала бара у Молли выше, чем у Моники
    img 31913
    w
    img 31914
    mt "Мерзкая подлая сука!"
    mt "В этот раз я не позволю тебе выиграть!"
    mt "!!!"
    menu:
        "Снять маску!":
            img 31915
            w
            img 31916
            mt "К черту эту маску!"
            mt "!!!"
            pass
        "Не делать этого!":
            img 31872
            mt "Я не буду делать этого!"
            mt "Это отвратительно и грязно!"
            mt "!!!"
            # возможность повтора драки и этого батла
            return
    # Моника выходит вперед, загораживая Молли и снимает с себя маску
    # Моника начинает тоже грязно позировать 3 движения потом встает
    img 31917
    # толпа ревет, что Моника королева, шкала бара у Моники на максимуме
    # безоговорочная победа Моники, триумф
    # она стоит посреди сцены, обнаженная и без маски
    # высокомерно смотрит на злую Молли
    img 31918
    w
    img 31920
    w
    img 31919
    w
    img 31921
    w
    img 31922
    w
    img 31923
    m "Поняла, дрянь, кто из нас королева?!"
    m "Корона теперь моя, а ты никто!"
    molly "!!!"
    # Молли сидит на сцене голая, полулежа, смотрит на Монику снизу вверх, как поверженный враг (на лице отчаяние)
    return

# Показываем картину с Моникой в гримерке вместо картины с Молли (королева shiny hole)

# гримерка после батла
# Моника вдвоем с Молли
label ep215_dialogues1_pub_11:
    # Моника торжествует, Молли злая и униженная
    img 19222
    m "Ну что, сучка?! Что ты скажешь новой королеве Shiny Hole?"
    img 19223
    molly "Я тебе этого просто так не оставлю!" # смотрит на картину (вид из картины)
    img 19224
    m "Ты еще угрожаешь мне, своей королеве?"
    # забегает довольная Эшли, обращается к Монике
    img 19225
    ashley "Я всегда знала, что эта попка покорит нашу сцену!"
    ashley "[monica_pub_name], теперь ты новая королева!"
    img 31947
    ashley "И чтобы больше никаких драк!!!"
    ashley "Это вас обеих касается! Тебе понятно, Молли?!"
    # Молли зло отвечает
    img 31948
    molly "ДА!"

    # затемнение, Молли оделась
    img 31949
    w
    img 31950
    w
    img 31951
    w
    img 31952
    ashley "С этого дня ты, Молли, должна отдавать мне проценты со своих чаевых."
    ashley "А [monica_pub_name] всю выручку будет забирать себе."
    # Эшли смотрит на Монику игриво
    img 31953
    ashley "Это твоя королевская привелегия, [monica_pub_name]..."
    # Эшли кладет руку на ее попу и сжимает ее, Моника делает вид, что не замечает этого
    img 31954
    w
    img 31956
    m "..."
    img 31955
    ashley "У королевской попки должны быть королевские чаевые..."
    # Моника все это время высокомерно смотрит на Молли, та молча зло на нее
    img 31957
    molly "!!!"
    m "!!!"

    # держа руку на попе Моники, игриво
    img 31958
    ashley "И, Молли, если королева пожалуется мне, то тебе придется извиняться перед ней..."
    # Молли с психом уходит
    img 31959
    # Эшли пошло подмигивает Монике и тоже выходит
    img 31954
    w
    img 31960
    # Моника про себя злорадствует
    img 31961
    w
    img 31962
    mt "Я сегодня заработала 200 долларов за одно выступление!"
    mt "И ни цента не должна теперь никому отдавать!"
    mt "В отличие от рыжеволосой шлюхи!"
    mt "Так и надо этой сучке! Пусть знает свое место!"
    mt "Неважно где и неважно как, но я всегда была и остаюсь королевой!"
    if monicaBitch == True:
        img 31963
        mt "И никакие жалкие людишки не смогут встать у меня на пути!"
    $ log1 = _("Теперь корона Shiny Hole принадлежит МНЕ! Я буду пользоваться королевскими привилегиями! А эта сучка Молли теперь никто!") # квест-лог
    return

# в другой рабочий день после 2-го батла Моника заходит в гримерку
# работает Молли
label ep215_dialogues1_pub_12:
    # не рендерить!!
    # Моника смотрит на Молли высокомерно, та на нее зло
    mt "Я не собираюсь с ней разговаривать!"
    mt "Не королевское это дело общаться с плебеями!"
    return

# в другой рабочий день после 2-го батла Моника заходит в гримерку
# работает Клэр
label ep215_dialogues1_pub_13:
    # Клэр, как обычно, сидит за своим столиком
    mt "Интересно, Клэр знает о том, как я поставила рыжую шлюху на место?"
    # Клэр поворачивается к Монике
    clare "Моника, привет!"
    clare "Слышала о твоем триумфе! Поздравляю!" # указывает на картину
    m "Привет, Клэр!"
    m "Да, я проучила рыжую стерву! Ты бы это видела!"
    clare "Я рада, что ты ее проучила и теперь сможешь хоть что-то здесь зарабатывать."
    clare "Но все равно будь аккуратнее с Молли..."
    clare "Она захочет теперь отомстить тебе."
    clare "Если что, ты знаешь, что я всегда готова помочь тебе, Моника."
    m "Спасибо, Клэр!"
    return

# при клике на Эшли, когда Моника отдает чаевые после того, как стала королевой
label ep215_dialogues1_pub_14:
    img 31978
    w
    img 31979
    ashley "[monica_pub_name], ты теперь королева Shiny Hole..."
    ashley "И тебе полагается не отдавать мне процент от заработка."
    mt "Наконец-то!!!"
    # Эшли улыбается, облизываясь и смотрит на попу Моники
    img 31980
    ashley "Но не забывай про свои королевские обязанности..."
    m "..."
    # подмигивает Монике и уходит
    img 31981
    mt "Извращенка!"
    mt "Что это еще за королевские обязанности?"
    mt "У королев нет никаких обязанностей!"
    mt "Мне плевать на это, я буду наслаждаться своими королевскими привилегиями!"
    mt "Моника, ты это заслужила!"
    return
