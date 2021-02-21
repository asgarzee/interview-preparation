'''
Two Sum problem
'''


def two_sum(arr, target):
    count = {}
    pairs = []

    for i, val in enumerate(arr):
        if (target - val) in count:
            pairs.append((target - val, val))
        else:
            count[val] = i
    return pairs


if __name__ == '__main__':
    arr = [1, 5, 7, -1, 5]
    target = 6
    print(two_sum(arr, target))
