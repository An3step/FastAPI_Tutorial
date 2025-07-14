l = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# l = [1, 1, 2, 3]

k = len(l)

i = 0
j = 1

isTh = False


while j < len(l):
    if l[j] == l[i]:
        if isTh:
            k -= 1
        else:
            i += 1
            isTh = True
    else:
        isTh = False
        l[i + 1] = l[j]
        i += 1
    i += 1
    j += 1

print(f'{k=}', l)