# 381 617 617

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
            Return(False)
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
                Return(False)
            ]
        viewport id "questhelp_viewport_categories":
#            xpos getRes(377+10)
#            ypos getRes(107+10)
            xpos 0
            ypos getRes(85)
            draggable True
#            scrollbars "vertical"
            xmaximum getRes(381-15)
            ymaximum getRes(852-85)
            mousewheel True
            pagekeys True
#            child_size (getRes(852-85), viewportHeight)

            frame:
                background None
                padding (getRes(10), getRes(10))
                vbox:
                    # active categories (bold)
                    for category in questHelpDataCategoriesBold:
                        python:
                            categoryStyle = False
                            if questHelpDataLastCategoryMemory.has_key(category) == True and questHelpDataCategoriesBold[category] == True:
                                categoryStatus = questHelpDataLastCategoryMemory[category]
                                if categoryStatus == -1:
                                    categoryStyle = "questhelp_category_failed"
                                if categoryStatus == 1:
                                    categoryStyle = "questhelp_category_completed"
                                if categoryStatus == 0:
                                    categoryStyle = "questhelp_category_active"
                                if questHelpCurrentCategory != category:
                                    categoryStyle = categoryStyle + "_bold"
                                else:
                                    categoryStyle = categoryStyle + "_selected"
                        if categoryStyle != False:
                            textbutton t__(category) style categoryStyle:
                                xsize getRes(350)
                                xpadding 10
                                top_padding 10
                                bottom_padding 7
                                action [
                                    Return(["category_click", category])
                                ]

                    # not-bold active categories
                    for category in questHelpDataLastCategoryMemory:
                        python:
                            categoryStyle = False
                            if questHelpDataCategoriesBold.has_key(category) == False or questHelpDataCategoriesBold[category] != True:
                                categoryStatus = questHelpDataLastCategoryMemory[category]
                                if categoryStatus == -1:
                                    categoryStyle = "questhelp_category_failed"
                                if categoryStatus == 1:
                                    categoryStyle = "questhelp_category_completed"
                                if categoryStatus == 0:
                                    categoryStyle = "questhelp_category_active"
                                if questHelpCurrentCategory == category:
                                    categoryStyle = categoryStyle + "_selected"
                        if categoryStyle != False:
                            textbutton t__(category) style categoryStyle:
                                xsize getRes(350)
                                xpadding 10
                                top_padding 10
                                bottom_padding 7
                                action [
                                    Return(["category_click", category])
                                ]

        viewport id "questhelp_viewport_events":
#            xpos getRes(377+10)
#            ypos getRes(107+10)
            xpos getRes(381)
            ypos getRes(85)
            draggable True
            scrollbars "vertical"
            xmaximum getRes(617-15)
            ymaximum getRes(852-85)
            mousewheel True
            pagekeys True
#            unscrollable "hide"

#            child_size (getRes(852-85), viewportHeight)
            frame:
                background None
                padding (getRes(10), getRes(10))
                vbox:
                    #description
                    python:
                        descriptionText = ""
                        for idx in range(0, len(questHelpDataCategoriesDescriptions)):
                            if questHelpDataCategoriesDescriptionsData.has_key(questHelpDataCategoriesDescriptions[idx][0]) and questHelpDataCategoriesDescriptions[idx][1] == questHelpCurrentCategory:
                                if len(descriptionText) > 0:
                                    descriptionText = descriptionText + "\n\n"
                                descriptionText = descriptionText + t__(questHelpDataCategoriesDescriptions[idx][2])


                    if len(descriptionText) > 0:
                        text descriptionText style "questhelp_category_description"
                        #рисуем разделитель
                        null height getRes(20)
#                        vbox:
#                            add "gui/frame6_delimeter.png"
    #                            ysize 5
                        frame:
                            left_margin getRes(20)
                            xysize(getRes(617 - 15 - 60), 1)
                            background "#c0c0c0"
                        null height getRes(20)

                    if questHelpData.has_key(questHelpCurrentCategory) == True:
                        # выводим квесты
                        # сначала завершенные и проваленные
                        for idx in range(0, len(questHelpData[questHelpCurrentCategory])):
                            $ questData = questHelpData[questHelpCurrentCategory][idx]
                            if questData[1] == 1 or questData[1] == -1:
                                if questHelpDataLastQuestsBold.has_key(questData[0]) == False or questHelpDataLastQuestsBold[questData[0]] == False: # если квест не жирный (не только что)
                                    python:
                                        questStyle = False
                                        questTextPrefix = ""
                                        if questData[1] == 1:
                                            questStyle = "questhelp_quest_completed"
                                            questTextPrefix = "{image=images/Icons/questhelp/checkmark_completed.png}  "
                                        if questData[1] == -1:
                                            questStyle = "questhelp_quest_failed"
                                            questTextPrefix = "{image=images/Icons/questhelp/checkmark_failed.png}  "
                                        if questData[0] == questHelpCurrentQuest:
                                            questStyle = questStyle + "_selected"
                                    if questStyle != False:
                                        # выводим
                                        textbutton questTextPrefix + t__(questHelpDataQuests[questData[0]][1]) style questStyle:
                                            xsize getRes(617 - 15)
                                            xpadding 10
                                            top_padding 20
                                            bottom_padding 0
                                            action [
                                                Return(["quest_click", questData[0]])
                                            ]

                        # Затем жирные или активные

                        for idx in range(0, len(questHelpData[questHelpCurrentCategory])):
                            $ questData = questHelpData[questHelpCurrentCategory][idx]
                            if questData[1] == 0 or (questHelpDataLastQuestsBold.has_key(questData[0]) == True and questHelpDataLastQuestsBold[questData[0]] == True): # если квест не жирный (не только что)
                                python:
                                    questStyle = False
                                    questTextPrefix = ""
                                    if questData[1] == 1:
                                        questStyle = "questhelp_quest_completed"
                                        questTextPrefix = "{image=images/Icons/questhelp/checkmark_completed.png}  "
                                    if questData[1] == -1:
                                        questStyle = "questhelp_quest_failed"
                                        questTextPrefix = "{image=images/Icons/questhelp/checkmark_failed.png}  "
                                    if questData[1] == 0:
                                        questTextPrefix = "{image=images/Icons/questhelp/checkmark_active.png}  "
                                        questStyle = "questhelp_quest_active"

                                    if questData[0] == questHelpCurrentQuest:
                                        questStyle = questStyle + "_selected"
                                    else:
                                        if questHelpDataLastQuestsBold.has_key(questData[0]) == True and questHelpDataLastQuestsBold[questData[0]] == True: # если жирный
                                            questStyle = questStyle + "_bold"
                                if questStyle != False:
                                    # выводим
                                    textbutton questTextPrefix + t__(questHelpDataQuests[questData[0]][1]) style questStyle:
                                        xsize getRes(617 - 15 - 20)
                                        xpadding 10
                                        top_margin 20
                                        top_padding 5
                                        bottom_padding 7
                                        action [
                                            Return(["quest_click", questData[0]])
                                        ]


#        vbar value YScrollValue("questhelp_viewport_events"):
#            xpos getRes(381 + 617 - 15)
#            ypos getRes(85)
#            xsize getRes(15)
#            ysize getRes(852-85)
#            ymaximum getRes(852-85)
#            unscrollable "hide"

#            top_bar "images/Icons/vertical_hover2_bar" + res.suffix + ".png"
#            bottom_bar "images/Icons/vertical_hover2_thumb" + res.suffix + ".png"
#            base_bar "images/Icons/vertical_hover2_bar" + res.suffix + ".png"
#            thumb "images/Icons/vertical_hover2_thumb" + res.suffix + ".png"
#                thumb_shadow img_name

        viewport id "questhelp_viewport_event_descriptions":
#            xpos getRes(377+10)
#            ypos getRes(107+10)
            xpos getRes(381 + 617)
            ypos getRes(85)
            draggable True
#            scrollbars "vertical"
            xmaximum getRes(617-15)
            ymaximum getRes(852-85)
            mousewheel True
            pagekeys True
#            child_size (getRes(852-85), viewportHeight)
            frame:
                background None
                padding (getRes(10), getRes(10))
                vbox:
                    if questHelpCurrentQuest != False and questHelpDataQuests.has_key(questHelpCurrentQuest) and len(questHelpDataQuests[questHelpCurrentQuest]) > 2:
                        text t__(questHelpDataQuests[questHelpCurrentQuest][2]) style "questhelp_quest_description_text"
