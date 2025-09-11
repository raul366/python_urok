a = list(map(str, input().split()))
notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a = list(sorted(a, key = lambda x: notes.index(x)))
print(*a)