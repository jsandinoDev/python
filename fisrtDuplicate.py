def findPos(array, el):
    occur = []
    for index,element in enumerate(array):
        if element == el:
            occur.append(index)
    return  occur


def solution(a):
    list = {}
    repeat = []
    for i in a:
        list[str(i)] = str(a.count(i))

    keys = list.keys()
    for key in keys:
        if int(list.get(key)) >= 2:
            repeat.append(key)

    dicOccu = {}
    for i in repeat:
        intI = int(i)
        occur = findPos(a, intI)
        dicOccu[intI] = occur[1]

    finalKey = -1
    if len(dicOccu) != 0:
        finalVal = min(dicOccu.values())

        for key, val in dicOccu.items():
            if val == finalVal:
                finalKey = key

    return finalKey

