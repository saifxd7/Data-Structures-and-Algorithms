# #######################################################Easy###########################################
# ---------------------------------Valid Palindrome------------------------------

# Solution 1:


def isPalindrome(s: str) -> bool:
    string = ""
    for elem in s:
        if isAlpha(elem):
            string += elem
    s = string
    return s.lower() == s[::-1].lower()


def isAlpha(char):
    return (
        ord("A") <= ord(char) <= ord("Z")
        or ord("a") <= ord(char) <= ord("z")
        or ord("0") <= ord(char) <= ord("9")
    )

# Solution 2:


def isPalindrome(s: str) -> bool:
    left, right = 0, len(s)-1
    while left < right:
        while left < right and not isAlpha(s[left]):
            left += 1
        while left < right and not isAlpha(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    return True


# ----------------------------------- 3Sum --------------------------------------------
def threeSum(nums: list[int]) -> list[list[int]]:
    res = []  # Empty list
    nums.sort()  # Sorted the nums

    for i, a in enumerate(nums):
        # traverse and check the number is postive or not
        # Skip positive integers
        if a > 0:
            break

        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


# -------------------------------------Container with most water------------------------------

def maxArea(height: list[int]) -> int:

    # output = 0
    # for l in range(len(height)):
    #     for r in range(l + 1, len(height)):
    #         area = (r - l) * min(height[l], height[r])
    #         output = max(output, area)

    # return output
    output = 0
    left, right = 0, len(height)-1
    while (left < right):
        area = (right - left) * min(height[left], height[right])
        output = max(output, area)

        if (height[left] < height[right]):
            left += 1
        else:
            right -= 1

    return output
