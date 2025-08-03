class Solution:
    def generateParenthese(self, n):
        stack = [] #to hold parentheses
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 3
    print(sol.generateParenthese(n))