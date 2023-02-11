import collections


def lengthOfLongestSubstring(s: str) -> int:
    charSet, l, res = set(), 0, 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        charSet.add(s[r])
        res = max(res, r - l + 1)

    return res


print(lengthOfLongestSubstring("abcabcbb"))


# ------------------------
def characterReplacement(s: str, k: int) -> int:
    count, l, res = {}, 0, 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res


print(characterReplacement("ABABABB", 2))


# -----------------------------Fruit into buckets---------
def totalFruit(fruits: list[int]) -> int:
    count = collections.defaultdict(int)
    l, total, res = 0, 0, 0

    for r in range(len(fruits)):
        count[fruits[r]] += 1
        total += 1

        while len(count) > 2:
            f = fruits[l]
            count[f] -= 1
            total -= 1
            l += 1

            if not count[f]:
                count.pop(f)

        res = max(res, total)

    return res
