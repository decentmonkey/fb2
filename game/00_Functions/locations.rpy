init python:
    def add_location(loc_name, **kwargs):
        global scenes_data
        if scenes_data["objects"].has_key(loc_name) == False:
            scenes_data["objects"][loc_name] = {"data":{}}
        kwargsArr = {}
        for key1, value1 in kwargs.items():
            scenes_data["objects"][loc_name]["data"][key1] = value1
#        print kwargs
        return
