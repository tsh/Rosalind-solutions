with open('input.txt') as f:
    f.readline()
    arr1 = list(map(int, f.readline().split()))
    f.readline()
    arr2 = list(map(int, f.readline().split()))

i,j = 0, 0
res = []
while True:
    if i > len(arr1)-1 or j > len(arr2)-1:
        res.extend(arr2[j:])
        res.extend(arr1[i:])
        break
    elif arr1[i] < arr2[j]:
        res.append(arr1[i])
        i += 1
    else:
        res.append(arr2[j])
        j += 1
print(' '.join(map(str, res)))