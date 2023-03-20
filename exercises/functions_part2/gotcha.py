# def add_thrice(val, lst=[]):
#     lst.append(val)
#     lst.append(val)
#     lst.append(val)
#     return lst

def add_thrice(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst
