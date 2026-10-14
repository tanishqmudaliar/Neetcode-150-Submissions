class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for index, num in enumerate(nums):
            result = 1
            for index2,n in enumerate(nums):
                if index2 != index:
                    result *= n
            output.append(result)
        return output