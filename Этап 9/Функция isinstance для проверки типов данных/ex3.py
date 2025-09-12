def get_list_dig(lst):
    return list(filter(lambda x: type(x) is int or type(x) is float, lst))