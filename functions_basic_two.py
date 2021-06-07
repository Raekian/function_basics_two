def countdown(num):
    countList = []
    for x in range(num, 0, -1):
        countList.append(x)
    return countList


print(countdown(5))


def printReturn (list):
    print(list[0])
    return list[1]

printReturn([5,6])

def firstPL(list):
    return (list[0] + len(list))

print(firstPL([1,2,3,4,5]))


def greaterThanSecond(list):
    newList = []
    for x in range(0, len(list)):
        if list[x] > list[1]:
            newList.append(list[x])
    print (len(newList))
    return newList

print(greaterThanSecond([5,2,3,4,6,1]))


def lenghtValue(list):
    newList = [list[0]] * list[1]
    return newList

print(lenghtValue([2,6]))