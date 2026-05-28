class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initial thoughts:
        # 1-indexed means the 0 index should be 1 in result
        # sorted array means that I can used two pointer
        # if sum is greater than target
        # I can shrink from right side
        # I will add index of left and right pointer when
        # sum = target

        right = len(numbers)-1

        for left in range(len(numbers)):
            while (numbers[right] + numbers[left]) > target:
                right -= 1
            if numbers[right] + numbers[left] == target:
                return [left + 1, right + 1]
            
            