default monicaShowedBoobsToVictoriaCamera = False
default monicaShowedAssToDickAndVictoria = False

default monicaEarnedWeeklyMoney = False # Моника заработала деньги для Виктории в эту неделю (поднимается после фотосессии)
default monicaWeeklyMoneySpent = False # Виктория потратила деньги на шоппинг
default monicaVictoriaPunishmentPlanned = False # Монику ожидает наказание у Виктории

label dickSecretaryProgressLevelUp:
    if char_data["level"] == 2:
        $ char_data["enabled"] = False
        $ char_data["caption_diabled"] = _("Work in progress...")

    return
