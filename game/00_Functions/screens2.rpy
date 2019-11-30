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

screen screen_betty_panties_select2():
    modal True
    fixed:
        xpos getRes(312-153)
        ypos getRes(280)
        $ offsetIdx = 0
        for pantiesIdx in range(1,6):
            hbox:
                if pantiesIdx != bettyPantiesCurrent or bettyMustNotWearPanties == True:
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
        if monicaLaundryBettyPantiesSelectNudeDisabled == False:
            imagebutton:
                xpos getRes(500 + 340)
                ypos getRes(340)
                idle "Icons2/Betty_Panties_Icon_7.png"
                hover "Icons2/Betty_Panties_Icon_7_hover.png"
                action Return(7)
        else:
            imagebutton:
                xpos getRes(500 + 340)
                ypos getRes(340)
                idle "Icons2/Betty_Panties_Icon_7_Disabled.png"
                action Return(-1)

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
                        idle monicaOutfitsIcons2[idx] + ".png"
                        hover monicaOutfitsIcons2[idx] + "_hover.png"
                        action Return(idx)
                    else:
                        if monicaOutfitsIcons2[idx] == "":
                            idle "/Icons2/Photoshoot_Empty_Icon_Disabled.png"
                        else:
                            idle monicaOutfitsIcons2[idx] + "_Disabled.png"
                        action Return(-1)
                $ idx += 1
                $ offsetXIdx += 1
            $ offsetYIdx +=1

screen choose_melanie_photoshoot_outfit():
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
                    if melanieOutfitsEnabled[idx] == True:
                        idle melanieOutfitsIcons[idx] + ".png"
                        hover melanieOutfitsIcons[idx] + "_hover.png"
                        action Return(idx)
                    else:
                        if melanieOutfitsIcons[idx] == "":
                            idle "/Icons2/Photoshoot_Empty_Icon_Disabled.png"
                        else:
                            idle melanieOutfitsIcons[idx] + "_Disabled.png"
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

screen camera_record_screen():
    fixed:
        xpos getRes(1600)
        ypos getRes(43)
        add "images/Icons2/Rec_Icon1.png" at camera_record_icon_transform

screen camera_viewfinder_screen():
    add "images/Icons2/Camera_ViewFinder.png"

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

screen achievements_screen():
    $ width1 = int(1217 * gui.resolution.koeff)
    $ height1 = int(872 * gui.resolution.koeff)
    $ x1 = int(377 * gui.resolution.koeff)
    $ y1 = int(107 * gui.resolution.koeff)

    $ rowOffset = getRes(22) #244x137
    $ cellSizeX = getRes(296)
    $ cellSizeY = getRes(170)
    $ cellsInRow = 4
    $ category_height = gui.resolution.gallery.category_height

    # calculate viewport size
    $ rowsAmount = 0
    for category in achievements_categories:
        $ rowsAmount += int(math.ceil(float(len(achievements_list[category[0]]))/float(cellsInRow)))
    $ viewportHeight = len(achievements_categories) * (category_height+gui.resolution.gallery.category_margin_down) + rowsAmount * cellSizeY

    layer "master"
    zorder 60
    modal True
    button:
        xfill True
        yfill True
        action [
            Return()
        ]
    frame:
        background Frame("gui/frame4" + res.suffix + ".png", left=2, top=int(80*gui.resolution.koeff), right=2, bottom=2)
        pos(x1, y1)
        anchor(0, 0)
        xysize (width1, height1)
        imagebutton:
            xpos 1.0
            ypos 0.0
            anchor (0.5, 0.5)
            idle "/icons/window_close" + res.suffix + ".png"
            hover "/icons/window_close_hover" + res.suffix + ".png"
            action [
                Return()
            ]
        viewport id "questlog_viewport":
#            xpos getRes(377+10)
#            ypos getRes(107+10)
            xpos 0
            ypos getRes(85)
            draggable True
            scrollbars "vertical"
            xmaximum getRes(1217-15)
            ymaximum getRes(852-85)
            mousewheel True
            pagekeys True
            child_size (getRes(852-85), viewportHeight)
            $ galleryX = 0
            $ galleryY = 0
            $ curY = 0
            for category in achievements_categories:
#                text category[1] style "char_face_style_caption":
                text category[1]:
                    pos(rowOffset, curY)
                    font "fonts/BebasNeue Regular.ttf"
                    color category[2]
                    size 40
                $ curY += category_height
                $ cellsList = achievements_list[category[0]]

                for i in range(0,len(cellsList)):
                    $ posX = i%cellsInRow * cellSizeX + rowOffset
                    $ posY = int(i/cellsInRow) * cellSizeY
                    if get_achievement(cellsList[i][0]) == True:
                        add "images/Achievements/ach_" + cellsList[i][0] + ".jpg":
                            pos(posX, posY + curY)
                        add "gui/gallery_frame" + res.suffix + ".png":
                            pos(posX-gui.resolution.gallery.frame.offset, posY-gui.resolution.gallery.frame.offset + curY)
                    else:
                        add "images/Achievements/ach_" + cellsList[i][0] + "_disabled.jpg":
                            pos(posX, posY + curY)
                        add "gui/gallery_frame" + res.suffix + ".png":
                            pos(posX-gui.resolution.gallery.frame.offset, posY-gui.resolution.gallery.frame.offset + curY)
                    text cellsList[i][1] style "gallery_caption_text":
                        pos(posX + getRes(244/2), posY + curY + getRes(137+15))
                        anchor (0.5, 0.5)
                $ curY += int(math.ceil(float(len(cellsList))/float(cellsInRow))) * cellSizeY + gui.resolution.gallery.category_margin_down


screen love_bar_screen(oldBarValue, newBarValue):
    fixed:
            bar:
                xpos getRes(17)
                ypos getRes(260)
                value AnimatedValue(float(newBarValue)/100, 1.0, 1.0, float(oldBarValue)/100)
                xoffset 5
                xysize(gui.resolution.hud_screen.love_bar_xysize)
                bar_vertical True
                top_bar "/icons/bar/love_bar_empty" + res.suffix + ".png"
                bottom_bar "/icons/bar/love_bar_full" + res.suffix + ".png"
                thumb "/icons/bar/love_bar_thumb" + res.suffix + ".png"
                bottom_gutter gui.resolution.hud_screen.love_bar_bottom_gutter
                top_gutter gui.resolution.hud_screen.love_bar_top_gutter
                thumb_offset gui.resolution.hud_screen.love_bar_thumb_offset


screen poledance_camera_icon(shootsArr):
    $ list1 = list(set(shootsArr))
    fixed:
        xpos getRes(40)
        ypos getRes(20)
        hbox:
            add "/Icons2/Photo_Cinema_icon.png"
            null width getRes(8)
            text str(len(list(set(shootsArr)))) + " / " + str(shotsTotalAmount) style "photoshoot_cinema_text_style"



screen poledance():
    fixed:
        xpos getRes(1650)
        ypos getRes(430)
        #up
        if arrowUp == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(-40)
                idle "/Icons2/dance_up.png"
                hover "/Icons2/dance_up_hover.png"
                action [SetVariable("arrowUp", False), Return("up")]
        else:
            add "/Icons2/dance_up_Disabled.png":
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
                idle "/Icons2/dance_left.png"
                hover "/Icons2/dance_left_hover.png"
                action [SetVariable("arrowSide", False), Return("side")]
        else:
            add "/Icons2/dance_left_Disabled.png":
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
                idle "/Icons2/dance_down.png"
                hover "/Icons2/dance_down_hover.png"
                action [SetVariable("arrowDown", False), Return("down")]
        else:
            add "/Icons2/dance_down_Disabled.png":
                xpos getRes(50)
                ypos getRes(200)
                xanchor 0.5
                yanchor 0.5
        #next
        if arrowStop == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(170)
                ypos getRes(80)
                idle "/Icons2/dance_stop.png"
                hover "/Icons2/dance_stop_hover.png"
                action Return("stop")
        else:
            add "/Icons2/dance_stop_Disabled.png":
                xanchor 0.5
                yanchor 0.5
                xpos getRes(170)
                ypos getRes(80)


screen atl_test1():
    add "/images/Slides/v_Monica_Strip_A1_end.jpg" at pole_dance_shake















#
