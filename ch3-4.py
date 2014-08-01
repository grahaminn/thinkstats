import percentile
from random import randrange

def partition(list, left, right, pivotIndex):
    pivotValue = list[pivotIndex]
    temp = list[right]
    list[right] = list[pivotIndex]
    list[pivotIndex] = temp
    storeIndex = left
    for i in range(left,right-1):
        if list[i] < pivotValue:
            temp = list[i]
            list[i] = list[storeIndex]
            list[storeIndex] = temp
            storeIndex += 1
    temp = list[right]
    list[right] = list[storeIndex]
    list[storeIndex] = temp
    return storeIndex

def FasterPercentile(scores, left, right, rank):
    if left == right:
        return scores[left]
    
    pivotIndex = randrange(left, right)
    pivotIndex = partition(scores, left, right, pivotIndex)

    if rank == pivotIndex:
       return scores[rank]
    elif rank < pivotIndex:
       return FasterPercentile(scores, left, pivotIndex - 1, rank)
    else: 
       return FasterPercentile(scores, pivotIndex + 1, right, rank)

scores = [55, 66, 77, 88, 99]
your_score = 90

for percent in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    print 'prank, score, score'
    rank = int((percent / 100.0) * (len(scores) - 1))
    print percent, 
    print percentile.Percentile(scores, percent),
    print FasterPercentile(scores, 0,  len(scores) - 1, rank)
