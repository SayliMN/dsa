class Solution:
    def majorityElement(self, nums):
        count = 0
        res = 0 #to store most frequent number

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res
        # O(n),O(1)

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,3]
    print(s.majorityElement(nums))
