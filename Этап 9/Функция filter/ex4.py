import string

def mail_sort(a):
    letters_and_digits=string.ascii_lowercase + string.digits
    b = 0
    for i in a:
        if i not in letters_and_digits and i != '@' and i != '.' and i != '_':
            return False
        if i == '@':
            b = 1
        if i == '.' and b == 1:
            return True
        elif i == '.' and b == 0:
            return False

a = input().split()
b = list(filter(lambda x: mail_sort(x), a))
print(*b)