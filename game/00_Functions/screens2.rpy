screen screen_betty_panties_select():
    modal True
    fixed:
        xpos getRes(312)
        ypos getRes(280)
        $ offsetIdx = 0
        for pantiesIdx in range(1,6):
            hbox:
                if pantiesIdx != bettyPantiesCurrent:
                    imagebutton:
                        xpos (offsetIdx * getRes(340))
                        idle "Icons2/Betty_Panties_Icon_" + str(pantiesIdx) + ".png"
                        hover "Icons2/Betty_Panties_Icon_" + str(pantiesIdx) + "_hover.png"
                        action Return(pantiesIdx)
                    $ offsetIdx += 1

        imagebutton:
            xpos getRes(500)
            ypos getRes(340)
            idle "Icons2/Betty_Panties_Icon_6.png"
            hover "Icons2/Betty_Panties_Icon_6_hover.png"
            action Return(6)
