def removeKdigits(num: str, k: int) -> str:
    stack =  []
    for n in num:
        while stack and k and stack[-1]>n:
            stack.pop()
            k-=1
        stack.append(n)
    
    if k:
        stack = stack[:-k]

    return ''.join(stack) if stack else '0'


num = "1342219"
k = 3
print(removeKdigits(num, k))


# why using stack to do it?
# there are many case need to thinking about at the first
# remove any number that with 0 behind them
# then, compare with for the smaller ones
# if there also some k left, like n='122234' and k=3, just remove the last num, like n='122'
# also need to thinking about when the last number is 0, like n='123000' k=2, in this case, i need to remove the no zero num

#  but, if i  usiing a simple algorithm, that all delete all number before a num that bigger than it
#  then all the situation will be satesified.
#  when there is 0 at the begining, then all of them need to be remove, as they bigger than 0
#  after this, when meet a zero, than just keep to remove the number before it, untill the k is out.
#  if k is not out, means all the number before this 0 is moveout, which also means this is a beginning 0