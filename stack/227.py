class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        preop = '+'
        stack = []
        s+='+'

        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c in '+-*/':
                if preop == '+':
                    stack.append(num)
                elif preop == '-':
                    stack.append(-num)
                elif preop == '*':
                    stack[-1]*=num
                elif preop == '/':
                    if stack[-1]<0:
                        stack[-1]*=-1
                        stack[-1]//=num
                        stack[-1]*=-1
                    else:
                        stack[-1]//=num
                        
                preop = c
                num = 0
        
        return sum(stack)
        
def main():
    input = " 3+5 / 2 "
    s = Solution()
    a = s.calculate(input)
    print(a)

if __name__ == "__main__":
    main()
