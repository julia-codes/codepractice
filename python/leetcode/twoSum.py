class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1 = 0
        num2 = 1
        if len(nums) <2:
            return None
        while num1 < len(nums):
            while num2 < len(nums):
                if num1 + num2 == target:
                    return twoIndexes(nums, num1, num2)
                num2=num2+1
            num1=num1+1
            num2 = num1+1
        return None
    
    def twoIndexes( nums: List[int], num1: int, num2: int):
        returnArray = []
        returnArray.append(nums.index(num1))
        returnArray.append(nums.index(num2))
        returnArray