# -------------------------medium-------------
# --------------------------------------Find minimum in rotated sorted array----------------------------
def findMin(nums: list[int]) -> int:
    # left, right, res = 0, len(nums)-1, nums[0]

    # while left <= right:
    #     if nums[left] < nums[right]:
    #         res = min(res, nums[left])
    #         break

    #     middle = (left + right) // 2
    #     res = min(res, nums[middle])

    #     if nums[middle] >= nums[left]:
    #         left = middle + 1
    #     else:
    #         right = middle - 1

    # return res

    left, right = 0, len(nums)-1
    while left < right:

        mid = (left + right) // 2

        if nums[left] > nums[mid]:
            right = mid
        elif nums[right] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return nums[left]


# ----------------------Search in Rotated Sorted Array---------------

def search(self, nums: list[int], target: int) -> int:
    left, right = 0, len(nums)-1

    while left <= right:
        middle = (left + right) // 2

        if target == nums[middle]:
            return middle

        if nums[left] <= nums[middle]:
            if target > nums[middle] or target < nums[left]:
                left = middle + 1
            else:
                right = middle - 1

        else:
            if target < nums[middle] or target > nums[right]:
                right = middle - 1
            else:
                left = middle + 1

    return -1
