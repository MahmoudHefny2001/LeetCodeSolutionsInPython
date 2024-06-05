class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2  
            
            if nums[middle_index] > target:
                right_index = middle_index - 1
            elif nums[middle_index] < target:
                left_index = middle_index + 1
            else:
                return middle_index
        
        return -1