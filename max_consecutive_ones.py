'''
Given a binary array, find the maximum number of consecutive 1s in this array.
Example: Input: [1,1,1,0,1,1,0]
'''


def max_consecutive_ones(arr):
    count = 0
    res = 0
    for i in arr:
        if i == 0:
            count = 0
        else:
            count += 1
            res = max(res, count)
    return res


if __name__ == '__main__':
    list_of_ones = [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
    print(max_consecutive_ones(list_of_ones))
