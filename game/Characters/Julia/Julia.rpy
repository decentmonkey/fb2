default monicaOfficeWorkOffendedCount1 = 0 # Кол-во раз Моника заставляла Юлию работать допоздна
default monicaOfficeWorkKindCount1 = 0 # Кол-во раз Моника жалела Юлию и не заставляла много работать
default juliaOfficeOffended1 = False # Моника заставляла Юлию работать допоздна
default juliaOfficeOffended2 = False # Моника заставляла Юлию собирать отчеты вместо себя и ругалась при этом


label juliaProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ char_data["caption"] = _("Юлия стесняется комплиментов Моники и боится ее.")
    if char_data["level"] == 3:
        $ char_data["enabled"] = False
#    $ char_data["caption_diabled"] = _("Ожидание дальнейшего прогресса сюжета игры...")
#    $ char_data["show_caption_diabled"] = True
#    if char_data["level"] == 4:
    return
