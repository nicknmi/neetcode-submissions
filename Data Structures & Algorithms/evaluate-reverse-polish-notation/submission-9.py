class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        
        for token in tokens:
            if token in ['+', '-', '*','/']:
                num1 = stack.pop()
                num2 = stack.pop()

                stack.append(self.matchOperation(int(num2), int(num1), token))

            else:
                stack.append(int(token))

        return stack[0]

    def matchOperation(self, num1: int, num2: int, operation: str) -> int:
        match operation:
            case '+':
                return num1 + num2
            case '-':
                return num1 - num2
            case '*':
                return num1 * num2
            case '/':
                return int((num1*1.0) / num2)


# ["1","2","+","3","*","4","-"]

# 9 - 4
    

