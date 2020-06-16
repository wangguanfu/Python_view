def bubble_sort(numberlist):
    length = len(numberlist)
    for i in range(length):
        for j in range(1, length - i):
            if numberlist[j - 1] > numberlist[j]:
                numberlist[j], numberlist[j - 1] = numberlist[j - 1], numberlist[j]
    return numberlist


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


import heapq

a = [43, 5, 65, 4, 5, 8, 87]

re1 = heapq.nlargest(3, a)  # 求最大的三个元素，并排序
re2 = map(a.index, heapq.nlargest(3, a))  # 求最大的三个索引    nsmallest与nlargest相反，求最小

print(re1)
print(list(re2))  # 因为re2由map()生成的不是list，直接print不出来，添加list()就行了




def  merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result

def merge_sort(numberlist):
    if len(numberlist) <= 1:
        return numberlist
    mid = len(numberlist) // 2
    left = numberlist[:mid]
    right = numberlist[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)









