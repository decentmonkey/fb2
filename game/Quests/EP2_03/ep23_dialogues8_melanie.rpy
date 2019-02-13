# Диалог Мелани и Моника после Дика
# Открывается локация гримерки
# Мелани днем и вечером в гримерке, прихорашивается.
label ep23_dialogues8_1:
# Если спросить у Алекса где Мелани, то он начинает отвечать что она в гримерке
    m "Алекс, ты знаешь где Мелани?"
    alex_photograph "Она в гримерной комнате, Миссис Бакфетт!"
    return

label ep23_dialogues8_2:
    # Моника начинает говорить с Мелани по поводу того как она сходила к Дику
    # Здавствуй, Мелани. Ты общалась с Диком?
    # Есть какие-то новости?
    # Мелани отвечает что да, она уже позаботилась об этом.
    # Моника заинтересована. Ну как? Расскажи?
    # У тебя получилось обойти эту сучку Викторию?
    # Мелани отвечает что она даже не заметила ее. Очень странно что Миссис Бакфетт обращает так много внимания на эту Викторию.
    # Говорит что пообщалась с Диком в приватной обстановке и узнала много нового про то дело, о котором говорила Моника.
    # И про саму Миссис Бакфетт (Мелани язвительно ухмыляется)
    img 9029
    m "Здравствуй, Мелани. Ты общалась с Диком?"
    "Есть какие-то новости?"
    melanie "Да, Миссис Бакфетт. Я уже позаботилась об этом."
    m "Ну и как? Расскажи!"
    "У тебя получилось обойти эту сучку Викторию?"
    img 9030
    melanie "Я даже не заметила ее."
    "Очень странно что Вы, Миссис Бакфетт, обращаете столько внимания на эту Викторию."
    "Мне удалось пообщаться с Диком в приватной обстановке и я узнала много нового."
    "Про то дело, о котором Вы мне говорили..."
    img 9031
    "И про Вас саму... Я не думала что у Вас все так далеко зашло..."
    # Моника зло спрашивает и что же она узнала? Кто за всем этим стоит? Этот мерзавец Дик?
    img 9032
    m "И что же ты узнала? Кто за всем этим стоит?"
    img 9033
    "Этот мерзавец Дик?"

    # Мелани отвечает что нет. Дик в этой ситуации никак не замешан и что он реагировал по мере развития событий.
    # Он действительно начал дело, чтобы помочь Монике и вытащил ее из тюрьмы.
    # Моника спрашивает зло: Помочь?? Да знаешь-ли ты как он теперь "помогает" мне?!
    # Мелани отвечает что знает (улыбается)
    img 9034
    melanie "Нет, Миссис Бакфетт."
    "Мистер Дик в этой ситуации никак не замешан. Он реагировал по мере развития событий."
    "Он действительно начал дело, чтобы помочь Вам и вытащил Вас из тюрьмы."
    img 9035
    m "Помочь?!"
    "Да знаешь-ли ты как он теперь 'помогает' мне?!"
    img 9036
    melanie "Знаю..."

    # Моника спрашивает откуда эта сучка Виктория взялась вообще? Почему она так не любит Монику.
    # Мелани говорит что Виктория была еще задолго до Моники. Их отношения с Диком начались ранее.
    # Дик параллельно пытался ухаживать за Вами, Миссис Бакфетт.
    # Но, когда Вы начали отвечать взаимностью и встречаться с ним, Виктория почувствовала опасность, исходящую от Вас.
    # Сначала она выжила с места текущую секретаршу Дика, чтобы быть поближе к нему.
    # Виктория ревнует, Миссис Бакфетт, и потому ведет себя так агрессивно.
    # Более того, я навела справки про эту девочку, и могу сказать что у нее
    # садистские наклонности по отношению к тем кто встает на ее пути.
    img 9037
    m "Ладно, давай дальше!"
    "Откуда вообще взялась эта сучка Виктория?"
    "И почему она так меня не любит?"
    img 9038
    melanie "Виктория общалась с Диком задолго до Вас, Миссис Бакфетт."
    "Их отношения с Диком начались ранее."
    "Дик параллельно пытался ухаживать за Вами, Миссис Бакфетт."
    "Но, когда Вы начали отвечать взаимностью и встречаться с ним, Виктория почувствовала опасность."
    "Опасность, исходящую от Вас."
    img 9039
    "Она даже выжила с места текущую секретаршу Дика, чтобы быть поближе к нему."
    img 9040
    "Виктория ревнует, Миссис Бакфетт. И потому ведет себя так агрессивно."
    img 9041
    m "..."
    img 9042
    melanie "Более того, я навела справки про эту девочку..."
    "И могу сказать что у нее садистские наклонности по отношению к тем..."
    "Кто встает на ее пути."

    # Я не знаю как Вы с ней "договорились" Миссис Бакфетт...
    # Вам ведь не пришлось делать никаких странных вещей при этом?
    # Моника смущенно спрашивает что Мелани имеет ввиду?
    # Мелани улыбается и молчит.
    # Моника зло отвечает что не понимает о чем вообще идет речь.
    # Что Моника просто поговорила с Викторией и та пошла ей навстречу.
    # И хватит об этом.
    img 9043
    melanie "Я не знаю как Вы с ней 'договорились' Миссис Бакфетт..."
    "Вам ведь не пришлось делать никаких странных вещей при этом?"
    img 9044
    m "Мелани, что ты имеешь ввиду? Каких странных вещей?"
    img 9045
    melanie "..."
    img 9046
    m "Мелани, я не понимаю о чем вообще идет речь!"
    "Я просто поговорила с Викторией и та пошла мне навстречу!"
    img 9047
    "Не только ты умеешь находить общий язык с людьми!"
    "И хватит об этом!!!"

    # Так значит это не Дик все затеял?
    # Мелани отвечает что нет, это не Дик. Дик наоборот, помогает Монике и той следует ценить его помощь.
    # Так как ему приходится тратить на это действительно много сил.
    # Дик действительно любил Монику, из-за ее социального статуса.
    # И, когда Моника лишилась его, то потерял интерес к ней.
    # Вам, Миссис Бакфетт, следовало бы поучиться тому как надо обращаться с мужчинами...
    # Моника саркастически спрашивает, что если он потерял интерес к Монике, то почему же он продолжает помогать ей?
    # Мелани говорит что сейчас его об этом попросила Виктория.
    # Это весьма удивительно. Потому я и спросила у Вас как Вам удалось "договориться" с ней?
    img 9045
    melanie "..."
    img 9048
    m "Так значит это не Дик все затеял?"
    img 9049
    melanie "Нет, это не Дик."
    "Наоборот, Дик помогает Вам."
    "И Вам следует ценить его помощь."
    "Ему приходится тратить на это действительно много сил."
    m "..."
    img 9050
    melanie "Дик действительно любил Вас, Миссис Бакфетт."
    "Из-за Вашего социального статуса."
    "И, когда Вы лишилсь его, то потерял интерес к Вам."
    img 9051
    "Вам, Миссис Бакфетт, следовало бы поучиться тому, как надо обращаться с мужчинами..."
    img 9052
    m "Да? Потерял интерес? Вот так вот прямо?"
    "Хорошо, если он потерял интерес ко мне, то почему же он продолжает помогать мне?"
    m "..."
    img 9053
    melanie "..."
    melanie "Потому что об этом его попросила Виктория."
    "Это весьма удивительно."
    "Потому я и спросила у Вас как Вам удалось 'договориться' с ней?"

    # Моника зло щурится.
    # Мелани улыбается
    # Моника говорит: хорошо, Мелани, спасибо за то что ты узнала.
    # Может быть ты скажешь тогда кто действительно стоит за этом?
    # Мелани отвечает: Маркус...
    # Моника испуганно спрашивает: Ты знаешь про Маркуса?!
    # Мелани спокойно говорит: Да, Дик рассказал мне про все. Он такой забавный медвежонок...
    # Моника кривится...
    img 9054
    m "..."
    img 9055
    melanie "..."
    img 9056
    m "Хорошо, Мелани..."
    "Спасибо за то что ты узнала."
    "Но, может быть, ты скажешь тогда кто действительно стоит за всем этим?"
    img 9057
    melanie "Маркус..."
    img 9058
    m "Ты знаешь про Маркуса?!"
    img 9059
    melanie "Да, Дик рассказал мне про все."
    "Он такой забавный медвежонок..."
    img 9060
    m "..."

    # Хорошо... Мелани...
    # Если ты такая умная, может быть у тебя есть идеи как мне решить все это?
    # Мелани отвечает: Конечно, Миссис Бакфетт. Это довольно просто.
    # И как же?! (Моника встает в позу)
    # Мелани улыбается: Найти подход к Маркусу...
    # Моника говорит ты представляешь себе о чем вообще говоришь? Ты хоть знаешь этого человека?
    # Мелани отвечает что Миссис Бакфетт просто не понимает.
    # Что то что с ней случилось - это не из-за денег.
    # Здесь явно замешаны отношения мужчины и женщины.
    # Вы просто кому-то понравились, Миссис Бакфетт. Кому-то у кого есть власть.
    # И Вам Вам характер не позволяет разобраться с этим.

    img 9061
    with fade
    m "Хорошо... Мелани..."
    "Если ты такая умная, может быть у тебя есть идеи как мне решить все это?"
    melanie "Конечно, Миссис Бакфетт. Это довольно просто."
    m "И как же?!"
    img 9062
    melanie "Найти подход к Маркусу..."
    img 9063
    m "Ты представляешь себе о чем вообще говоришь? Ты хоть знаешь что это за человек?"
    img 9064
    melanie "Миссис Бакфетт, Вы просто не понимаете..."
    "То что с Вами случилось - это не из-за денег."
    "Здесь явно замешаны отношения мужчины и женщины."
    img 9065
    "Вы просто кому-то понравились, Миссис Бакфетт."
    "Кому-то у кого есть власть."
    "И Вам Ваш характер не позволяет разобраться с этим."
    img 9066
    "Вместо того чтобы улыбнуться пауку, Вы продолжаете дергаться."
    "Все больше запутываясь в его паутину."

    img 9065
    if monicaBitch == True:
        # Monica Bitch:
        melanie "Вы просто сучка, которая думает только о себе."
    else:
        # Monica Decent:
        melanie "Вы слишком скромная, Миссис Бакфетт."

    # Моника отвечает что Мелани не стоит оценивать ее, пусть она не забывает свое место.
    # Мелани улыбается.
    img 9067
    with fade
    m "Мелани, тебе не стоит оценивать меня, не забывай свое место!"
    img 9065
    melanie "..."

    # Моника говорит что у нее не получится найти подход к Маркусу.
    # Это невозможно.
    img 9068
    with fade
    m "Я... Я не смогу найти подход к Маркусу."
    img 9069
    "Это невозможно...."

    # Мелани говорит: Вам снова нужна моя помощь, Миссис Бакфетт?
    # Моника спрашивает как Мелани может помочь?
    img 9070
    melanie "Вам снова нужна моя помощь, Миссис Бакфетт?"
    img 9071
    m "И как ты, Мелани, можешь помочь?"

    # Мелани говорит что хотела бы чтобы Миссис Бакфетт вернула свое положение, ведь это хорошо для карьеры Мелани.
    # Мелани может сделать так, чтобы Виктория исчезла с горизонта, а Мистер Дик помогал Монике в впредь.
    # Но для этого Мелани придется переспать с ним. Но она не любит это делать с теми, кто ей не нравится.
    # Спрашивает, этот Маркус, он симпатичный?
    img 9072
    melanie "Миссис Бакфетт, я бы хотела чтобы Вы вернули свое положение."
    "Это хорошо для моей карьеры..."
    melanie "Я могу сделать так, чтобы Виктория исчезла с горизонта."
    "А Мистер Дик помогал бы Вам и впредь."
    img 9073
    "Но, боюсь, что для этого мне придется переспать с Диком."
    "А я не люблю это делать с теми, кто мне не нравится."
    img 9074
    m "..."
    img 9075
    melanie "Миссис Бакфетт, скажите."
    "Маркус симпатичный?"

    # Моника запинается... Ммаркус? Симпатичный?
    # Я... не знаю... Мелани
    # Мне трудно об этом судить...
    # Ну Вы же видел его, Миссис Бакфетт?

    # Ддда... видела.
    # Воспоминания как Моника сидит голая у Маркуса.
    # На фоне голос Мелани.
    # Ну и как он выглядит? Он не слишком толстый?
    # Моника отвечает что нет...
    # Он красавчик...
    img 9076
    m "Мммаркус? Симпатичный???"
    "Я... не знаю... Мелани..."
    "Мне трудно об этом судить..."
    melanie "Ну Вы же видели его, Миссис Бакфетт?"

    m "Ддда... видела."
    # Воспоминания как Моника сидит голая у Маркуса.
    img 9077
    melanie "Ну и как он выглядит?"
    "Он не слишком толстый?"
    img 9078
    m "Нннет..."
    img 9079
    melanie "А какой он? Он красавчик?"
    img 9080
    m "Ддддаа..."

    # Возвращение к Мелани

    # Мелани говорит: В таком случае я могу помочь Вам, Миссис Бакфетт.
    # Моника говорит Мелани: Ты хочешь идти к Маркусу?!
    # Ты представляешь насколько это опасно?
    # Мелани отвечает, смеясь: Так опасно, как идти мимо Виктории? Хи-хи
    # Миссис Бакфетт. Красивые женщины любят опасных мужчин!
    # Это даже интереснее!
    # Моника говорит: Но...
    # Мелани: Миссис Бакфетт, можете быть уверены в моих силах...
    img 9079
    melanie "В таком случае, я могу помочь Вам, Миссис Бакфетт."
    img 9081
    m "Ты хочешь идти к Маркусу?!"
    "Ты представляешь насколько это опасно?"
    img 9082
    melanie "Также опасно, как идти мимо Виктории? Хи-хи"
    img 9083
    "Миссис Бакфетт, красивые женщины любят опасных мужчин!"
    "Это даже интереснее!"
    m "Но..."
    melanie "Миссис Бакфетт, можете быть уверены в моих силах..."

    # Моника: То есть ты можешь решить вопрос Маркусом, чтобы он оставил меня в покое?
    # Мелани: Я думаю что даже смогу уговорить его восстановить Ваши документы, Миссис Бакфетт.
    # И вернуть Вашу компанию...
    # Моника думает: ЧТО? НЕУЖЕЛИ ЭТО МОЖЕТ ПРОИЗОЙТИ?!?
    # Я ДАЖЕ НЕ МОГЛА ОБ ЭТОМ МЕЧТАТЬ!!!
    # Моника: Мелани, ты действитеьно можешь сделать это? Правда?
    # Мелани: Да, Миссис Бакфетт, но не просто так...
    # Моника говорит: Мелани, проси все что хочешь... Деньги, положение, все!
    # Мелани отвечает: Я подумаю, Миссис Бакфетт. Дайте мне время до завтра!
    # Моника: Хорошо, Мелани! Тогда до завтра!
    # До завтра, Миссис Бакфетт!
    img 9084
    m "То есть, ты можешь решить вопрос с Маркусом, чтобы он оставил меня в покое?"
    img 9085
    melanie "Я думаю что даже смогу уговорить его восстановить Ваши документы, Миссис Бакфетт."
    "И вернуть Вашу компанию..."
    img 9086
    mt "ЧТО? НЕУЖЕЛИ ЭТО МОЖЕТ ПРОИЗОЙТИ?!?"
    "Я ДАЖЕ НЕ МОГЛА ОБ ЭТОМ МЕЧТАТЬ!!!"
    img 9087
    m "Мелани, ты... действительно может сделать это? Правда?"
    img 9088
    melanie "Да, Миссис Бакфетт, но не за просто так..."
    img 9089
    m "Мелани, проси все что хочешь... Деньги, положение, ВСЕ!"
    img 9090
    melanie "Я подумаю, Миссис Бакфетт."
    "Дайте мне время до завтра!"
    img 9091
    m "Хорошо, Мелани! Тогда до завтра!"
    melanie "До завтра, Миссис Бакфетт!"
    return

label ep23_dialogues8_2a:
    # Если Моника пытается войти в гримерку, то текст что не надо беспокоить Мелани до завтра, а то вдруг он передумает!
    mt "Я думаю мне не стоит беспокоить Мелани до завтра..."
    "А то вдруг она передумает!"
    return

label ep23_dialogues8_3:
    # С утра монолог Моники о том что появился шанс решить все трудности.
    # Пикчи взять из начала эпизода
    # Что пока рано радоваться, но Мелани доказала что она может решить с мужчинами любой вопрос .
    # И еще неизвестно что Мелани хочет попросить взамен.
    # Но, если честно, Моника готова пойти на все, НА ВСЕ, чтобы прекратить этот бесконечный кошмар!
    # Первым делом Моника выгонит из дома эту сучку Бетти!
    # И эту мелюзгу Барди, который позволяет себе немыслимые вещи!
    # Уволит Фреда, максимально жестко!
    # Затем примется за офис!

    # MonicaBitch
    # Да, кстати, Мелани в новом журнале места явно не найдется. Она слишком много знает про Монику.
    # Желательно ее вообще задвинуть куда-нибудь подальше, в провинцию!
    #

    # Итак, сейчас надо отправляться к Мелани! Чем скорее она займется Маркусом, тем скорее я смогу претворить в жизнь мои планы!
    mt "Итак, у меня появился шанс решить все трудности."
    "Конечно, пока рано радоваться..."
    "Но Мелани доказала что она может решить с мужчинами любой вопрос."
    "И еще неизвестно что Мелани хочет попросить взамен..."
    "Но, если честно, я готова пойти на все, НА ВСЕ!"
    "Чтобы прекратить этот бесконечный кошмар!"
    "..."
    "Первый делом я выгоню из дома эту сучку Бетти!"
    #если носит трусы
    "И выкину все эти гребаные трусы, которые мне приходится носить!!!"

    "Затем выгоню эту мелюзгу Барди, который позволяет себе немыслимые вещи!"
    "И уволю Фреда!!! Максимально жестко!!!"
    "Он нигде и никогда не найдет работы, клянусь!"
    "А лучше посадить его в тюрьму!"
    "А затем я примусь за офис!"

    if monicaBitch == True:
        mt "Да, кстати, Мелани в новом журнале места явно не найдется."
        "Она слишком многое знает про меня..."
        "Желательно ее вообще задвинуть куда-нибудь подальше, в провинцию!"

    mt "Итак, сейчас надо отправляться к Мелани!"
    "Чем скорее она займется Маркусом, тем скорее я смогу претворить в жизнь мои планы!"
    return


label ep23_dialogues8_4:
    # Моника приходит к Мелани (Мелани в гримерке, без разницы день/вечер)
    # Привет, Мелани!
    # Здравствуйте, Миссис Бакфетт!
    # Моника говорит что подумала над возможностью Мелани решить вопрос с Маркусом.
    # И готова дать на это согласие. В конце концов, Мелани сама сказал что хотела бы, чтобы Моника Бакфетт была обязана ей.
    # И Моника считает что это действительно будет стоить благодарности с ее стороны.
    # Мелани улыбаясь смотрит на Монику
    # Да, Миссис Бакфетт. Большое спасибо.
    # Как Вы помните, я обещала подумать над тем что я получу взамен.
    # Моника говорит: Как что? Деньги, должность... Что еще?
    # Видите-ли, Миссис Бакфетт. У меня вполне хорошее состояние и, даже если я чего-то не могу себе позволять, то обязательно найдется мужчина, который это даст.
    # Также у меня есть власть над любым мужчиной.
    # Моника спрашивает: И чего же тебе не хватает?
    # Мелани отвечает: Власти над женщиной...
    # Моника спрашивает что не понимает о чем Мелани говорит.
    # Мелани спрашивает помнит-ли Моника о кастинге, который проводила Моника с ней?
    # Моника спрашивает о каком кастинге? Что не припоминает.
    # Мелани говорит что о том, когда Миссис Бакфетт заставила Мелани раздеться перед ней.
    # Моника говорит что вспомнила. И что, это как-то обидело Мелани?
    # Мелани отвечает что вовсе нет, Вы были мой Босс, а для Босса это обычные вещи.
    img 9092
    m "Привет, Мелани!"
    melanie "Здравствуйте, Миссис Бакфетт."
    img 9093
    m "Мелани, Я подумала над возможностью решить вопрос с Маркусом."
    "И готова дать на это согласие."
    "В конце концов, ты сама просила об этом, потому что хотела бы, чтобы Моника Бакфетт была обязана тебе..."
    m "И это, действительно, будет стоить кое-какой благодарности с моей стороны."
    img 9094
    melanie "..."
    melanie "Да, Миссис Бакфетт. Большое спасибо."
    "Как Вы помните, я обещала подумать над тем, что я получу взамен."
    m "Как что? Деньги, должность...Что еще?"
    img 9095
    melanie "Видите-ли, Миссис Бакфетт."
    "У меня вполне хорошее состояние и, даже если чего-то не могу себе позволить..."
    "То обязательно найдется мужчина, который это даст."
    "Также у меня есть власть над любым мужчиной, которого я захочу..."
    img 9096
    m "И чего же тебе не хватает?"
    img 9097
    melanie "Власти над женщиной..."
    img 9098
    m "Я не понимаю о чем ты говоришь..."
    img 9099
    melanie "Миссис Бакфетт, помните-ли Вы о кастинге, который проводили со мной?"
    img 9100
    m "О каком еще кастинге? Я не припоминаю..."
    img 9101
    melanie "О том, Миссис Бакфетт, когда Вы заставили меня раздеться перед Вами..."
    img 9102
    m "..."
    m "Да, я вспомнила..."
    "И что, Мелани, это как-то обидело тебя?"
    img 9103
    melanie "Вовсе нет, Вы были мой Босс, а для Босса это обычные вещи..."

    if monkeysOffended2 == False:
        # Если Моника не раздевала мартышек
        # Моника: Но ты знаешь, я подумала и прекратила эту практику.
        # Недавно ко мне приходили модели на кастинг и я решила не делать этого.
        # Мелани: да, я понимаю, Миссис Бакфетт, но не было бы ничего страшного, если бы вы это сделали...
        img 9104
        m "Но ты знаешь, я подумала и прекратила эту практику."
        "Недавно ко мне приходили модели на кастинг и решила не раздевать их..."
        img 9105
        melanie "Да, я понимаю, Миссис Бакфетт."
        "Но не было бы ничего страшного, если бы Вы это сделали..."


    # Моника: то есть ты считаешь что так делать нормально и не обижаешься на это?
    # думает: черт, мне не хватало сейчас чтобы Мелани стала вспоминать прошлые обиды!!!
    # мне надо чтобы она сделала это, сходила к Маркусу и он бы оставил в покое меня!
    img 9106
    m "То есть ты считаешь что так делать нормально и не обижаешься на это?"
    img 9107
    mt "Черт! Мне не хватало сейчас чтобы Мелани стала вспоминать прошлые обиды!"
    mt "Мне надо чтобы она сходила к Маркусу и чтобы он оставил в покое меня!"

    # Мелани: Да, Миссис Бакфетт, я считаю что это нормально.
    # Моника: Ты так говоришь, будто сама бы делала то же самое, если бы была Боссом!
    # Мелани: Конечно, Мэм... (улыбается)
    # Моника: Мелани, я не понимаю, к чему ты клонишь?
    # Что ты хочешь от меня?
    img 9108
    melanie "Да, Миссис Бакфетт, я считаю что это нормально."
    m "Ты так говоришь, будто сама бы делала то же самое, если бы была Боссом!"
    img 9109
    melanie "Конечно, Мэм..."
    img 9110
    m "Мелани, я не понимаю, к чему ты клонишь?"
    "Что ты хочешь от меня?"

    # Мелани: Побыть Вашим Боссом...
    # Моника: Но зачем? Что за чушь? Зачем тебе это надо?
    # Мелани: Это мой маленький каприз... Моя мечта... очень давно...
    img 9111
    melanie "Побыть Вашим Боссом..."
    img 9112
    m "Но зачем? Что за чушь? Зачем тебе это надо?"
    img 9113
    melanie "Это мой маленький каприз... Моя мечта... очень давно..."

    # Моника: Я не понимаю, Мелани. Ты хочешь быть главой журнала? Это можно обсудить.
    # Но ты не можешь быть главнее меня!
    img 9114
    m "Я не понимаю, Мелани. Ты хочешь быть главой журнала?"
    "Это можно обсудить."
    img 9115
    "Но ты не можешь быть главнее меня!"

    # Мелани: Нет, Миссис Бакфетт! Я не хочу быть главнее Вас! Это слишком опасно...
    # Моника: Я рада, что ты это понимаешь, дорогуша...
    # Мелани: Я просто хочу немного справедливости. И сейчас это единственная возможность добиться ее.
    # Моника: Какой справедливости? Что ты хочешь от меня, я никак не могу понять!
    # Мелани: Я хочу чтобы Вы прошли кастинг, Миссис Бакфетт. Такой же как и я когда-то...
    # Моника: Кастинг? Но где? И перед кем?
    # Мелани: В Вашем кабинете, Миссис Бакфетт. Днем, когда там нет Биффа.
    # Моника: То есть, Мелани... Я правильно понимаю?
    # Ты хочешь усесться на мой стул и командовать мной?
    # Заставить меня раздеться перед тобой?
    # Я ПРАВИЛЬНО ПОНИМАЮ??!? (Моника злится)
    img 9116
    melanie "Нет, Миссис Бакфетт! Я не хочу быть главнее Вас!"
    "Это слишком опасно..."
    img 9117
    m "Я рада, что ты это понимаешь, дорогуша..."
    img 9118
    melanie "Я просто хочу немного справедливости."
    "И сейчас это единственная возможность добиться ее."
    m "Какой справедливости? Что ты хочешь от меня, я никак не могу понять!"
    img 9119
    melanie "Я хочу чтобы Вы прошли кастинг, Миссис Бакфетт."
    "Такой же как и я когда-то..."
    img 9120
    m "Кастинг? Но где? И перед кем?"
    img 9121
    melanie "В вашем кабинете, Миссис Бакфетт. Днем, когда там нет Биффа."
    img 9122
    m "То есть, Мелани... Я правильно понимаю?"
    "Ты хочешь усесться на мой стул и командовать мной?"
    "Заставить меня раздеться перед тобой?"
    img 9123
    "Я ПРАВИЛЬНО ПОНИМАЮ?!?!"

    # Мелани: Нет, Миссис Бакфетт, не совсем так.
    # Не я буду командовать Вами, это будет делать другой человек...
    # Я буду только смотреть...
    # Моника: Какой другой человек? Мной все пытается покомандовать Биф и он поплатится за это рано или поздно!
    # Мелани: Я знаю это. Я знаю Вас хорошо, Миссис Бакфетт.
    # Человек, который осмелится командовать Вами, в будущем очень пожалеет об этом. Вы отомстите ему и отомстите очень сильно...
    # Моника щурится: Ты правильно понимаешь, Мелани...
    # Мелани: Поэтому я и не хочу рисковать собой. Я буду просто смотреть со стороны.
    # Вы же можете потом в будущем сделать с этим человеком все что захотите.
    # Моника: Мне, как владелице этого журнала, как-то странно слышать такие предложения от какой-то модели...
    # Мелани: Это не предложение, Миссис Бакфетт. Это условие...
    # Условие возвращения этого журнала Вам, а также документов и денег...
    # Когда я шла к Мистеру Дику, я не ожидала что у Вас на самом деле все так плохо.
    img 9124
    melanie "Нет, Миссис Бакфетт, не совсем так."
    "Не я буду командовать Вами, это будет делать другой человек..."
    "Я буду только смотреть..."
    img 9125
    m "Какой другой человек? Мной все пытается покомандовать Биф."
    "И он поплатится за это рано или поздно!"
    img 9126
    melanie "Я знаю это. Я знаю Вас хорошо, Миссис Бакфетт."
    "Человек, который осмелится командовать Вами, в будущем очень пожалеет об этом."
    "Вы отомстите ему... И отомстите очень сильно..."
    img 9127
    if monicaBitch == True:
        m "Ты правильно понимаешь, Мелани..."
    else:
        m "..."
    img 9128
    melanie "Поэтому я и не хочу рисковать собой. Я буду просто смотреть со стороны."
    "Вы же можете потом, в будущем, сделать с этим человеком все что захотите."
    img 9129
    m "..."
    img 9130
    melanie "..."
    img 9131
    m "Мне, как владелице этого журнала, как-то странно слышать такие предложения от какой-то модели..."
    img 9132
    melanie "Это не предложение, Миссис Бакфетт. Это условие..."
    "Условие возвращения этого журнала Вам, а также документов и денег..."
    img 9133
    melanie "Когда я шла к Мистеру Дику, я не ожидала что у Вас на самом деле все так плохо."

    # Скажите, Миссис Бакфетт, где Вы ночуете?
    # Моника отвечает: Это не твое дело, Мелани...
    # Мелани: Если Ваша жизнь - это не мое дело, тогда я могу быть свободна, Миссис Бакфетт?
    # Моника: Стой! Итак, этот кастинг...
    # Что ты хочешь чтобы я там делала?
    # Мелани: Не я хочу, Миссис Бакфетт! Вам будет говорить другой человек!
    # Который потом будет отвечать за все это, перед Вами!
    # Моника: Может быт обойдемся без другого человека, Мелани?
    # Мелани: Это исключено, Миссис Бакфетт! Вы, в последствии, сотрете меня в порошок, а я этого не хочу.
    # Моника: Я так полагаю что будет за что?
    # Мелани улыбается: Скорее всего да...
    # Моника: Как зовут того человека, который будет приказывать мне?
    # Мелани улыбается: Его будут звать Миссис Бакфетт...
    # Моника: ЧТО???
    img 9134
    melanie "Скажите, Миссис Бакфетт, где Вы ночуете?"
    img 9135
    m "Это не твое дело, Мелани..."
    img 9136
    melanie "Если Ваша жизнь - это не мое дело, тогда я могу быть свободна, Миссис Бакфетт?"
    img 9137
    with fade
    w
    img 9138
    m "Стой!"
    img 9139
    "Итак, этот кастинг..."
    "Что ты хочешь чтобы я там делала?"
    melanie "Не я хочу, Миссис Бакфетт! Вам будет говорить другой человек!"
    "Который потом будет отвечать за все это, перед Вами!"
    img 9140
    m "Может быть обойдемся без другого человека, Мелани?"
    img 9141
    melanie "Это исключено, Миссис Бакфетт!"
    "Вы, в последствии, сотрете меня в порошок, а я этого не хочу."
    img 9142
    m "Я так полагаю, что будет за что?"
    img 9143
    melanie "Скорее всего да..."
    img 9144
    m "Как зовут того человека, который будет приказывать мне?"
    img 9143
    melanie "Его будут звать Моника Бакфетт..."
    img 9145
    m "ЧТО???"

    # Мелани: Это просто игра. Тот человек будет называться Вами, а Вы придете как модель, которую должны взять в журнал.
    # Этот человек будет говорить Вам что делать. И, если Вы выполните все что от Вас требуется, то, скорее всего, Вы будете приняты.
    # Моника: А зачем мне это надо? Принимать себя же в свой же журнал???
    # Мелани: Потому что если Вы не будете приняты, то наша сделка не состоится...
    # Моника: Я понимаю, Мелани. Ты хочешь унизить меня. Таким образом пощекотать свое ЭГО...
    # Мелани: Нет, Миссис Бакфетт, что Вы? Наоборот, я буду просить того человека быть к Вам поснисходительнее.
    # Моника: То есть ты хочешь защитить меня от унижения? Но зачем тебе тогда вообще этот кастинг?
    # Мелани: Я хочу увидеть что Вы действительно хотите этого... Ведь мне, скорее всего, придется переспать с Маркусом, чтобы добиться для Вас результатов...
    # Мелани: А моя честь для меня много значит, Миссис Бакфетт.
    img 9146
    melanie "Это просто игра."
    "Тот человек будет называться Вами, а Вы придете как модель, которую должны взять в журнал."
    "Этот человек будет говорить Вам что делать."
    "И, если Вы выполните все что от Вас требуется, то, скорее всего, Вы будете приняты."
    img 9147
    m "А зачем мне это надо? Принимать себя же в свой же журнал???"
    img 9148
    melanie "Потому что если Вы не будете приняты, то наша сделака не состоится..."
    img 9149
    m "Я понимаю, Мелани. Ты хочешь унизить меня. Таким образом пощекотать свое ЭГО..."
    img 9150
    melanie "Нет, Миссис Бакфетт, что Вы?"
    "Наоборот, я буду просить того человека быть к Вам поснисходительнее."
    img 9151
    m "То есть ты хочешь защитить меня от унижения?"
    "Но зачем тебе тогда вообще этот кастинг?"
    img 9152
    melanie "Я хочу увидеть что Вы действительно хотите этого..."
    "Ведь мне, скорее всего, придется переспать с Маркусом, чтобы добиться для Вас результатов..."
    "А моя честь для меня много значит, Миссис Бакфетт."

    if monicaBitch == True or melanieOffended2 == True or melanieOffended1 == True:
        if monicaBitch == True:
            $ notif_monica()
        else:
            $ notif(_("У Моники плохие отношения с Мелани"))

        # Если Моника сучка или была плохой с Мелани
        # Моника: О, Мелани! Кто бы говорил о чести!!!
        # Мелани подозрительно смотрит
        # Моника подозрительно смотрит
        img 9153
        m "О, Мелани! Кто бы говорил о чести!!!"
        img 9154
        melanie "..."
        img 9155
        m "..."

    # Моника: Итак, Мелани, ты хочешь чтобы я разделась, так?
    # Но ведь не будет никаких фото и видео, правда?
    # Мелани: Это не будет никуда записано, Миссис Бакфетт.
    # Я не думаю что надо будет просто раздеться.
    # Есть условие: ЧТО-БЫ ВАС НИ ПОПРОСИЛИ СДЕЛАТЬ, ВЫ ЭТО СДЕЛАЕТЕ.
    # И ВЫ БУДЕТЕ СТАРАТЬСЯ ЭТО СДЕЛАТЬ!
    # Это кастинг. И Вы должны показать лучшее!
    # Моника: Я не собираюсь заниматься сексом с мужчиной у тебя на глазах!!!
    # Мелани: Это будет девушка...
    # Моника: Девушка?..
    # Я ее знаю?
    # Мелани: Я сомневаюсь что Вы ее помните...
    # Итак, Миссис Бакфетт, что Вы решили?
    img 9156
    m "Итак, Мелани, ты хочешь чтобы я разделась, так?"
    "Не ведь не будет никаких фото и видео, правда?"
    img 9157
    melanie "Это не будет никуда записано, Миссис Бакфетт."
    "И я не думаю что надо будет просто раздеться."
    img 9158
    melanie "Есть условие: ЧТО-БЫ ВАС НИ ПОПРОСИЛИ СДЕЛАТЬ, ВЫ ЭТО СДЕЛАЕТЕ."
    "И ВЫ БУДЕТЕ СТАРАТЬСЯ ЭТО СДЕЛАТЬ!"
    melanie "Это кастинг. И Вы должна показать лучшее!"
    img 9159
    m "Я не собираюсь заниматься сексом с мужчиной у тебя на глазах!!!"
    img 9160
    melanie "Это будет девушка..."
    img 9161
    m "Девушка?.."
    "Я ее знаю?"
    img 9162
    melanie "Я сомневаюсь, что Вы ее помните..."
    "Итак, Миссис Бакфетт, что Вы решили?"

    menu:
        "Согласиться на кастинг.":
            # Согласиться на кастинг.
            # Моника: Мелани, если я соглашусь, то ты обещаешь что решишь мою проблему с Маркусом?
            # Мелани: Я обещаю, Мэм...
            # Моника: И ты понимаешь, что я уничтожу того человека, который будет приказывать мне?!
            # Мелани: Можете делать с ним все что захотите, Миссис Бакфетт...
            # А я останусь тем человеком, который спас Вас...
            # Моника: И человеком, который пощекотал свое Эго...
            # Мелани: Это невинная шалость, Миссис Бакфетт. К тому же, как я говорила, приказывать буду не Я...
            # Моника: Я понимаю, ты умная девушка. Ты отвела будущую месть от себя...
            # Мелани улыбается
            # Моника: Я согласна, Мелани. Итак, когда будет этот твой кастинг?
            # Мелани: Завтра днем, Миссис Бакфетт. Приходите днем...
            img 9163
            m "Мелани, если я соглашусь, то ты обещаешь что решишь мою проблему с Маркусом?"
            img 9162
            melanie "Я обещаю, Мэм..."
            img 9164
            m "И ты понимаешь, что я уничтожу того человека, который будет приказывать мне?!"
            melanie "Можете делать с ним все что захотите, Миссис Бакфетт..."
            img 9165
            "А я останусь тем человеком, который спас Вас..."
            img 9164
            m "И человеком, который пощекотал свое Эго..."
            img 9165
            melanie "Это невинная шалость, Миссис Бакфетт."
            "К тому же, как я говорила, приказывать буду не Я..."
            img 9166
            m "Я понимаю, ты умная девушка. Ты отвела будущую месть от себя..."
            img 9167
            melanie "..."
            img 9168
            m "Я согласна, Мелани. Итак, когда будет этот твой кастинг?"
            melanie "Завтра днем, Миссис Бакфетт. Приходите днем..."
            return True

        "Отказаться."
            # Отказаться.
            # Я подумаю, Мелани. Я пока не готова для этого...
            # Мелани: Подумайте, Миссис Бакфетт.
            # Когда решите, сообщите мне...
            img 9168
            m "Я подумаю, Мелани. Я пока не готова для этого..."
            melanie "Подумайте, Миссис Бакфетт."
            "Когда решите, сообщите мне..."
            return False

        "Попросить Мелани помочь без кастинга. (хорошие отношения с Мелани)": if melanieOffended2 == False and melanieOffended1 == False:
            # Если Моника хорошая и отношения с Мелани хорошие
            # Моника: Мелани, я понимаю тебя...
            # Но поверь, для меня та жизнь, которой я живу - она и так является самым большим унижением, которое я когда-либо испытывала!
            # Возможно ты помнишь о том кастинге, когда я заставила тебя раздеться.
            # Но у уже совсем другая!
            # Я прошу прощения у тебя, Мелани!
            # И прошу тебя о помощи, пожалуйста!
            # Помоги мне! Помоги, как девушке, попавшей в беду!
            # И не используй мою слабость для собственных утех!
            # Я знаю ты добрая внутри! Ты послушаешь меня!
            # Мелани: Миссис Бакфетт, я не ожидала что Вы так можете говорить...
            # Хорошо, мы забудем про кастиги...
            # Я завтра же пойду к Маркусу. Ждите от меня новостей!
            # Хорошо, Мелани! Спасибо тебе!
            img 9169
            m "Мелани, я понимаю тебя..."
            "Но поверь, для меня та жизнь, которой я живу -"
            "- она и так является самым большим унижением, которое я когда-либо испытывала!"
            "Возможно ты помншиь о том кастинге, когда я заставила тебя раздеться."
            "Но я уже совсем другая!"
            img 9170
            "Я прошу прощения у тебя, Мелани!"
            "И прошу тебя о помощи, Пожалуйста!"
            "Помоги мне! Помоги, как девушке, попавшей в беду!"
            "И не используй мою слабость для собственных утех!"
            img 9171
            "Я знаю, ты добрая внутри! Ты послушаешь меня!"
            img 9172
            melanie "Миссис Бакфетт, я не ожидала что Вы так можете говорить..."
            "..."
            "Хорошо, мы забудем про кастинги..."
            "Я завтра же пойду к Маркусу. Ждите от меня новостей!"
            m "Хорошо, Мелани! Спасибо тебе!"
            return True

        "Попросить Мелани помочь без кастинга. (плохие отношения с Мелани)": if melanieOffended2 == True or melanieOffended1 == True:
            pass
    return




























label ep23_dialogues8:
    return
