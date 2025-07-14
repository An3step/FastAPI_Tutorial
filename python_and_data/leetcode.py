l = [0,1,2,2,3,0,4,2]

val = 2

k = len(l)

i, j = 0, k

while i < j:
    if l[i] == val:
        k -= 1
        j -= 1
        while i < j:
            if l[j] == val:
                k -= 1
                j -= 1
            else:
                l[i], l[j] = l[j], l[i]
                break
        else:
            break
    i += 1



print(f'{k=}',l)