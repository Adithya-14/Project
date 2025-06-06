def two_sum(n,target):
    d={}
    for i,num in enumerate(n):
        r=target-num
        if r in d:
            return [d[r],i]
        else:
            d[num]=i

print(two_sum([2,3,4,5,6,7,8],9))