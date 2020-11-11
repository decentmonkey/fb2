default questLogJustUpdated = False
default questLogUpdatedDay = 0
default questHelpJustUpdated = False
default questHelpUpdatedDay = 0
default questHelpData = []

init python:
    def add_objective(objective_id, objective_name, objective_color="#ffffff", objective_priority=0):
        global objectives_list
        for objective in objectives_list:
            if objective[0] == objective_id:
                return
        objective = [objective_id, objective_name, objective_color, objective_priority]
        if len(objectives_list) > 0:
            for idx in range(0, len(objectives_list)):
                if objectives_list[idx][3] >= objective_priority:
                    objectives_list.insert(idx, objective)
                    return;
        objectives_list.append(objective)


    def remove_objective(objective_id):
        global objectives_list
        for idx in range(len(objectives_list)-1, -1, -1):
            if objectives_list[idx][0] == objective_id:
                objectives_list.pop(idx)
#                renpy.pause()
#                idx = 0
#        print objectives_list

    def questLog(questLogIdx, status):
        global questLogDataEnabled, questLogLinesUpdated, questLogJustUpdated, questLogUpdatedDay, day
        if status == True and (questLogDataEnabled.has_key(str(questLogIdx)) == False or questLogDataEnabled[str(questLogIdx)] != True):
            if day > 0:
                notif(t__("Журнал обновлен"))
            questLogLinesUpdated.append(str(questLogIdx))
            questLogJustUpdated = True
            questLogUpdatedDay = day
        questLogDataEnabled[str(questLogIdx)] = status
#        for idx in range(0, len(questLogData)):
#            if questLogData[idx][0] == questLogIdx:
#                questLogData[idx][2] = status
#                break
        return

    def questHelp(*args): # questHelp(questHelpName, True/False) #True - пройден, False - провален, без второго аргумента - просто новый квест (желтенький)
        questHelpName = args[0]
        if len(args) > 1:
            status = 1 if args[1] == True else -1
        else:
            status = 0
        for idx in range(0, len(questHelpData)):
            if questHelpData[idx][0] == questHelpName:
                questHelpData[idx][1] = status
                return
        questHelpData.append([questHelpName, status])

        return
