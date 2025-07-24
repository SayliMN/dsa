class Solution:
    def is_valid_palindrome(self, s: str, k: int) -> bool:
        def helper(l, r, k):
            while l < r:
                if s[l] != s[r]:
                    if k == 0:
                        return False
                    return helper(l, r-1, k-1) or helper(l+1, r, k-1)
                l += 1
                r -= 1
            return True

        return helper(0, len(s) - 1, k)


if __name__ == '__main__':
    sol = Solution()
    s = "abcdefed"
    k = 2
    print(sol.is_valid_palindrome(s,k))