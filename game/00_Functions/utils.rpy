
init python:
    def getRes(pixels):
        return int(pixels * gui.resolution.koeff)

    def getMousePosition():
        import pygame
        x, y = pygame.mouse.get_pos()
        store.mousex = x
        store.mousey = y

    def checkDialogueExists():
        if renpy.get_screen("choice") != None or renpy.get_screen("window") != None:
            return True
        return False

    def mycopytext(t):
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, t.encode("utf-8"))
        return

    def makeDump():
        global scenes_data, debugMode
        if debugMode != True:
            return
        print "Debug!"
        if os.path.isdir("/Users//Documents/work/browse") == True:
            str1 = json.dumps(scenes_data)
            f = open("/Users//Documents/work/browse/renpy_debug.json","w")
            f.write(str1)
            f.close()
        return

    def notif(str1):
        global notifList, lastNotifTime
        notifList.append(str1)
#        renpy.notify(str1)
        lastNotifTime = time.time()
        renpy.hide_screen("notify")
        renpy.show_screen("notify", "notifList")
        return

    def notifCheckTimeout(): #костыль на исчезание нотификаций при скиппинге текста
        global lastNotifTime
        if time.time() - lastNotifTime > 60.0:
            print "force remove notifications"
            notifList = []
            renpy.hide_screen("notify")
        return

    def notif_monica():
        global monicaBitch
        if monicaBitch:
            notif(_("Моника стерва"))
        else:
            notif(_("Моника приличная"))

        return

    def rand(from_int, to_int):
        return renpy.random.randint(from_int,to_int)

    def convertMoneyStr(in_money):
        return '{:3,.2f}'.format(in_money)

label mycopytext_label(txt):
    $ mycopytext(txt)
    return


label photoshop_flash():
    sound snd_photo_capture
    show screen photoshot_screen()
    pause 0.7
    hide screen photoshot_screen
    return

label textonblack(in_text):
    scene black_screen
    with Dissolve(1)
    show screen textonblack_screen(in_text)
    with Dissolve(1)
    $ renpy.pause(1.0, hard=True)
    pause 0.5
    scene black_screen
    with Dissolve(1)
    return


label textonblack_long(in_text):
    scene black_screen
    with Dissolve(1)
    show screen textonblack_screen(in_text)
    with Dissolve(1)
    $ renpy.pause(5.0, hard=True)
    scene black_screen
    with Dissolve(1)
    return

label textonblack_pause(in_text):
#    $ _dismiss_pause = False
    scene black_screen
    with Dissolve(1)
    show screen textonblack_screen(in_text)
    with Dissolve(1)
#    $ _dismiss_pause = True
    pause
    scene black_screen
    with Dissolve(1)
    return

label cleanNotifList():
    $ notifList = []
    return

label showRandomImages(imagesList, imagesAmount, makeRandom=False):
    $ imagesList = random.sample(set(imagesList), imagesAmount)
    if makeRandom == False:
        $ imagesList.sort()
    $ imagesListIdx = 0
    label showRandomImages_loop:
        if imagesListIdx < imagesAmount:
            $ imageName = str(imagesList[imagesListIdx])
            img imageName
            w
            $ imagesListIdx += 1
            jump showRandomImages_loop
    return

label showRandomImagesDiss(imagesList, imagesAmount, makeRandom=False):
    $ imagesList = random.sample(set(imagesList), imagesAmount)
    if makeRandom == False:
        $ imagesList.sort()
    $ imagesListIdx = 0
    label showRandomImages_loop_diss:
        if imagesListIdx < imagesAmount:
            $ imageName = str(imagesList[imagesListIdx])
            img imageName
            with diss
            w
            $ imagesListIdx += 1
            jump showRandomImages_loop_diss
    return


label showRandomImagesFirstFade(imagesList, imagesAmount, makeRandom=False):
    $ firstFlag = True
    $ imagesList = random.sample(set(imagesList), imagesAmount)
    if makeRandom == False:
        $ imagesList.sort()
    $ imagesListIdx = 0
    label showRandomImages_loop2:
        if imagesListIdx < imagesAmount:
            $ imageName = str(imagesList[imagesListIdx])
            img imageName
            if firstFlag == True:
                with fade
                $ firstFlag = False
            w
            $ imagesListIdx += 1
            jump showRandomImages_loop2
    return








#
