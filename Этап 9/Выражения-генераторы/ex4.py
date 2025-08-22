a, b = map(int, input().split())

gen = (round(0.5 * pow(a + i*0.01, 2) - 2.0, 2) 
       for i in range(int((b - a) / 0.01) + 2))

result = []
for _ in range(20):
    result.append(next(gen))
print(*result)