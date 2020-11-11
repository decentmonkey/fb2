screen questhelp_screen():
    $ width1 = int(1617 * gui.resolution.koeff)
    $ height1 = int(872 * gui.resolution.koeff)
    $ x1 = int(177 * gui.resolution.koeff)
    $ y1 = int(107 * gui.resolution.koeff)

#    $ rowOffset = getRes(22) #244x137

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
        background Frame("gui/frame6" + res.suffix + ".png", left=2, top=int(80*gui.resolution.koeff), right=2, bottom=2)
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
        viewport id "questhelp_viewport_categories":
#            xpos getRes(377+10)
#            ypos getRes(107+10)
            xpos 0
            ypos getRes(85)
            draggable True
            scrollbars "vertical"
            xmaximum getRes(617-15)
            ymaximum getRes(852-85)
            mousewheel True
            pagekeys True
#            child_size (getRes(852-85), viewportHeight)

        viewport id "questhelp_viewport_events":
#            xpos getRes(377+10)
#            ypos getRes(107+10)
            xpos getRes(617)
            ypos getRes(85)
            draggable True
            scrollbars "vertical"
            xmaximum getRes(500-15)
            ymaximum getRes(852-85)
            mousewheel True
            pagekeys True
#            child_size (getRes(852-85), viewportHeight)

        viewport id "questhelp_viewport_event_descriptions":
#            xpos getRes(377+10)
#            ypos getRes(107+10)
            xpos getRes(617 + 500)
            ypos getRes(85)
            draggable True
            scrollbars "vertical"
            xmaximum getRes(500-15)
            ymaximum getRes(852-85)
            mousewheel True
            pagekeys True
#            child_size (getRes(852-85), viewportHeight)
