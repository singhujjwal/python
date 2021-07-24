import collections
import pdb


class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                # create the number
                num = num*10 + int(s[i])
                print (f"num is now {num}")
            if s[i] in '+-*/' or i  == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(num*stack.pop())
                elif sign == '/':
                    stack.append(num/stack.pop())
                sign = s[i]
                num = 0
        return sum(stack)
  
              

if __name__ == '__main__':
    s = Solution()
    print (s.calculate("1"))


