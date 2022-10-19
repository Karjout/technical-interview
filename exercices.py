
# exerice 1
nomber_n = int(input("donnez un nombre: "))
counter = 0
for i in range(1, nomber_n+1):
    counter = counter + i
print("La somme  de la suite 1 + 2 + 3 +....+n  est ", counter)


# exercie 2
def isFoundChar(str_a, char_a):
    counter = 0
    for x in str_a:
        if x == char_a:
            counter += 1
    if counter >= 2:
        return True


def list_all_char(str_a):
    res = []
    for i in str_a:
        if isFoundChar(str_a, i) and i not in res:
            res.append(i)
    return res
