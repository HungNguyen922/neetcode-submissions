class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for t in range(len(temperatures)):
            if not stack:
                stack.append(t)
            else:
                while stack and temperatures[t] > temperatures[stack[-1]]:
                    popped = stack.pop()
                    output[popped] = t - popped
                stack.append(t)
        return output