# Офис. Когда Моника приходит в очередной раз на работу в офис (днем)
# Моника начинает работать и автоматически включается сцена в гримерке, после нее управление переходит на Мелани
label ep29_dialogues3_melanie_monica_victoria_1:
    # Мелани сидит перед зеркалом в гримерке, поправляет макияж кистью для мейкапа
    melanie_t "Я выгляжу какой-то уставшей..."
    melanie_t "Мне нужно взять несколько выходных и отдохнуть."
    melanie_t "Возможно, стоит полететь на острова... Океан, пальмы, никаких папарацци..."
    melanie_t "Нужно будет подойти к Бифу, попросить у него небольшй отпуск."
    melanie_t "Он не сможет мне отказать."
    melanie_t "Еще ни один мужчина не отказывал мне. И Биф не станет первым..."
    # в гримерку заходит серкретарша Бифа
    img 15386
    secretary "Мисс Мелани..."
    # Мелани поворачивается к ней
    img 15387
    melanie "Да?"
    img 15388
    secretary "Сейчас звонила Мисс Виктория."
    # Мелани вопросительно смотрит на нее
    img 13932
    melanie "И что Мисс Виктория сказала?"
    img 13930
    secretary "Она просила передать Вам, что она сегодня ждет Вас у себя."
    secretary "Она сказала, что это очень срочно."
    # Мелани смотрит на секретаря вопросительно
    img 15389
    melanie "Говорила ли Мисс Виктория еще что-нибудь?"
    img 15390
    secretary "Нет, Мисс Мелани. Она только сказала, что это очень срочно."
    img 15391
    melanie "..."
    img 13929
    melanie "Спасибо. Я проведаю Мисс Викторию сегодня."
    melanie "Вы можете идти."
    # секретарша уходит, Мелани поворачивается снова к зеркалу и задумчиво смотрит на свое отражение
    img 13935
    melanie_t "Что этой мерзкой Мисс Виктории снова нужно от меня?"
    melanie_t "Почему Я должна ехать к ней по первому же ее звонку?"
    melanie_t "..."
    # Мелани снова берет в руки кисть для мейка и проводит ею по скуле
    melanie_t "Эта мелкая стерва возомнила себя самой умной и хитрой..."
    melanie_t "Нужно будет придумать, как поставить ее на место."
    melanie_t "Кто она вообще такая, чтобы вести себя со МНОЙ подобным образом?"
    melanie_t "Нужно во что бы то ни стало лишить эту сучку возможности шантажировать меня."
    melanie_t "Если я узнаю, кто снабжает ее моими фотографиями, шпионя за мной..."
    melanie_t "То у меня будет хоть какая-то зацепка. Я смогу договориться с этим папарацци."
    melanie_t "Уверена, что все дело в деньгах."
    melanie_t "..."
    # положила кисть на столик, поправляет прическу
    melanie_t "Конечно, проще всего было бы соблазнить Дика."
    melanie_t "В моих силах сделать так, чтобы он вышвырнул эту сучку на улицу..."
    melanie_t "Где он ее и подобрал, я так полагаю."
    melanie_t "Но ведь она сидит и охраняет Дика, как цепной пес."
    melanie_t "Хм... Интересно, Дик вообще ходит куда-нибудь без нее?"
    melanie_t "Нужно будет узнать об этом."
    # Мелани смотрит на себя в зеркало
    melanie_t "А пока мне придется поехать к этой мелкой сучке..."
    melanie_t "И узнать, что взбрело ей в голову на этот раз."
    melanie_t "Сейчас мне нужно ехать в офис Дика."
    # встает со стула
    $ log1 = _("Пойти в офис Дика и узнать, что нужно Виктории")
    return

# управление перешло на Мелани
# появляется иконка Мелани справа
# в заданиях появляется "Пойти в офис Дика и узнать, что нужно Виктории"
# денег у Мелани 500 000 баксов

# мысли Мелани в гримерке
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1a:
    # смотрит на свой портрет
    melanie_t "Это одна из моих любимых работ."
    return
label ep29_dialogues3_melanie_monica_victoria_1b:
    # смотрит на другие свои фотографии
    melanie_t "Любая моя фотография - произведение искусства."
    return
label ep29_dialogues3_melanie_monica_victoria_1c:
    # смотрит на зеркала
    melanie_t "Люблю, когда меня окружает много зеркал. Мне нравится смотреть на себя."
    return
label ep29_dialogues3_melanie_monica_victoria_1d:
    # смотрит на косметику на столе
    melanie_t "Косметики много не бывает. Я готова покупать ее каждый день."
    return
label ep29_dialogues3_melanie_monica_victoria_1e:
    # смотрит на чемоданы
    melanie_t "Здесь можно найти красивый наряд для любого события. Дорогие наряды отлично подчеркивают мою красоту."
    return
label ep29_dialogues3_melanie_monica_victoria_1f:
    # клик на Мелани
    melanie_t "Я не могу позволить, чтобы мною командовала какая-то девочка. И где только Дик ее нашел?"
    return

# мысли Мелани в фотостудии
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1g:
    # смотрит на съемочную площадку
    melanie_t "Перед объективом камеры я чувствую себя превосходно. Люблю быть в центре внимания."
    return
label ep29_dialogues3_melanie_monica_victoria_1h:
    # смотрит на оборудование для фотосессии
    melanie_t "В этой студии самое лучшее оборудование. Мне нравится работать здесь."
    return
label ep29_dialogues3_melanie_monica_victoria_1i:
    # смотрит на Алекса (глазик)
    melanie_t "Алекс. Неплохой фотограф. А я его любимая модель."
    return
label ep29_dialogues3_melanie_monica_victoria_1j:
    # смотрит на Алекса (разговор)
    melanie_t "Он снова начнет уговаривать меня сняться для его личной коллекции... Мне пока не до этого."
    return

# мысли Мелани на ресепшене перед кабинетом Бифа
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1k:
    # смотрит на любой предмет в приемной Бифа
    melanie_t "Всегда не любила это место. Никогда не знаешь, что ожидать, когда входишь в дверь босса. Будь то Миссис Бакфетт или Биф..."
    return
label ep29_dialogues3_melanie_monica_victoria_1l:
    # смотрит на секретаря Бифа (глазик)
    melanie_t "Секретарю Бифа не помешало бы сходить к косметологу. Нельзя же себя так запускать..."
    return
label ep29_dialogues3_melanie_monica_victoria_1m:
    # смотрит на секретаря Бифа (разговор, когда Бифа нет на месте)
    melanie "Биф у себя?"
    secretary "К сожалению, Мисс Мелани, он будет только вечером. Что-нибудь ему передать?"
    melanie "Нет, спасибо. Я позже сама с ним поговорю."
    melanie_t "Бифа сложно застать на рабочем месте. Такое ощущение, что он сюда приходит только выпить виски по вечерам..."
    return
label ep29_dialogues3_melanie_monica_victoria_1n:
    # смотрит на секретаря Бифа (разговор, когда Биф на работе, вечером после посещения офиса Дика)
    melanie "Биф у себя?"
    secretary "Да, Мисс Мелани. Проходите."
    melanie "Спасибо."
    return

# мысли Мелани в кабинете Бифа
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1o:
    # смотрит на Бифа (глазик)
    melanie_t "Если Биф выпивает полбутылки виски, то становится намного сговорчивее."
    return
label ep29_dialogues3_melanie_monica_victoria_1p:
    # смотрит на любой предмет в кабинете Бифа
    melanie_t "Миссис Бакфетт, должно быть, очень хочет вернуться в свой кабинет."
    melanie_t "Хотя, я тоже была бы не прочь оказаться в этом кресле..."
    return

# мысли Мелани в холле у лифта
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1q:
    # если не была еще в офисе Дика, при любом клике, кроме выхода
    melanie_t "Сейчас мне нужно ехать в офис Дика. Что этой ненормальной Виктории снова от меня нужно?"
    return

# мысли Мелани в отделе отчетов
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1r:
    # смотрит на сотрудников отдела отчетов
    melanie_t "Никогда не понимала, как люди целыми днями могут работать с документами? Это так скучно."
    melanie_t "И зачем здесь так много сотрудников? Неужели этот отдел настолько важен для журнала?"
    return
label ep29_dialogues3_melanie_monica_victoria_1s:
    # смотрит на подхалима (глазик)
    melanie_t "У него такой важный вид, как-будто он здесь всеми руководит."
    return
label ep29_dialogues3_melanie_monica_victoria_1t:
    # смотрит на айтишника (глазик)
    melanie_t "Очередной мой поклонник, который ни слова при мне не может сказать..."
    melanie_t "Мужчины часто в моем присутствии теряют дар речи..."
    return

# мысли Мелани в кабинете Моники
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1u:
    # смотрит на Юлию (глазик)
    melanie_t "Это кто? Наверное, помощница Миссис Бакфетт. Я не хотела бы оказаться на ее месте."
    return
label ep29_dialogues3_melanie_monica_victoria_1v:
    # смотрит на Юлию (разговор)
    melanie_t "Мне с ней не о чем разговаривать."
    return
label ep29_dialogues3_melanie_monica_victoria_1w:
    # смотрит на Монику (глазик)
    melanie_t "Миссис Бакфетт. Она неплохо тут устроилась."
    melanie_t "У нее есть много подчиненных и помощница. Можно целыми днями командовать людьми, как она любит."
    return
label ep29_dialogues3_melanie_monica_victoria_1x:
    # смотрит на предмет в кабинете Моники
    melanie_t "Вполне приличный рабочий кабинет. Конечно, не сравнить с бывшим кабинетом Миссис Бакфетт."
    melanie_t "Она, наверное, скучает по кастингам..."
    return

# мысли Мелани на ресепшене в офисе Дика на первом этаже
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1y:
    # смотрит на секретаря на ресепшене (глазик)
    melanie_t "Она неплохо выглядит... В отличие от секретарши Бифа."
    return
label ep29_dialogues3_melanie_monica_victoria_1z:
    # смотрит на секретаря на ресепшене (разговор)
    reception_secretary "Здравствуйте, Мисс Мелани!"
    reception_secretary "Я так рада Вас видеть!"
    reception_secretary "Вы, как всегда, великолепно выглядите!"
    melanie "Спасибо."
    reception_secretary "Вы пришли к Мистеру Дику? Он как раз у себя."
    reception_secretary "Уверена, что Мистер Дик будет рад Вашему визиту! Я могу проводить Вас, Мисс Мелани."
    melanie "Это совсем необязательно. Я помню, где находится кабинет Мистера Дика."
    melanie_t "Не хватало еще, чтобы мелкая сучка сказала что-нибудь унизительное мне при этой женщине."
    return

# мысли Мелани в приемной перед офисом Дика, второй этаж
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1aa:
    # смотрит на Викторию (глазик)
    melanie_t "Эта мелкая стервозная сучка начинает раздражать меня..."
    melanie_t "Нужно найти способ поставить ее на место."
    return
label ep29_dialogues3_melanie_monica_victoria_1bb:
    # смотрит на дверь в кабинет Дика
    melanie_t "Может проигнорировать Викторию и пойти напрямую к Дику?"
    melanie_t "Дик быстро разберется с ней. Мне стоит только попросить его об этом."
    melanie_t "С другой стороны... Неужели Я не смогу справиться с ней?"
    return

# мысли Мелани в ее квартире
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1cc:
    # смотрит на сумочку Виктории
    melanie_t "Эта мелкая сучка снова раздобыла какую-то компрометирующую информацию."
    return
label ep29_dialogues3_melanie_monica_victoria_1dd:
    # смотрит на свои портреты
    melanie_t "Все мои портреты - произведения искусства."
    melanie_t "Мне нравится окружать себя прекрасным."
    return
label ep29_dialogues3_melanie_monica_victoria_1ee:
    # смотрит на столик с бокалами
    melanie_t "Это вино многолетней выдержки - подарок одного коллекционера."
    melanie_t "Вряд ли Виктория сможет понять разницу между ним и дешевкой из магазина."
    return
label ep29_dialogues3_melanie_monica_victoria_1ff:
    # смотрит на мебель
    melanie_t "Интерьер моей квартиры разрабатывал один из лучших дизайнеров города."
    melanie_t "В целом, мне нравится. Просто и со вкусом."
    return

# мысли Мелани, когда вышла из здания, где расположен офис Моники
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1gg:
    # перед посещением офиса Дика
    melanie_t "Мне нужно ехать в офис Дика. Виктория передала, что это срочно."
    melanie_t "Эта девочка Дика начинает мне надоедать..."
    return
label ep29_dialogues3_melanie_monica_victoria_1hh:
    # перед тем, как поехать к себе домой
    melanie_t "Скоро ко мне придет Миссис Бакфетт и эта мелкая дрянь."
    melanie_t "Надеюсь, мне не придется долго терпеть ее присутствие в моей квартире."
    return

# мысли Мелани перед зданием, где расположен офис Моники
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1ii:
    # после посещения офиса Дика
    melanie_t "Необходимо убедить Миссис Бакфетт в необходимости ее присутствия на встрече с Викторией."
    melanie_t "Виктория ясно дала понять, что она обязательно должна быть сегодня вечером у меня."
    return

# мысли Мелани перед зданием, где расположен офис Дика
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1jj:
    # перед посещением офиса Дика
    melanie_t "В прошлый раз Мистер Дик был крайне рад меня видеть."
    melanie_t "И достаточно пренебрежительно обошелся с Викторией в моем присутствии."
    melanie_t "После такого Виктория и близко меня к нему не подпустит."
    return

# мысли Мелани, когда вышла из здания, где расположен офис Дика
label ep29_dialogues3_melanie_monica_victoria_1kk:
    # после посещения офиса Дика
    melanie_t "Мелкая дрянь... Кем она себя возомнила?"
    melanie_t "Мне нужно вернуться на работу и поговорить с Миссис Бакфетт."
    return

# мысли Мелани перед домом, где расположена ее квартира
label ep29_dialogues3_melanie_monica_victoria_1ll:
    melanie_t "Виктория сегодня обещала устроить девичник."
    melanie_t "Что ж... Посмотрим, чем это закончится..."
    return

# клик на Мелани возле здания, где офис Моники (глазик)
label ep29_dialogues3_melanie_monica_victoria_1mm:
    melanie_t "Любая девушка в мире может только мечтать о такой работе, как у меня."
    melanie_t "Но они - не я. Недостаточно быть просто красивой."
    return

# клик на Мелани возле здания, где офис Дика (глазик)
label ep29_dialogues3_melanie_monica_victoria_1nn:
    melanie_t "Я сегодня выгляжу сногсшибательно. Впрочем, как всегда..."
    melanie_t "Виктория ненавидит меня за это."
    return

# клик на Мелани возле ее дома (глазик)
label ep29_dialogues3_melanie_monica_victoria_1oo:
    melanie_t "Люблю свою квартиру. Там я могу скрыться от посторонних глаз и объективов камер."
    return

# если Мелани хочет зайти снова к Виктории после разговора с ней
label ep29_dialogues3_melanie_monica_victoria_1pp:
    melanie_t "Виктория ясно дала понять, что продолжит разговор вечером."
    melanie_t "Сейчас нет смысла возвращаться в офис Дика."
    return

# если Мелани хочет зайти снова к Монике после разговора с ней
label ep29_dialogues3_melanie_monica_victoria_1rr:
    melanie_t "Думаю, Миссис Бакфетт поняла, что должна прийти ко мне вечером."
    melanie_t "Уверена, что она не проигнорирует эту встречу."
    return

# если Мелани хочет зайти снова к Бифу после разговора с ним
label ep29_dialogues3_melanie_monica_victoria_1ss:
    melanie_t "Я больше не хочу с ним разговаривать."
    return

# Мелани поднимается на лифте в приемную Дика
label ep29_dialogues3_melanie_monica_victoria_2:
    # Виктория сидит за своим рабочим столом с самодовольным видом
    melanie "Мисс Виктория, мне передали, что вы просили меня приехать к вам..."
    # Виктория смотрит на нее с недоброй ухмылкой
    victoria "Подружка, мне кажется, что ты не рада меня видеть..."
    victoria "Хорошие подружки так себя не ведут."
    victoria "Давай сделаем вид, что ты ничего мне сейчас не говорила. И ты подойдешь снова."
    # Мелани смотрит на нее непроницаемым взглядом
    melanie "..."
    menu:
        "Сделать, как требует Виктория":
            pass
    melanie_t "Мне было бы приятно видеть ее лицо не здесь..."
    melanie_t "Например, на обложке журнала Фермы 218 она смотрелась бы неплохо."
    # разворачивается, отходит от стола, потом подходит снова
    # Виктория внимательно наблюдает за ней
    # Мелани с каменным лицом
    melanie "Виктория, здравствуй. Я рада нашей встрече."
    victoria "Уже лучше."
    victoria "Хорошие подружки целуются при встрече. Потому что действительно рады встрече."
    victoria "..."
    victoria "Ты же хорошая подружка?"
    # Мелани молча смотрит на нее
    melanie "..."
    melanie_t "Эта сучка откровенно издевается надо мнойю."
    melanie_t "Сейчас я поиграю по ее правилам..."
    melanie_t "Она ведь не просто так позвала меня."
    melanie_t "Нужно узнать, что она хочет."
    melanie_t "Но я не оставлю подобное поведение безнаказанным..."
    menu:
        "Подойти к Виктории и поцеловать ее":
            pass
    # Мелани подходит и целует Виктория в щеку, та самодовольно улыбается
    victoria "Подружка соскучилась по мне?"
    # Мелани отходит от Викториии снова встает перед ее столом, сверлит ее взглядом
    melanie "..."
    victoria "Я не слышу ответа..."
    victoria "Возможно, я ошибаюсь и ты не моя подружка?"
    victoria "Ты не соскучилась по мне?"
    melanie "Конечно, соскучилась... Подружка."
    # Виктория довольно хихикает
    victoria "Раз ты так скучаешь по мне, подружка..."
    victoria "То, так уж и быть, я найду время, чтобы навестить тебя сегодня."
    victoria "Я приду к тебе вечером в гости."
    victoria "И еще я хочу, чтобы вторая наша подружка тоже пришла."
    victoria "Уверена, она тоже соскучилась по мне. Как ты думаешь?"
    # Мелани удивленно приподнимает бровь
    melanie "Ко мне в гости?"
    melanie "..."
    victoria "Да. Я тут подумала, что ни разу не была у тебя в гостях."
    victoria "А подружки ходят друг другу в гости и устраивают девичники."
    victoria "Сегодня вечером я хочу устроить девичник с моими хорошими подружками."
    victoria "Ты ведь рада, что я приду к тебе в гости?"
    victoria "Ты же хорошая подружка?"
    # Мелани молчит
    melanie "..."
    menu:
        "Согласиться на предложение Виктории":
            melanie_t "Она явно что-то задумала..."
            melanie_t "Узнать это можно только одним способом - согласиться, чтобы она пришла ко мне."
            melanie_t "Эта мелкая сучка не напугает меня, как бы она не старалась."
            melanie_t "Она ничего мне не сделает. Она и может только, что угрожать и все. На большее она не способна."
            pass
        "Отказаться":
            melanie "Cегодня вечером я буду занята."
            melanie "Меня не будет дома."
            # Виктория хмурится и пристально смотрит на Мелани
            victoria "Подружка хочет сказать, что у нее нет времени на меня?"
            melanie "..."
            victoria "Хорошая подружка отменила бы все свои планы."
            victoria "Иначе она может поссориться со мной."
            victoria "И тогда о ее маленькой тайне узнает один наш общий друг..."
            melanie "..."
            victoria "Подружка же не хочет со мной ссориться?"
            melanie_t "Чертова интриганка."
            pass
    # Мелани равнодушно
    melanie "Я хорошая подружка и буду ждать тебя сегодня в гости."
    # Виктория довольно улыбается
    victoria "Я очень расстроюсь, если вторая наша подружка не придет сегодня."
    victoria "Я тогда подумаю, что она не соскучилась по мне."
    victoria "Как ты думаешь, ведь вторая подружка не захочет меня расстраивать?"
    # Мелани с покерфейсом
    melanie "..."
    melanie "Я уверена, что она с радостью с тобой встретится."
    # Виктория хихикает
    victoria "Не могу дождаться нашей встречи!"
    # Мелани бросает взгляд на дверь Дика, Виктория это видит и хмурит брови
    victoria "Ты можешь идти, подружка."
    victoria "Я понимаю, что ты с радостью повторила бы нашу встречу в этом кабинете..."
    victoria "Поэтому ты туда так смотришь. Но не расстраивайся. Мы увидимся сегодня вечером."
    # молча смотрят друг на друга
    victoria "До встречи, подружка."
    victoria "Я принесу тебе подарок сегодня."
    victoria "И не только тебе..."
    melanie "..."
    # Мелани бросает на нее непроницаемый взгляд, разворачивается и уходит
    # в заданиях появляется "Вернуться в студию и поговорить с Миссис Бакфетт"
    $ log1 = _("Вернуться в студию и поговорить с Миссис Бакфетт")
    return

# мысли Мелани в холле у лифта
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_2a:
    # после разговора с Викторией в офисе Дика
    melanie_t "Будет не так просто заставить Миссис Бакфетт придти на встречу с Викторией..."
    melanie_t "Нужно сказать это так, чтобы она не смогла отказаться."
    return

# Мелани заходит в отдел отчетов
label ep29_dialogues3_melanie_monica_victoria_3:
    # подхалим подрывается с места, системный администратор подскакивает, все остальные смотрят на Мелани с изумлением
    # подхалим подбегает к Мелани
    w5 "Мисс Мелани! Вы великолепно выглядите!"
    w5 "Я так рад Вас видеть в моем... нашем отделе!"
    w5 "Желаете, я проведу Вам небольшую экскурсию?"
    w5 "Расскажу немного о нашей работе..."
    w5 "И угощу Вас чашечкой великолепного кофе!"
    # системный администратор смотрит на нее, открыв рот взглядом, как у Эрика
    w2 "!!!"
    # Мелани смотрит на него, потом на подхалима и, игнорируя его предложения, спрашивает
    melanie "Миссис Бакфетт у себя?"
    w5 "Да, Мисс Мелани. Она у себя в кабинете. Я провожу Вас!"
    # подхалим ведет ее через офис и открывает ей дверь в кабинет Моники, та заходит
    # Моника сидит за своим столом со скучающим видом и "работает", Юлия как всегда вся в работе
    return

# кабинет Моники, Мелани зашла в кабинет
label ep29_dialogues3_melanie_monica_victoria_3a:
    # Мелани появляется в кабинете Моники
    melanie_t "Миссис Бакфетт не так уж и плохо тут устроилась."
    melanie_t "По ней не скажешь, что она особо здесь перерабатывает."
    melanie_t "Хотя... Заметно, что ей здесь откровенно скучно..."
    return

# кабинет Моники, Мелани кликает на Монику
label ep29_dialogues3_melanie_monica_victoria_3b:
    # Моника смотрит на Мелани удивленно
    m "Мелани? Ты ко мне?"
    mt "Мелани не просто так зашла ко мне в гости. Что-то случилось."
    mt "Надеюсь, это не касается Маркуса!"
    mt "!!!"
    # Мелани равнодушно
    melanie "Миссис Бакфетт. Я сейчас была на встрече с нашим общим хорошим другом..."
    # Моника явно напугана
    mt "!!!"
    m "Нашим общим д-другом?"
    melanie "Да, Миссис Бакфетт. Этот человек хочет сегодня встретиться с нами."
    mt "!!!"
    melanie "Встреча состоится вечером у меня."
    melanie "В Ваших же интересах, Миссис Бакфетт, присутствовать на встрече..."
    # Моника смотрит на Мелани ошарашенно
    julia "???"
    melanie "..."
    mt "Встреча с Маркусом?!"
    mt "У Мелани дома?!"
    mt "Сегодня?!"
    mt "!!!"
    # Юлия заинтересованно наблюдает за их диалогом
    # Моника смотрит на Юлию, потом снова на Мелани, берет себя в руки
    m "Я поняла, Мисс Мелани. Я приду вечером."
    melanie "Договорились, Миссис Бакфетт."
    # Мелани выходит из кабинета Моники
    melanie_t "Миссис Бакфетт явно напугана..."
    melanie_t "Теперь она точно придет ко мне."
    melanie_t "..."
    melanie_t "Сейчас мне нужно поговорить с Бифом."
    melanie_t "Мне понравилась моя идея насчет небольшого отпуска."
    melanie_t "Думаю, он мне не откажет..."
    # в заданиях появляется "Пойти в кабинет Бифа и поговорить с ним"
    $ log1 = _("Пойти в кабинет Бифа и поговорить с ним")
    return

# Мелани заходит в кабинет Бифа
label ep29_dialogues3_melanie_monica_victoria_4:
    # Биф, как обычно, сидит за столом с бутылкой алкоголя
    biff "А! Моя лучшая цыпочка пришла!"
    biff "Чем порадуешь папочку сегодня?"
    melanie_t "У него вокруг одни цыпочки... Как это пошло..."
    melanie "Биф, я хотела поговорить с тобой."
    melanie "Надеюсь, ты мне не откажешь..."
    # смотрит на него заигрывающе, Биф сидит расплывается в улыбке
    biff "Цыпочка что-то хотела попросить у меня?"
    biff "Говори. Папочка сегодня добрый."
    melanie "..."
    melanie "Возможно, ты позволишь мне..."
    melanie "Взять несколько выходных дней и немного отдохнуть?"
    biff "Цыпочка устала? Конечно, папочка позволит ей отдохнуть!"
    biff "..."
    biff "Только цыпочка сначала сделает фотосессию!"
    melanie "Какую фотосессию?"
    biff "Мне нужны фотографии для следующего номера журнала."
    biff "И я хочу видеть на этих фотографиях твое лицо, цыпочка..."
    biff "И не только лицо..."
    biff "У цыпочки есть, что показать в объектив камеры."
    # Мелани приподнимает бровь удивленно
    melanie "..."
    biff "В прошлый раз я просил тебя сделать фотосессию."
    biff "А ты сама не стала в ней сниматься."
    biff "Поэтому мне сейчас нужны именно твои фотографии."
    biff "А не той цыпочки, которая притворяется Моникой Бакфетт."
    melanie_t "Хм... Я надеялась, что его устроят фотографии Миссис Бакфетт..."
    melanie "В каком костюме нужно провести съемку?"
    biff "Да без разницы, цыпочка..."
    biff "Хоть в том, что на тебе сейчас надет..."
    melanie "..."
    biff "Сделай эту фотосессию и можешь взять несколько выходных."
    biff "Папочка добрый, папочка разрешает."
    # сидит с видом "хозяин мира", улыбается
    menu:
        "Согласиться на фотосессию":
            pass
        "Отказаться (пропуск фотосессии)"
            melanie_t "Он намекнул, что ему нужны откровенные фотографии..."
            melanie_t "Думаю, Биф обойдется без этих фотографий."
            melanie "Биф, я пока не совсем готова к фотосессии..."
            melanie "Я ее сделаю, но позже..."
            melanie_t "... возможно."
            biff "Папочка добрый, поэтому разрешает тебе подумать."
            return False # пропуск фотосессии, сразу в гримерку, оттуда домой на девичник
    melanie_t "Что ж... У меня как раз есть время до встречи с мелкой дрянью Викторией."
    melanie "Хорошо, Биф. Я сделаю, как ты хочешь." # без эмоций
    biff "Хорошая цыпочка. Папочка цыпочкой очень доволен."
    melanie_t "Нужно пойти в фотостудию. Надеюсь, Алекс на месте."
    # в заданиях появляется "Провести фотосессию"
    $ log1 = _("Провести фотосессию")
    return

# Мелани заходит в фотостудию
label ep29_dialogues3_melanie_monica_victoria_5:
    # Алекс на своем рабочем месте
    alex_photograph "Мисс Мелани! Надеюсь, Вы пришли поработать со мной?"
    melanie "Да, Алекс. Сегодня у нас фотосессия."
    menu:
        "Переодеться":
            pass
    # появляется окно выбора костюма, там только один
    melanie "Я сейчас переоденусь и вернусь."
    # через несколько минут
    # в студии появляется Мелани в костюме, Алекс смотрит на нее как на богиню
    alex_photograph "Мисс Мелани! Этот костюм! Вы в нем просто великолепны!!!"
    melanie_t "Мне не нравится этот костюм. Он практически ничего не прикрывает."
    melanie_t "Надо сказать Алексу, чтобы не брал откровенных ракурсов."
    # Мелани бросает на него взгляд и идет на съемочную площадку
    melanie "Алекс?"
    alex_photograph "Да, Мисс Мелани?"
    melanie "Ты все еще хочешь, чтобы мои фотографии появились в твоей личной коллекции?"
    # Алекс воодушевленно
    alex_photograph "Конечно, Мисс Мелани! Я давно мечтаю об этом! Так Вы согласны?"
    melanie "Алекс, я обещаю подумать об этом. При одном условии."
    alex_photograph "???"
    melanie "Мое условие простое, Алекс."
    melanie "Никаких откровенных ракурсов на этой фотосессии."
    melanie "Тогда я обдумаю возможность согласиться на твое предложение..."
    alex_photograph "Мисс Мелани! Вы можете не переживать! Я сделаю все, как Вы скажете!"
    melanie "Отлично, Алекс. У меня мало времени. Приступим?"
    # Мелани принимает первую позу
    alex_photograph "Итак, мотор!"
    melanie "Алекс, я буду следить за тем, какие ты берешь ракурсы."
    alex_photograph "Да, Мисс Мелани. Конечно."# фотографирует
    alex_photograph "Следующая поза, Мисс Мелани!"
    # Мелани меняет позу
    melanie "Алекс, ты помнишь, о чем мы с тобой договаривались?"
    alex_photograph "Конечно, Мисс Мелани. Никаких откровенных ракурсов!"
    alex_photograph "Я делаю все, как Вы сказали!"# сам, как обычно, делает откровенные фото
    melanie "Алекс, меня, как Миссис Бакфетт, не проведешь..."
    melanie "Не смей снимать меня с такого ракурса."
    alex_photograph "Мисс Мелани, не переживайте. На снимке ничего не видно."
    alex_photograph "Следующая поза, Мисс Мелани!"
    # Мелани меняет позу
    melanie "Алекс, что ты делаешь?"
    alex_photograph "Мисс Мелани, я нашел интересный ракурс."
    alex_photograph "Вы просто божественно прекрасны получитесь на снимке."
    alex_photograph "Ничего лишнего не будет видно, Мисс Мелани."# фоткает
    alex_photograph "Следующая поза, Мисс Мелани!"
    # Мелани меняет позу
    melanie "Алекс. Не смей делать такие кадры!"
    alex_photograph "Я не фотографирую, Мисс Мелани." # сам фоткает
    alex_photograph "Я просто пытаюсь подобрать интересный ракурс."
    melanie "Ты меня за кого принимаешь, Алекс?"
    melanie "Я не первый раз участвую в фотосессии."
    melanie "Думаешь, я не понимаю, что ты сейчас сделал?"
    alex_photograph "Мисс Мелани, я потом покажу Вам снимки."
    alex_photograph "Вы увидите, что я делаю вполне приличные кадры."
    alex_photograph "Следующая поза, Мисс Мелани!"
    # Мелани меняет позу
    melanie "Алекс, я не буду принимать такую позу."
    melanie "Это пошло. Я тебе не порномодель."
    alex_photograph "Мисс Мелани, я обещаю, что эти снимки будут настоящим произведением искусства!"
    alex_photograph "Когда Вы их увидите, то захотите разместить их, как свои портреты, в гримерке!"
    melanie "Чтобы я никаких своих интимных мест на них не видела, Алекс."
    alex_photograph "Конечно, Мисс Мелани!"
    alex_photograph "Следующая поза, Мисс Мелани!"
    # Мелани меняет позу
    melanie "Алекс, если ты и дальше будешь продолжать делать такие кадры..."
    melanie "То я откажусь от этой фотоссесии."
    alex_photograph "Мисс Мелани. Снимки получаются очень приличные."
    alex_photograph "Вы зря так переживаете. На них совсем ничего не видно."
    alex_photograph "Следующая поза, Мисс Мелани!"
    # Мелани меняет позу
    melanie "А сейчас что ты делашь?"
    alex_photograph "Это будет великолепный кадр, Мисс Мелани!"
    melanie "Если ты меня обманешь, Алекс, то я не буду больше с тобой работать."
    alex_photograph "Мисс Мелани, Вы можете не беспокоиться."
    alex_photograph "Я помню, о чем мы с Вами договаривались."
    # после окончания фотосессии
    alex_photograph "Мы закончили, Мисс Мелани! Вы были просто великолепны!!!"
    melanie "..."
    alex_photograph "Мисс Мелани, Вы подумаете над моим предложением?"
    # Мелани смотрит на него пристально
    melanie "Я уже подумала, Алекс."
    melanie "Я не могу себе позволить сотрудничать с фотографом..."
    melanie "Который так пренебрежительно относится к моим просьбам."
    alex_photograph "Мисс Мелани... Но ведь я..."
    melanie "Алекс, ответ 'нет'."
    melanie "Я не хочу больше ничего слышать о твоей личной коллекции."
    alex_photograph "Мисс..."
    melanie "Надеюсь, ты доволен сегодняшней фотосессией..."
    melanie "..."
    # Алекс смотрит расстроенно
    melanie_t "Нужно переодеться и ехать домой. Скоро придут Миссис Бакфетт и Виктория."
    # в заданиях появляется "Идти в гримерку, переодеться"
    $ log1 = _("Идти в гримерку, переодеться")
    return

# Гримерка
label ep29_dialogues3_melanie_monica_victoria_6:
    # Мелани переоделась, сидит возле зеркала
    melanie_t "Ну что ж... Посмотрим, что мелкая сучка Дика приготовила нам."
    melanie_t "Что бы это ни было, меня это вряд ли порадует. Как и Миссис Бакфетт."
    melanie_t "Должен существовать способ поставить Викторию на место..."
    melanie_t "Возможно, стоит поговорить об этом с Миссис Бакфетт..."
    # в заданиях появляется "Нужно ехать домой. Скоро придет Виктория"
    $ log1 = _("Нужно ехать домой. Скоро придет Виктория")
    return

# мысли Мелани в холле у лифта
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_6a:
    # едет к себе домой, при любом клике, кроме выхода
    melanie_t "Сейчас мне нужно ехать к себе домой."
    melanie_t "Скоро придут Миссис Бакфетт и Виктория."
    return

# при нажатии на локацию Дом Мелани управление переходит на Монику
# кабинет Моники
label ep29_dialogues3_melanie_monica_victoria_7:
    # Моника сидит в своем кабинете за столом, она одна, уже вечер
    # Моника взволнованна
    mt "Почему-то, мне совсем не хочется ехать к Мелани..."
    mt "Ничего хорошего меня там не ждет."
    mt "..."
    mt "Она сказала 'наш общий друг'..."
    mt "Это может быть только один человек. Маркус."
    mt "Я уверена в этом!"
    mt "Хм... А почему тогда у Мелани дома? Почему не в полиции?"
    mt "???"
    mt "Я могу не ехать к Мелани, но..."
    mt "Тогда меня могут ждать большие неприятности с Маркусом!"
    mt "Даже не хочу думать о том, что тогда меня может ожидать!"
    mt "!!!"
    mt "Лучше мне пойти сейчас к Мелани и самой все узнать."
    mt "Да, так будет лучше всего."
    # в заданиях появляется "Нужно переодеться и ехать к Мелани"
    $ log1 = _("Нужно переодеться и ехать к Мелани")
    return

# мысли Моники
label ep29_dialogues3_melanie_monica_victoria_7a:
# Моника пытается пойти к Мелани в красивом платье
    mt "Думаю, мне стоит надеть что-то более простое..."
    mt "В прошлый раз я была у Мелани в одежде шлюхи. Сегодня тоже нужно надеть его."
    return

label ep29_dialogues3_melanie_monica_victoria_7b:
# Моника пытается пойти к Мелани в любой другой одежде, кроме одежды шлюхи
    mt "В прошлый раз я была у Мелани в одежде шлюхи. Сегодня тоже нужно надеть его."
    return

label ep29_dialogues3_melanie_monica_victoria_7c:
# Моника пытается лечь спать
    mt "Я, конечно, могу не ехать к Мелани, но..."
    mt "Тогда меня могут ждать большие неприятности с Маркусом!"
    mt "Даже не хочу думать о том, что тогда меня может ожидать!"
    mt "!!!"
    mt "Лучше мне пойти сейчас к Мелани и самой все узнать."
    return

# при клике на Дом Мелани на карте включается сцена у Мелани дома
