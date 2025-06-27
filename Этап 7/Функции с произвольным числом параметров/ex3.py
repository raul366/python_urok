lst2D = [[0, 1, 0],
         [0, 0, 0],
         [1, 0, 1]]

def verify(lst2D):
    a = True

    for i in range(len(lst2D)):
        for j in range(len(lst2D[i])):
            if is_isolate(lst2D, i, j):
                a = False
                break
        if not a:
            break
    return a

def is_isolate(lst2D, i, j):
    return True if lst2D[i][j] == 1 and ((i - 1 >= 0 and lst2D[i - 1][j] == 1) 
                                         or (j - 1 >= 0 and lst2D[i][j - 1] == 1) 
                                         or (i + 1 <= len(lst2D) - 1 and lst2D[i + 1][j] == 1) 
                                         or (j + 1 <= len(lst2D) - 1 and lst2D[i][j + 1] == 1) 
                                         or (i - 1 >= 0 and j - 1 >= 0 and lst2D[i - 1][j - 1] == 1)
                                         or (i - 1 >= 0 and j + 1 <= len(lst2D) - 1 and lst2D[i - 1][j + 1] == 1)
                                         or (i + 1 <= len(lst2D) - 1 and j - 1 >= 0 and lst2D[i + 1][j - 1] == 1)
                                         or (i + 1 <= len(lst2D) - 1 and j + 1 <= len(lst2D) - 1 and lst2D[i + 1][j + 1] == 1)) else False

print(verify(lst2D))