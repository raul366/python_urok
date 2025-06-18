things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

sorted_things = sorted(things.items(), key=lambda x: x[1], reverse=True)

N = int(input()) * 1000

for i in range(len(sorted_things)):
    if N - sorted_things[i][1] >= 0:
        N -= sorted_things[i][1]
        print(sorted_things[i][0], end = " ")