class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initial thoughts:
        # 1-indexed means the 0 index should be 1 in result
        # sorted array means that I can used two pointer
        # if sum is greater than target
        # I can shrink from right side
        # if sum is less than target
        # I can shrink from left side
        # I will add index of left and right pointer when
        # sum = target

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        # if no solution found return empty list
        return []
            