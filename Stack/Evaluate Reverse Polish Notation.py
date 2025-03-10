import math

def evalRPN(tokens: list[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stack = []
        
        for op in tokens:
            if op in operators:
                result = -1
                
                match op:
                    case '+':
                        result = stack[-2] + stack[-1]
                    case '-':
                        result = stack[-2] - stack[-1]
                    case '*':
                        result = stack[-2] * stack[-1]
                    case '/':
                        result = stack[-2] / stack[-1]
                        if result<0:
                            result = math.ceil(result)
                        else:
                            result = math.floor(result)
                
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(int(op))
        
        return stack[0]

#Test
print(evalRPN(["4","13","5","/","+"]))