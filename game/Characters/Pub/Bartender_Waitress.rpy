label bartenderWaitressProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ progress_character_name = _("Эшли")
        help "Прогресс [progress_character_name] максимален, ждите следующих обновлений игры!"
        $ char_data["enabled"] = False
        $ char_data["caption_diabled"] = _("Work in progress...")
    return
