'''
Given an array with at least one positive integer, find the contiguous sub-array with the largest sum.
'''


def maxSubArraySum(nums):

    maximum = nums[0]
    sum = 0

    for i, val in enumerate(nums):
        if sum < 0:
            sum = 0
        sum += val
        maximum = max(sum, maximum)
    return maximum


if __name__ == '__main__':
    print(maxSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
