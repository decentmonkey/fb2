    # Общие 7420, 7422, 7423, 7424, 7425, 7426, 7427, 7428, 7429, 7430, 7431

    # Если Governess Pants (Betty 7419), 7421, 7432, 7433, 7434, 7435
    # Если Governess Pants Betty_1 (Betty 7436) 7437, 7438, 7439
    # Если Governess Pants Betty_2 (Betty 7440) 7441, 7442, 7443
    # Если Governess Pants Betty_3 (Betty 7444) 7445, 7446, 7447
    # Если Governess Pants Betty_4 (Betty 7448) 7449, 7450, 7451
    # Если Governess Pants Betty_5 (Betty 7452) 7453, 7454, 7455

label ep22_Act_Images_monica_cleaning_spot:
    $ images = [7420, 7422, 7423, 7424, 7425, 7426, 7427, 7428, 7429, 7430, 7431]
    $ imagesList = random.sample(set(images), 4)
    $ amount = 4
    $ bettyHere = False
    if get_active_objects("Betty", scene="floor2") != False:
        $ bettyHere = True
    if cloth == "Governess":
        if monicaBettyPanties == False:
            if bettyHere == True:
                img 7419
                w
            img 7421
            call showRandomImages(images, 4, True)
            img 7432
            w
        else:
            if monicaBettyPantiesId == 1:
                if bettyHere == True:
                    img 7436
                    w
                img 7437
                call showRandomImages(images, 4)
                img 7437
                w
            if monicaBettyPantiesId == 2:
                if bettyHere == True:
                    img 7440
                    w
                img 7441
                call showRandomImages(images, 4)
                img 7441
                w
            if monicaBettyPantiesId == 3:
                if bettyHere == True:
                    img 7444
                    w
                img 7445
                w
                img 7446
                w
                call showRandomImages(images, 4)
                img 7447
                w
            if monicaBettyPantiesId == 4:
                if bettyHere == True:
                    img 7448
                    w
                img 7449
                call showRandomImages(images, 4)
                img 7449
                w
            if monicaBettyPantiesId == 5:
                if bettyHere == True:
                    img 7452
                    w
                img 7453
                w
                img 7454
                w
                call showRandomImages(images, 4)
                img 7455
                w
    call ep22_dialogue2_7()
    return
