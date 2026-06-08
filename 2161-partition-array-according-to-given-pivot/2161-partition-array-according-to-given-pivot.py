class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        befour = []
        mid = []
        after = []

        for n in nums:
            if n < pivot: befour.append(n)
            elif n > pivot: after.append(n)
            else: mid.append(n)

        return befour + mid + after
        