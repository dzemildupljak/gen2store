def convert_to_dict(obj):
    key = ''
    for i in obj.keys():
        if '_sa_instance_state' in i:
            key = i
    obj.pop(key)
    return obj
