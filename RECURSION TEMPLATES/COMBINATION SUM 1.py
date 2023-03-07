class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = [];
        candidates.sort()
        self.solve(candidates, 0, [], ans, target)
        return ans

    def solve(self, arr, index, l, l1, target):
        if index == len(arr):
            if target == 0:
                l1.append(l.copy())
            return
        if arr[index] <= target:
            l.append(arr[index])
            target -= arr[index]
            self.solve(arr, index, l, l1, target)
            target += arr[index]
            l.pop()
            self.solve(arr, index + 1, l, l1, target)
        else:
            self.solve(arr, index + 1, l, l1, target)
