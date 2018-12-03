init python:
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
