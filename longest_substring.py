def lengthOfLongestSubstring(s):
    '''
    Longest unique substring wihtout repeating characters
    '''
    seen = {}
    max_length = 0
    start = 0

    for i, val in enumerate(s):
        if val in seen:
            start = max(start, seen[val] + 1)
        seen[val] = i
        max_length = max(max_length, i - start +1 )
    return max_length

if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))