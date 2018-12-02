default hooks_stack = []

init python:

    def add_hook(*args, **kwargs): #устанавливает хук
        obj_name = args[0]
        hook_label = args[1]
        if kwargs.has_key("scene"):
            room_name = kwargs["scene"]
            del kwargs["scene"]
        else:
            room_name = api_scene_name

        hook_data = {"hook_label":hook_label}
        for var1, value1 in kwargs.items():
            hook_data[var1] = value1
        if hook_data.has_key("priority") == False:
            hook_data["priority"] = 100

        if scenes_data["hooks"].has_key(room_name) == False:
            scenes_data["hooks"][room_name] = {}
        if scenes_data["hooks"][room_name].has_key(obj_name) == False:
            scenes_data["hooks"][room_name][obj_name] = []

        remove_hook(obj_name, hook_label, scene=room_name)
        hooks_list = scenes_data["hooks"][room_name][obj_name]
        flag1 = False
        hooks_list.append(hook_data)
        hooks_list = sort_hooks(hooks_list)
        scenes_data["hooks"][room_name][obj_name] = hooks_list
        return

    def remove_hook(*args, **kwargs):
        if kwargs.has_key("scene"):
            if kwargs["scene"] == "all":
                rooms_list = list(scenes_data["hooks"].keys())
            else:
                rooms_list = [kwargs["scene"]]
            del kwargs["scene"]
        else:
            rooms_list = [api_scene_name]

        if len(args) == 2: #obj_name, hook_label
            obj_name = args[0]
            hook_label = args[1]
        if len(args) == 1: #hook_label
            obj_name = False
            hook_label = args[0]
        if len(args) == 0: #() удаление текущего хука, либо удаление хука по фильтру
            if len(kwargs) > 0:
                flag1 = False
                filter_arr = {}
                for var1, value1 in kwargs.items():
                    filter_arr[var1] = value1

                for room_name in rooms_list:
                    for obj_name1 in scenes_data["hooks"][room_name]:
                        flag2 = False
                        hooks_list = scenes_data["hooks"][room_name][obj_name1]

                        for idx in reversed(range(len(hooks_list))):
                            if check_filter(filter_arr, hooks_list[idx]) == True:
                                hooks_list.pop(idx)
                                flag2 = True

                        if flag2 == True:
                            scenes_data["hooks"][room_name][obj_name1] = hooks_list

            else:
                if scenes_data["hooks"].has_key(last_hook_scene) and scenes_data["hooks"][last_hook_scene].has_key(last_hook_obj_name) == True:
                    hooks_list = scenes_data["hooks"][last_hook_scene][last_hook_obj_name]
                    idx = find_hook_by_label(hooks_list, last_hook_label)
                    if idx != -1:
                        hooks_list.pop(idx)
                        scenes_data["hooks"][last_hook_scene][last_hook_obj_name] = hooks_list
                        return True
                    return False
        else:
            flag1 = False
            for room_name in rooms_list:
                if obj_name == False:
                    for obj_name1 in scenes_data["hooks"][room_name]:
                        hooks_list = scenes_data["hooks"][room_name][obj_name1]
                        idx = find_hook_by_label(hooks_list, hook_label)
                        if idx != -1:
                            hooks_list.pop(idx)
                            hooks_list = scenes_data["hooks"][room_name][obj_name1] = hooks_list
                            flag1 = True
                else:
                    if scenes_data["hooks"][room_name].has_key(obj_name) == True:
                        hooks_list = scenes_data["hooks"][room_name][obj_name]
                        idx = find_hook_by_label(hooks_list, hook_label)
                        if idx != -1:
                            hooks_list.pop(idx)
                            hooks_list = scenes_data["hooks"][room_name][obj_name] = hooks_list
                            return True

        return flag1

    def replace_hook(*args, **kwargs):
        if kwargs.has_key("scene"):
            if kwargs["scene"] == "all":
                rooms_list = list(scenes_data["hooks"].keys())
            else:
                rooms_list = [kwargs["scene"]]
            del kwargs["scene"]
        else:
            rooms_list = [api_scene_name]


        filter_arr = {}
        for var1, value1 in kwargs.items():
            filter_arr[var1] = value1

        if len(args) == 3: #obj_name, hook_label, new_hook_label, [scene=scene_name]
            obj_name = args[0]
            hook_label = args[1]
            new_hook_label = args[2]
            flag1 = False
            for room_name in rooms_list:
                if scenes_data["hooks"][room_name].has_key(obj_name) == True:
                    hooks_list = scenes_data["hooks"][room_name][obj_name]
                    idx = find_hook_by_label(hooks_list, hook_label)
                    if idx != -1:
                        hooks_list[idx]["hook_label"] = new_hook_label
                        scenes_data["hooks"][room_name][obj_name] = hooks_list
                        flag1 = True
            return flag1
        if len(args) == 2: #hook_label, new_hook_label, [scene=scene_name]
            hook_label = args[0]
            new_hook_label = args[1]
            flag1 = False
            for room_name in rooms_list:
                for obj_name in scenes_data["hooks"][room_name]:
                    hooks_list = scenes_data["hooks"][room_name][obj_name]
                    idx = find_hook_by_label(hooks_list, hook_label)
                    if idx != -1:
                        if len(filter_arr) == 0 or (len(filter_arr) > 0 and check_filter(filter_arr, hooks_list[idx]) == True):
                            hooks_list[idx]["hook_label"] = new_hook_label
                            scenes_data["hooks"][room_name][obj_name] = hooks_list
                            flag1 = True
            return flag1

        if len(args) == 1: #new_hook_label, [scene=scene_name, filters]
            new_hook_label = args[0]
            if len(filter_arr) > 0:
                for room_name in rooms_list:
                    for obj_name in scenes_data["hooks"][room_name]:
                        hooks_list = scenes_data["hooks"][room_name][obj_name]
                        for idx in range(len(hooks_list)):
                            if check_filter(filter_arr, hooks_list[idx]) == True:
                                hooks_list[idx]["hook_label"] = new_hook_label
                                flag1 = True
                                scenes_data["hooks"][room_name][obj_name] = hooks_list
                return flag1
        return False


    def find_hook_by_label(hooks_list, hook_label):
        for idx in range(len(hooks_list)):
            if hooks_list[idx]["hook_label"] == hook_label:
                return idx

        return -1

    def sort_hooks(hooks_list):
        priority_list = []
        for idx in range(len(hooks_list)):
            if (hooks_list[idx]["priority"] in priority_list) == False:
                priority_list.append(hooks_list[idx]["priority"])
        priority_list.sort()
        hooks_list_sorted = []
        for priority_value in priority_list:
            for idx in range(len(hooks_list)):
                if hooks_list[idx]["priority"] == priority_value:
                    hooks_list_sorted.append(hooks_list[idx])
#        print priority_list
        return hooks_list_sorted

label process_hooks(obj_name, room_name = False, sprites_hover_dummy_screen = False):
    $ _return = None

    if room_name == False:
        $ room_name = api_scene_name

    if scenes_data["hooks"].has_key(room_name) == False or scenes_data["hooks"][room_name].has_key(obj_name) == False:
        return _return

    $ hooks_list = scenes_data["hooks"][room_name][obj_name]
    $ processed_hooks = []
    $ len1 = len(hooks_list)
    if len1 == 0:
        return _return
    $ idx = len1 - 1
    label .hooks_call_loop:
        $ hooks_list = scenes_data["hooks"][room_name][obj_name] #повтор для цикла, восстановление из-за глобальных переменных
        $ hook_data = hooks_list[idx]
        $ label_name = hook_data["hook_label"]
        $ hooks_stack.append([room_name, obj_name, label_name, idx, processed_hooks])
        $ last_hook_scene = room_name
        $ last_hook_obj_name = obj_name
        $ last_hook_label = label_name
        if label_name not in processed_hooks: #если во время вызова стерлись несколько хуков и список сдвинулся. Защита от повторения
            if sprites_hover_dummy_screen == True:
                show screen sprites_hover_dummy_screen()
                $ sprites_hover_dummy_screen = False
            call expression label_name #вызов хука
        $ stack_data = hooks_stack.pop()
        $ label_name = stack_data[2]
        $ idx = stack_data[3]
        $ processed_hooks = stack_data[4]
        $ processed_hooks.append(label_name)
        if len(hooks_stack) > 0:
            $ stack_data = hooks_stack[-1]
        $ last_hook_scene = stack_data[0]
        $ last_hook_obj_name = stack_data[1]
        $ last_hook_label = stack_data[2]
        $ hooks_list = scenes_data["hooks"][room_name][obj_name] #повтор для цикла

        if _return != True: #для продолжения череды выполнения хуков, надо возвращать True
            return _return
        label .hooks_call_loop2:
            $ idx = idx - 1
            if idx >= len(hooks_list):
                jump .hooks_call_loop2
#        $ print idx
        if idx >= 0:
            jump .hooks_call_loop


    return _return
