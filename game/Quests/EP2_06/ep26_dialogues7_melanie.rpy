

label ep26_dialogues7_melanie1:

    return

# Моника подходит к Мелани в гримерной (первый раз)
# Мелани сидит за гримерным столиком
m "Мелани, ты вернулась?"
m "Где ты так долго была? Что с тобой случилось?"
melanie "Миссис Бакфетт, это Вы?"
m "Да, Мелани, это Я!"
m "И я ждала тебя все это время!"
m "Почему тебя так долго не было?!"
m "Я уже думала что Маркус забрал тебя!"
melanie "Миссис Бакфетт, я не понимаю о чем Вы говорите..."
m "Что значит ты не понимаешь, Мелани?"
m "Я говорю про твой визит к Маркусу!"
m "Ты должна была решить с ним вопрос по поводу меня!"
m "Но, вместо этого, ты куда-то пропала!"
melanie "Мэм, Я не знаю о чем и о ком Вы говорите..."
m "Ты что, играешь со мной, Мелани?!"
m "Ты прекрасно знаешь что я говорю о Маркусе!"
# Мелани отворачивается
melanie "Мэм, я не знаю кто это..."
melanie "Миссис Бакфетт, я очень занята. Пожалуйста, не отвлекайте меня..."

mt "Она не хочет говорить про Маркуса..."
mt "Она что, обманула меня и не ходила к нему?!"


menu:
    "Мелани, ты вернулась?":
        pass
    "Посмотреть на Мелани.":
        m "У меня странное чуство..."
        m "Мелани?"
        m "Мелани!"
        # убирает волосы
        m "Что там? Что там такое?"
        m "О БОЖЕ!"
        m "НЕТ!"
        melanie "Миссис Бакфетт, я просила Вас не беспокоить меня."
        m "!!!"
#    "Мелани, сучка, ты что, никуда не ходила?! (next update) (disabled)":
#        pass
    "Мелани, пожалуйста, для меня это очень важно! (next update) (disabled)"
        pass






























#
