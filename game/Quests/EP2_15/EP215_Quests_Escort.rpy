label ep215_quests_esort_change_name:
    call ep215_dialogues3_escort_23_change_name()
    $ autorun_to_object("ep215_dialogues3_escort_23_change_name_b")
    call refresh_scene_fade()
    return
