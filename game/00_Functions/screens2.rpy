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

screen choose_photoshoot_outfit():
    modal True
    fixed:
        xpos getRes(480)
        ypos getRes(220)
        $ offsetYIdx = 0
        $ idx = 0
        for row1 in range(0,2):
            $ offsetXIdx = 0
            for col1 in range(0,5):
                imagebutton:
                    xpos (offsetXIdx * getRes(200))
                    ypos (offsetYIdx * getRes(330))
                    if monicaOutfitsEnabled[idx] == True:
                        idle monicaOutfitsIcons[idx] + ".png"
                        hover monicaOutfitsIcons[idx] + "_hover.png"
                        action Return(idx)
                    else:
                        if monicaOutfitsIcons[idx] == "":
                            idle "/Icons2/Photoshoot_Empty_Icon_Disabled.png"
                        else:
                            idle monicaOutfitsIcons[idx] + "_Disabled.png"
                        action Return(-1)
                $ idx += 1
                $ offsetXIdx += 1
            $ offsetYIdx +=1

screen photoshoot_camera_icon(shootsArr):
    $ list1 = list(set(shootsArr))
    fixed:
        xpos getRes(40)
        ypos getRes(20)
        hbox:
            add "/Icons2/Photo_Cinema_icon.png"
            null width getRes(8)
            text str(len(list(set(shootsArr)))) + " / " + str(shotsTotalAmount) style "photoshoot_cinema_text_style"
    fixed:
        xpos getRes(40)
        ypos getRes(935)
        hbox:
            add "/Icons2/Photo_camera_icon2.png"
            null width getRes(5)
            text str(shotsAmount) style "photoshoot_camera_text_style":
                if shotsAmount <= 5:
                    color "#f83c2e"


screen photoshoot():
    fixed:
#        xpos getRes(1600)
        xpos getRes(1650)
        ypos getRes(430)
        #up
        if arrowUp == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(-40)
                idle "/Icons2/photo_up.png"
                hover "/Icons2/photo_up_hover.png"
                action [SetVariable("arrowUp", False), Return("up")]
        else:
            add "/Icons2/photo_up_Disabled.png":
                xpos getRes(50)
                ypos getRes(-40)
                xanchor 0.5
                yanchor 0.5
        #left
        if arrowSide == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(0)
                ypos getRes(80)
                idle "/Icons2/photo_left.png"
                hover "/Icons2/photo_left_hover.png"
                action [SetVariable("arrowSide", False), Return("side")]
        else:
            add "/Icons2/photo_left_Disabled.png":
                xpos getRes(0)
                ypos getRes(80)
                xanchor 0.5
                yanchor 0.5
        #down
        if arrowDown == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(200)
                idle "/Icons2/photo_down.png"
                hover "/Icons2/photo_down_hover.png"
                action [SetVariable("arrowDown", False), Return("down")]
        else:
            add "/Icons2/photo_down_Disabled.png":
                xpos getRes(50)
                ypos getRes(200)
                xanchor 0.5
                yanchor 0.5
        #next
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos getRes(170)
            ypos getRes(80)
            idle "/Icons2/photo_next2.png"
            hover "/Icons2/photo_next2_hover.png"
            action Return("next")

screen photoshoot_no_next():
    fixed:
#        xpos getRes(1600)
        xpos getRes(1650)
        ypos getRes(430)
        #up
        if arrowUp == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(-40)
                idle "/Icons2/photo_up.png"
                hover "/Icons2/photo_up_hover.png"
                action [SetVariable("arrowUp", False), Return("up")]
        else:
            add "/Icons2/photo_up_Disabled.png":
                xpos getRes(50)
                ypos getRes(-40)
                xanchor 0.5
                yanchor 0.5
        #left
        if arrowSide == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(0)
                ypos getRes(80)
                idle "/Icons2/photo_left.png"
                hover "/Icons2/photo_left_hover.png"
                action [SetVariable("arrowSide", False), Return("side")]
        else:
            add "/Icons2/photo_left_Disabled.png":
                xpos getRes(0)
                ypos getRes(80)
                xanchor 0.5
                yanchor 0.5
        #down
        if arrowDown == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(200)
                idle "/Icons2/photo_down.png"
                hover "/Icons2/photo_down_hover.png"
                action [SetVariable("arrowDown", False), Return("down")]
        else:
            add "/Icons2/photo_down_Disabled.png":
                xpos getRes(50)
                ypos getRes(200)
                xanchor 0.5
                yanchor 0.5

screen pylon_screen(sceneImage, objectsList):
    layer "master"
    add sceneImage:
        xpos 0
        ypos 0
    for objData in objectsList:
        $ canvas_offset = get_canvas_offset(objData[0])
        if canvas_offset == False:
            $ canvas_offset = [0, 0]
        add objData[1]:
            xpos canvas_offset[1]
            ypos canvas_offset[0]
