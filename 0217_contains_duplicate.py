class Solution:
    def containsDuplicate(self, nums):
        if len(nums) == len(set(nums)):
            return False
        return True
        # O(n),O(1)

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,2,3]
    print(s.containsDuplicate(nums))
