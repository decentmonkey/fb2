label ep27_police1_init:
    $ add_hook("Building", "ep27_police2_enter", scene="street_police", label="police_quest1")
    return


label ep27_police2_enter: #вход в здание полиции
    if act=="l":
        return
    m "police"
    return
