# libraries / modules
import collections

# ########################################################## EASY ##################################################################
# -------------------------------------Contains Duplicate------------------------------------------


def containsDuplicate(nums: list[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


# --------------------------------------Valid Anagram----------------------------------------------


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}  # value --> count

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT


# --------------------------------------Two Sum-----------------------------------------------------
def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {}  # val -> index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


# ############################################################ Medium ##############################################################
# ---------------------------------------Group Anagrams--------------------------------------------


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = collections.defaultdict(list)

    for string in strs:
        count = [0] * 26
        for char in string:
            count[ord(char) - ord("a")] += 1
        result[tuple(count)].append(string)

    return result.values()

# ----------------------------------------Top K Frequent--------------------------------------------


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


# ------------------------------------------Product of Array Except Self-----------------------------
def productExceptSelf(nums: list[int]) -> list[int]:
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


# -------------------------------------------Encode and Decode Strings--------------------------------
def encode(strs: list[str]) -> str:
    res = ''
    for word in strs:
        encoded = str(len(word)) + "/" + word
        res += encoded

    return res


def decode(strs: str) -> list[str]:

    res, i = [], 0
    while i < len(strs):
        e = i
        while strs[e] != "/":
            e += 1
        size = int(strs[i:e])
        word = strs[e+1: e+1+size]
        i = e+1+size
        res.append(word)
    return res


print(encode(["we", "say", ":", "yes"]))
print(decode("2/we3/say1/:3/yes"))


# ------------------------------------------- Longest Consecutive Sequence ---------------------------
def longestConsecutive(nums: list[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
