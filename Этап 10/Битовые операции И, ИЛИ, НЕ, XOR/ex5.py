a = input()
b = ''

for x in a:
    x = ord(x) ^ 123
    b += chr(x)

print(b)