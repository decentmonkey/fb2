# админ
label worker2_dialogue_workplace:
    mt "Этот неудачник, похоже, разбирается в компьютерах... Но я в них ничего не понимаю..."
    mt "Да и мне неинтересно..."
    mt "У меня может быть какое-то дело нему?"
    menu:
        "Задать умный вопрос.":
            m "Послушай, а где здесь кнопка, которая выключает интернет?"
            w2 "Что?!"
            m "Ну такая специальная кнопка, на которую нажимаешь и отключается интернет."
            w2 "(Похоже наш босс не слишком силен в этом...)"
            w2 "Она на кухне, рядом с холодильником."
            m "Хорошо, спасибо."
            w2 "(Ха-ха-ха.)"
            # моника отошла
            mt "Рядом с холодильником?! Так, ерунда какая-то..."
            mt "Это такая умная шутка?"
            mt "Он играет с огнем..."
#            mt "Ладно, лучше не буду в это лезть, все равно в этом ничего не понимаю..."
#            mt "Зато я точно знаю, кто в этом разбирается..."
            return
        "Уйти":
            m "Все равно я в этом ничего не понимаю..."
            return

label worker2_dialogue_office:
    w2 "Босс, я все проверил. Все работает стабильно."
    w2 "Могу я чем нибудь помочь?"
    menu:
        "Разве тебя не учили стучаться?":
            m "Разве тебя не учили стучаться?"
            w2 "Ну... Я постучал..."
            m "Не правда! А теперь выйди из кабинета и если ты хочешь войти, постучись."
            w2 "Хорошо..."
            # выыходит - стучится
            w2 "Миссис Бакфет, можно?"
            m "Да, заходи."
            m "Вот видишь, все просто. Ты говоришь, что у тебя все работает..."
            m "Хорошо. А теперь можешь идти."
            w2 "?!"
            m "Да, да, иди работай."
            return
        "Больше ничего.":
            m "Больше ничего. Можешь идти."
            w2 "Хорошо. Если Вам что-то понадобится, зовите."
            mt "Хм... Он ведет себя как болван."
            mt "Возможно я смогу его как-то использовать..."
            mt "Но как? Пока не знаю..."
#            mt "Хм...Возможно я смогу использовать этого болвана..."
#            mt ""
            return
