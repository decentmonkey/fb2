default new_owner = False
default owners_data = {"Monica":{}, "Betty":{"money":150, "objectives":[], "inventory":[]}, "Bardie":{"money":15, "objectives":[], "inventory":[]}, "Driver":{}, "Melanie":{}, "Secretary":{}, "Julia":{}, "Steve":{}}

label change_owner(in_new_owner):
    $ new_owner = in_new_owner
    call process_hook("change_owner", "global")
    $ owner = new_owner
    return
