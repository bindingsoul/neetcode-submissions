class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i]<0:
                if len(stack)==0:
                    stack.append(asteroids[i])
                else:
                    while(len(stack)):
                        top = stack[-1]
                        if top>0:
                            if abs(top)>abs(asteroids[i]):
                                break
                            elif abs(top)==abs(asteroids[i]):
                                stack.pop()
                                i+=1
                                break
                            else:
                                stack.pop()
                                continue
                    
                        elif top<0:
                            stack.append(asteroids[i])

            elif asteroids[i]>0:
                stack.append(asteroids[i])

        return stack