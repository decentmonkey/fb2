label monica_gas_station_thief_dialogue1:
    #Моника заходит на заправку (голодная)
    mt "На этой заправке продается еда."
    "Если я буду осторожна, то могу украсть какое-нибудь пирожное..."
    "Но стоит-ли мне рисковать?"
    return

    #Моника заходит на заправку (сытая)
    mt "Что я здесь делаю?"
    mt "Есть я пока не хочу, а говорить с этой кассиршей мне не о чем..."

    return

label monica_gas_station_thief_dialogue2:
    #Моника ворует еду
    menu:
        "Украсть еду.":
            pass
        "Не делать этого.":
            mt "Я не стану рисковать..."
            return

    #render
    img 7072
    w
    img 7073
    w
    img 7074
    mt "Думаю не будет ничего страшного если я украду одно пирожное..."
    img 7075
    w
    #вариации (случайно)
    img 7076
    #
    img 7077
    #
    img 7078
    #
    "Я заслужила его за все то что пережила..."

    return

label monica_pissing_basement:
    #Моника писает
    #звук
    #whore
    #вариации (случайно)
    $ toilet_images = ["7079", "7080", "7081", "7082", "7083", "7084", "7085", "7086", "7087"]

    #governess
    $ toilet_images = ["7088", "7089", "7090", "7091", "7092", "7093", "7094"]


    return

label monica_shower_basement:
    #Моника принимает душ
    #вариации (случайно)
    #звук душа
    img 7095
    w
    $ shower_images = ["7096", "7097", "7098", "7099", "7100", "7101", "7102", "7103", "7104", "7105", "7106", "7107"]
    return
