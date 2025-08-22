import random
from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
random.seed(1)

# здесь продолжайте программу
def random_password(length):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    a = []
    for j in range(5):
        for i in range(length):
            a.append(chars[random.randint(0, len(chars) - 1)])
        a = "". join(a)
        yield a
        a = []


N = int(input())
x = random_password(N)

for i in x:
    print(i)