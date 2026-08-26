class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack  = []
        for i in range(len(operations)):
            if operations[i]=='C':
                stack.pop()
            elif operations[i]=='+':
                stack.append(int(stack[len(stack)-1]+stack[len(stack)-2]))
            elif operations[i]=='D':
                stack.append(int(2*stack[len(stack)-1]))
            else:
                stack.append(int(operations[i]))

        for y in range(len(stack)):
            res+=stack[y]

        return res