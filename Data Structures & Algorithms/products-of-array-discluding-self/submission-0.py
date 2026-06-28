class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        productList = [1] * n

        prefix = 1
        for i in range(n):
            productList[i] *= prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            productList[i] *= suffix 
            suffix *= nums[i]
        
        return productList