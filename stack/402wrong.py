def removeKdigits(num: str, k: int) -> str:
    if k == len(num):
        return 0


    num = list(num)

    def first_delete()->int:
        count = 0
        index = 0
        res = k
        for i in range(len(num)):
            if num[i] != '0':
                count += 1
            else:
                if count <= k:
                    index = i+1
                    res = k-count
        
        num[:] = num[index:]
        return res

    k = first_delete()
    if k == len(num):
        return 0
    
    res = []
    # this is actually a wrong answer, when some thing like num='56712' and k=3
    # 6 is smaller than 7 and it will keep in this algorithm, but it should be delete, because is also smaller then 1
    # this algrithm seems only delete one number, that can't deal with lots of number are need to deleted.
    for i in range(len(num)-1):
        if num[i]>num[i+1] and k:
            k-=1
            continue
        else:
            res.append(num[i])
    
    res.append(num[-1])

    return res[:-k] if k else res


# and this is the case that this algorithm is not right.
# it must delete all the number biger than it
# so stack is kind of the only way to do it
num = "14532219"
k = 3
print(removeKdigits(num, k))