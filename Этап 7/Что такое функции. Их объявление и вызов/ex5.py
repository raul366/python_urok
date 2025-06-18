def prov_pocht(a: str):
    t = "@.zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP1234567890_"
    if "@" in a and "." in a:
        a = list(a)
        for i in a:
            if i not in t:
                print("НЕТ")
                break
        else:
            print("ДА")
    else:
        print("НЕТ")


a = input()
prov_pocht(a)