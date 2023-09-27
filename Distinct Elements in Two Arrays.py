def fun(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    ans1 = list(set1 - set2)
    ans2 = list(set2 - set1)
    return ans1, ans2
N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res1, res2 = fun(arr1, arr2)
print(*res1)
print(*res2)
