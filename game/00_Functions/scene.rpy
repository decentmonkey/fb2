init python:
    def store_scene(scene_name): #сохранить сцену в переменную
        stored_scene = {}
        if scenes_data["objects"].has_key(scene_name) == True:
            stored_scene["objects"] = copy.deepcopy(scenes_data["objects"][scene_name])
        if scenes_data["hooks"].has_key(scene_name) == True:
            stored_scene["hooks"] = copy.deepcopy(scenes_data["hooks"][scene_name])
        if scenes_data["substs"].has_key(scene_name) == True:
            stored_scene["substs"] = copy.deepcopy(scenes_data["substs"][scene_name])
        if scenes_data["autorun"].has_key(scene_name) == True:
            stored_scene["autorun"] = copy.deepcopy(scenes_data["autorun"][scene_name])

        return stored_scene

    def restore_scene(scene_name, stored_scene): #восстановить сцену из переменной
        if stored_scene.has_key("objects") == True:
            scenes_data["objects"][scene_name] = stored_scene["objects"]
        if stored_scene.has_key("hooks") == True:
            scenes_data["hooks"][scene_name] = stored_scene["hooks"]
        if stored_scene.has_key("substs") == True:
            scenes_data["substs"][scene_name] = stored_scene["substs"]
        if stored_scene.has_key("autorun") == True:
            scenes_data["autorun"][scene_name] = stored_scene["autorun"]

        return stored_scene
