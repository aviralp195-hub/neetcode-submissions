class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ch in operations:

            if ch == '+':
                score = stack[-1] + stack[-2]
                stack.append(score)

            elif ch == 'D':
                score = stack[-1] * 2
                stack.append(score)

            elif ch == 'C':
                stack.pop()

            else:
                stack.append(int(ch))

        res = 0

        for score in stack:
            res += score

        return res


        