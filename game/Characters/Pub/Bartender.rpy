label bartenderProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ char_data["caption"] = _("Бармен в Shiny Hole. Лапает меня, пока Эшли не видит.")
        pass
    if char_data["level"] == 3:
        $ progress_character_name = _("Джо")
        help "Прогресс [progress_character_name] максимален, ждите следующих обновлений игры!"
        $ char_data["enabled"] = False
        $ char_data["caption_diabled"] = _("Work in progress...")

    return
