init python:
    def get_bitchmeter_description():
        global bitchmeterValue, maxBitchness
        bitchmeter_captions = ["Shy Girl", "Decent Girl", "Casual Girl", "Hot-Tempered", "Bitch", "Complete Bitch", "Bitch from the Hell"]

#        if bitchmeterValue < float(maxBitchness) / 100 * 20:
        if bitchmeterValue <= 153:
            return bitchmeter_captions[0]
        if bitchmeterValue <= float(maxBitchness) / 100 * 49:
            return bitchmeter_captions[1]
        if bitchmeterValue <= float(maxBitchness) / 100 * 51:
            return bitchmeter_captions[2]
        if bitchmeterValue < float(maxBitchness) / 100 * 60:
            return bitchmeter_captions[3]
        if bitchmeterValue < float(maxBitchness) / 100 * 80:
            return bitchmeter_captions[4]
        if bitchmeterValue < float(maxBitchness) / 100 * 100:
            return bitchmeter_captions[5]
        if bitchmeterValue >= maxBitchness:
            return bitchmeter_captions[6]


    def changeDayTime(dayTime):
        global day_time, day_suffix, day, week_day, scene_name
        if dayTime == day_time:
            return
        if dayTime == "evening":
            day_time = "evening"
            day_suffix = "_Evening"
            renpy.call("process_hooks", "change_time_evening", "global")
            renpy.call("process_hooks", "day_" + str(week_day) + "_evening", "global_week_day")
            renpy.call("process_hooks", "day_" + str(day) + "_evening", "global_day")
            return
        if dayTime == "day":
            day_time = "day"
            day_suffix = ""
            day = day + 1
            week_day = (day)%7 + 1
            renpy.call("process_hooks", "change_time_day", "global")
            renpy.call("process_hooks", "day_" + str(week_day), "global_week_day")
            renpy.call("process_hooks", "day_" + str(day), "global_day")
            return
        return

    def getNextDayByWeekDay(target_week_day): #найти дату для следующего дня недели
        if target_week_day == week_day:
            return day + 7
        if target_week_day < week_day:
            return day + 7 - week_day + target_week_day
        if target_week_day > week_day:
            return day + target_week_day - week_day
        return

    def get_scene_label(scene_label):
        global sceneStages
        for idx in reversed(range(0, len(sceneStages))):
            if renpy.has_label(scene_label + sceneStages[idx]):
                return scene_label + sceneStages[idx]
        return scene_label
