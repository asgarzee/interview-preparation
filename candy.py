'''
Question:

There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements: 
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''


def candy(self, ratings: List[int]) -> int:
    l = len(ratings)
    candy = [1] * l
    for i in range(1, l):
        if ratings[i] > ratings[i-1]:
            candy[i] = candy[i-1]+1
    for i in range(l-1, 0, -1):
        if ratings[i-1] > ratings[i]:
            candy[i-1] = max(candy[i-1], candy[i]+1)
    return sum(candy)
