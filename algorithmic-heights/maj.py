def get_candidate(arr):
    maj_i = 0
    count = 1
    for i in range(len(arr)):
        if arr[maj_i] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_i = i
            count = 1
    return arr[maj_i]

def check_candidate(arr, candidate):
    count = 0
    for el in arr:
        if el == candidate:
            count += 1
        if count > len(arr) / 2:
            return True
    return False

def moore(arr):
    candidate = get_candidate(arr)
    if check_candidate(arr, candidate):
        return candidate
    else:
        return -1

if __name__ == '__main__':
    with open('input.txt') as f:
        f.readline()
        inputs = []
        for line in f:
            inputs.append(list(map(int, line.split())))
    print(' '.join(map(str, map(moore, inputs))))