# Solution to https://www.hackerrank.com/challenges/candies

# Test Cases:
# [1, 2, 3, 4] -> 10
# [4, 3, 2, 1] -> 10
# [1, 1, 1, 1] -> 4
# [1, 2, 3, 3, 3, 2, 1, 2] -> 15
# [1, 3, 2, 1] -> 7

n = int(input())

a = []
floor = None;

for _ in range(n):
    i = int(input())
    a.append(i)

candies = 1
rating = a[0]
total = 0
peakIndex = 0
peakCandies = 1

for i in range(n):
    if a[i] == rating:
        # peak must be the same as before, but reset candies
        candies = 1
        peakIndex = i
        peakCandies = candies
    elif a[i] > rating:
        # found a new peak, update peakIndex and peakCandies
        # child must have one more candy than the previous child
        candies = candies + 1
        peakIndex = i
        peakCandies = candies
    else:
        # lower rating, so reset candies to 1
        # total must be increased for the downward slope (excluding the peak)
        # if this downward slope is longer than the previous upward slope,
        # the peak's candy count must increase
        candies = 1
        total = total + i - peakIndex - 1
        if i - peakIndex >= peakCandies:
            total = total + 1
    rating = a[i]
    total = total + candies

print(total)
