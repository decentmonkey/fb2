default ep211_quests_load_init_flag = False

label ep211_quests_load_init:
    if ep211_quests_load_init_flag == False:
        # check Monica pub name, костыль для испорченных сейвов
        if monicaWorkingAsDishwasher == True and monica_pub_name == False:
            $ monica_pub_name = __("Мэрилин")

        if ep22_quests_monica_presentation_completed == True and ep22_quests_monica_presentation_completed_day == -1:
            $ ep22_quests_monica_presentation_completed_day = day

        if char_info.has_key("Julia") and char_info["Julia"]["level"] == 4:
            $ char_info["Julia"]["enabled"] = True
            $ char_info["Julia"]["caption"] = _("Юлия приняла ухаживания Моники, но еще побаивается ее.")


        $ ep211_quests_load_init_flag = True
    return
