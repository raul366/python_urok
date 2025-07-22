def get_path(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return get_path(N - 1) + get_path(N - 2)

N = int(input())
print(get_path(N))