label ep24_quests_betty1:
    # Бетти ловит Монику, чтобы сказать что теперь Моника может проверять ее трусики
    if cloth != "Governess":
        return
    $ remove_hook(label="bardie_catch1")
    m "betty catch1"
    return
