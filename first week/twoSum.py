def twoSum(nums, target):
    result = {}
    for i, n in enumerate(nums):
        if n in result:
            return [result[n], i]
        result[target - n] = i


def main():
    nums = [3,3,1,2,4,5,7,9]
    target = 7
    
    print(twoSum(nums, target))


if __name__ == "__main__":
    main()

# https://leetcode.com/problems/two-sum/

