def merge_sort(nums):
    if len(nums) < 2:
        return nums

    index = len(nums) // 2
    lst1 = nums[:index]
    lst2 = nums[index:]

    return merge(merge_sort(lst1), merge_sort(lst2))


def merge(first, second):
    final = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    if i < len(first):
        for i in range(i, len(first)):
            final.append(first[i])

    elif j < len(second):
        for j in range(j, len(second)):
            final.append(second[j])

    return final





