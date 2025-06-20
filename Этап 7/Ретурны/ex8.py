def proiz(min, max):
    return min * max


digs = list(map(int, input().split()))
print(proiz(min(digs), max(digs)))