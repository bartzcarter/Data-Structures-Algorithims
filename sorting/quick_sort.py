def quick_sort(nums, low, high):
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high+1):
        if nums[j] < pivot:
            i += 1
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

    temp = nums[i + 1]
    nums[i + 1] = pivot
    nums[j] = temp

    return i+1