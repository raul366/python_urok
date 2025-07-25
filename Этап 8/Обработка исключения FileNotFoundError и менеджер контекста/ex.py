try:
    f = open("abc.txt")
    r = f.read(1)
    f.close()
except:
    print("File Not Found")