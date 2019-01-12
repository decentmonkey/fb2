default bettyLocation = "none"

default bettyPantiesLog = []
default bettyPantiesCurrent = 3
default bettyPantiesCurrentList = []
define bettyPantiesList = [1, 2, 3, 4, 5]

default bettyTouchedFredDick = False
default bettyFredLandrySexPlanned = False

label bettyInteract1:
    if act == "l":
        mt "Это Бетти..."
        "Редкая сучка!"
        "Она следит за мной, за каждым моим шагом."
        "Мне надо быть осторожнее с ней, пока..."
        if monicaBettyPanties == True:
            mt "К тому же на мне одеты ее трусики... Ужас!!!"
        "Она еще поплатится за свое ко мне отношение!"

    if act == "t":
        if bettyLocation == "Bedroom1":
            if day_time == "day":
                call bettyDialogue1() from _call_bettyDialogue1
                return
    return

label bettyGetTodayPanties:
    if len(bettyPantiesCurrentList) > 0:
        $ bettyPantiesCurrent = bettyPantiesCurrentList.pop(0)
        $ bettyPantiesLog.insert(0, bettyPantiesCurrent)
        return
    python:
        bettyPantiesCurrentList = copy.deepcopy(bettyPantiesList)
        print bettyPantiesCurrentList
        idx = bettyPantiesCurrentList.index(bettyPantiesCurrent)
        bettyPantiesCurrentList.pop(idx)
        print bettyPantiesCurrentList
        shuffle(bettyPantiesCurrentList)
        print bettyPantiesCurrentList
        bettyPantiesCurrentList.append(bettyPantiesCurrent)
        print bettyPantiesCurrentList

    call bettyGetTodayPanties() from _call_bettyGetTodayPanties
    return

label bettyProgressLevelUp1:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        if ep22_started == False:
            $ char_data["enabled"] = False
            $ char_data["caption_diabled"] = _("Ожидание дальнейшего прогресса сюжета игры...")
        $ move_object("Betty", "floor2")
        $ add_hook("Betty_Life_day", "Betty_Life_day1_lower", scene="global", priority=50, label="betty_level2_onetime")
    return
