def bubble_sort(nums):
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                temp = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = temp
                swapping = True

        end -=1

    return nums