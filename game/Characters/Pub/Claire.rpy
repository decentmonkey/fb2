label claireProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ char_data["caption"] = _("Клэр относится к Монике с симпатией. Она ее друг.")
    if char_data["level"] == 3:
        $ char_data["caption"] = _("Клэр знает имя Моники и помогает ей. Она ее друг.")
    return
