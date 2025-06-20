def obertka(a, tag = "h1"):
    return f"<{tag}>{a}</{tag}>"


a = input()
print(obertka(a))
print(obertka(a, "div"))