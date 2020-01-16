default ep210_quests_stage = 0
default ep210_picture_marked = False
default ep210_picture_marked_day = 0
default ep210_picture_was_marked = False
default ep210_picture_marked_claire_comment = False
default ep210_picture_marked_molly_comment = False
default ep29_quests_monica_molly_fine = False # Моника отдает все чаевые, пока Молли ее не простит
default ep29_quests_monica_molly_was_fine = False
default ep29_quests_claire_dance_planned = False
default ep29_quests_molly_fall_panties_planned0 = False # Запланировано падение трусиков
default ep29_quests_molly_fall_panties_planned = False # Запланировано падение трусиков
default ep29_quests_molly_fall_panties_completed = False
default ep29_quests_dancing_with_claire_active = False
default ep29_quests_dancing_with_claire_last_day = 0

label ep210_quests_pub1:
    if ep210_quests_stage == 0 and get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") != False: # Если есть Молли
        $ add_hook("before_open", "ep210_quests_pub1_molly", scene="pub_makeuproom", once=True)
        $ ep210_quests_stage = -1
    if ep210_quests_stage == 1 and get_active_objects("Pub_StripteaseGirl2", scene="pub_makeuproom") != False: # Если есть Клэр
        $ add_hook("Pub_StripteaseGirl2", "ep210_quests_pub2_claire", scene="pub_makeuproom")
        $ ep210_quests_stage = -1
    if ep210_quests_stage == 2:
        $ add_hook("before_open", "ep210_quests_pub3_molly", scene="pub_makeuproom", once=True)
        $ add_hook("exit_scene", "ep210_quests_pub3_molly2", scene="pub_makeuproom", label="ep210_quests_pub3_molly2")
        $ ep210_quests_stage = -1
    if ep210_quests_stage == 3:
        $ add_hook("before_open", "ep210_quests_pub7_molly", scene="pub_makeuproom", once=True)
        $ ep210_quests_stage = -1

    if ep210_quests_stage == 4 and ep210_picture_was_marked == True:
        if game.extra == True:
            $ ep29_quests_molly_fall_panties_planned0 = True
    if ep29_quests_molly_fall_panties_planned0 == True and get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") != False:
        $ ep29_quests_molly_fall_panties_planned = True
        $ add_hook("Pub_StripteaseGirl2", "ep210_quests_pub8_claire_panties", scene="pub_makeuproom", label="ep210_quests_pub8_claire_panties")
        $ add_hook("exit_scene", "ep210_quests_pub8_ashley_panties", scene="pub_makeuproom", label="ep210_quests_pub8_ashley_panties")
        $ ep210_quests_stage = 5
    return


label ep210_quests_pub1_molly: # Диалог с Молли
    call ep210_dialogues4_dance_strip_1()
    $ add_char_progress("Pub_StripteaseGirl1", 25, "molly_offend2")
    call refresh_scene_fade()
    $ pub_makeuproom_monica_suffix = 2
    $ ep210_quests_stage = 1
    return

label ep210_quests_pub2_claire: # Разговор с Клэр
    if act=="l":
        return
    $ remove_hook()
    call ep210_dialogues4_dance_strip_2()
    $ add_char_progress("Pub_StripteaseGirl2", 25, "claire_conversation1")
    call refresh_scene_fade()
    $ ep210_quests_stage = 2
    return False

label ep210_quests_pub3_molly: # Диалог с Молли
    call ep210_dialogues4_dance_strip_3()
    $ add_char_progress("Pub_StripteaseGirl1", 25, "molly_offend3")
    call refresh_scene_fade()
    $ pub_makeuproom_monica_suffix = 2
    $ ep210_quests_stage = -1
    return


label ep210_quests_pub3_molly2: # Диалог с Молли после выступления
    if monicaDancedLastDay == day and cloth_type == "Whore":
        $ remove_hook()
        call ep210_dialogues4_dance_strip_4()
        $ add_char_progress("Pub_StripteaseGirl1", 25, "molly_offend4")
        $ questLog(66, True)
        $ add_hook("enter_scene", "ep210_quests_pub4_molly_photo1", scene="pub_makeuproom", label="ep210_quests_pub4_molly_photo1")
        $ ep29_quests_only_claire = True
        $ ep29_quests_monica_molly_fine = True
        $ add_hook("Pub_StripteaseGirl2", "ep210_quests_pub4_claire", scene="pub_makeuproom", label="ep210_quests_pub4_claire")
    return

label ep210_quests_pub4_molly_photo1: # Комментарий по поводу фото Молли
    if get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False and get_active_objects("Pub_StripteaseGirl2", scene="pub_makeuproom") == False: # Если никого нет
        $ remove_hook(label="ep210_quests_pub4_molly_photo1")
        call ep210_dialogues4_dance_strip_5_0()
        $ add_hook("Picture", "ep210_quests_pub4_molly_photo2", scene="pub_makeuproom", label="ep210_quests_pub4_molly_photo2")
        call refresh_scene_fade()
    return


label ep210_quests_pub4_molly_photo2: # Действие с фото Молли
    img 22718
    with fadelong
    mt "Никчемная!"
    mt "Бесполезная!"
    mt "Сучка!!!"
    mt "!!!"
#    if victoria_drawn_melanie_photo1 == True: # Если Моника видела как Виктория рисует на портрете Мелани
    menu:
        "Сделать пакость...":
            if get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") != False or get_active_objects("Pub_StripteaseGirl2", scene="pub_makeuproom") != False:
                call ep210_dialogues4_dance_strip_5_1()
                return False
            if cloth != "Whore":
                $ cloth = "Whore"
                $ cloth_type = "Whore"
                sound snd_fabric1
                img black_screen
                with Dissolve(0.5)

            call ep210_dialogues4_dance_strip_5()
            if _return == False:
                return False
            $ remove_hook(label="ep210_quests_pub4_molly_photo2")
            $ set_var("Picture", img="Pub_MakeupRoom_Picture_Marked", scene="pub_makeuproom")
            $ add_hook("Picture", "ep210_dialogues4_dance_strip_5_2", scene="pub_makeuproom", label="ep210_dialogues4_dance_strip_5_2")
            $ add_hook("before_open", "ep210_quests_pub4_molly_photo3", scene="pub_makeuproom", priority = 1000)

            $ ep210_picture_marked = True
            $ ep210_picture_was_marked = True
            $ ep210_picture_marked_day = day
            $ pub_makeuproom_monica_suffix = 2
            $ add_char_progress("Pub_StripteaseGirl1", 25, "molly_offend5")
            call refresh_scene_fade()
            return False
        "Уйти.":
            pass
    return False

label ep210_quests_pub4_molly_photo3: # Чекаем что надо стереть надпись на след.день
    if ep210_picture_marked_day != day and ep210_picture_marked == True:
        call pub_makeuproom_init2()
#        $ set_var("Picture", img=False, scene="pub_makeuproom")
        $ ep210_picture_marked = False
        $ remove_hook()
    return

label ep210_quests_pub4_claire:
    if act=="l":
        return
    $ remove_hook()
    call ep210_dialogues4_dance_strip_6()
    $ add_char_progress("Pub_StripteaseGirl2", 25, "claire_help1")

    $ ep29_quests_only_claire = False
    $ add_hook("Pub_StripteaseGirl2", "ep210_quests_pub5_claire", scene="pub_makeuproom", label="claire_dance_dialogue1")
    $ add_hook("Pub_StripteaseGirl1", "ep210_quests_pub5_molly", scene="pub_makeuproom", label="claire_dance_dialogue1")
    call refresh_scene_fade()
    return False


label ep210_quests_pub5_claire:
    if act=="l":
        return
    call ep210_dialogues4_dance_strip_7()
    if _return == False:
        call refresh_scene_fade()
        return False
    call ep210_dialogues4_dance_strip_8()
    if _return == False:
        call refresh_scene_fade()
        return False
    $ remove_hook(label="claire_dance_dialogue1")
    $ ep29_quests_claire_dance_planned = True
    $ stage_shoots_total_amount_cur = stage_shoots_total_amount_default + stage_shoots_total_amount_claire
    $ add_hook("Pub_StripteaseGirl2", "dialogue_5_dance_strip_9b", scene="pub_makeuproom", label="remove_after_dance")
    $ pub_makeuproom_claire_suffix = "Look1"
    $ cloth = "StripOutfit1"
    $ cloth_type = "StripOutfit"
    $ add_hook("exit_scene", "ep210_quests_pub6_ashley", scene="pub_makeuproom", label="ep210_quests_pub6_ashley")
    $ pubMakeupRoomSkipMusicOnce = True
    call refresh_scene_fade()
    return False

label ep210_quests_pub5_molly:
    if act=="l":
        return
    call ep210_dialogues4_dance_strip_7()
    call refresh_scene_fade()
    return False


label ep210_quests_pub6_ashley: # Эшли встречает Монику после танца с Клэр
    if cloth == "Whore":
        $ remove_hook()
        call ep210_dialogues4_dance_strip_10()
        $ ep29_quests_monica_molly_fine = False
        $ ep29_quests_monica_molly_was_fine = True
        $ monica_shared_tips_with_ashley_last_day = day
        $ ep210_quests_stage = 3
        $ ep29_quests_dancing_with_claire_active = True
        $ add_char_progress("Pub_StripteaseGirl2", 25, "claire_dance1")
        $ questLog(66, False)
    return

label ep210_quests_pub7_molly:
    call ep210_dialogues4_dance_strip_11()
    $ pub_makeuproom_monica_suffix = 2
    $ ep210_quests_stage = 4
    return

label ep210_quests_pub8_ashley_panties: # Молли смеется Монике чтобы она танцевала без трусиков
    if cloth == "Whore" and ep29_quests_molly_fall_panties_completed == True:
        $ remove_hook()
        call ep210_dialogues4_dance_strip_14()
    return

label ep210_quests_pub8_claire_panties:
    if ep29_quests_molly_fall_panties_completed == False:
        return
    if act=="l":
        return
    $ remove_hook()
    call ep210_dialogues4_dance_strip_15()
    call refresh_scene_fade()
    return False

label ep210_quests_pub9_claire_offer_check:
    if ep29_quests_dancing_with_claire_active == True:
        $ add_hook("Pub_StripteaseGirl2", "ep210_quests_pub9_claire_offer_dance", scene="pub_makeuproom", label="remove_after_dance")
    return
label ep210_quests_pub9_claire_offer_dance: # Моника предлагает Клэр потанцевать с ней
    if act=="l":
        return
    call ep210_dialogues4_dance_strip_17()
    if _return == False:
        return False
    $ remove_hook()
    $ ep29_quests_claire_dance_planned = True
    $ add_char_progress("Pub_StripteaseGirl2", 25, "claire_dance1")
    return False





#
