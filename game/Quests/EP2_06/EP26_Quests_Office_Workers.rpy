label ep26_quests_office_workers1:
    # Клик на работников
    if obj_name == "Worker1":
        if act=="l":
            call worker1_look()
            call refresh_scene_fade()
        if act=="t":
            call worker1_dialogue_workplace()
            call refresh_scene_fade()
    if obj_name == "Worker2":
        if act=="l":
            call worker2_look()
            call refresh_scene_fade()
        if act=="t":
            call worker2_dialogue_workplace()
            call refresh_scene_fade()
    if obj_name == "Worker3":
        if act=="l":
            call worker3_look()
            call refresh_scene_fade()
        if act=="t":
            call worker3_dialogue_workplace()
            call refresh_scene_fade()
    if obj_name == "Worker4":
        if act=="l":
            call worker4_look()
            call refresh_scene_fade()
        if act=="t":
            call worker4_dialogue_workplace()
            call refresh_scene_fade()
    if obj_name == "Worker5":
        if act=="l":
            call worker5_look()
            call refresh_scene_fade()
        if act=="t":
            call worker5_dialogue_workplace()
            call refresh_scene_fade()
    if obj_name == "Worker6":
        if act=="l":
            call worker6_look()
            call refresh_scene_fade()
        if act=="t":
            call worker6_dialogue_workplace()
            call refresh_scene_fade()
    if obj_name == "Worker7":
        if act=="l":
            call worker7_look()
            call refresh_scene_fade()
        if act=="t":
            call worker7_dialogue_workplace()
            call refresh_scene_fade()

    return
