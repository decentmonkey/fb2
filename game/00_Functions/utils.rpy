
init python:
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
        print "Debug!"
        if debugMode != True:
            return
        if os.path.isdir("/Users/Denis/Documents/work/browse") == True:
            str1 = json.dumps(scenes_data)
            f = open("/Users/Denis/Documents/work/browse/renpy_debug.json","w")
            f.write(str1)
            f.close()
        return

    def notif(str1):
        renpy.show_screen("notify", str1)
        return

    def notif_monica():
        global monicaBitch
        if monicaBitch:
            renpy.show_screen("notify", _("Моника стерва"))
        else:
            renpy.show_screen("notify", _("Моника приличная"))

        return

    def rand(from_int, to_int):
        return renpy.random.randint(from_int,to_int)

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
    pause 1.5
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
    $ _dismiss_pause = False
    scene black_screen
    with Dissolve(1)
    show screen textonblack_screen(in_text)
    with Dissolve(1)
    $ _dismiss_pause = True
    pause
    scene black_screen
    with Dissolve(1)
    return











#
