# Дом. Комната Барди. Разговор Барди и Бетти.
label dialogue_doublephoto_1:
    # Барди с телефоном в руках сидит на своей кровати, Бетти стоит в комнате Барди и недовольно кричит
    betty "Гувернантка!!!"
    # спустя несколько минут появляется Моникаg
    mt "Она опять орет на весь дом..."
    mt "Что этой деревенщине снова от меня нужно?"
    m "Да, миссис Робертс..."
    # Бетти и Моника стоят перед Барди, он сидит на кровати
    betty "Гувернантка, я..."
    betty "..."
    bardie "Мне нужно проверить, насколько хорошо ты соблюдаешь правила этого дома и..."
    bardie "...сделать фото!"
    mt "Он опять хочет фото?! Когда он уже отстанет от меня?!"
    bardie "Давай, без лишних разговоров. Поднимай юбку!"
    # Моника зло смотрит на него
    m "Я не собираюсь фотографироваться с задранной юбкой!"
    m "Достаточно того, что ты при каждом удобном случае заглядываешь мне под юбку!"
    mt "Мелкий озабоченный извращенец!"
    bardie "Гувернантка слишком много разговаривает!"
    bardie "Если ты хорошая гувернантка и соблюдаешь правила, то делай, что тебе говорят!"
    m "..."
    # Барди с угрозой
    bardie "Или ты отказываешься и хочешь, чтобы я тебя наказал?"
    mt "!!!"
    mt "Ненавижу эту малявку! И эту чокнутую деревенщину Бетти!"
    mt "Когда этот дом снова станет моим, я возьму ее к себе гувернанткой. Будет работать у меня за еду."
    mt "!!!"
    # Моника смотрит зло, Бетти все это время стоит с каменным лицом
    m "Зачем тебе нужна эта фотография?"
    bardie "Гувернантку это не касается! Поднимай юбку!"
    # Барди поднимает руку с телефоном, чтобы сделать фото
    mt "..."
    if monicaUnder != "Nude":
        mt "Черт!!!"
        mt "Он увидит, что я в трусиках и снова накажет меня!"
        m "Я хорошая гувернантка! Но я не буду этого делать!"
        return False
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            return False
    # Моника, срипя зубами соглашается, поднимает юбку
    bardie "Хорошая гувернантка."
    # Барди фото не делает и смотрит на Бетти
    bardie "Бетти?.."
    betty "!!!"
    # Бетти фыркает, психует, но подчиняется и задирает юбку
    betty "Давай, быстрее!"
    betty "Только одно фото!"
    # Барди с довольным видом делает фотку
    betty "Все?"
    bardie "Подождите, что-то не получилось фото. Ну-ка еще раз."
    # Барди делет еще несколько кадров
    betty "Все! Хватит!"
    # Бетти опускает юбку, Моника следом за ней
    betty "Надеюсь, ты доволен?"
    bardie "Очень! Вы обе доказали мне, что соблюдаете правила этого дома."
    bardie "..."
    bardie "Моему однокласснику точно понравится!"
    # Бетти с Моникой офигевают
    mt "!!!"
    betty "!!!"
    # Бетти начинает орать, Моника зло смотрит
    betty "ЧТООООО?!!"
    betty "Какому еще однокласснику?!"
    # Барди нагло
    bardie "Ах да... Вы же еще не знакомы... Я скоро приглашу его в гости."
    mt "Он совсем обнаглел! Ненавижу эту малявку!"
    mt "И почему у этой деревенщины не хватает мозгов, чтобы приструнить его?!"
    betty "Нет!!! Не смей! Ты говорил, что это фото никто не увидит!"
    betty "!!!"
    bardie "Я так сказал?! Хм... Никто, кроме моего одноклассника."
    bardie "Аха-ха!"
    betty "Да как ты смеешь так обращаться со мной, порядочной женщиной?! Сопляк!"
    betty "Я - жена твоего отца! А ты собираешься показываеть фото, где я голая, да еще и с этой шлюхой, своему однокласснику!!!"
    mt "Ненавижу эту семейку! Когда она будет моей гувернанткой, я ее уволю!"
    mt "!!!"
    bardie "Если ты и дальше будешь со мной так разговаривать, то женой моего отца ты будешь недолго..."
    bardie "Ты забыла, что у меня есть много фото, интересных фото...?"
    bardie "И в интересной компании..."
    bardie "???"
    # Бетти смотрит испепеляющим взглядом, но молчит
    betty "!!!"
    mt "Хм. Кто из нас после этого шлюха?"
    bardie "Вы на сегодня свободны. Можете идти."
    return
