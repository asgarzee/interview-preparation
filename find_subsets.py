def subsets(nums):
    output = [[]]
    for num in nums:
        output += [curr + [num] for curr in output]
    return output


subsets([1, 2, 3])
