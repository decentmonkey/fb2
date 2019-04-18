define wardrobeBasementWhoreTakeFlag = False
define wardrobeLastUsedDay = 0

define monicaCatchedByBettyGovernessFirstTime = True

init python:
    def checkGovernessWithoutPantiesActive():
        return True

label wardrobeBasement:
    $ wardrobeLastUsedDay = day
#    img 3368
    img 7119
#    with fadelong
    mt "Что мне одеть?"
    $ menuName = "wardrobe_menu"
    menu:
        "Одежда шлюхи.":
            if monicaBettyPanties == True:
                call ep22_dialogues3_13() from _call_ep22_dialogues3_13
                $ monicaBettyPanties = False
            $ cloth = "Whore"
            $ cloth_type = "Whore"
            sound snd_fabric1
            img black_screen
            with Dissolve(0.5)
#            $ renpy.pause(0.5)

#            $ monicaUnder = "Whore"
            $ autorun_to_object("basement_bedroom1", "wardrobeBasement_dialogue1_whore")

        "Униформа гувернантки.":
            $ cloth = "Governess"
            $ cloth_type = "Governess"
            $ monicaUnder = "Panties"
            sound snd_fabric1
            img black_screen
            with Dissolve(0.5)
#            $ renpy.pause(0.5)
            $ autorun_to_object("basement_bedroom1", "wardrobeBasement_dialogue2_governess")
        "Только трусики.":
            $ cloth = "GovernessPants"
            $ cloth_type = "Nude"
            $ monicaUnder = "Panties"
            sound snd_fabric1
            img black_screen
            with Dissolve(0.5)
#            $ renpy.pause(0.5)
            if monicaBettyPanties == True:
                $ autorun_to_object("basement_bedroom1", "wardrobeBasement_dialogue2_pants_betty")
            else:
                $ autorun_to_object("basement_bedroom1", "wardrobeBasement_dialogue2_pants")
#        "Одеть трусики Юлии." if cloth == "Nude":
#            $ cloth = "GovernessPants"
#            $ cloth_type = "Nude"
#            sound snd_fabric1
#            img black_screen
#            with Dissolve(0.5)
##            $ renpy.pause(0.5)
#            $ autorun_to_object("basement_bedroom1", "wardrobeBasement_dialogue2_pants")

        "Снять все.":
            if monicaBettyPanties == True:
                call ep22_dialogues3_13() from _call_ep22_dialogues3_13_1
                $ monicaBettyPanties = False
            $ cloth = "Nude"
            $ cloth_type = "Nude"
            $ monicaUnder = "Nude"
            sound snd_fabric1
            img black_screen
            with Dissolve(0.5)
#            $ renpy.pause(0.5)
            $ autorun_to_object("wardrobeBasement_dialogue2_nude")

        "":
            pass

    call refresh_scene_fade() from _call_refresh_scene_fade_37
    return

label wardrobeBasement_dialogue1_whore:
    if wardrobeBasementWhoreTakeFlag == True:
        mt "Никогда не представляла себя в этом..."
        "Это просто ужас..."
    else:
        mt "Я не могла подумать, когда увидела эти тряпки в хостеле, что мне придется носить их."
        "Вместо моего красивого платья... Рррррр!!!"
    $ wardrobeBasementWhoreTakeFlag = True
    return
label wardrobeBasement_dialogue2_pants:
    mt "Это не мои трусики..."
    "И мне не комфортно их носить..."
    "Но это лучше чем вообще без них..."
    return
label wardrobeBasement_dialogue2_pants_betty:
    mt "Это трусики Бетти..."
    "Какой ужас..."
    return
label wardrobeBasement_dialogue2_governess:
    mt "Кошмарная униформа."
    "Я никогда себя не представляла в этом..."
    return

label wardrobeBasement_dialogue2_nude:
    mt "Какой ужас..."
    return

label hook_basement_bedroom_check_exit_cloth: #проверка при выходе из спальни по дому
    if target_scene_name != "map" and cloth_type == "Nude" and check_scene_parent(target_scene_name, "basement_hole", recursive=True) == False:
        if wardrobeLastUsedDay != day: #Если сегодня еще не использовали гардероб:
#            $ wardrobeLastUsedDay = day
            $ cloth = "Governess" #Принудительно переодеваем Монику в одежду гувернантки
            $ cloth_type = "Governess"
            return True
        else:
            mt "Я не могу идти в дом в таком виде!"
            "Этот сопляк Барди только этого и ждёт!"
            "И, не представляю что со мной сделает Бетти за это!"
            "Она и так все время называет меня шлюхой..."
            if monicaBitch == True:
                "Сучка..."
            call refresh_scene_fade() from _call_refresh_scene_fade_38
        return False
    return

label hook_basement_bedroom_check_exit_cloth_map: #проверка при выходе из спальни по карте
    if obj_name != "Teleport_House" and map_scene == "House" and (map_source_scene == "basement_bedroom1" or map_source_scene == "basement_bedroom2"):
        if cloth_type == "Nude": #если Моника голая
            if wardrobeLastUsedDay == day: #Если сегодня уже использовали гардероб (одежда надета пользователем)
                mt "Я не могу идти на улицу в таком виде."
                "Я еще не сошла с ума!!!"
                "Мне надо одеться."
                return False
            else: #Гардероб не использовали
#                $ wardrobeLastUsedDay = day
                if monicaBettyPanties == True:
                    call ep22_dialogues3_13() from _call_ep22_dialogues3_13_2
                    $ monicaBettyPanties = False
                $ cloth = "Whore" #Принудительно переодеваем Монику
                $ cloth_type = "Whore"
                return True
        if cloth_type == "Governess": #Бетти запрещает выходить из дома в одежде гувернантки!
            if get_active_objects("Betty", scene="House", recursive=True) != False:
                if monicaCatchedByBettyGovernessFirstTime == False:
                    menu:
                        "Переодеться в одежду шлюхи (другой нет!).":
                            if monicaBettyPanties == True:
                                call ep22_dialogues3_13() from _call_ep22_dialogues3_13_3
                                $ monicaBettyPanties = False
                            $ cloth = "Whore" #Принудительно переодеваем Монику
                            $ cloth_type = "Whore"
                            return True
                        "Не переодеваться.":
                            pass

                $ monicaCatchedByBettyGovernessFirstTime = False
                call monica_goout1_governess_restrict() from _call_monica_goout1_governess_restrict
                call change_scene("street_house_gate", "Fade", False) from _call_change_scene_118
                $ map_source_scene = "street_house_gate"
#               call refresh_scene_fade()
                return False

    if obj_name != "Teleport_House" and map_scene == "House":
        if cloth_type == "Governess": #Моника пытается убежать с улицы в одежде гувернантки (мимо ворот)
            if get_active_objects("Betty", scene="House", recursive=True) != False:
                call monica_goout1_governess_restrict() from _call_monica_goout1_governess_restrict_1
                call change_scene("street_house_gate", "Fade", False) from _call_change_scene_119
                $ map_source_scene = "street_house_gate"
                return False
    return

label hook_basement_bedroom_check_exit_cloth_gates: #проверка на выход Моники из дома в одежде гувернантки через Ворота
    if act != "w":
        return True
    if cloth_type == "Governess":
        if get_active_objects("Betty", scene="House", recursive=True) != False:
            call monica_goout1_governess_restrict() from _call_monica_goout1_governess_restrict_2
            call refresh_scene_fade() from _call_refresh_scene_fade_39
            return False

    return


label wardrobePutGovernessWithoutPanties:
    $ monicaUnder = "Nude"
    $ cloth = "Governess"
    $ cloth_type = "Governess"
    $ monicaBettyPanties = False
    sound snd_fabric1
    img black_screen
    with Dissolve(0.5)
    $ autorun_to_object("basement_bedroom1", "wardrobeBasement_dialogue2_governess")
    return
