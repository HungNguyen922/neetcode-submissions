class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        posspd = sorted(zip(position, speed), reverse = True)
        
        for pos, spd in posspd:
            time = (target - pos) / spd
            if stack and time > stack[-1]:
                stack.append(time)
            elif not stack:
                stack.append(time)
        return len(stack)