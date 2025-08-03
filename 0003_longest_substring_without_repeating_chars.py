class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        charSet = set()
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) #shrink sliding window/substring until we have no duplicates in it
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "pwwwwwkew"
    print(sol.lengthOfLongestSubstring(s))