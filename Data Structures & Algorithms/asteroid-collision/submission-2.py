class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i]<0:
                if len(stack)==0:
                    stack.append(asteroids[i])
                else:
                    alive = True
                    while(len(stack)) and alive:
                        top = stack[-1]
                        if top>0:
                            if abs(top)>abs(asteroids[i]):
                                alive = False
                                break
                            elif abs(top)==abs(asteroids[i]):
                                alive = False
                                stack.pop()
                                break
                            else:
                                stack.pop()
                    
                        elif top<0:
                            alive==False
                            stack.append(asteroids[i])
                            break
                    if alive==True:
                        stack.append(asteroids[i])

            elif asteroids[i]>0:
                stack.append(asteroids[i])

        return stack