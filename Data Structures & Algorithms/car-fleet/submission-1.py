class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pairs = list(zip(position, speed))
        pairs.sort(reverse=True, key=lambda x: x[0])

        for pair in pairs:
            time = (target - pair[0]) / pair[1]
            stack.append(time)

            if not stack:
                stack.append(time)
                continue

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            

        return len(stack)


