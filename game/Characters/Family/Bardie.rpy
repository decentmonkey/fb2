default bardieLocation = "none"
default monicaBardieOffended1 = False

label bardieInteract1:
    if act == "l":
        mt "Этот маленький оболтус меня бесит!"
        return
    if act == "t":
        if scene_name == "street_house_main_yard":
            call bardie_comment5()
            return
    return
#        if bardieLocation == "BedroomBardie":
#            call bardieDialogue1()
#            return

#    if bardieLocation == "Floor1" and act == "w":
#        call change_scene("floor1_fountain", "Fade", "snd_fountain")


    return


label bardieMonicaCleaningInteract:
    if act == "l":
        mt "Он так и пытается подкрасться ко мне!"
        "Мне надо быть осторожнее..."
        return False
    if act == "t":
        if scene_name == "floor1":
            call cleaning_bardie_comment1()
        if scene_name == "bedroom_bardie":
            call cleaning_bardie_comment2()
        if scene_name == "bedroom_second":
            call cleaning_bardie_comment3()
        $ move_object("Bardie", "empty")
        $ monicaCleaningObject = "" # Ставим Монику в исходное положение стоя
        $ add_char_progress("Bardie", 15, "cleaning_upskirt_day " + str(day))
        call refresh_scene_fade()
        return False
    return
