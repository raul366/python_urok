from string import ascii_lowercase, ascii_uppercase
import random

random.seed(1)

def random_mail(max_size):
    chars = ascii_lowercase + ascii_uppercase
    a = []
    for i in range(5):
        for j in range(max_size):
            a.append(chars[random.randint(0, len(chars) - 1)])
        a = "".join(a) + "@mail.ru"
        yield a
        a = []


N = int(input())
b = random_mail(N)

for i in b:
    print(i)