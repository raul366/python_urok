def get_biggest_city(*a):
    l = 0
    j = 0
    for i in range(len(a)):
        if len(a[i]) > l:
            l = len(a[i])
            j = i
    return a[j]