def selection_sort(nums):
    for i in range(len(nums)):
        smallest_index = i
        for j in range(smallest_index + 1, len(nums)):
            if nums[j] < nums[smallest_index]:
                smallest_index = j

        temp = nums[i]
        nums[i] = nums[smallest_index]
        nums[smallest_index] = temp

    return nums
