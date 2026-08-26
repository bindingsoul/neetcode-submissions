class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i]=='+':
                stack.append(int(stack.pop())+int(stack.pop()))
            elif tokens[i]=='*':
                stack.append(int(stack.pop())*int(stack.pop()))
            elif tokens[i]=='-':
                stack.append(-(int(stack.pop())-int(stack.pop())))
            elif tokens[i]=='/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b//a)
            else:
                stack.append(int(tokens[i]))
        return stack[0]

