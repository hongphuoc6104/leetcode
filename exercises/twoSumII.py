from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        while L < R:
            if numbers[L] + numbers[R] > target:
                R-=1
            elif numbers[L] + numbers[R] < target:
                L+=1 
            else:
                return [L +1, R + 1]
 

if __name__ == "__main__":
    s = Solution()
    # Example 1: numbers = [2,7,11,15], target = 9 → [1,2]
    print(s.twoSum([2, 7, 11, 15], 13))
    # Example 2: numbers = [2,3,4], target = 6 → [1,3]
    print(s.twoSum([2, 3, 4], 6))
