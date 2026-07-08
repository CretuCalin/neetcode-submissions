class Solution:
    def isOperation(self, s: str) -> bool:
        return s in ["+", "-", "*", "/"]
 
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            print(stack)
            if not self.isOperation(tokens[i]):
                stack.append(int(tokens[i]))
            else:
                number1 = stack.pop()
                number2 = stack.pop()
                print(number2, number1)


                operation = tokens[i]
                if operation == "+":
                    stack.append(number2 + number1)
                if operation == "-":
                    stack.append(number2 - number1)
                if operation == "*":
                    stack.append(number2 * number1)
                if operation == "/":
                    stack.append(int(number2 / number1))
        return stack.pop()