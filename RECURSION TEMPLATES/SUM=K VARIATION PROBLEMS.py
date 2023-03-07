"""
#PRINT ALL SUBSEQUENCES IF SUM==K
def solve(index,arr,variable_sum,k,arr1,n):
    if index==n:
        if variable_sum==k:
            print(*arr)
        return
    arr.append(arr1[index])
    variable_sum+=arr1[index]
    solve(index+1,arr,variable_sum,k,arr1,n)
    variable_sum-=arr[-1]
    arr.pop()
    solve(index+1,arr,variable_sum,k,arr1,n)



def solve(index,arr,variable_sum,k,arr1,n):
    if index==n:
        if variable_sum==k:
            print(*arr)
            return True
        return False
    arr.append(arr1[index])
    variable_sum+=arr1[index]
    if solve(index+1,arr,variable_sum,k,arr1,n)==True:return True
    variable_sum-=arr[-1]
    arr.pop()
    if solve(index+1,arr,variable_sum,k,arr1,n)==True:return True

    return
"""


def solve(index, variable_sum, k, arr, n):
    if index == n:
        if variable_sum == k:
            return 1
        return 0
    l = solve(index + 1, variable_sum + arr[index], k, arr, n)
    r = solve(index + 1, variable_sum, k, arr, n)
    return l + r


arr = [1, 2, 1];
k = 2;
n = len(arr)
p = solve(0, 0, k, arr, n)
print(p)
