def get_sort(d):
    a = dict(sorted(d.items(), reverse = True))
    a = list(a.values())
    return a