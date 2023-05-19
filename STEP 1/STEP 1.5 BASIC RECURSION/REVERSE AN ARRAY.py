def rev(l,begin,end):
    if begin>=end:
        return l
    l[begin],l[end]=l[end],l[begin]
    return rev(l,begin+1,end-1)

l=[10,20,30,40,50,60]
p=len(l)-1
print(rev(l,0,p))
