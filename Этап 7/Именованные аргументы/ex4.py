def obertka(a, tag = "h1", up = True):
    return f"<{tag.upper() if up else tag.lower()}>{a}</{tag.upper() if up else tag.lower()}>"


a = input()
print(obertka(a, "div"))
print(obertka(a, "div", False))