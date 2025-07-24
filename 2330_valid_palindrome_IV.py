class Solution:
    def valid_palindrome(self, s: str):
        l, r = 0, len(s) - 1
        counter = 0
        while l < r:
            if s[l] != s[r]:
                counter += 1
            l += 1
            r -= 1
        return counter in [1,2]



if __name__ == '__main__':
    sol = Solution()
    s = "abcdaaas"
    print(sol.valid_palindrome(s))